---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 27
lecture: Lec27 Chapter 6 Lossy Data Compression and Transmission：6.1 Preliminaries、6.2 Fixed-length lossy data compression codes
date: 待補
video: https://youtu.be/Lf-3W5Gv1sY
notes: Alajaji & Chen §6.1–6.2（pp. 219–227，Example 6.1–Observation 6.15）
---

# 第 27 集 · Lec27 §6.1–6.2：有損壓縮的動機、distortion measure、rate–distortion function 的定義 [▶ 影片](https://youtu.be/Lf-3W5Gv1sY)

← 上一集：[26](26-correlated-parallel-gaussian-non-gaussian.md) ｜ [總目錄](README.md) ｜ 下一集：[28](28-rate-distortion-theorem.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 27 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（32:09，whisper large-v3-turbo）＋ 課本 §6.1–6.2（pp. 219–227）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：開頭 [00:00] 有亂碼（混了韓文、印尼文）。「lossy」聽成「Lawsey／Lawseed／Law C」，「distortion measure」聽成「Distortion Major／dittortion／detotion」，「quantization」聽成「Quantation」，「erasure」聽成「eratial／erratial／Eratio」，「Hamming」聽成「Heming／Hemmins／Hemi」，「additive distortion」聽成「Active Distortion／Active Dissolution」，「bit」聽成「beat／病」，「stationary ergodic」聽成「Station or Guardic」，「Kolmogorov」聽成「Comargrove」，「Shannon」聽成「Channon」，「實數」聽成「時數」，「大數法則」聽成「大樹法」，「位階」聽成「位接」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 為什麼要有損壓縮](#1-為什麼要有損壓縮)
- [2. Distortion measure 與分組的例子](#2-distortion-measure-與分組的例子)
- [3. 目標：distortion 不超過 D 下 rate 最小](#3-目標distortion-不超過-d-下-rate-最小)
- [4. 重建字母可以多一個：erasure](#4-重建字母可以多一個erasure)
- [5. 常用的 distortion measure](#5-常用的-distortion-measure)
- [6. Additive distortion：為了大數法則](#6-additive-distortion為了大數法則)
- [7. k ≠ n 怎麼辦：拆成兩步](#7-k--n-怎麼辦拆成兩步)
- [8. Fixed-length lossy code、achievable pair、R(D)](#8-fixed-length-lossy-codeachievable-pairrd)
- [9. 預告：R(D) 和 mutual information](#9-預告rd-和-mutual-information)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

進入第六章：Shannon 的**第三定律**——**有損資料壓縮（lossy data compression）**。先講動機，再定義 **distortion measure**、**有損壓縮碼**、**achievable rate–distortion pair** 和 **rate–distortion function $R(D)$**，最後預告 $R(D)$ 會寫成 mutual information 的最小值。

| 主題 | 課本 |
|---|---|
| 動機 | §6.1.1 Example 6.1–6.3（pp. 219–220） |
| Distortion measure、分組例子、erasure | §6.1.2 Definition 6.4（pp. 220–222） |
| Hamming、absolute、squared error | §6.1.3 Example 6.5–6.7（pp. 222–223） |
| Additive／maximum distortion、兩步壓縮 | Definition 6.8–6.9（pp. 223–224） |
| Lossy code、achievable、region、$R(D)$ | §6.2 Definition 6.10–6.14、Lemma 6.13、Observation 6.15（pp. 224–227） |

---

## 1. 為什麼要有損壓縮

[▶ 00:00](https://youtu.be/Lf-3W5Gv1sY?t=0)

**Channel capacity 是瓶頸**（Example 6.3，p. 219）：
- Source 每 $m$ 個符號用 $n$ 次 channel 送（例如 80 張影像用 1000 次傳輸）。比例 $r=\frac mn$ 叫 **channel expansion factor**（source 符號 / channel 符號）。
- 若 $mH>nC$（即 $rH>C$），Shannon（第 21 集的 joint source–channel coding theorem）說送不過去：錯誤率 bounded away from zero。
- 【口頭】硬送的話，接收端也許還知道一點東西，但雜訊掉的部分**完全不可控制（unmanageable）**：一定會掉，可是不知道掉哪一塊——左上角、右下角、中間都可能。
- 人對**高頻**比較不敏感、對低頻改變比較敏感。所以若真的送不過去，就**刻意丟掉**人比較不敏感的資訊，讓剩下的 entropy 有限、而且比 capacity 小，後半段就能幾乎無損地送過去。這樣錯誤是 **manageable**：丟的部分是我先控制好的（資訊有 priority）。
- 【課本補充】另一個不用有損壓縮的方法：把 $r$ 降到 $r'$ 使 $r'H<C$，代價是系統變慢。

**連續 source**（Example 6.1）：連續的聲音、影像，entropy 是無限大，一定要有損壓縮才能變成有限個 bit。

【口頭】例子：JPEG、MP1～MP4 都是有損壓縮，壓縮比可能 1:30、1:60（30 MB 壓成 1 MB），才能在有線管道送過去。

【課本補充】Example 6.2：有時 source 不是全部都有用，例如 hypothesis testing 只在乎 likelihood ratio，產生相同 likelihood ratio 的兩個字母不必分開編碼——這也是有損的。

---

## 2. Distortion measure 與分組的例子

[▶ 03:37](https://youtu.be/Lf-3W5Gv1sY?t=217)

【口頭】**Distortion measure 是自己定的**：自己決定哪裡重要、哪裡不重要。例如語音每個 sample 原本 8 bit（256 個位階），太多送不過去，壓成每個 sample 2 bit，聲音就沒那麼完美。

**Definition 6.4（distortion measure）**（p. 220）：$\rho:\mathcal Z\times\hat{\mathcal Z}\to\mathbb R^+$。$\mathcal Z$ 是 source 字母、$\hat{\mathcal Z}$ 是**重建（reproduction）字母**。$\rho(z,\hat z)$ 是「用 $\hat z$ 代表 $z$」的代價。
- 【口頭】它就是「兩個符號對到一個非負實數」，數字是你的感覺。合理的 distortion 對角線都是 0（自己代表自己沒有損失），外面一般是正的。可以是 0、1、2，也可以是 0、1、1.5，都沒關係，事先給好、固定。

**分組（grouping）的例子**（p. 221）：$\mathcal Z=\hat{\mathcal Z}=\{1,2,3,4\}$，uniform，要從 4 個結果降到 2 個（2 bit 變 1 bit），
$$[\rho(i,j)]=\begin{bmatrix}0&1&2&2\\1&0&2&2\\2&2&0&1\\2&2&1&0\end{bmatrix}.$$
- 分成 $\{1,2\}$、$\{3,4\}$，分別用 **1 和 3** 當代表（representative）。【口頭】2 用 1 代表，感覺是 1 倍的 distortion；若 3 用 1 代表，感覺是 2 倍，影響很大。這就是 quantization 的意思——grouping。
- 平均 distortion：$\frac14\rho(1,1)+\frac14\rho(2,1)+\frac14\rho(3,3)+\frac14\rho(4,3)=\frac14(0+1+0+1)=\frac12$。
- Entropy：原本 $H(Z)=2$ bit（長期觀察 1 萬個，平均每個 2 bit）；壓縮後只出現 1 或 3、各 $\frac12$，$H(\hat Z)=1$ bit——搞不好就送得過去。

> ⚠️ 逐字稿缺字：[▶ 06:39](https://youtu.be/Lf-3W5Gv1sY?t=399) 「算出來……就是1分之1」應為「**二分之一**」（課本：expected cost $=\frac12$）。

---

## 3. 目標：distortion 不超過 D 下 rate 最小

[▶ 07:41](https://youtu.be/Lf-3W5Gv1sY?t=461)

資料壓縮一定有一個 distortion measure；希望 **rate 越低越好**，但平均 distortion 要**不超過**某個門檻 $D$（人的感覺：超過某個數字就覺得不舒服）。

> ⚠️ 逐字稿口誤：[▶ 07:41](https://youtu.be/Lf-3W5Gv1sY?t=461) 老師先說「Distortion 平均來講要大於等於某個 Threshold」，馬上改口「要小於一個量，不要大於」。正確是 $\le D$。

所以問題是：**在 distortion $\le D$ 下 minimize rate**——答案是 $D$ 的函數。
- Distortion 要求越嚴格，rate 越壓不下來。
- **$D=0$**（完全不能有 distortion，要精確回復）：最好的 rate 就是 **entropy**（Shannon 第一定律）。所以 **lossless 是 lossy 的特例**。
- $D$ 放大一點點，可以壓得更好，例如 1:60、1:100，只要人看不出來就好。

---

## 4. 重建字母可以多一個：erasure

[▶ 08:42](https://youtu.be/Lf-3W5Gv1sY?t=522)

**重建字母的大小可以和 source 不一樣嗎？** 例如 source 每個 sample 256 個位階，重建用 257、258 個？
- 【口頭】不一定全部用到，只是讓選擇比較多。Mapping 也不一定要 deterministic：看到某個位階，可以從幾個值裡隨機選一個（統計式的資料壓縮）。
- 【口頭】已經有人證明：**多沒有用**，就算用隨機的也一樣。一般 $|\hat{\mathcal Z}|\le|\mathcal Z|+1$ 就夠了，多兩個以上不會讓 rate 更小、distortion 更好。（課本：$|\hat{\mathcal Z}|>|\mathcal Z|+1$ 通常沒有好處。）

**多一個什麼時候有用：erasure**（p. 221–222）：
- 【口頭】畫影像時，有一點實在不知道要壓到 1、2、3、4 哪一個，就用一個特定的符號、特定的顏色或顯示方式表示「這點我不顯示」——叫 **erasure**，記作 $E$。
- 例：$\mathcal Z=\{1,2,3\}$，$\hat{\mathcal Z}=\{1,2,3,E\}$，
$$[\rho(i,j)]=\begin{bmatrix}0&2&2&0.5\\2&0&2&0.5\\2&2&0&0.5\end{bmatrix}.$$
  用錯一個數字的代價是 2，用 $E$ 的代價是 0.5（四倍差）。
- Uniform source、只允許 2 個結果、平均 distortion $\le\frac13$：最佳選擇是 **1 代表 $\{1\}$、$E$ 代表 $\{2,3\}$**。
  - 【口頭】序列 1 2 3 3 2 1 → 數字 1、E、E、E、E、數字 1。沒辦法恢復，是 lossy 的。
  - 平均 distortion：$\frac13\cdot0+\frac23\cdot0.5=\frac13$。
  - Entropy 從 $\log_23$ 降到 $\log_23-\frac23$ bit。

> 以下**不是逐字稿內容**，是依課本數字推論的驗算：$\hat Z$ 的分布是 $(\frac13,\frac23)$，$H(\hat Z)=\frac13\log_23+\frac23\log_2\frac32=\log_23-\frac23$。

---

## 5. 常用的 distortion measure

[▶ 14:15](https://youtu.be/Lf-3W5Gv1sY?t=855)

【口頭】實際做影像、語音壓縮，會用模擬人眼、人耳（非線性）的 **perceptual filter** 定 distortion，但數學上不好處理。所以有幾個數學上好處理、實作上也有一點用的：

**Example 6.5（Hamming distortion）**：$\rho(z,\hat z)=0$ 若 $z=\hat z$，否則 1（矩陣對角線 0、外面 1）。
- 也叫 **probability of error distortion**：$E[\rho(Z,\hat Z)]=\Pr(Z\ne\hat Z)$。
- 【口頭】例：送 9 個 bit，接收端錯 2 個，錯誤率 $\frac29$ = Hamming distance ÷ $n$。只要告訴我輸入和輸出的 distortion，就知道錯誤率——在通訊上很有用。

**Example 6.6（absolute error）**：$\rho(z,\hat z)=|z-\hat z|$（影像強度常用）。

**Example 6.7（squared error）**：$\rho(z,\hat z)=(z-\hat z)^2$——代表**能量**的差距，非常常用。

【口頭】介紹這些是因為數學上好處理、容易分析；但人的感覺通常不和它們成正比。例：兩個聲音的 squared error 很大，不代表聽起來不一樣——相位平移只是晚一點聽到，對 information 量沒影響；非線性的相位失真若不多也還聽得懂，只是像唐老鴨的聲音。

---

## 6. Additive distortion：為了大數法則

[▶ 18:19](https://youtu.be/Lf-3W5Gv1sY?t=1099)

**Definition 6.8（additive distortion）**：$\rho_n(z^n,\hat z^n)=\sum_{i=1}^n\rho(z_i,\hat z_i)$。

【口頭】看到這個，理論的直覺就要出來：**為什麼要這樣定義？因為需要大數法則**。
- 平均 $\frac1n\sum\rho(z_i,\hat z_i)$，若每項獨立，會收斂到 $E[\rho(Z,\hat Z)]$——有收斂才會有 Shannon 的定理。
- 不能拆成個別相加，就沒有大數法則的行為，很難產生有效的定理。
- 大數法則的條件有很多研究：i.i.d.、stationary ergodic、Kolmogorov 給的條件……

**Definition 6.9（maximum distortion）**：$\rho_n=\max_i\rho(z_i,\hat z_i)$。
- 【口頭】反例：只要有一個錯，max 永遠是 1，拉多長都一樣；但平均下來可能收斂到 0。

（這和上一章 power constraint 要寫成平均的形式是同一個道理。）

---

## 7. k ≠ n 怎麼辦：拆成兩步

[▶ 19:56](https://youtu.be/Lf-3W5Gv1sY?t=1196)

**問題**：前面的例子壓縮前後長度一樣（1000 筆壓成 1000 筆），但壓縮是要降低量——1000 筆可以只存 30 筆（$k\ne n$）。這樣就沒辦法一筆對一筆比較，**additive distortion 沒辦法用**，數學上就出問題。

**解法（Shannon）：拆成兩步**（課本 pp. 223–224）：
- **Step 1**：有損的 mapping $h_n:\mathcal Z^n\to\hat{\mathcal Z}^n$（**長度不變**，1000 對 1000），滿足 distortion 和 rate 的要求——這裡可以用 additive distortion、有大數法則。
- **Step 2**：對 $h_n(Z^n)$ 做 **lossless** 壓縮到 $k$ 個 bit。由第一定律（Theorem 3.6），只要
$$\frac kn>\frac1nH(h_n(Z^n)),$$
  就能完全重建。這部分早就做完了。
- 【口頭】例：每個 $Z$ 原本 3.2 bit，Step 1 之後每個 1.1 bit；Step 2 無損，總量不變，30 筆帶的是 $\frac{1000\times1.1}{30}$ bit。
- 【口頭】影像的例子：Step 1 把 80 張畫面壓成 80 張比較「空洞」（變化少、entropy 小）的畫面；Step 2 無損地壓成搞不好 3 張畫面——這 3 張很複雜、沒辦法看，但能完全重建那 80 張可以看但空洞的畫面。

所以**有損壓縮的定理其實是 Step 1 的定理**。【口頭】Shannon 的論文是完整地解決問題：Step 2 第一定律已解決，現在講第三定律（老師口誤說「第二定律」）。

---

## 8. Fixed-length lossy code、achievable pair、R(D)

[▶ 25:34](https://youtu.be/Lf-3W5Gv1sY?t=1534)

**Definition 6.10（$(n,M,D)$ 有損壓縮碼）**（p. 224）：compression function $h:\mathcal Z^n\to\hat{\mathcal Z}^n$，codebook 大小 $|h(\mathcal Z^n)|=M$，平均 distortion
$$E\left[\frac1n\rho_n(Z^n,h(Z^n))\right]\le D.$$
- Rate $=\frac1n\log_2M$ bits/source symbol（$\log_2M$ 個 bit 就能表示一個長度 $n$ 的 sourceword）。
- 【口頭】$h$ 是 deterministic mapping；distortion 用 additive，$=\frac1n\sum\rho(z_i,\hat z_i)$，才有大數法則。不是 additive，定理就不能用。
- 可能性越少越好（例如 256 個位階壓成 4 個），entropy rate 就越低。
- 【課本補充】等價的 encoder–decoder：$f:\mathcal Z^n\to\{1,\dots,M\}$、$g:\{1,\dots,M\}\to\hat{\mathcal Z}^n$，$g(f(z^n))=h(z^n)$。

**Definition 6.11（achievable）**：若存在一串 $(n,M_n,D)$ 碼，$\limsup_{n\to\infty}\frac1n\log M_n<R$，則 $(R,D)$ **achievable**。

**$R$ 和 $D$ 是 trade-off**【口頭】：兩者不能同時變小。要越像（$D$ 小），需要越多細節，rate 壓不下來；可以越不像，就有越多壓縮空間。$D=0$ 時 worst case 就是 entropy。

**Definition 6.12（rate–distortion region）**：所有 achievable pair 的 closure。【口頭】圖上斜線部分做得到、沒畫斜線的做不到。

【課本補充】**Lemma 6.13（time-sharing）**：additive distortion 下，region 是 convex：$\lambda$ 比例的時間用碼 1、$1-\lambda$ 用碼 2，達到 $(\lambda R_1+(1-\lambda)R_2,\ \lambda D_1+(1-\lambda)D_2)$。

**Definition 6.14（rate–distortion function）**：
$$R(D):=\min\{R:(R,D)\in\mathcal R\}.$$
固定 distortion 下最小的 rate。【口頭】也有人畫 **distortion–rate function**，把 x、y 軸對調。

【課本補充】Observation 6.15：additive distortion 下 $R(D)$ **非遞增、convex**（由 time-sharing）。

到這裡只是定義完問題，還不知道答案。

---

## 9. 預告：R(D) 和 mutual information

[▶ 29:40](https://youtu.be/Lf-3W5Gv1sY?t=1780)

【口頭】先把觀念講出來（Venn 圖）：
- $\hat Z=h(Z)$ 是 $Z$ 的函數，$\hat Z$ 的訊息量一定**包含在** $Z$ 裡面（不可能額外亂加東西）。
- 所以 $I(Z;\hat Z)=H(\hat Z)-H(\hat Z|Z)=H(\hat Z)$：**rate 其實就是 $Z$ 和 $\hat Z$ 的 mutual information**。
- 我們要讓 $H(\hat Z)$ 越小越好，但 distortion 不能太大。
- 壓縮也可以**不 deterministic**：碰到 1，擲一個不公平的骰子，90% 對到 1、10% 對到 2；碰到 2 也類似。這樣得到的是條件機率 $P_{\hat Z|Z}$。
- 要找的就是這個分布，讓 **mutual information 最小**——又回到 Shannon 發明的這個量。真正要做的是讓輸出的 entropy 越小越好，但寫成 $I(Z;\hat Z)$ 很容易計算、公式很漂亮。

> 以下**不是逐字稿內容**，是依課本 Theorem 6.20（下一集）先寫出的結論：
> $$R(D)=\min_{P_{\hat Z|Z}:\ E[\rho(Z,\hat Z)]\le D}I(Z;\hat Z).$$

---

## 10. 一頁速查表

**動機**：$rH>C$ 時硬送 → 錯誤不可控；先刻意丟掉不重要的資訊，讓 rate 小於 $C$ → 錯誤可控。連續 source entropy 無限大，一定要有損。

**Distortion measure** $\rho:\mathcal Z\times\hat{\mathcal Z}\to\mathbb R^+$（自己定，對角線通常 0）。
- 分組例：$\{1,2\}\to1$、$\{3,4\}\to3$，distortion $\frac12$，entropy 2 → 1 bit。
- Erasure 例：$\{1\}\to1$、$\{2,3\}\to E$，distortion $\frac13$，entropy $\log_23\to\log_23-\frac23$。$|\hat{\mathcal Z}|\le|\mathcal Z|+1$ 就夠。

**常用**：Hamming（= 錯誤率）、absolute $|z-\hat z|$、squared $(z-\hat z)^2$（能量）。

**Additive** $\rho_n=\sum\rho(z_i,\hat z_i)$：平均會收斂（大數法則）才有定理；max distortion 不行。

**兩步**：Step 1 有損 $\mathcal Z^n\to\hat{\mathcal Z}^n$（同長度）；Step 2 無損，$\frac kn>\frac1nH(h_n(Z^n))$。定理只管 Step 1。

**定義**：$(n,M,D)$ 碼 $E[\frac1n\rho_n]\le D$，rate $\frac1n\log_2M$；achievable：$\limsup\frac1n\log M_n<R$；$R(D)=\min\{R:(R,D)\in\mathcal R\}$，非遞增、convex；$R(0)=H$（lossless 是特例）。

**預告**：$\hat Z=h(Z)$ ⇒ $I(Z;\hat Z)=H(\hat Z)$；$R(D)=\min_{E\rho\le D}I(Z;\hat Z)$。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $R(D)=\min I(Z;\hat Z)$、distortion typical set、rate–distortion theorem | 第 28 集（§6.3） |
| 二元 source（Hamming）、高斯 source（squared error）的 $R(D)$ | 第 29 集（§6.4） |
| $rR(D)<C$：有損的 joint source–channel coding | 第 30 集（§6.5） |
| Shannon limit | 第 31 集（§6.6） |

---

## 附：本集一句話總結

> **送不過去時，與其讓雜訊隨機亂丟，不如自己先挑不重要的丟掉——用自訂的 distortion measure（要可加，才有大數法則）衡量損失，在平均 distortion 不超過 $D$ 下找最小 rate $R(D)$；$D=0$ 時就是 entropy，而答案會是 $Z$ 和 $\hat Z$ 的 mutual information 的最小值。**

---

*筆記依據陳伯寧老師「消息理論」Lec27 錄影逐字稿（whisper large-v3-turbo，32:09）與 Alajaji & Chen 課本 §6.1–6.2 整理。*
