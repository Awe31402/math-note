---
course: Mobile Sensing and Robotics 2（Uni Bonn, Summer 2021）
episode: 2-35
lecture: Epipolar Geometry Basics
date: 待補（2021 夏季學期）
video: https://youtu.be/cLeF-KNHgwU
notes: MVG §9.1–9.2（書頁 239–246，PDF 頁 257–264）；《視覺 SLAM 十四講》第 2 版 §7.3.1（書頁 165–167，PDF 頁 188–190）
---

# 第 2-35 集 · 對極幾何基礎 [▶ 影片](https://youtu.be/cLeF-KNHgwU)

← 上一集：[2-33-relative-orientation](2-33-relative-orientation.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[2-37-fundamental-essential-direct](2-37-fundamental-essential-direct.md) →

> **課程**：Mobile Sensing and Robotics 2，Uni Bonn，2021 夏季學期 — 第 2-35 集
> **講者**：Cyrill Stachniss
> **來源**：YouTube 錄影逐字稿（24:35，Whisper `medium.en` 轉錄）＋ MVG §9.1–9.2 ＋《視覺 SLAM 十四講》§7.3.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `【十四講補充】` 十四講有、課堂沒講

（記號沿用 2-33：$\mathbf x'^{\mathsf T}F\mathbf x'' = 0$，$'$ 是影像 1、$''$ 是影像 2。MVG 的 $F$ 是本課的轉置。）

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 為什麼需要對極幾何](#1-為什麼需要對極幾何)
- [2. 五個元素](#2-五個元素)
- [3. 為什麼對應點在對極線上](#3-為什麼對應點在對極線上)
- [4. 為什麼叫「對極軸」](#4-為什麼叫對極軸)
- [5. 用 P 和 F 計算各元素](#5-用-p-和-f-計算各元素)
  - [5.1 對極軸](#51-對極軸)
  - [5.2 對極線](#52-對極線)
  - [5.3 極點](#53-極點)
- [6. 總結](#6-總結)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

**對極幾何**（epipolar geometry）：描述影像對的幾何關係——影像 1 的一個點，在影像 2 中會落在哪裡。最重要的用途：讓找對應點的搜尋從**整張影像（2D）**縮小到**一條線（1D）**。

---

## 1. 為什麼需要對極幾何

[▶ 00:38](https://youtu.be/cLeF-KNHgwU?t=38)

- 相機對（雙眼相機只是其中一例）：兩個投影中心，兩條射線交於一點——2-33 推 $E$、$F$ 時用的共面約束，這裡也會用到。
- 實際情況：在影像 1 找到一個有希望的特徵點，要在影像 2 找它。要搜尋整張影像嗎？還是能縮小範圍？
- 對極幾何利用相機對、基線、射線落在平面上，以及這些平面怎麼映到影像上 → 把搜尋從 2D 降到 **1D**（一條特定的線）。

**好處** [▶ 02:41](https://youtu.be/cLeF-KNHgwU?t=161)：

1. **更快**（顯然）。
2. **減少資料關聯錯誤**：影像中可能有好幾個彼此相似的物體，描述子也很像；限制在一條對極線上後，可能只有其中一個物體被這條線穿過 → 比較不會配錯。

---

## 2. 五個元素

[▶ 03:37](https://youtu.be/cLeF-KNHgwU?t=217)

圖：影像 1、影像 2，投影中心 $O'$、$O''$，真實世界的點 $\boldsymbol X$（映到兩張影像各一點），另一點 $\boldsymbol Y$（映到另外的位置）。

| 元素 | 定義 |
|---|---|
| **對極軸**（epipolar axis） | 連接兩投影中心的直線（就是前面的**基線**） |
| **對極平面**（epipolar plane） | 由 $O'$、$O''$ 和 3D 點 $\boldsymbol X$ 三點決定的平面；不同的 3D 點可能給不同的對極平面 |
| **極點**（epipole） | 另一台相機的**投影中心投影到這張影像**上的點；每張影像一個 |
| **對極線**（epipolar line） | 對極平面和影像平面的**交線**；每張影像各一條 |
| 影像點 | $\boldsymbol X$ 在兩張影像中的像 $\mathbf x'$、$\mathbf x''$ |

**另一種寫法** [▶ 10:17](https://youtu.be/cLeF-KNHgwU?t=617)：

- 極點 = 對極軸（基線）和影像平面的交點：$\boldsymbol e' = \overline{O'O''} \cap \mathcal E'$、$\boldsymbol e'' = \overline{O'O''} \cap \mathcal E''$（$\mathcal E', \mathcal E''$ 是兩個影像平面）。
- 對極線 = 對極平面和影像平面的交線。
- 對極線也可以看成：從相機 1 指向該點的射線，投影到相機 2 的影像上。

**都在對極平面上的東西** [▶ 11:46](https://youtu.be/cLeF-KNHgwU?t=706)（假設透鏡無畸變）：兩個投影中心、3D 點本身、兩條對極線、兩個極點（投影中心在平面上，極點是它們和影像平面的交點）、兩個影像點。→ 對極平面是一個可以利用的**約束**。

- 極點是一張影像中**所有對極線的交點**。

【課本補充】MVG §9.1（書頁 239–241）的定義相同：極點 = 基線和影像平面的交點 = 另一台相機中心的像 = **基線（平移）方向的消失點**；對極平面是含基線的平面，有一個參數的一族（平面束，pencil）；所有對極線交於極點。特例（圖 9.4）：平移平行於影像平面、旋轉軸垂直於影像平面時，基線和影像平面的交點在**無窮遠** → 極點在無窮遠，對極線**互相平行**。

【十四講補充】§7.3.1（書頁 165–166）的術語：$O_1O_2$ 是**基線**；$O_1, O_2, P$ 決定**極平面**；$O_1O_2$ 和像平面 $I_1, I_2$ 的交點 $e_1, e_2$ 是**極點**；極平面和像平面的交線 $l_1, l_2$ 是**極線**。

---

## 3. 為什麼對應點在對極線上

[▶ 06:37](https://youtu.be/cLeF-KNHgwU?t=397)

- 只看影像 1：只知道 $\boldsymbol X$ 在從 $O'$ 出發、穿過 $\mathbf x'$ 的那條**射線**上，不知道在射線的哪裡。
- 讓一個點沿這條射線滑動，投影到影像 2：它會**沿著對極線滑動**。點越靠近，投影越靠近極點；點越遠，投影往另一邊走。
- 不管 $\boldsymbol X$ 在射線上哪裡，射線投影到影像 2 就是那條線 = 對極平面和影像平面 2 的交線。
- → 只要在**對極線**上找對應點 [▶ 07:41](https://youtu.be/cLeF-KNHgwU?t=461)。

**預測對應點的位置** [▶ 12:31](https://youtu.be/cLeF-KNHgwU?t=751)：已知 $\mathbf x'$ → 對極平面由 $\mathbf x'$（加兩投影中心）決定 → 它和影像平面 2 的交線 = 影像 2 的對極線 → 只要沿這條線搜尋。

【十四講補充】§7.3.1（書頁 166）：從第一幀看，射線 $\overrightarrow{O_1p_1}$ 上所有點都投影到同一個像素；不知道 $P$ 的位置時，第二張影像的極線 $\overrightarrow{e_2p_2}$ 就是 $P$ 可能出現的投影位置（射線 $\overrightarrow{O_1p_1}$ 在第二個相機中的投影）。透過特徵匹配確定了 $p_2$，才能推斷 $P$ 的位置和相機運動——**多虧了正確的特徵匹配**；沒有匹配時，就必須在極線上搜尋（書中第 12 講）。

---

## 4. 為什麼叫「對極軸」

[▶ 08:24](https://youtu.be/cLeF-KNHgwU?t=504)

- 換一個 3D 點 $\boldsymbol Y$：$O'$、$O''$ 仍在對極平面上，但 $\boldsymbol X$ 不在了 → 另一個對極平面。
- 所有對極平面都包含 $O'O''$ 這條線 → 可以看成一個平面**繞著這條軸旋轉**。例如基線水平時，對極平面只由點的高度決定。
- 所以這條線叫**對極軸**。

---

## 5. 用 P 和 F 計算各元素

[▶ 13:48](https://youtu.be/cLeF-KNHgwU?t=828)

### 5.1 對極軸

[▶ 14:24](https://youtu.be/cLeF-KNHgwU?t=864)

$$
\mathbf B = \boldsymbol X_{O''} - \boldsymbol X_{O'}
$$

- 寫成齊次向量，強調只知道**方向**、不知道長度。
- 投影中心可以從投影矩陣取得（2-33：$\boldsymbol X_O = -A^{-1}\boldsymbol a$）。

### 5.2 對極線

[▶ 15:02](https://youtu.be/cLeF-KNHgwU?t=902)

- 齊次座標中，點 $\mathbf x$ 在直線 $\boldsymbol l$ 上 ⇔ $\mathbf x^{\mathsf T}\boldsymbol l = 0$。
- 影像 1 的對極線 $\boldsymbol l'$ 要滿足 $\mathbf x'^{\mathsf T}\boldsymbol l' = 0$。
- 和共面約束 $\mathbf x'^{\mathsf T}F\mathbf x'' = 0$ 對照 → 

$$
\boxed{\;\boldsymbol l' = F\,\mathbf x''\;}
$$

**影像 1 的對極線 = 基本矩陣 × 影像 2 的點**。反過來，影像 2 的對極線要滿足 $\boldsymbol l''^{\mathsf T}\mathbf x'' = 0$；由 $\mathbf x'^{\mathsf T}F\mathbf x'' = 0$ 得 $\boldsymbol l''^{\mathsf T} = \mathbf x'^{\mathsf T}F$ [▶ 17:38](https://youtu.be/cLeF-KNHgwU?t=1058)：

$$
\boxed{\;\boldsymbol l'' = F^{\mathsf T}\,\mathbf x'\;}
$$

- 這就是從 2D 到 1D 的縮減：預測點在另一張影像中必須落在哪條線上，沿線搜尋即可。

【課本補充】MVG §9.2.3–9.2.4（書頁 245）用它的記號（$F_{\text{MVG}} = F^{\mathsf T}$）寫成 $\boldsymbol l' = F_{\text{MVG}}\mathbf x$、$\boldsymbol l = F_{\text{MVG}}^{\mathsf T}\mathbf x'$——代入 $F_{\text{MVG}} = F^{\mathsf T}$ 後和講者的兩式一致。MVG 還指出：$\mathbf x'^{\mathsf T}F\mathbf x = 0$ 等價於「兩條射線共面」，這是點對應的**必要**條件；而且這個關係可以不提相機矩陣、只用影像對應點來刻畫 $F$ → 可以只從影像對應算出 $F$（2-37）。

### 5.3 極點

[▶ 19:53](https://youtu.be/cLeF-KNHgwU?t=1193)

- 定義：另一台相機的投影中心投影到這張影像：

$$
\boldsymbol e' = P'\,\mathbf X_{O''}, \qquad \boldsymbol e'' = P''\,\mathbf X_{O'}
$$

  （$\mathbf X_O$ 是投影中心的齊次座標；$P$ 已知時直接算。）

- **所有對極線都通過極點** [▶ 20:45](https://youtu.be/cLeF-KNHgwU?t=1245)：對所有 $\boldsymbol l'$，$\boldsymbol e'^{\mathsf T}\boldsymbol l' = 0$；影像 2 同理。
- 代入 $\boldsymbol l' = F\mathbf x''$：$\boldsymbol e'^{\mathsf T}F\mathbf x'' = 0$ 對**任何** $\mathbf x''$ 都成立 → $\boldsymbol e'^{\mathsf T}F = \mathbf 0^{\mathsf T}$。同理 $F\boldsymbol e'' = \mathbf 0$：

$$
\boxed{\;F^{\mathsf T}\boldsymbol e' = \mathbf 0, \qquad F\,\boldsymbol e'' = \mathbf 0\;}
$$

- 影像 1 的極點是 $F^{\mathsf T}$ 的**零空間**；影像 2 的極點是 $F$ 的零空間。也就是 $F$ 的**左、右零向量**（講者說是「特徵值為 0 的特徵向量」；嚴格說是對應奇異值 0 的左、右奇異向量）[▶ 22:07](https://youtu.be/cLeF-KNHgwU?t=1327)。
- 可以用來推論點必須落在哪、$F$ 的零空間是什麼等。

（推論：$F$ 有非零的零向量 → $F$ 奇異、秩不足——和 2-33 的「$F$ 秩 2」一致。以下不是逐字稿內容，是由這兩式推得的。）

【課本補充】MVG §9.2.4 性質 (iii)（書頁 245）：對任何 $\mathbf x$（除了 $\boldsymbol e$），對極線 $\boldsymbol l' = F\mathbf x$ 都含極點 $\boldsymbol e'$，所以 $\boldsymbol e'^{\mathsf T}F = 0$（$\boldsymbol e'$ 是 $F$ 的左零向量）；同理 $F\boldsymbol e = 0$（右零向量）。例 9.2：$P = K[I \mid 0]$、$P' = K'[R \mid \boldsymbol t]$ 時，$\boldsymbol e = KR^{\mathsf T}\boldsymbol t$、$\boldsymbol e' = K'\boldsymbol t$（式 9.3）。

---

## 6. 總結

[▶ 23:02](https://youtu.be/cLeF-KNHgwU?t=1382)

- 用影像對推導：只知道是**保直線**的相機（未校正）時，能對幾何說什麼。
- 對極幾何的關鍵元素：對極線、對極軸、極點。
- 重要性：知道相對定向（基本矩陣）和影像 1 的一個點 → 只要在影像 2 的**一條線**上找對應點，不用搜尋整張影像 → 大幅減少工作量和資料關聯錯誤的機會。
- 找對應、限制影像中某些東西必須落在哪、極點構成零空間……都會用到對極幾何。

---

## 7. 一頁速查表

### 7.1 元素

| 元素 | 定義 | 計算 |
|---|---|---|
| 對極軸 | 兩投影中心連線 | $\mathbf B = \boldsymbol X_{O''} - \boldsymbol X_{O'}$（只有方向） |
| 對極平面 | $O', O'', \boldsymbol X$ 決定的平面；繞對極軸旋轉的平面束 | — |
| 極點 | 另一台相機中心的像 | $\boldsymbol e' = P'\mathbf X_{O''}$；$F^{\mathsf T}\boldsymbol e' = 0$ |
| | | $\boldsymbol e'' = P''\mathbf X_{O'}$；$F\boldsymbol e'' = 0$ |
| 對極線 | 對極平面 ∩ 影像平面 | $\boldsymbol l' = F\mathbf x''$，$\boldsymbol l'' = F^{\mathsf T}\mathbf x'$ |

（記號：$\mathbf x'^{\mathsf T}F\mathbf x'' = 0$。）

### 7.2 關鍵一步

| 結論 | 推導 |
|---|---|
| $\boldsymbol l' = F\mathbf x''$ | 點在線上 ⇔ $\mathbf x'^{\mathsf T}\boldsymbol l' = 0$；對照 $\mathbf x'^{\mathsf T}(F\mathbf x'') = 0$ |
| $\boldsymbol l'' = F^{\mathsf T}\mathbf x'$ | $(\mathbf x'^{\mathsf T}F)\mathbf x'' = 0$ ⇔ $\boldsymbol l''^{\mathsf T}\mathbf x'' = 0$ |
| $F^{\mathsf T}\boldsymbol e' = 0$ | 所有對極線過極點：$\boldsymbol e'^{\mathsf T}F\mathbf x'' = 0$ 對所有 $\mathbf x''$ |

### 7.3 用途

找對應：2D 搜尋 → 沿對極線的 1D 搜尋；更快、更少錯配。

### 7.4 和 MVG 對照

本課 $F$ ↔ MVG $F^{\mathsf T}$：MVG 寫 $\boldsymbol l' = F\mathbf x$、$F\boldsymbol e = 0$、$F^{\mathsf T}\boldsymbol e' = 0$，其中無撇號的是**第一**張影像。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $F$ 秩 2（極點是零空間） | 2-37 強制 $F$ 的奇異性 |
| 沿對極線搜尋 | 立體匹配、密集重建 |
| 對應點滿足 $\mathbf x'^{\mathsf T}F\mathbf x'' = 0$ | 2-37 從點對應直接估 $F$、$E$ |

---

## 附：本集一句話總結

> **對極幾何：兩投影中心的連線是對極軸，它和 3D 點決定對極平面；對極平面和影像平面的交線是對極線，另一台相機中心的像是極點（所有對極線都通過它）。用基本矩陣算：$\boldsymbol l' = F\mathbf x''$、$\boldsymbol l'' = F^{\mathsf T}\mathbf x'$，極點是 $F$ 的左右零向量（$F^{\mathsf T}\boldsymbol e' = 0$、$F\boldsymbol e'' = 0$）。對應點只要沿對極線找，2D 搜尋變 1D。**

---

*筆記依據 Cyrill Stachniss「Mobile Sensing and Robotics 2」Epipolar Geometry Basics 錄影逐字稿（Whisper `medium.en`，24:35）、MVG §9.1–9.2 與《視覺 SLAM 十四講》§7.3.1 整理。*
