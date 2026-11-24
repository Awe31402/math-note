---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 31
lecture: Lecture 11 (Part 1) – Two-view and multi-view stereo
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/OpZs7kfjFPA
notes: 講者說內容取自 UIUC、多倫多大學的課程投影片（BRIEF 沒列，未查）；可對照 MVG §11.12 影像校正（書頁 302–308，PDF 頁 320–326）
---

# 第 31 集 · Lecture 11 (Part 1)：雙視角 stereo、視差、stereo 校正 [▶ 影片](https://youtu.be/OpZs7kfjFPA)

← 上一集：[30-sfm-bundle-adjustment-part4](30-sfm-bundle-adjustment-part4.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[32-stereo-part2](32-stereo-part2.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 31 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（49:12，Whisper `medium.en` 轉錄）＋ MVG §11.12（只對照校正）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 雙視角 stereo 的問題](#1-雙視角-stereo-的問題)
- [2. 為什麼稠密對應很難](#2-為什麼稠密對應很難)
- [3. 最簡單的情況：極線 = 掃描線](#3-最簡單的情況極線--掃描線)
  - [3.1 條件：R = I、t = (T, 0, 0)](#31-條件r--it--t-0-0)
  - [3.2 用 E 證明 v = v'](#32-用-e-證明-v--v)
  - [3.3 視差、只搜尋一半](#33-視差只搜尋一半)
- [4. Stereo 校準（calibration）](#4-stereo-校準calibration)
- [5. Stereo 校正（rectification）](#5-stereo-校正rectification)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/OpZs7kfjFPA?t=0)

Lecture 11 的目標（四集合起來）：

| 目標 | 本集？ |
|---|---|
| **stereo 校正**、沿掃描線找對應得到**視差圖** | ✅ |
| 從視差圖算深度 | 第 32 集 |
| **掃描線最佳化**、**半全域匹配（SGM）**讓視差圖全域一致 | 第 33 集 |
| **平面掃描（plane sweeping）**做多視角 stereo，得到稠密 3D 重建 | 第 34 集 |

講者說內容主要取自 UIUC 和多倫多大學的課程；平面掃描依 CVPR 2007 的論文；推薦 Furukawa 2015 年的多視角 stereo 教學（免費線上取得）。

⚠️ 逐字稿缺字：Whisper 把 Furukawa 寫成 “Furugawa”、depth 寫成 “dead”。

---

## 1. 雙視角 stereo 的問題

[▶ 01:20](https://youtu.be/OpZs7kfjFPA?t=80)

**給定**：

- 左影像 $I_L$、右影像 $I_R$，有很大的重疊視野。
- 兩台相機的相對位姿 $R$、$\mathbf{t}$（**有絕對尺度**），內參 $K$、$K'$。

**求**：**稠密 3D 點雲**。中間步驟是**視差圖（disparity map）**，等價於**深度圖（depth map）**。

【口頭】[▶ 02:40](https://youtu.be/OpZs7kfjFPA?t=160) 背景：

- 立體視覺對生物很重要：兩隻眼睛讓人感知深度、安全移動。
- 1833 年 Charles Wheatstone 發明立體鏡（stereogram）：兩張同時拍、位置稍微錯開的照片，透過特殊眼鏡看就有深度感。
- 演變成今天的 **3D 電影**：左右影像用紅、藍兩色疊在一起，戴眼鏡看就有深度。

**和第 16–19 集的關係** [▶ 06:13](https://youtu.be/OpZs7kfjFPA?t=373)：

- 有了 $R$、$\mathbf{t}$ → 有 $E$ 和 $P$、$P'$ → 用線性三角化得 3D 點（第 19 集）。
- 從 $E$ 分解的 $\mathbf{t}$ 只有方向；但這裡 $\mathbf{t}$ 有**絕對尺度**，所以三角化出來是**公制**尺度。

**設定** [▶ 07:56](https://youtu.be/OpZs7kfjFPA?t=476)：

- 兩台相機**剛性**固定在一個架子上，基線（$R$、$\mathbf{t}$）已知。
- 例：市售的 Bumblebee 2 stereo 相機。出廠前廠商就做好校準和校正（本集後半講）。
- **目標**：選一張當**參考視角**（通常是左圖），求參考影像**每個像素**的深度。
- 深度圖：越亮表示越近（例如近處的草地比遠處亮）。

---

## 2. 為什麼稠密對應很難

[▶ 11:03](https://youtu.be/OpZs7kfjFPA?t=663)

| | 雙視角幾何（第 16–19 集） | 雙視角 stereo |
|---|---|---|
| 對應點 | **稀疏**的特徵點 | 參考影像的**每個像素** |
| 用來 | 估 $E$／$F$、三角化少數點 | 每個像素都三角化 → 稠密深度 |

**直接做法** [▶ 12:49](https://youtu.be/OpZs7kfjFPA?t=769)（對參考影像一個像素 $\mathbf{x}$）：

1. 從 $R,\mathbf{t},K,K'$ 算 $E$，再得 $F$。
2. 算極線 $\mathbf{l}'=F\mathbf{x}$。
3. 拿 $\mathbf{x}$ 周圍的小方塊（patch），**沿極線滑動**，找外觀最相似的位置。
4. 用 $P$、$P'$ 三角化得 3D 點和深度 $Z$。

- 一般情況下，每個像素的極線都不同（第 16 集）→ 每個像素都要算一條極線再沿它搜尋 → **很慢**。

---

## 3. 最簡單的情況：極線 = 掃描線

[▶ 15:21](https://youtu.be/OpZs7kfjFPA?t=921)

若極線剛好是**同一列的掃描線**：參考影像的點 $\mathbf{x}$ 在右圖的對應點，就在**同一個 $y$ 座標**的那一列上。不必算極線，直接把 patch 沿同一列滑動就好。

### 3.1 條件：R = I、t = (T, 0, 0)

[▶ 18:30](https://youtu.be/OpZs7kfjFPA?t=1110)

- **純平移**（第 17 集）：$R=I$，兩台相機的**主軸平行**。
- 兩條極線同高 → $y$ 方向沒有平移。
- 兩個影像平面共面 → $z$ 方向沒有平移；兩台相機**焦距相同**。
- 只剩 $x$ 方向的平移：$\mathbf{t}=(T,0,0)^\mathsf{T}$。

### 3.2 用 E 證明 v = v'

[▶ 24:06](https://youtu.be/OpZs7kfjFPA?t=1446)

極線約束（第 18 集，正規化座標）：$\mathbf{x}'^\mathsf{T}E\mathbf{x}=0$，$E=[\mathbf{t}]_\times R$。代 $R=I$、$\mathbf{t}=(T,0,0)^\mathsf{T}$：

$$
E=[\mathbf{t}]_\times=\begin{pmatrix}0&0&0\\0&0&-T\\0&T&0\end{pmatrix}
$$

只有兩個非零元素。代入（$\mathbf{x}=(u,v,1)^\mathsf{T}$、$\mathbf{x}'=(u',v',1)^\mathsf{T}$）：

$$
\begin{pmatrix}u'&v'&1\end{pmatrix}\begin{pmatrix}0&0&0\\0&0&-T\\0&T&0\end{pmatrix}\begin{pmatrix}u\\v\\1\end{pmatrix}=\begin{pmatrix}u'&v'&1\end{pmatrix}\begin{pmatrix}0\\-T\\Tv\end{pmatrix}=-Tv'+Tv=0
$$

$$
\Longrightarrow\quad Tv'=Tv\quad\Longrightarrow\quad v'=v
$$

- 兩張圖對應點的 **$y$ 座標相同** → 極線是同一條水平掃描線。

（$E$ 的元素和代入的中間步驟依 $[\mathbf{t}]_\times$ 的定義補上；逐字稿只說「得到這個只有兩個非零元素的矩陣，代入後 $Tv'=Tv$」。）

**幾何** [▶ 26:46](https://youtu.be/OpZs7kfjFPA?t=1606)：左圖點的反投影光線投到右圖，是同一列的極線；右圖點反過來也一樣，兩條極線對齊在同一條掃描線上。

### 3.3 視差、只搜尋一半

[▶ 28:30](https://youtu.be/OpZs7kfjFPA?t=1710)

- 對應點 $x$（左）和 $x'$（右）的 $x$ 座標差叫**視差（disparity）**：
$$
d=x-x'
$$
- 對參考影像每個像素找到對應，把 $d$ 記在一張表上 → **視差圖（disparity map）**。
- **不必搜尋整條掃描線**：$d$ 一定 $>0$。若 $d<0$，三角化出來的點會在相機**後方**（深度為負），不可能。所以只在 $x'<x$ 那一側搜尋。

> 以下**不是逐字稿內容**，是說明：這裡假設右相機在左相機的右邊（基線沿 $+x$）。點投到左圖會比投到右圖更靠右，所以 $x>x'$；下一集推導 $Z=fT/d$ 會看到 $d>0$ 和深度為正是同一件事。

⚠️ 逐字稿缺字 [▶ 20:28](https://youtu.be/OpZs7kfjFPA?t=1228)：講者說「$x-x'=t$ 是 $x$ 方向的相對平移」，把像素座標差（視差）和平移量混在一起；依上下文，平移是 $T$、像素座標差是視差 $d$，兩者的關係是 $d=fT/Z$（下一集）。

---

## 4. Stereo 校準（calibration）

[▶ 31:53](https://youtu.be/OpZs7kfjFPA?t=1913)

實際的兩台相機一般**不平行**（$R\neq I$、$\mathbf{t}\neq(T,0,0)$）。要先**校準**、再**校正**，把它們「數學上」對齊成平行。

**Stereo 校準的步驟**：

1. **各自的內參** [▶ 33:06](https://youtu.be/OpZs7kfjFPA?t=1986)：拿棋盤格在兩台相機前移動，用 Zhang 方法（第 12 集）分別求 $K$、$K'$。
   - 即使同廠牌同型號，兩台相機的內參也不會完全一樣。
   - 同時求兩台各自的 **5 個畸變參數**（徑向、切向）。
2. **去畸變** [▶ 34:31](https://youtu.be/OpZs7kfjFPA?t=2071)：用畸變參數把影像校正成像素排列整齊的樣子（第 12 集）。
3. **外參** [▶ 35:17](https://youtu.be/OpZs7kfjFPA?t=2117)：
   - 在兩張去畸變的影像上找稀疏對應，用 **RANSAC + 8 點法**求 $E$（第 18 集）。
   - 用 $E$ 而不是 $F$：內參已知；$F$ 有射影模糊，$E$ 沒有。
   - 分解 $E$ 得四組解，用一個點在兩相機前方挑出正確的 $R,\mathbf{t}$。
4. **平移的尺度** [▶ 37:10](https://youtu.be/OpZs7kfjFPA?t=2230)：$E$ 分解的 $\mathbf{t}$ 只到尺度。但對應點來自棋盤格，**棋盤格方格大小已知**——三角化（到尺度）後，用一對點的已知距離做相似變換，就得到公制尺度的 $\mathbf{t}$。

---

## 5. Stereo 校正（rectification）

[▶ 38:23](https://youtu.be/OpZs7kfjFPA?t=2303)

**目標**：用校準得到的內參、外參，把兩張影像**數學上**對齊到同一個觀看平面，使所有極線都變成水平、同列的掃描線。

**流程示意** [▶ 39:24](https://youtu.be/OpZs7kfjFPA?t=2364)：原始影像（有畸變）→ 去畸變（方格變方正）→ 用 $R,\mathbf{t}$ 校正（極線對齊成水平掃描線）→ 裁切。之後對參考影像任一像素，只要沿另一張圖的同一列搜尋。

**「數學上」對齊的意思** [▶ 41:22](https://youtu.be/OpZs7kfjFPA?t=2482)：

- 不是真的去調相機——實體上不可能精確調成 $R=I$、$\mathbf{t}=(T,0,0)$。
- 而是對左、右影像各套一個 **homography** $H$、$H'$：
$$
\tilde{\mathbf{x}}=H\mathbf{x},\qquad\tilde{\mathbf{x}}'=H'\mathbf{x}'
$$
  得到新的影像，使 $\tilde{\mathbf{x}}$、$\tilde{\mathbf{x}}'$ 落在同一條水平極線上。

**校正後應滿足** [▶ 46:22](https://youtu.be/OpZs7kfjFPA?t=2782)：

1. 極線**互相平行**且**沿水平軸**。
2. 對應點有**相同的垂直座標**。

**怎麼找 $H$** [▶ 47:02](https://youtu.be/OpZs7kfjFPA?t=2822)：

- 校正後所有極線平行 → 它們交於**無窮遠** → **極點必須被送到無窮遠**。
- 而且極線是水平的 → 極點要送到 **$x$ 方向**的無窮遠點：
$$
H\mathbf{e}=\begin{pmatrix}1\\0\\0\end{pmatrix},\qquad H'\mathbf{e}'=\begin{pmatrix}1\\0\\0\end{pmatrix}
$$
  - 第三個分量 0 → 無窮遠點。
  - $(1,0)$ → $x$ 方向（$y$ 分量 0）。

（本集到 49:05 結束，下一集接著講怎麼具體求 $H$、$H'$。）

【課本補充】MVG §11.12.1：「把極點送到 $(1,0,0)^\mathsf{T}$」只用掉 $H$ 的一部分自由度，還剩 4 個自由度；選得不好會讓影像嚴重扭曲。MVG 建議讓 $H$ 在影像中心附近**盡量像剛體變換**（一階近似下只有旋轉加平移），重新取樣的影像看起來才和原圖相似。

---

## 6. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| 雙視角 stereo | 已知 $K,K',R,\mathbf{t}$（公制）→ 參考影像每個像素的深度 | — |
| 一般情況 | 每像素算極線 $F\mathbf{x}$、沿極線滑 patch | 慢 |
| 平行情況 | $R=I$、$\mathbf{t}=(T,0,0)^\mathsf{T}$ → 對應點 $v=v'$，沿同一列搜尋 | $E=[\mathbf{t}]_\times$，$\mathbf{x}'^\mathsf{T}E\mathbf{x}=T(v-v')=0$ |
| 視差 | $d=x-x'>0$，記成視差圖；只搜一側 | $d<0$ → 點在相機後方 |
| 校準 | 棋盤格 → 各自 $K$、畸變；去畸變；RANSAC 8 點法 → $E$ → $R,\mathbf{t}$；方格大小給尺度 | 用 $E$ 避開射影模糊 |
| 校正 | 兩張圖各套 $H$、$H'$，使 $H\mathbf{e}=H'\mathbf{e}'=(1,0,0)^\mathsf{T}$ | 平行極線交於無窮遠 |

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 校正的 homography $H,H'$ | 第 32 集（具體構造） |
| 視差 → 深度 | 第 32 集（$Z=fT/d$） |
| 沿掃描線比對 patch | 第 32–33 集（匹配代價、掃描線最佳化、SGM） |
| 多視角 | 第 34 集（平面掃描） |

---

## 附：本集一句話總結

> **雙視角 stereo 要替參考影像的每個像素找對應並三角化；一般情況每個像素都得算極線再搜尋，太慢——但兩台相機平行（$R=I$、$\mathbf{t}=(T,0,0)$）時，$E=[\mathbf{t}]_\times$ 讓極線約束化成 $v=v'$，對應點就在同一列，只要沿掃描線找視差 $d=x-x'>0$；實際相機不平行，所以先用棋盤格校準內參、畸變、外參（含公制尺度），再用兩個把極點送到 $(1,0,0)$ 的 homography 做 stereo 校正。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 11 (Part 1) 錄影逐字稿（Whisper `medium.en`，49:12）整理；校正部分對照 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §11.12。*
