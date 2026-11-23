---
course: Mobile Sensing and Robotics 2（Uni Bonn, Summer 2021）
episode: 2-37
lecture: Direct Solution for Estimating the Fundamental and Essential Matrix
date: 待補（2021 夏季學期）
video: https://youtu.be/zX5NeY-GTO0
notes: MVG 第 11 章 §11.1–11.2（書頁 279–282，PDF 頁 297–300）、§9.6（書頁 257–259，PDF 頁 275–277）；《視覺 SLAM 十四講》第 2 版 §7.3.2（書頁 168–170，PDF 頁 191–193）
---

# 第 2-37 集 · 基本矩陣與本質矩陣的直接解 [▶ 影片](https://youtu.be/zX5NeY-GTO0)

← 上一集：[2-35-epipolar-geometry](2-35-epipolar-geometry.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：（本系列最後一集）

> **課程**：Mobile Sensing and Robotics 2，Uni Bonn，2021 夏季學期 — 第 2-37 集
> **講者**：Cyrill Stachniss
> **來源**：YouTube 錄影逐字稿（1:02:47，Whisper `medium.en` 轉錄）＋ MVG §11.1–11.2、§9.6 ＋《視覺 SLAM 十四講》§7.3.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `【十四講補充】` 十四講有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

（記號沿用 2-33：$\mathbf x'^{\mathsf T}F\mathbf x'' = 0$。MVG 的 $F$ 是本課的轉置。）

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習：F 與共面約束](#1-複習f-與共面約束)
- [2. 八點演算法：建立線性系統](#2-八點演算法建立線性系統)
- [3. 用 SVD 解](#3-用-svd-解)
- [4. 強制秩 2](#4-強制秩-2)
- [5. 正規化座標](#5-正規化座標)
- [6. 退化情況](#6-退化情況)
- [7. 本質矩陣的八點演算法](#7-本質矩陣的八點演算法)
- [8. 七點與五點演算法](#8-七點與五點演算法)
- [9. 從 E 拆出 R 和 b](#9-從-e-拆出-r-和-b)
  - [9.1 四個解的幾何](#91-四個解的幾何)
  - [9.2 代數解（Hartley & Zisserman）](#92-代數解hartley--zisserman)
- [10. 總結](#10-總結)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 系列總結](#12-系列總結)

---

## 0. 這堂課要做什麼

只有一對影像和**點對應**（例如兩張巴黎的照片，紅點標出對應），不知道投影矩陣、內外參、物體大小，估計：

1. 未校正相機的**基本矩陣** $F$；
2. 已校正相機的**本質矩陣** $E$（大多數情況用這個）；
3. 從 $E$ 拆出旋轉 $R$ 和基線 $\boldsymbol b$（只有**方向**，不知道長度：$E$ 只有 5 個自由度 = 旋轉 3 ＋ 平移方向 2）。

---

## 1. 複習：F 與共面約束

[▶ 03:00](https://youtu.be/zX5NeY-GTO0?t=180)

$$
F = K'^{-\mathsf T}R'\,S_{\boldsymbol b}\,R''^{\mathsf T}K''^{-1}, \qquad \mathbf x'^{\mathsf T}F\,\mathbf x'' = 0
$$

- 兩點對應同一個真實點 ⇒ 乘積必為零。**反過來不成立**：乘積為零不代表是對應點（只是單向蘊含）[▶ 04:17](https://youtu.be/zX5NeY-GTO0?t=257)。
- 已知 $K, R, \boldsymbol b$ 或兩個投影矩陣時可直接算 $F$（2-33）。今天走另一條路：只用影像中的對應點估 $F$。

---

## 2. 八點演算法：建立線性系統

[▶ 05:24](https://youtu.be/zX5NeY-GTO0?t=324)

**給定**：$N$ 組對應 $(x'_n, y'_n) \leftrightarrow (x''_n, y''_n)$。**求**：$F$。

每組對應給一個共面約束：

$$
\begin{bmatrix} x'_n & y'_n & 1 \end{bmatrix}
\begin{bmatrix} f_{11} & f_{12} & f_{13} \\ f_{21} & f_{22} & f_{23} \\ f_{31} & f_{32} & f_{33} \end{bmatrix}
\begin{bmatrix} x''_n \\ y''_n \\ 1 \end{bmatrix} = 0
$$

- 座標是觀測（已知）；$F$ 的 9 個元素是未知數（齊次只定到比例，還有另一個約束）。
- 展開後，**每個 $f_{ij}$ 都只以線性形式出現**，係數是已知的座標乘積 → 把矩陣的未知數排成向量（和 DLT 一樣）[▶ 08:00](https://youtu.be/zX5NeY-GTO0?t=480)：

$$
\boldsymbol a_n^{\mathsf T}\boldsymbol f = 0
$$

**Kronecker 積** [▶ 09:51](https://youtu.be/zX5NeY-GTO0?t=591)：不用手動排係數，用標準運算：

$$
\boldsymbol a_n^{\mathsf T} = (\mathbf x''_n \otimes \mathbf x'_n)^{\mathsf T}, \qquad \boldsymbol f = \operatorname{vec}(F)
$$

（$\operatorname{vec}$ 把矩陣按**欄**堆成向量。驗證，筆記補：$\mathbf x'^{\mathsf T}F\mathbf x'' = \sum_{i,j} x'_i F_{ij} x''_j$；$\operatorname{vec}(F)$ 中 $F_{ij}$ 的位置是 $3(j-1) + i$，$\mathbf x'' \otimes \mathbf x'$ 在同一位置是 $x''_j x'_i$，對得上。）

- 【口頭】這對所有 $\boldsymbol u^{\mathsf T}M\boldsymbol v$ 形式的乘積都成立，估計這類量時很好用 [▶ 10:57](https://youtu.be/zX5NeY-GTO0?t=657)。

**堆疊**：$N$ 組對應 →

$$
A\,\boldsymbol f = \mathbf 0, \qquad A = \begin{bmatrix} \boldsymbol a_1^{\mathsf T} \\ \vdots \\ \boldsymbol a_N^{\mathsf T} \end{bmatrix} \in \mathbb R^{N \times 9}
$$

【課本補充】MVG §11.1（書頁 279）用它的記號（$\mathbf x'^{\mathsf T}F_{\text{MVG}}\mathbf x = 0$，$\mathbf x' = (x', y', 1)$ 在第二張）把係數寫成 $(x'x,\ x'y,\ x',\ y'x,\ y'y,\ y',\ x,\ y,\ 1)\cdot\boldsymbol f = 0$（$\boldsymbol f$ 按**列**排，式 11.2–11.3）——和 Kronecker 寫法差在記號的轉置與排列順序，內容相同。

【十四講補充】§7.3.2（書頁 168–169）對本質矩陣用歸一化座標 $\boldsymbol x_1 = [u_1, v_1, 1]$、$\boldsymbol x_2 = [u_2, v_2, 1]$（$\boldsymbol x_2^{\mathsf T}E\boldsymbol x_1 = 0$）：$[u_2u_1, u_2v_1, u_2, v_2u_1, v_2v_1, v_2, u_1, v_1, 1]\cdot\boldsymbol e = 0$（式 7.12），8 個方程構成 $8 \times 9$ 係數矩陣（式 7.13），$\boldsymbol e$ 在它的零空間中；係數矩陣秩 8 時零空間是一維（一條線），和 $\boldsymbol e$ 的尺度等價一致。

---

## 3. 用 SVD 解

[▶ 12:05](https://youtu.be/zX5NeY-GTO0?t=725)

- 齊次系統 → **SVD**：$A = UDV^{\mathsf T}$。有零空間時，某個奇異值為 0，對應的奇異向量（$V$ 的最後一欄，或 $V^{\mathsf T}$ 的最後一列，看工具怎麼回傳）就是 $\boldsymbol f$。
- 維度：$A$ 是 $N \times 9$；$U$ 是 $N \times N$；$D$ 是 $N \times 9$（9 個奇異值，由大到小排）；$V^{\mathsf T}$ 是 $9 \times 9$ [▶ 15:37](https://youtu.be/zX5NeY-GTO0?t=937)。

**需要幾個點** [▶ 13:31](https://youtu.be/zX5NeY-GTO0?t=811)：$\boldsymbol f$ 有 9 個未知數；有解時 $A$ 秩最多 8 → 需要 **8 組對應**（產生 8 列）→ **八點演算法**。

**有雜訊時** [▶ 14:14](https://youtu.be/zX5NeY-GTO0?t=854)：超過 8 點時 $A$ 會滿秩（秩 9），不再有精確解 → 在 $\lVert\boldsymbol f\rVert = 1$ 下最小化 $\lVert A\boldsymbol f\rVert$ → 取**最小奇異值**對應的奇異向量 $\hat{\boldsymbol f}$。

**MATLAB 草稿** [▶ 17:06](https://youtu.be/zX5NeY-GTO0?t=1026)：

```matlab
function F = computeF(xp, xpp)   % xp: x'，xpp: x''（齊次）
  for n = 1:N
    A(n,:) = kron(xpp(:,n), xp(:,n))';
  end
  [U, D, V] = svd(A);
  Fa = reshape(V(:,9), 3, 3);    % 最小奇異值的奇異向量 → 近似的 F
  % 下一步：強制秩 2
```

---

## 4. 強制秩 2

[▶ 18:27](https://youtu.be/zX5NeY-GTO0?t=1107)

- 解出的只是**近似**：沒有真的解 $A\boldsymbol f = 0$ → 得到的矩陣一般**不是秩 2**，沒有零空間；但 $F$ 的零空間對對極幾何很重要（極點，2-35）。
- 要盡量少改動 $F$，但讓它秩不足：

$$
F_a = U_a\operatorname{diag}(d_1, d_2, d_3)V_a^{\mathsf T}
\quad\longrightarrow\quad
F = U_a\operatorname{diag}(d_1, d_2, 0)V_a^{\mathsf T}
$$

- 把最小的奇異值 $d_3$（通常本來就很小）**明確設為零** → 秩 2；在影響最小的方向上產生秩不足。

```matlab
  [Ua, Da, Va] = svd(Fa);
  F = Ua * diag([Da(1,1) Da(2,2) 0]) * Va';
end
```

- 這就是有名的**八點演算法**，至今仍很好實作、很流行 [▶ 22:33](https://youtu.be/zX5NeY-GTO0?t=1353)。

【課本補充】MVG §11.1.1（書頁 280–281）：$F$ 不奇異時，算出的對極線**不會交於同一個極點**（圖 11.1）。用 Frobenius 範數最小的修正：$F = U\operatorname{diag}(r, s, t)V^{\mathsf T}$（$r \ge s \ge t$）→ $F' = U\operatorname{diag}(r, s, 0)V^{\mathsf T}$ 是最接近 $F$ 的奇異矩陣。八點演算法 = (i) 線性解 ＋ (ii) 強制約束。§11.3 指出這種 SVD 修正在數值上不是最佳（$F$ 各元素受資料約束的程度不同），但簡單快速。

---

## 5. 正規化座標

[▶ 23:05](https://youtu.be/zX5NeY-GTO0?t=1385)

- 問題：條件數可能很差。例：1200 萬像素相機（4000 × 3000），點座標像 $(1800, 1400)$，齊次的第三維是 1 → 各維數量級差很多 → 數值不穩定。
- 做法：換座標系讓各維大小相近：平移使所有點的**重心在 $(0, 0)$**，縮放使座標落在 **$[-1, 1]$**（例：2000 像素對應 1，點變成 $(0.9, 0.7, 1)$）。

$$
\hat{\mathbf x} = T\,\mathbf x
$$

- 在正規化座標中算出 $\hat F$，再轉回來 [▶ 25:51](https://youtu.be/zX5NeY-GTO0?t=1551)：

$$
\mathbf x'^{\mathsf T}F\mathbf x'' = \hat{\mathbf x}'^{\mathsf T}\,\underbrace{T'^{-\mathsf T}F\,T''^{-1}}_{\hat F}\,\hat{\mathbf x}''
\quad\Rightarrow\quad
F = T'^{\mathsf T}\,\hat F\,T''
$$

（式子依「$\mathbf x = T^{-1}\hat{\mathbf x}$ 代入」整理；講者口述「轉換的反矩陣出現在這裡，可以來回轉換」。）

- 【口頭】沒什麼特別，但**強烈建議**這樣做，避免數值不穩定 [▶ 26:58](https://youtu.be/zX5NeY-GTO0?t=1618)。

【課本補充】MVG §11.2 演算法 11.1（書頁 282）**正規化八點演算法**：(i) 每張影像各自平移、縮放，使重心在原點、到原點的 RMS 距離為 $\sqrt 2$；(ii)(a) 線性解、(b) 強制 $\det\hat F = 0$；(iii) 反正規化 $F = T'^{\mathsf T}\hat F'T$（MVG 記號）。建議在**反正規化之前**強制奇異性。原始的八點演算法是 Longuet-Higgins 提出的；成功的關鍵是仔細正規化，增加的複雜度微不足道。

---

## 6. 退化情況

[▶ 27:07](https://youtu.be/zX5NeY-GTO0?t=1627)

| 情況 | 後果 |
|---|---|
| **所有點在同一平面上**（類似 DLT） | $A$ 的秩可能小於 8 → 解不出來；接近平面也會數值不穩定。例：「fundamental matrix song」裡雪梨港灣大橋上的對應點都在一個平面上 |
| **只有旋轉、沒有平移** | 兩個投影中心相同，平移為零 → 無法重建 $F$ |

- 【口頭】追蹤相機運動時，如果相機靜止或只在原地轉動，八點演算法「不會是你的朋友」；要明確偵測這些情況，例如另外估旋轉 [▶ 29:22](https://youtu.be/zX5NeY-GTO0?t=1762)。
- `⚠️ 逐字稿缺字`：Whisper 寫 “Harper Bridge”，應為雪梨的 **Harbour Bridge**（港灣大橋）。

【課本補充】MVG §9.2.2（書頁 244）：兩相機中心相同時，$P'C = 0$，由 $F = [\boldsymbol e']_\times P'P^+$ 得 $F$ 為**零矩陣**——和「只有旋轉」的退化一致。

---

## 7. 本質矩陣的八點演算法

[▶ 31:13](https://youtu.be/zX5NeY-GTO0?t=1873)

- 大多數幾何重建都會先校正相機（問題變簡單）→ 用 $E$。

$$
E = R'\,S_{\boldsymbol b}\,R''^{\mathsf T} \quad\xrightarrow{\ R' = I,\ R'' = R\ }\quad E = S_{\boldsymbol b}\,R^{\mathsf T}, \qquad {}^{k}\mathbf x'^{\mathsf T}E\,{}^{k}\mathbf x'' = 0
$$

- 點用**相機座標系**：${}^{k}\mathbf x = K^{-1}\mathbf x$（校正矩陣已套用）；第三個分量不是 1，而是相機常數（講者口述）[▶ 34:36](https://youtu.be/zX5NeY-GTO0?t=2076)。
- 5 個自由度（旋轉 ＋ 基線方向）。

**步驟**：前半段和 $F$ **完全一樣**（建 $A$、SVD、近似的 $E$），只有最後強制約束不同 [▶ 35:33](https://youtu.be/zX5NeY-GTO0?t=2133)：

| | 強制成 |
|---|---|
| $F$ | $U\operatorname{diag}(d_1, d_2, 0)V^{\mathsf T}$（秩 2） |
| $E$ | $U\operatorname{diag}(1, 1, 0)V^{\mathsf T}$（秩 2 **且兩個非零奇異值相等**；齊次 → 可以設為 1） |

- 正規化也一樣：平移、縮放點座標，最後把 $\hat E$ 轉回來。

**$E$ 的性質** [▶ 38:48](https://youtu.be/zX5NeY-GTO0?t=2328)：齊次；$\det E = 0$；秩 2；兩個相同的非零奇異值（可以設為 1）；還有一個由反對稱矩陣導出、$E$ 必須滿足的額外方程（投影片上有，講者沒有念出、也沒有推導，說推導在 Förstner 的書裡）→ `⚠️ 待確認`。

【課本補充】MVG §9.6.1 結果 9.17（書頁 257）：$3 \times 3$ 矩陣是本質矩陣 ⇔ **兩個奇異值相等、第三個為零**。證明：$E = SR$（$S$ 反對稱），$S = kUZU^{\mathsf T}$，$Z = \operatorname{diag}(1, 1, 0)W$（差正負號）→ $E = U\operatorname{diag}(1, 1, 0)(WU^{\mathsf T}R)$ 就是兩奇異值相等的 SVD。看起來 $U, V$ 各 3 個自由度共 6 個，但兩奇異值相等使 SVD 不唯一（有一個參數的一族），所以仍是 5 個。

【十四講補充】§7.3.2（書頁 170）：線性解出的 $E$ 奇異值不一定是 $(\sigma, \sigma, 0)$；對它做 SVD 得 $\operatorname{diag}(\sigma_1, \sigma_2, \sigma_3)$（$\sigma_1 \ge \sigma_2 \ge \sigma_3$），取

$$
E = U\operatorname{diag}\!\left( \tfrac{\sigma_1 + \sigma_2}{2},\ \tfrac{\sigma_1 + \sigma_2}{2},\ 0 \right)V^{\mathsf T} \qquad (7.16)
$$

等於把矩陣投影到 $E$ 所在的流形上；更簡單的做法是直接取 $\operatorname{diag}(1, 1, 0)$（因為尺度等價）——講者用的是後者。

---

## 8. 七點與五點演算法

[▶ 39:50](https://youtu.be/zX5NeY-GTO0?t=2390)

- $F$ 只有 7 個自由度、$E$ 只有 5 個，理論上應該有用更少點的演算法。
- **七點演算法**（$F$）：存在，比八點稍複雜。
- **五點演算法**（$E$）：**Nistér**（2003、2004 年）提出，今天已是已校正相機相對定向的**標準解法**：幾乎所有從單相機影像估平移和旋轉的方法，內部都用它。歸結成解一個 **10 次多項式** → 最多 10 個解；推導約一兩頁。OpenCV 有現成實作。
- `⚠️ 逐字稿缺字`：Whisper 寫 “NISTAS”、“NISTAR”、“NISTIR”、“Mr. Skrup”，應為 **Nistér**。

**為什麼 5 點比 8 點重要** [▶ 42:04](https://youtu.be/zX5NeY-GTO0?t=2524)：

- 只靠描述子算對應一定會有錯 → 錯的關聯導致錯的 $E$ → 要用 **RANSAC**（2-22）：取 5 組對應假設是對的、算 $E$，用共面約束看其他點是否（接近）為零、數內點，重複。
- 抽 8 個全是內點比抽 5 個難得多 → 最小子集越小，RANSAC 越有效率，試驗次數大幅減少。

【課本補充】MVG §11.1.2（書頁 281）的**七點演算法**：7 組對應 → $7 \times 9$ 的 $A$ 秩 7，解空間是二維的 $\alpha F_1 + (1 - \alpha)F_2$；再用 $\det(\alpha F_1 + (1 - \alpha)F_2) = 0$ 得到 $\alpha$ 的**三次方程** → 1 或 3 個實解。MVG 的強健演算法（§11.6）就用這個最小解放進 RANSAC。

【十四講補充】§7.3.2（書頁 168、170）：$E$ 有 5 個自由度 → 最少 5 對點；但 $E$ 的內在性質是**非線性**的，估計時很麻煩 → 只考慮尺度等價、用 8 對點 = 經典八點法（只用 $E$ 的線性性質，可以在線性代數框架下解）。五點法形式複雜；平常有幾十甚至上百對匹配點，從 8 減到 5 意義不明顯，所以書中只介紹八點法。（和講者「在 RANSAC 中 5 點很重要」的觀點互補：十四講講的是不考慮離群值的情況。）

---

## 9. 從 E 拆出 R 和 b

[▶ 43:45](https://youtu.be/zX5NeY-GTO0?t=2625)

目的：估相機的軌跡，要知道相機實際怎麼動 → $E \to (S_{\boldsymbol b}, R)$；基線只能到比例（通常取單位長）。

### 9.1 四個解的幾何

[▶ 44:38](https://youtu.be/zX5NeY-GTO0?t=2678)

- 數學上不只一個解；其他解在幾何上說得通，但對一般相機**物理上不合理**，可以排除到只剩一個。
- 想要的解：相機 1、相機 2、兩條射線交於一個在兩台相機**前方**的點。
- 其他解來源：$\boldsymbol b$ 只定到比例（齊次）→

| 變化 | 結果 |
|---|---|
| $\boldsymbol b \to -\boldsymbol b$ | 兩條射線在相機**後方**相交（就像我面對你時，對應點在我背後）——相機朝前看，物理上不合理，但數學模型允許 |
| 相機 2 轉 $\pi$（或某向量反向，等價） | 交點在很遠處，一台相機朝後看 |
| 兩者都做 | 交點又在後方 |

- 只有一個解：兩台相機都朝前看，交點在兩台相機前方。

### 9.2 代數解（Hartley & Zisserman）

[▶ 48:19](https://youtu.be/zX5NeY-GTO0?t=2899)

$E$ 的 SVD：

$$
E = U\operatorname{diag}(1, 1, 0)V^{\mathsf T}
$$

$U, V$ 是旋轉矩陣。定義兩個「天上掉下來的」矩陣（不是推出來的，知道它們就能得到解）：

$$
Z = \begin{bmatrix} 0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}\ (\text{反對稱}), \qquad
W = \begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}\ (\text{繞 } z \text{ 軸的旋轉})
$$

- $ZW = \operatorname{diag}(1, 1, 0)$（驗證，筆記補：$Z$ 第一列 $(0, 1, 0)$ 乘 $W$ = $W$ 的第二列 $(1, 0, 0)$；第二列 $(-1, 0, 0)$ 乘 $W$ = $-W$ 的第一列 $(0, 1, 0)$；第三列為零）。

**拆解** [▶ 50:16](https://youtu.be/zX5NeY-GTO0?t=3016)：

$$
E = U\,ZW\,V^{\mathsf T} = U Z\,\underbrace{U^{\mathsf T}U}_{I}\,W V^{\mathsf T} = \underbrace{(UZU^{\mathsf T})}_{\text{反對稱}}\ \underbrace{(UWV^{\mathsf T})}_{\text{旋轉}}
$$

- $UZU^{\mathsf T}$：旋轉 × 反對稱 × 旋轉的轉置 → 仍是**反對稱**矩陣 → $S_{\boldsymbol b}$。
- $UWV^{\mathsf T}$：三個旋轉矩陣的乘積 → 仍是**旋轉**矩陣。
- 正好是一般參數化 $E = S_{\boldsymbol b}R^{\mathsf T}$ 的形式。$U, V$ 來自 SVD，$Z, W$ 自己定義 → 全部已知。
- （在本課 $E = S_{\boldsymbol b}R^{\mathsf T}$ 的寫法下，第二個因子對應 $R^{\mathsf T}$；講者直接稱它「旋轉矩陣」。以下不是逐字稿內容，是依 2-33 的定義對照的提醒。）

**四種寫法** [▶ 52:44](https://youtu.be/zX5NeY-GTO0?t=3164)：$\operatorname{diag}(1, 1, 0)$ 也可以寫成 $(-Z^{\mathsf T})W$（反對稱矩陣的負轉置就是它自己）、$Z^{\mathsf T}W^{\mathsf T}$ 等——自己動手乘，都會得到 $\operatorname{diag}(1, 1, 0)$。於是

$$
S_{\boldsymbol b} \in \{\, UZU^{\mathsf T},\ \ UZ^{\mathsf T}U^{\mathsf T} \,\}, \qquad
\text{旋轉} \in \{\, UWV^{\mathsf T},\ \ UW^{\mathsf T}V^{\mathsf T} \,\}
$$

組合起來 → **四組解** $E_1, \dots, E_4$。

**演算法** [▶ 55:23](https://youtu.be/zX5NeY-GTO0?t=3323)：

```
1. SVD(E) = U D Vᵀ
2. 正規化 U、V，確保是正確方向的旋轉（依 SVD 實作而定）
3. 建四組解：S ∈ {U Z Uᵀ, U Zᵀ Uᵀ}，旋轉 ∈ {U W Vᵀ, U Wᵀ Vᵀ}
4. 對每組解，三角化點，看點在相機前方還是後方
5. 只有一組讓點在兩台相機前方 → 物理上合理的解
```

（「正規化 U、V」以下不是逐字稿內容，是依 MVG 的常見做法補的：若 $\det U < 0$ 或 $\det V < 0$，把它乘 $-1$，讓它成為行列式 +1 的旋轉；$E$ 只定到正負號，所以這樣做不影響。）

【課本補充】MVG §9.6.2–9.6.3（書頁 258–259）：

- **結果 9.18**：$E = U\operatorname{diag}(1, 1, 0)V^{\mathsf T}$ 時，（不計正負號）只有兩種分解 $E = SR$：$S = UZU^{\mathsf T}$，$R = UWV^{\mathsf T}$ 或 $UW^{\mathsf T}V^{\mathsf T}$（式 9.14）。證明：$S$ 的左零空間必須和 $E$ 相同 → $S = UZU^{\mathsf T}$；$R = UXV^{\mathsf T}$ → $ZX = \operatorname{diag}(1, 1, 0)$ → $X = W$ 或 $W^{\mathsf T}$。
- $S = UZU^{\mathsf T}$ 的 Frobenius 範數是 $\sqrt 2$ → $S = [\boldsymbol t]_\times$ 時 $\lVert\boldsymbol t\rVert = 1$（方便的基線正規化）；$S\boldsymbol t = 0$ → $\boldsymbol t = U(0, 0, 1)^{\mathsf T} = \boldsymbol u_3$。$E$ 的正負號、因此 $\boldsymbol t$ 的正負號無法決定。
- **結果 9.19**：$P = [I \mid 0]$ 時，$P' \in \{[UWV^{\mathsf T} \mid +\boldsymbol u_3],\ [UWV^{\mathsf T} \mid -\boldsymbol u_3],\ [UW^{\mathsf T}V^{\mathsf T} \mid +\boldsymbol u_3],\ [UW^{\mathsf T}V^{\mathsf T} \mid -\boldsymbol u_3]\}$。
- 幾何（圖 9.12）：前兩個只差在平移方向相反；第一和第三個是「**twisted pair**」：$V\!W^{\mathsf T}W^{\mathsf T}V^{\mathsf T} = V\operatorname{diag}(-1, -1, 1)V^{\mathsf T}$ 是繞基線轉 180°。重建點只在四個解中的**一個**同時位於兩台相機前方 → 用**一個點**測試就夠了。

【十四講補充】§7.3.2（書頁 169–170）同樣的四個解：$\boldsymbol t_1^\wedge = UR_Z(\tfrac{\pi}{2})\Sigma U^{\mathsf T}$、$R_1 = UR_Z^{\mathsf T}(\tfrac{\pi}{2})V^{\mathsf T}$；$\boldsymbol t_2^\wedge = UR_Z(-\tfrac{\pi}{2})\Sigma U^{\mathsf T}$、$R_2 = UR_Z^{\mathsf T}(-\tfrac{\pi}{2})V^{\mathsf T}$（式 7.15，$R_Z(\tfrac{\pi}{2})$ 是繞 $Z$ 軸轉 90°）；$-E$ 和 $E$ 等價，$\boldsymbol t$ 取負號也一樣 → 共 4 個解。圖 7-10：只有第一種解 $P$ 在兩台相機中都有**正深度**；把任一點代入四種解、檢查深度就能確定哪個正確。

---

## 10. 總結

[▶ 56:58](https://youtu.be/zX5NeY-GTO0?t=3418)

- 只用影像資料（點對應）算相對定向，不需要場景中已知的 3D 點（後方交會、DLT 才需要）。
- 已校正相機：用影像 1→2、2→3、3→4…… 的對應，可以估相機的運動，但只到一個比例（只知道基線方向和相機旋轉）→ **視覺里程計**的基礎。再用場景知識或其他感測器（IMU、GPS……）提供尺度，就能得到真實世界中完整 6 自由度的剛體運動。

| 方法 | 點數 | 約束 |
|---|---|---|
| $F$：八點演算法 | ≥ 8 | 秩 2 |
| $E$：八點演算法 | ≥ 8 | 兩奇異值相等（設為 1）、第三個為 0 |
| $E$：Nistér 五點演算法 | 5 | 今天已校正相機的黃金標準 |
| $E \to R, \boldsymbol b$ | — | Hartley & Zisserman：四組解，選點在兩相機前方的 |

**直接解的角色** [▶ 59:04](https://youtu.be/zX5NeY-GTO0?t=3544)：

- 不需初始猜測，但統計上**不是最佳**（例如不考慮點定位的不確定性橢圓）。
- 常和 **RANSAC** 結合：分出內點和離群值，丟掉離群值。
- 內點和直接解當作後續**最小平方**的初始猜測：只用內點、考慮不確定性，得到更好的 $R$、$\boldsymbol b$ 估計和它們的不確定性；可以給量測更可信的點較高權重。
- 【口頭】直接解的兩個關鍵優點：(1) 提供最小平方「非常需要」的初始猜測；(2) 和 RANSAC 結合分出內點與離群值——這是讓最小平方收斂到正解的基礎（輸入要沒有離群值）[▶ 1:00:32](https://youtu.be/zX5NeY-GTO0?t=3632)。
- 這些直接解是**視覺里程計**（串接相機的相對定向、描述相機在世界中的運動）的基礎；自駕車、移動機器人裝相機就能估下一刻的位置（到比例，再用 GPS、IMU 補尺度）。

**延伸閱讀**：Förstner & Wrobel *Photogrammetric Computer Vision* 第 12.3 節；Hartley〈In Defense of the Eight-Point Algorithm〉（八點演算法相對於少點演算法的優點）；Nistér 的五點演算法論文；Förstner 的 Photogrammetry II 講義。

- `⚠️ 逐字稿缺字`：Whisper 寫 “Hartley Scissor / Sizemann / Harley-Sizemann”，應為 **Hartley & Zisserman**；“Wolfgang Ferschner / Furstner” 應為 **Wolfgang Förstner**。

---

## 11. 一頁速查表

### 11.1 八點演算法（F）

$$
\boldsymbol a_n = \mathbf x''_n \otimes \mathbf x'_n, \quad \boldsymbol f = \operatorname{vec}(F), \quad A\boldsymbol f = 0
$$

| 步驟 | 做法 |
|---|---|
| 0 | 正規化：$\hat{\mathbf x} = T\mathbf x$（重心 0、座標在 $[-1, 1]$） |
| 1 | 建 $A$（$N \times 9$，$N \ge 8$） |
| 2 | $A = UDV^{\mathsf T}$，$\boldsymbol f$ = $V$ 最後一欄 → $\hat F_a$ |
| 3 | $\hat F_a = U_aD_aV_a^{\mathsf T}$，$\hat F = U_a\operatorname{diag}(d_1, d_2, 0)V_a^{\mathsf T}$ |
| 4 | 反正規化：$F = T'^{\mathsf T}\hat FT''$ |

關鍵一步：$\mathbf x'^{\mathsf T}F\mathbf x'' = (\mathbf x'' \otimes \mathbf x')^{\mathsf T}\operatorname{vec}(F)$ → 對 $F$ 的元素**線性**。

### 11.2 E

點用 ${}^k\mathbf x = K^{-1}\mathbf x$；步驟 3 改成 $E = U_a\operatorname{diag}(1, 1, 0)V_a^{\mathsf T}$。

### 11.3 退化

共平面、純旋轉（$F = 0$）。

### 11.4 E → R, b

$$
E = U\operatorname{diag}(1,1,0)V^{\mathsf T}, \quad Z = \begin{bmatrix} 0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}, \quad W = \begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}, \quad ZW = \operatorname{diag}(1,1,0)
$$

$$
S_{\boldsymbol b} \in \{UZU^{\mathsf T}, UZ^{\mathsf T}U^{\mathsf T}\}, \quad \text{旋轉} \in \{UWV^{\mathsf T}, UW^{\mathsf T}V^{\mathsf T}\}, \quad \boldsymbol b \propto \pm\boldsymbol u_3
$$

四組解 → 三角化一點，選兩相機前方（正深度）的那組。

### 11.5 最小點數與 RANSAC

| 演算法 | 點數 | 解的個數 |
|---|---|---|
| 八點（$F$ 或 $E$） | 8 | 1 |
| 七點（$F$） | 7 | 1 或 3 |
| 五點（$E$，Nistér） | 5 | ≤ 10 |

$e = 50\%$、$p = 99\%$ 時 RANSAC 次數（MVG 表 4.3）：$s = 5$ 要 146 次、$s = 8$ 要 1177 次。

---

## 12. 系列總結

本集是 MSR2 播放清單的最後一集長片。MSR2 的脈絡：

| 主題 | 集數 |
|---|---|
| SLAM 與最小平方 | 2-03、2-05 |
| 點雲對齊（ICP） | 2-07、2-08、2-10 |
| 圖式 SLAM | 2-11、2-12、2-14、2-15 |
| 視覺特徵與 RANSAC | 2-17、2-20、2-22 |
| 單相機幾何 | 2-24、2-27、2-29、2-31 |
| 雙相機幾何 | 2-33、2-35、2-37 |

---

## 附：本集一句話總結

> **八點演算法：每組對應給一個對 $F$ 線性的方程 $(\mathbf x'' \otimes \mathbf x')^{\mathsf T}\operatorname{vec}(F) = 0$，≥8 點用 SVD 取最小奇異向量，再把最小奇異值設 0 強制秩 2（點座標要先正規化）；$E$ 用相機座標、強制成 $\operatorname{diag}(1, 1, 0)$。實務上用 Nistér 五點演算法配 RANSAC。最後 $E = (UZU^{\mathsf T})(UWV^{\mathsf T})$ 拆出四組 $(S_{\boldsymbol b}, R)$，選讓點落在兩台相機前方的那組；基線長度（尺度）需要外部資訊。**

---

## ⚠️ 待確認清單

1. [▶ 39:12](https://youtu.be/zX5NeY-GTO0?t=2352) 本質矩陣由反對稱矩陣導出的額外約束式：投影片上有，講者沒有念出也沒有推導（說在 Förstner 的書裡）；BRIEF 列的來源中，MVG 只給「兩奇異值相等、第三為零」的刻畫，沒有這條式子。待補。

---

*筆記依據 Cyrill Stachniss「Mobile Sensing and Robotics 2」Direct Solution for Estimating the Fundamental and Essential Matrix 錄影逐字稿（Whisper `medium.en`，1:02:47）、MVG §11.1–11.2、§9.6 與《視覺 SLAM 十四講》§7.3.2 整理。*
