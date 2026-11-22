---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 20
lecture: Lec20 4.4 Example of Polar Codes for the BEC
date: 待補
video: https://youtu.be/zYOXFt0Ixwk
notes: Alajaji & Chen §4.4（pp. 127–131，Fig. 4.6–4.7、Example 4.14）；回顧 §4.5（Lemma 4.25、Observation 4.28）、§4.3 末（p. 126 的編碼史）
---

# 第 20 集 · Lec20 §4.4：回顧 KKT 與對稱通道、polar code（BEC 的例子） [▶ 影片](https://youtu.be/zYOXFt0Ixwk)

← 上一集：[19](19-calculating-channel-capacity-symmetric-kkt.md) ｜ [總目錄](README.md) ｜ 下一集：[21](21-joint-source-channel-separation.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 20 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（1:04:48，whisper large-v3-turbo）＋ 課本 §4.4（pp. 127–131）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「polar code」聽成「Poder Code／Polder-Code／Portocode」，「Arıkan（Erdal Arıkan）」聽成「Erican Erdol／Arican」，「Bilkent University」聽成「Bilken University」，「polarization」聽成「Poderization」，「erasure」聽成「erratial／Uradial」，「frozen」聽成「Flozen」，「successive cancellation」正確，「XOR」聽成「equusivore／eclusive all／equal for」，「trellis-coded modulation」聽成「Tradis Code Demodulation／Tralis-Code Demodulation」，「Ungerboeck」聽成「Unclebach」，「Forney」聽成「FORNI／Fornier」，「concatenated code」聽成「Concatenate Code／Konkinic-Code」，「Berrou」聽成「Beroux」，「Verizon」聽成「Virizon」，「error floor」聽成「Aerror Flower／Aero Flower」，「quasi-symmetric」聽成「Quisi-Symmetric」，「weakly symmetric」聽成「weekly symmetric」，「T-symmetric」正確，「斜率」聽成「邪律」，「基地台」聽成「記憶台」，「concern」聽成「concent」。開頭「中文字幕 李宗盛」是幻覺。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 半學期回顧：capacity 的精神](#1-半學期回顧capacity-的精神)
- [2. 回顧：KKT 與簡化的 KKT](#2-回顧kkt-與簡化的-kkt)
- [3. 逼近 Shannon capacity 的歷史](#3-逼近-shannon-capacity-的歷史)
- [4. 回顧：對稱類通道與 T-symmetric](#4-回顧對稱類通道與-t-symmetric)
- [5. Polar code 的背景](#5-polar-code-的背景)
- [6. 極化的想法：capacity 總量不滅](#6-極化的想法capacity-總量不滅)
- [7. Basic transformation（n = 2）](#7-basic-transformationn--2)
- [8. 兩個新通道都是 BEC](#8-兩個新通道都是-bec)
- [9. 多層極化：n = 4、n = 8](#9-多層極化n--4n--8)
- [10. Polar code 的性質與 5G](#10-polar-code-的性質與-5g)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 與後續集數的連結](#12-與後續集數的連結)

---

## 0. 這堂課要做什麼

前半回顧半學期的重點（capacity、KKT、對稱類通道）；後半介紹 **polar code**——第一個**有明確結構、又可以證明達到 capacity** 的碼，用 BEC 說明**通道極化（channel polarization）**。

| 主題 | 課本 |
|---|---|
| KKT、對稱類通道回顧 | §4.5（Lemma 4.25、Observation 4.28） |
| 編碼史 | §4.3 末（p. 126） |
| Polar code：basic transformation、SC decoding | §4.4、Fig. 4.6（pp. 127–129） |
| Channel combining／splitting、n = 8 的例子 | Fig. 4.7、Example 4.14（pp. 129–131） |

---

## 1. 半學期回顧：capacity 的精神

[▶ 00:00](https://youtu.be/zYOXFt0Ixwk?t=0)

【口頭】
- Channel capacity 的精神：**工程上的操作**（設計一個傳輸方式、讓傳輸越快越好）可以用**數學／機率的方法**完全解釋，而且算得出最好的極限（reliable transmission rate）——這在一般工程上很少見。
- 背後是統計現象：**大數法則**。分析巨大數量的統計現象若沒有大數法則，就很難分析，因為它還是一個隨機變數。
- $C=\max_{P_X}I(X;Y)$。最有名的公式：**AWGN** $Y=X+N$，$X^2$ 是傳送能量、$N$ 有雜訊能量，
$$C=\frac12\log_2(1+\text{SNR}).$$
  這要求輸入是**高斯**（可以是任意實數）；實際上送的是 ±1，有點差距。
- 單一輸入的 mutual information $I(x;Y)$：被用到的輸入（$P_X(x)>0$）都達到 $C$，沒用的 $\le C$。
- Mutual information 是理論量，只要給機率就能算，跟怎麼設計系統無關；**Shannon 的貢獻是把這兩個看似無關的量畫上等號**。

---

## 2. 回顧：KKT 與簡化的 KKT

[▶ 05:05](https://youtu.be/zYOXFt0Ixwk?t=305)

【口頭】（考試第 5 題的內容）
- 很多工程理論要在限制下 minimize 函數：不等式限制都寫成 $g_i(x)\le0$，等式限制 $h_j(x)=0$。一般用 Lagrange multipliers 加進去再微分，變成沒有限制的問題。
- 問題：這樣得到的**不保證是最佳解**。KKT 的價值：告訴你**什麼時候是最佳解**（strong duality）——$f$、$g$ convex、$h$ linear（affine）時，用 KKT 就能找到真正的最佳解；否則只是一組可能不錯的解。
- 為什麼在 information theory 特別重要：MI 對輸入 concave（加負號就是 convex 的 minimize）；等式限制 $\sum P_X(x_i)=1$；不等式限制 $P_X(x_i)\ge0$（寫成 $-x_i\le0$）——全部是線性的，**完全符合 KKT**。

**簡化的 KKT**（機率分布專用）[▶ 10:18](https://youtu.be/zYOXFt0Ixwk?t=618)：
- 原始 KKT：$g_i(x)\le0$、$\lambda_i\ge0$、$\lambda_ig_i(x)=0$、$h(x)=0$、微分 = 0。
- 因為不等式限制 $-x_i\le0$ 是線性的（微分是 −1），可以把那些 multiplier 拿掉，只留等式限制的一個 $\lambda$：
$$\frac{\partial f}{\partial x_i}+\lambda\ \begin{cases}=0,&x_i>0\\\ge0,&x_i=0.\end{cases}$$
  （minimize 的寫法；對 capacity 就是課本 (4.5.9)。）
- 微分的重點：MI 對輸入分布的微分剛好是 $I(x;Y)$（加常數）。斜率越正，越該給它多一點機率，衝到最大就是 capacity。

---

## 3. 逼近 Shannon capacity 的歷史

[▶ 13:21](https://youtu.be/zYOXFt0Ixwk?t=801)

【口頭】Shannon 1948–49 年用純機率算出傳輸極限，大家很驚訝；經過 50 年，1998 年才在 AWGN 上達到：
- 開始用 **convolutional code**，離 AWGN 的 Shannon capacity 約差 6–7 dB；
- **Trellis-coded modulation**（Ungerboeck）：接近到約 4 dB；
- **Concatenated code**（Forney）：NASA 用在外太空傳輸，約 2 dB；
- 1993 年 **Turbo code**：0.7 dB；
- 1998 年 **LDPC code**：0.0 幾 dB——完全達到 Shannon capacity 的方法終於找到了。
- 這些都是工程上的設計，和理論沒有直接連結：設計完再驗證離 capacity 多遠。

【課本補充】課本 p. 126 的整理：從隨機碼中搜尋好碼的複雜度隨 block length **雙重指數**成長，所以催生了 coding theory（Hamming、Golay、BCH、Reed–Muller、Reed–Solomon、convolutional codes 等線性碼；Turbo、LDPC；2007 年 Arıkan 的 polar code 是第一個可證明達到 capacity 的確定性構造）。

---

## 4. 回顧：對稱類通道與 T-symmetric

[▶ 14:22](https://youtu.be/zYOXFt0Ixwk?t=862)

- 實際碰到的通道多半對稱（例如 AWGN 送 ±1），所以常問：**uniform 輸入能不能達到 capacity**？
- Symmetric（列、行都是重排）→ weakly symmetric（列重排、行和相等；BSC、BEC）→ quasi-symmetric（行切成弱對稱子矩陣）：都用 uniform 就達到，而且有 closed form（quasi-symmetric：$C=\sum a_iC_i$，$a_i$ 是子矩陣的列和）。

**T-symmetric**（【口頭】說約 2004 年）[▶ 17:28](https://youtu.be/zYOXFt0Ixwk?t=1048)：比 quasi-symmetric 更廣——若 uniform 輸入下 $I(x;Y)$ 是 $x$ 的**常數函數**（即「微分是常數」），uniform 就達到 capacity。
- 用觀念記：$I(x;Y)$ 是 MI 對輸入機率的微分（斜率）。往每個方向的斜率都一樣，就應該平均分配量；某個方向斜率特別大，就該多給它——那就不是 uniform 了。
- T-symmetric 不一定能切成弱對稱子矩陣，所以**沒有 closed form**，要特別寫程式算。（課本 Observation 4.28 的例子：$Q=\begin{bmatrix}\frac13&\frac13&\frac13\\\frac16&\frac16&\frac23\end{bmatrix}$。）

**現況**（【口頭】）[▶ 20:36](https://youtu.be/zYOXFt0Ixwk?t=1236)：很多通道的 capacity 公式還算不出來。fading channel 只有上下界（已經很接近，差一兩個 bit）；有些光學通道只知道 high-power（高 SNR）時的漸近公式。

---

## 5. Polar code 的背景

[▶ 21:07](https://youtu.be/zYOXFt0Ixwk?t=1267)

【口頭】
- 土耳其的理論學者 **Erdal Arıkan** 約 2008–2009 年訪問 TUM（慕尼黑工大）時想到的設計，經典論文也得了獎。
- Shannon 用 random coding（期望值）證明，不知道怎麼設計；之後的 convolutional、TCM、concatenated、Turbo code 都和理論沒有直接連結。**Polar code 在論文裡就有真正的碼的設計，同時直接證明它達到 Shannon capacity**——第一個有真正結構又可證明達到 capacity 的碼。
- 對任何 DMC 都能做到，**前提是 uniform input**：它達到的是 **symmetric capacity**（輸入限定 uniform 時的 capacity，例如 012 各 $\frac13$）。對 weakly symmetric、quasi-symmetric、T-symmetric 這些「uniform 就是最好」的通道，polar code 就達到真正的 capacity——這就是為什麼和前面有關係。
- Arıkan 在土耳其的 Bilkent University（私立，土耳其第二好；老師說曾排在交大前面、現在在後面，世界排名約 200 名掉到 400 名），他和他的兄弟都在那邊當教授。
- 名稱 polar 不是人名，而是 **polarization（極化）**——一個全新的理論思維。

【課本補充】課本（p. 127）：polar code 可以證明達到任何 binary-input memoryless channel 的 capacity，只要該通道的 capacity 由 uniform 輸入達到（例如 quasi-symmetric）；構造和證明都純粹基於 information theory 的概念，而且編解碼複雜度低。

---

## 6. 極化的想法：capacity 總量不滅

[▶ 27:16](https://youtu.be/zYOXFt0Ixwk?t=1636)

**要記的兩個 capacity**（【口頭】）：
- BSC：$C=1-h_b(\varepsilon)$，$h_b(\varepsilon)=-\varepsilon\log\varepsilon-(1-\varepsilon)\log(1-\varepsilon)$；
- BEC：$C=1-\varepsilon$（$\varepsilon$ 是 erasure probability）。BEC 單一參數、很簡單，所以用它說明。

**極化**（課本 p. 127）：把 $n$ 個獨立的 BEC($\varepsilon$) 轉換成**極端的**通道——要嘛**完美（無雜訊）**，要嘛**完全是雜訊**。$n\to\infty$ 時，沒有極化的通道比例趨近 0，完美通道的比例趨近 $1-\varepsilon$（= capacity）。

**能量不滅**（【口頭】）：
- 雜訊是自然界量出來的、不能改，所以 $n$ 個通道能帶的 information 總量是常數。不管怎麼操作，**總 capacity 不變**——只能重新分配。
- 例：$\varepsilon=\frac12$，$C=\frac12$。用 1 萬個 bit，可靠地最多帶 5000 bit（超過就是 strong converse，錯誤率很糟；少於就存在錯誤率趨近 0 的方法——當然 $n$ 要很大）。
- 用一個線性操作把總量 5000 bit 集中到某 5000 個位置（capacity 都是 1），其他位置 capacity 都是 0。
- 【口頭】entropy 是能量的概念、知識是能量，mutual information 也是能量的概念——能量不滅。
- 資訊放在好的位置送；壞的位置設為 **frozen bit**（固定為 0，接收端也知道，不用偵測）。
- 好處：rate 容易調——只送 4000 bit 就在 5000 個好位置裡挑更好的 4000 個，送 3000 就再挑。但要對 reliability **排序（sorting）**，$n$ 很大（例如 1 萬）時排序也是困難的問題，所以有近似公式或預先決定的順序。理想上可靠度圖是一群全 0、一群全 1，實際上中間會有一些不那麼漂亮的。

---

## 7. Basic transformation（n = 2）

[▶ 34:27](https://youtu.be/zYOXFt0Ixwk?t=2067)

**設定**（課本 p. 127，Fig. 4.6a）：兩個獨立的 BEC($\varepsilon$)：$(X_1,Y_1)$、$(X_2,Y_2)$，各有 $\varepsilon$ 的機率被 erase。$X_1$、$X_2$ uniform 時 $I(Q)=I(X_1;Y_1)=I(X_2;Y_2)=1-\varepsilon$。
- 【口頭】例：$\varepsilon=\frac12$，送一個 bit 一半機率送對、一半完全 erase。erase 後對輸入一無所知（來自 0、1 機率一樣）；收到 0 或 1 則百分之百對。Shannon 說送兩個 bit 能帶一個 bit。

**線性 mod-2 操作**：
$$X_1=U_1\oplus U_2,\qquad X_2=U_2,$$
$U_1,U_2$ 是獨立 uniform 的訊息 bit。【口頭】兩個 bit 的線性二元操作，大概就只有這個選項，所以叫 basic transformation。

**Successive cancellation（SC）decoding**：先用 $(Y_1,Y_2)$ 解 $U_1$；再用 $(Y_1,Y_2)$ 和**已解出的 $U_1$**（假設正確）解 $U_2$。
- 【口頭】successive 是循序（先 $U_1$ 再 $U_2$），cancellation 是把解出來的當作對的、cancel 掉。5G 的非正交多工也用 cancellation 一個一個解。
- 缺點：前一個錯，後面全錯——**error propagation**。但 $U_1$ 將來是 frozen，接收端早就知道。

這產生兩個新通道（把它們當黑箱子）：
$$Q^-:\ U_1\to(Y_1,Y_2),\qquad Q^+:\ U_2\to(Y_1,Y_2,U_1).$$
（$Y_2$ 雖然只含 $U_2$，但能幫忙把 $X_1$ 解回來，所以 $U_1$ 要用 $Y_1,Y_2$ 兩個。）

---

## 8. 兩個新通道都是 BEC

[▶ 40:33](https://youtu.be/zYOXFt0Ixwk?t=2433)

【口頭】erasure channel：要嘛完全正確，要嘛一錯就對輸入一無所知。逐一看四種情形：

**$Q^-$（解 $U_1$）**：
1. $Y_1$、$Y_2$ 都收到（0 或 1）：$X_1=U_1\oplus U_2$、$X_2=U_2$ 都知道，$U_1=X_1\oplus X_2$，**完全正確**。
2. $Y_1$ erase、$Y_2$ 收到：知道 $U_2$，但 $U_1\oplus U_2$ 不知道——$U_1$ 只能亂猜（uniform 的 bit 跟任何固定值 XOR 還是 uniform）。
3. $Y_2$ erase、$Y_1$ 收到：知道 $U_1\oplus U_2$，但 $U_2$ 是 uniform 不知道，$U_1$ 還是 uniform——亂猜。
4. 都 erase：亂猜。

只有情形 1 正確，所以 $Q^-$ 是 BEC，
$$\varepsilon^-=1-(1-\varepsilon)^2.$$
$\varepsilon=\frac12$ 時 $\varepsilon^-=\frac34$：**變差了**（原本 50% 被 erase，現在 75%）。

**$Q^+$（解 $U_2$，已知 $U_1$）**：
1. $Y_1$ 收到：$U_2=Y_1\oplus U_1$，正確。
2. $Y_2$ 收到：$U_2=Y_2$，正確。
3. 兩個都 erase：亂猜。

所以 $Q^+$ 是 BEC，
$$\varepsilon^+=\varepsilon^2.$$
$\varepsilon=\frac12$ 時 $\varepsilon^+=\frac14$：**變好了**。

**總量不變**（課本 (4.4.1)–(4.4.2)）：
$$I(Q^+)+I(Q^-)=(1-\varepsilon^2)+(1-\varepsilon)^2=2(1-\varepsilon)=2I(Q),$$
$$(1-\varepsilon)^2=I(Q^-)\le I(Q)=1-\varepsilon\le I(Q^+)=1-\varepsilon^2,$$
等號 iff $\varepsilon\in\{0,1\}$。basic transformation 沒有損失任何 mutual information，只是一個變好、一個變差——**polarization**。
- 【口頭】BEC 的好處：capacity 直接加就好；erasure probability 加起來 = $n$ 減總 capacity（0.5 + 0.5 = 1，0.75 + 0.25 = 1）。
- $n=2$ 時：$U_1$ frozen、$U_2$ 放資訊，達到 $\frac12$ 的 usage；但 25% 還不夠好，所以要再加層。

【課本補充】p. 128 註 12：$Q^-$ 的輸出對 $(y_1,y_2)$ 可以重新標成一個三值符號：$(0,0),(1,1)\to0$；$(0,1),(1,0)\to1$；含 $E$ 的 $\to E$，就精確地是一個 BEC。p. 129 註 13：兩個不同的 BEC($\varepsilon_1$)、BEC($\varepsilon_2$) 做 basic transformation，得到 BEC($\varepsilon_1\varepsilon_2$) 和 BEC($1-(1-\varepsilon_1)(1-\varepsilon_2)$)。

> ⚠️ 逐字稿缺字：[▶ 46:40](https://youtu.be/zYOXFt0Ixwk?t=2800) 老師一度把 $Q^+$、$Q^-$ 的 capacity 說反，隨即自己更正：$1-\varepsilon^2$ 是好的 $Q^+$、$(1-\varepsilon)^2$ 是差的 $Q^-$。

---

## 9. 多層極化：n = 4、n = 8

[▶ 47:10](https://youtu.be/zYOXFt0Ixwk?t=2830)

**$n=4$**：兩個 $Q^-$ 再做一次 basic transformation、兩個 $Q^+$ 再做一次（壞的配壞的、好的配好的）：
$$\varepsilon^{--}=1-(1-\varepsilon^-)^2,\quad\varepsilon^{-+}=(\varepsilon^-)^2,\quad\varepsilon^{+-}=1-(1-\varepsilon^+)^2,\quad\varepsilon^{++}=(\varepsilon^+)^2.$$
$\varepsilon=\frac12$：
$$\varepsilon^{--}=0.9375,\quad\varepsilon^{-+}=0.5625,\quad\varepsilon^{+-}=0.4375,\quad\varepsilon^{++}=0.0625.$$
加起來還是 2（四個 capacity 加起來也是 2）——能量不滅。

> ⚠️ 逐字稿缺字：[▶ 48:41](https://youtu.be/zYOXFt0Ixwk?t=2921) 老師口述 $1-(1-0.25)^2$「就是 0.1375」，應為 $1-0.5625=0.4375$。

**名詞**（課本 p. 129）[▶ 56:18](https://youtu.be/zYOXFt0Ixwk?t=3378)：
- **Channel combining**：用多個 basic transformation 從 $U_1,\dots,U_n$ 得到 $X_1,\dots,X_n$（編碼）。
- **Channel splitting**：用 $Y_1,\dots,Y_n$ 和 $U_1,\dots,U_{i-1}$ 解 $U_i$——不是整串一次解，而是一個 bit 一個 bit 循序解。
- 合起來叫 **channel polarization**。
- 長度 $n=2^m$、$2^k$ 個 codeword：做 $m$ 層極化，$k$ 個訊息 bit 放在 mutual information 最大的 $k$ 個位置（不編碼直接送），其餘 $n-k$ 個放 frozen bit；解碼用 SC decoder。

**解碼順序與 bit reversal** [▶ 54:46](https://youtu.be/zYOXFt0Ixwk?t=3286)（【口頭】）：$n=4$ 時先用 $Y_1..Y_4$ 解 $U_1$（最爛，其實是 frozen），再用 $U_1$ 已知解 $U_2$……。圖上的排列順序是 1、3、2、4——把 index 寫成二進位（00、01、10、11）再**頭尾對調（bit reversal）**。bit reversal 用標準邏輯線路就能做，不難。

**Example 4.14：$n=8$、$\varepsilon=0.5$**（課本 Fig. 4.7，pp. 130–131）：再極化一層。

> 以下是依 $\varepsilon^-=1-(1-\varepsilon)^2$、$\varepsilon^+=\varepsilon^2$ 逐層算出的 erasure probability（課本 Fig. 4.7 的數字；老師口述了其中幾個）：

| $U_i$ | 路徑 | erasure prob. |
|---|---|---|
| $U_1$ | $---$ | 0.9961 |
| $U_2$ | $--+$ | 0.8789 |
| $U_3$ | $-+-$ | 0.8086 |
| $U_4$ | $-++$ | 0.3164 |
| $U_5$ | $+--$ | 0.6836 |
| $U_6$ | $+-+$ | 0.1914 |
| $U_7$ | $++-$ | 0.1211 |
| $U_8$ | $+++$ | 0.0039 |

- 總和 = 4（$=n\varepsilon$），總 capacity 仍是 4。
- 最好的 $U_8$ 只有 0.0039 的機率被 erase；最差的 $U_1$ 有 0.9961。
- 【口頭】第一個最糟、最後一個最好是對的，但**中間不一定照順序**：第二糟的是 0.8789（$U_2$），不是 $U_5$。
- $\varepsilon=\frac12$，Shannon 說 8 個能送 4 個 bit：選 erasure 最小的四個 **$U_4,U_6,U_7,U_8$** 送資訊，其他 frozen——這就是 (8, 4) polar code。
- 例：$U_1$ 的 0.9961 來自 $1-(1-0.9375)^2$。

**長度**（【口頭】）：Arıkan 原本都是 2 的冪次（2、4、8、16、32）。現在可以設計長度 3 的 **polar kernel**，例如 $24=2\times2\times2\times3$，湊出不同長度。

**$n\to\infty$**：好通道的比例趨近 capacity——證明了 Shannon 是對的，而且可以操作（結構重複、很容易實作）。證明要證收斂，非常複雜，老師不講。

---

## 10. Polar code 的性質與 5G

[▶ 50:13](https://youtu.be/zYOXFt0Ixwk?t=3013)

【口頭】
- **發明到納入標準非常快**：2008 年左右發明，2016 年底就進 5G 標準——很少見；通常要經過一段時間確認才變標準。
- **5G 標準的角力**：各公司提自己的 proposal（最好有專利）。Huawei 看到 polar code 的潛力大力發展；Qualcomm 提 LDPC；法國公司提 Turbo code 2.0。結果：**control channel（檔頭）用 polar code**，資料部分還是 LDPC（比較成熟）。polar code 還有重傳、和 CRC 合作等問題沒完全解決；但檔頭長度固定、需要很好的保護（reliable），適合 polar code。標準給了一個固定的可靠度排序（Huawei 大量模擬得到），因為一般對付的是每個位置雜訊 variance 都一樣的 AWGN，和 BEC 類似，可以事先預測順序。
- 第六代行動通訊在討論要不要延續 polar code。
- **優點**：
  - 一開始就有明確的低複雜度實作架構（explicit low-complexity construction），二進位、很容易實作；
  - 效能可以直接證明達到 Shannon capacity；
  - rate 可以動態調整（對 reliability 排序、選 frozen set 和 information set），前提是排序做好（通常用近似）；
  - **沒有明顯的 error floor**：LDPC 和 Turbo code 畫 SNR 對錯誤率時，到某個階段增加能量也換不到錯誤率（平掉），早期 Turbo code 還有 zigzag（增加能量反而變差）。polar code 保證沒有 zigzag，也沒有明顯的 error floor——要 control channel 送得好，多給能量就一定換得到效能。
- **行動通訊的閒聊**：3G 時韓國花了很大力氣布局專利；4G 的 OFDM 歐美拿回優勢；5G 時大家搶誰第一個上線（韓國、Verizon 在芝加哥、Huawei 說上海最早），實測約是 4G 的兩倍（四、五百 Mbps），目標是 1 Gbps。未來是 big data、到處蒐集資料，基地台要更密（幾十公尺一個）。大學校園一般沒有基地台（怕學生抗議電波影響），都從校外往校內打——「雞生蛋、蛋生雞」的問題。老師開玩笑：各位將來可以發明一個頭盔擋電波。

---

## 11. 一頁速查表

**簡化的 KKT（機率分布）**：$\partial f/\partial x_i+\lambda=0$（$x_i>0$）、$\ge0$（$x_i=0$）；MI 的微分 = $I(x;Y)$ + 常數。

**Uniform 達到 capacity 的通道**：symmetric ⊂ weakly symmetric ⊂ quasi-symmetric ⊂ T-symmetric（$I(x;Y)$ 在 uniform 下與 $x$ 無關；沒有 closed form）。

**逼近 capacity 的歷史（AWGN）**：convolutional 6–7 dB → TCM ~4 dB → concatenated ~2 dB → Turbo (1993) 0.7 dB → LDPC (1998) 0.0x dB → polar (Arıkan 2008/09) 可證明達到。

**Polar code（BEC($\varepsilon$)）**
- Basic transformation：$X_1=U_1\oplus U_2$、$X_2=U_2$；SC decoding。
- $Q^-:U_1\to(Y_1,Y_2)$，$\varepsilon^-=1-(1-\varepsilon)^2$；$Q^+:U_2\to(Y_1,Y_2,U_1)$，$\varepsilon^+=\varepsilon^2$。
- 總量不滅：$I(Q^-)+I(Q^+)=2(1-\varepsilon)$；$I(Q^-)\le I(Q)\le I(Q^+)$。
- 多層：$\varepsilon=0.5$，$n=4$：0.9375、0.5625、0.4375、0.0625；$n=8$：最好的四個 $U_4,U_6,U_7,U_8$（0.3164、0.1914、0.1211、0.0039）。
- Channel combining（編碼）、channel splitting（循序解碼）、polarization；資訊 bit 放好位置、其餘 frozen；bit-reversal 排列。
- $n\to\infty$：完美通道比例 → $1-\varepsilon$。

---

## 12. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Source 和 channel 合起來（separation） | 第 21 集（§4.6） |
| AWGN capacity $\frac12\log(1+\text{SNR})$、高斯輸入最佳 | 第 22–24 集（第 5 章） |
| Parallel channels、water-filling（KKT） | 第 25–26 集（§5.5–5.6） |
| Shannon limit（BER vs SNR 的極限） | 第 31 集（§6.6） |

---

## 附：本集一句話總結

> **Polar code 用最簡單的 $X_1=U_1\oplus U_2,\ X_2=U_2$ 一層層把 $n$ 個相同的通道「極化」成幾乎完美或幾乎全廢的通道，總 capacity 一點不少；資訊放在完美的那 $n(1-\varepsilon)$ 個位置、其餘凍結，再用 successive cancellation 循序解——第一個有明確結構、又能證明達到 capacity 的碼。**

---

*筆記依據陳伯寧老師「消息理論」Lec20 錄影逐字稿（whisper large-v3-turbo，1:04:48）與 Alajaji & Chen 課本 §4.4 整理。*
