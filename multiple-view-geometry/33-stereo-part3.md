---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 33
lecture: Lecture 11 (Part 3) – Two-view and multi-view stereo
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/hfQR7X8eH9s
notes: MVG 沒有對應章節（稠密 stereo 匹配不在 MVG 範圍），只依逐字稿
---

# 第 33 集 · Lecture 11 (Part 3)：互資訊的計算、視差轉深度、block matching 的失敗、掃描線最佳化 [▶ 影片](https://youtu.be/hfQR7X8eH9s)

← 上一集：[32-stereo-part2](32-stereo-part2.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[34-stereo-part4](34-stereo-part4.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 33 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（40:16，Whisper `medium.en` 轉錄）
> **標記說明**：
> - `【口頭】` 講者口頭補充、投影片沒有
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 用 Parzen 視窗估機率](#1-用-parzen-視窗估機率)
- [2. 四種代價的比較例子](#2-四種代價的比較例子)
- [3. 視差轉深度](#3-視差轉深度)
  - [3.1 相似三角形推導](#31-相似三角形推導)
  - [3.2 另一種情況](#32-另一種情況)
  - [3.3 Z 和 d 成反比的後果](#33-z-和-d-成反比的後果)
- [4. Block matching 和它的失敗](#4-block-matching-和它的失敗)
- [5. 掃描線最佳化](#5-掃描線最佳化)
  - [5.1 把視差當成標籤](#51-把視差當成標籤)
  - [5.2 能量函數](#52-能量函數)
  - [5.3 動態規劃](#53-動態規劃)
  - [5.4 條紋問題、全域匹配](#54-條紋問題全域匹配)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

1. 講完互資訊：怎麼從兩個 patch 估機率。
2. 從視差算深度：$Z=bf/d$。
3. 逐像素的 block matching 會失敗 → 加平滑項，用動態規劃做**掃描線最佳化**。

---

## 1. 用 Parzen 視窗估機率

[▶ 00:00](https://youtu.be/hfQR7X8eH9s?t=0)

互資訊需要 $p(x,y)$、$p(x)$、$p(y)$。用 **Parzen 視窗（Parzen window）**，也就是**核密度估計（kernel density estimation）**。

**一維例子** [▶ 00:24](https://youtu.be/hfQR7X8eH9s?t=24)：

- $3\times3$ patch → $\mathbf{f}$ 有 9 個值（視窗可以是任意大小）。
- 每個值 $f_i$ 放一個高斯核 $K(x-f_i)$（寬度 $\sigma$ 是超參數）。
- 9 個高斯疊加起來 = 估出來的分佈。相鄰像素灰階常常接近，所以有些核會重疊。

$$
p(x)\approx\frac{1}{|\Omega|}\sum_{i}K\left(x-f_i\right)
$$

**二維（聯合機率）** [▶ 02:43](https://youtu.be/hfQR7X8eH9s?t=163)：每一對 $(f_i,g_j)$ 放一個二維高斯核，全部疊加：

$$
p(x,y)\approx\frac{1}{|\Omega|^2}\sum_{i}\sum_{j}K\left(x-f_i,\ y-g_j\right)
$$

- $3\times3$ 例子共有 $9\times9$ 個核。

（兩條式子依講者口述寫出；正規化常數投影片沒唸。）

> 以下**不是逐字稿內容**，是說明：講者說「9 乘 9 個核」，也就是 $\mathbf{f}$ 和 $\mathbf{g}$ 的所有組合。比較常見的作法是只用**同一位置**的對 $(f_i,g_i)$（9 個核），這樣才量得到「同一個像素在兩張圖的灰階關係」。哪一種是投影片原意，以投影片為準。

**離散化** [▶ 03:25](https://youtu.be/hfQR7X8eH9s?t=205)：

- 聯合機率存成一張**二維表**：第 $(x,y)$ 格 = $p(X=x,Y=y)$，對所有核代入那個 $(x,y)$ 求和。
- **邊際機率** [▶ 04:54](https://youtu.be/hfQR7X8eH9s?t=294)：
  - $p(x)=\sum_yp(x,y)$：把每一**列**加起來。
  - $p(y)=\sum_xp(x,y)$：把每一**行**加起來。
- 代入互資訊公式（第 32 集），取負號當匹配代價。

⚠️ 逐字稿缺字：Whisper 把 Parzen 寫成 “Parson”，把 mutual information 寫成 “mutual probability”。

---

## 2. 四種代價的比較例子

[▶ 06:39](https://youtu.be/hfQR7X8eH9s?t=399)

一對校正好的影像，紋理**高度重複**。對參考影像某個像素，沿掃描線算代價，畫成「代價 vs. 逆深度」：

| 代價 | 結果 |
|---|---|
| SSD | 有明顯的最小值（深度約在 0.5 附近） |
| SAD | 也有全域最小值，但沒有 SSD 那麼明顯 |
| NCC（找最大值） | 最大值**不突出**，很多地方差不多高——重複紋理會讓它混淆 |
| 互資訊 | 在這個重複紋理的例子裡最好：有**很清楚的全域最小值** |

⚠️ 逐字稿缺字 [▶ 08:15](https://youtu.be/hfQR7X8eH9s?t=495)：Whisper 寫「SSD 的最小值也很明顯，但不如 sum of squares difference」——同一個東西比自己，依投影片順序第二個應是 **SAD**。

---

## 3. 視差轉深度

[▶ 09:36](https://youtu.be/hfQR7X8eH9s?t=576)

校正後極線就是掃描線。找到視差後，**不必做三角化**，就能直接算深度。

### 3.1 相似三角形推導

[▶ 10:55](https://youtu.be/hfQR7X8eH9s?t=655)

**設定**：

- 兩台相機焦距都是 $f$（用正規化座標就能做到）。
- 基線 $b$：兩個光心沿 $x$ 方向的距離（校正後只有 $x$ 方向的平移）。
- 3D 點深度 $Z$；在左、右圖的 $x$ 座標是 $x$、$x'$（各自以主點為原點）。
- 點的垂足把基線分成 $b_1$（左光心那一側）和 $b_2$（右光心那一側），$b_1+b_2=b$。

**兩對相似三角形**：

- 左相機：小三角形（光心、主點、像點）和大三角形（光心、垂足、3D 點）相似：
$$
\frac{x}{f}=\frac{b_1}{Z}
$$
- 右相機：像點在主點左邊，座標方向相反，所以用 $-x'$：
$$
\frac{-x'}{f}=\frac{b_2}{Z}
$$

**兩式相加** [▶ 13:13](https://youtu.be/hfQR7X8eH9s?t=793)：

$$
\frac{x-x'}{f}=\frac{b_1+b_2}{Z}=\frac{b}{Z}
$$

$$
\boxed{\ Z=\frac{bf}{x-x'}=\frac{bf}{d}\ }
$$

- $b$、$f$ 來自 stereo 校準 → 有了視差圖，每個像素的深度直接算出來。

⚠️ 逐字稿缺字 [▶ 12:33](https://youtu.be/hfQR7X8eH9s?t=753)：Whisper 寫「$-x'$ divided by x, which is the focal length」，應是除以 $f$。

### 3.2 另一種情況

[▶ 15:25](https://youtu.be/hfQR7X8eH9s?t=925)

3D 點落在兩個光心**同一側**（例如右相機的右邊）：

- 這時垂足到兩個光心的距離是 $b_1$（較長）和 $b_2$（較短），$b_1-b_2=b$。
- 相似三角形給 $\dfrac{x}{f}=\dfrac{b_1}{Z}$、$\dfrac{x'}{f}=\dfrac{b_2}{Z}$。
- **相減**：
$$
\frac{x-x'}{f}=\frac{b_1-b_2}{Z}=\frac{b}{Z}\quad\Longrightarrow\quad Z=\frac{bf}{x-x'}
$$
- 結果一樣。

（各式的正負號依講者的說法「這次要相減，讓 $b_1-b_2=b$」整理。）

### 3.3 Z 和 d 成反比的後果

[▶ 17:09](https://youtu.be/hfQR7X8eH9s?t=1029)

1. **只搜一側**：$b>0$、$f>0$，點在相機前面要 $Z>0$ → $d=x-x'>0$ → $x'$ 只能在 $x$ 的左邊。若在另一側找到對應，3D 點會在相機後面。（第 31 集的說法在這裡得到證明。）
2. **視差越小、深度越大**。
3. **小視差時不準** [▶ 18:44](https://youtu.be/hfQR7X8eH9s?t=1124)：$d$ 一點點擾動就造成很大的深度誤差 → stereo 相機有**有效距離**。

【口頭】例如 Bumblebee 相機的有效距離大約 10 到 11 公尺。

> 以下**不是逐字稿內容**，是把第 3 點寫成式子：對 $Z=bf/d$ 微分，$\left|\dfrac{\partial Z}{\partial d}\right|=\dfrac{bf}{d^2}=\dfrac{Z^2}{bf}$——視差誤差 $\Delta d$ 造成的深度誤差約 $\dfrac{Z^2}{bf}\Delta d$，隨距離**平方**成長。

---

## 4. Block matching 和它的失敗

[▶ 19:15](https://youtu.be/hfQR7X8eH9s?t=1155)

到目前為止的作法叫 **block matching**：每個像素**獨立**沿掃描線找最像的 patch。

**視窗大小的兩難** [▶ 20:09](https://youtu.be/hfQR7X8eH9s?t=1209)：

| 視窗 | 結果 |
|---|---|
| 小（例如 3） | 細節多（樹幹邊界清楚），但**很多雜訊和洞**、很破碎 |
| 大 | 平滑，但**過度平滑**，細節不見了 |

**對應失敗的原因** [▶ 21:02](https://youtu.be/hfQR7X8eH9s?t=1262)：

1. **無紋理表面**：例如一面白牆，沿掃描線每個 patch 都一樣 → 代價一樣，分不出最好和次好。
2. **重複紋理**：代價曲線有好幾個差不多的峰，無法區分。
3. **遮擋（occlusion）**：講者和重複紋理一起提到。
4. **非 Lambert 表面（non-Lambertian）** [▶ 22:30](https://youtu.be/hfQR7X8eH9s?t=1350)：會**鏡面反射**的表面，例如亮亮的車身、相框玻璃。從不同角度看外觀不同 → 匹配不好，深度圖糊成一片。

---

## 5. 掃描線最佳化

[▶ 23:15](https://youtu.be/hfQR7X8eH9s?t=1395)

**想法**：相鄰像素不會無緣無故相鄰——它們通常在同一個物體表面上，**深度差很小**。所以算視差時要考慮鄰居，不要每個像素各算各的。

→ 沿每條掃描線加一個**平滑約束（smoothness constraint）**：相鄰像素盡量取相同的視差。

### 5.1 把視差當成標籤

[▶ 24:46](https://youtu.be/hfQR7X8eH9s?t=1486)

- 像素座標是整數 → 視差 $d=x-x'$ 只能是**有限個整數**：$d_p\in\{1,\dots,L\}$。
- 求視差圖 = **標籤問題（labeling problem）**：替參考影像每個像素 $p$ 從 $L$ 個標籤中挑一個。
- 視差還要**限制範圍** $|x-\tilde x|\le\alpha$（$\tilde x$ 是右圖候選位置）：$x'$ 不能跑出影像；而且視差越小越不準（§3.3），所以只考慮一個範圍內的視差。

### 5.2 能量函數

[▶ 27:31](https://youtu.be/hfQR7X8eH9s?t=1651)

$$
E(D)=\sum_pC\left(p,d_p\right)+\sum_p\sum_{q\in\mathcal{N}_p}V\left(d_p,d_q\right)
$$

- **一元項（unary）** $C(p,d_p)$：像素 $p$ 取視差 $d_p$ 時的**匹配代價**（不相似度，越小越好）。只用這一項 = block matching。
- **二元項（pairwise／binary）** $V(d_p,d_q)$：**平滑項**，$q$ 是 $p$ 的鄰居。也可以有更高階的項。

**平滑項** [▶ 30:40](https://youtu.be/hfQR7X8eH9s?t=1840)：

$$
V\left(d_p,d_q\right)=\begin{cases}0,& d_p=d_q\\P_1,&\left|d_p-d_q\right|=1\\P_2,&\left|d_p-d_q\right|>1\end{cases}\qquad P_2>P_1
$$

- 視差一樣：不罰。
- 差 1：小罰 $P_1$（允許緩坡，例如斜面）。
- 差很多：大罰 $P_2$。

（$P_1$、$P_2$ 是懲罰參數，不是機率。）

- 最簡單的鄰居：同一條掃描線上左、右各一個像素。先考慮**所有鄰居都在同一條掃描線**的情況。

### 5.3 動態規劃

[▶ 32:03](https://youtu.be/hfQR7X8eH9s?t=1923)

鄰居都在同一條掃描線上時，可以用**動態規劃（dynamic programming）**，也就是 **Viterbi 演算法**，精確求解。

**相似度矩陣** [▶ 32:29](https://youtu.be/hfQR7X8eH9s?t=1949)：

- 取左圖一條掃描線、右圖同一條掃描線。
- 矩陣第 $(p,\cdot)$ 列 = 左掃描線像素 $p$ 的 patch 和右掃描線**每個位置**的匹配代價。

**Block matching vs. 掃描線最佳化**：

- Block matching：每一列各自取最小值。相鄰兩個像素 $p$、$q$ 可能挑到視差差很多的位置 → 違反平滑先驗。
- 掃描線最佳化 [▶ 35:12](https://youtu.be/hfQR7X8eH9s?t=2112)：在矩陣上找一條**從掃描線第一個像素到最後一個像素的最短路徑**。
  - 路徑長度 = 經過的格子的代價（一元項）**加上**每一步轉移的代價（二元項：相鄰兩列選的視差差多少）。
  - 超出視差範圍 $\alpha$ 的那部分矩陣**不搜尋**。
  - 在所有可能路徑中挑總代價最低的。

> 以下**不是逐字稿內容**，是動態規劃的遞迴式（Viterbi 的標準寫法），幫助理解「最短路徑」：沿掃描線由左到右，令 $S(p,d)$ 為「從第一個像素走到像素 $p$、且 $p$ 取視差 $d$」的最小累積代價：
> $$
> S(p,d)=C(p,d)+\min_{d'}\left[S(p-1,d')+V(d,d')\right]
> $$
> 算到最後一個像素，取 $\min_dS$，再沿記下的 $d'$ 往回追，就得到整條掃描線的視差。每條掃描線的計算量約是（像素數）×$L^2$。

### 5.4 條紋問題、全域匹配

[▶ 37:40](https://youtu.be/hfQR7X8eH9s?t=2260)

- 比 block matching 好：考慮了同一條掃描線上的鄰居關係，不再破碎。
- 但**不同掃描線之間仍然獨立** → 每一列內很一致，列與列之間跳來跳去 → **條紋（streaking）**現象。

**全域匹配** [▶ 38:46](https://youtu.be/hfQR7X8eH9s?t=2326)：

- 讓 $q$ 可以是**任何方向**的鄰居，極端情況是和整張影像一致 → **全域匹配（global matching）**，結果更好。
- 但變成 **NP-complete**，大多數時候解不了。
- 有近似方法：**α-expansion**（graph cut 的一種特例）。超出本課範圍。

【口頭】[▶ 40:06](https://youtu.be/hfQR7X8eH9s?t=2406) 有興趣可以修講者下學期的「AI 中的不確定性建模」課，會詳細講。

---

## 6. 一頁速查表

| 項目 | 公式 | 關鍵一步 |
|---|---|---|
| Parzen 視窗 | $p(x)\approx\frac{1}{|\Omega|}\sum_iK(x-f_i)$；聯合用二維高斯 | 每個樣本放一個核，疊加 |
| 邊際機率 | $p(x)=\sum_yp(x,y)$、$p(y)=\sum_xp(x,y)$ | 聯合表按列／行加總 |
| 視差 → 深度 | $Z=\dfrac{bf}{d}$，$d=x-x'$ | 兩對相似三角形 $\frac{x}{f}=\frac{b_1}{Z}$、$\frac{-x'}{f}=\frac{b_2}{Z}$ 相加 |
| 搜尋範圍 | $d>0$ | $Z>0$、$b,f>0$ |
| 不準度 | 小 $d$ → 大誤差 | $Z\propto1/d$ |
| 能量 | $E(D)=\sum_pC(p,d_p)+\sum_p\sum_{q\in\mathcal{N}_p}V(d_p,d_q)$ | 一元 = 匹配；二元 = 平滑 |
| 平滑項 | $0$（相同）、$P_1$（差 1）、$P_2$（差 >1），$P_2>P_1$ | — |
| 掃描線最佳化 | 動態規劃（Viterbi）找相似度矩陣上的最短路徑 | 鄰居都在同一列 → 鏈狀 → 可精確解 |

| 方法 | 問題 |
|---|---|
| Block matching | 小視窗破碎；大視窗過度平滑 |
| 掃描線最佳化 | 條紋 |
| 全域匹配 | NP-complete（近似：α-expansion／graph cut） |

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 掃描線最佳化的條紋 | 第 34 集（半全域匹配 SGM：多個方向的掃描線） |
| 匹配代價、$Z=bf/d$ | 第 34 集（平面掃描的多視角 stereo） |

---

## 附：本集一句話總結

> **互資訊用 Parzen 視窗估出聯合與邊際機率，在重複紋理時最穩；找到視差後用兩對相似三角形得 $Z=bf/d$，所以視差一定為正、而且越小越不準；逐像素的 block matching 在無紋理、重複紋理、遮擋、反光處都會失敗，於是把視差當標籤、在匹配代價外加平滑項（相同 0、差 1 罰 $P_1$、差更多罰 $P_2$），沿掃描線用動態規劃找最短路徑——但掃描線之間仍獨立，會出現條紋，而全域匹配又是 NP-complete。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 11 (Part 3) 錄影逐字稿（Whisper `medium.en`，40:16）整理；MVG 無對應章節。*
