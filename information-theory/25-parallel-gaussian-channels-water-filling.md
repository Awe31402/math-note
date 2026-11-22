---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 25
lecture: Lec25 Fading channel、5.5 Capacity of uncorrelated parallel Gaussian channels（water-filling）
date: 待補
video: https://youtu.be/rk2pStZDrxg
notes: Alajaji & Chen §5.4 Theorem 5.33、Observation 5.35；§5.5 Theorem 5.36、Observation 5.37（pp. 194–200）
---

# 第 25 集 · Lec25 §5.4–5.5：高斯雜訊最難對付、fading channel、平行高斯通道與 water-filling [▶ 影片](https://youtu.be/rk2pStZDrxg)

← 上一集：[24](24-continuous-aep-gaussian-channel-capacity.md) ｜ [總目錄](README.md) ｜ 下一集：[26](26-correlated-parallel-gaussian-non-gaussian.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 25 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（51:43，whisper large-v3-turbo）＋ 課本 §5.4–5.5（pp. 194–200）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：開頭 [▶ 00:00](https://youtu.be/rk2pStZDrxg?t=0) 一段是亂碼（混了俄文、德文、義大利文），只認得出「上一次……AWGN……$\frac12\log_2(1+\frac P{\sigma^2})$……signal power……noise power」。另外「高斯」聽成「高詞／高思／高學／高濕」，「三大公設」聽成「三大公社」，「Proakis」聽成「prockets」，「water-filling」聽成「water feeling／Water Freedom」，「uncorrelated」聽成「uncollated／uncreated」，「Lagrange multiplier」聽成「legrange multiply」，「KKT」聽成「KET」，「Jensen's inequality」聽成「Jensen Equality／Jensenyqually」，「supremum」聽成「suprement／Supreement」，「接收端」聽成「結合端／接收段」，「two-phase」聽成「Two-Face」，「第五代行動通訊」聽成「第五代形容器」，「Laplacian」聽成「Laprasian」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 為什麼高斯雜訊最難對付](#1-為什麼高斯雜訊最難對付)
- [2. Theorem 5.33 的證明](#2-theorem-533-的證明)
- [3. Fading channel：接收端知道 A](#3-fading-channel接收端知道-a)
- [4. Fading 讓 capacity 變小（Jensen）](#4-fading-讓-capacity-變小jensen)
- [5. 傳送端也知道 A：water-filling 出現](#5-傳送端也知道-awater-filling-出現)
- [6. 平行高斯通道：Theorem 5.36](#6-平行高斯通道theorem-536)
- [7. 用 KKT 找最好的功率分配](#7-用-kkt-找最好的功率分配)
- [8. Water-filling 真的對嗎：mercury／water-filling](#8-water-filling-真的對嗎mercurywater-filling)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

接著上一集：先證明 **Theorem 5.33（高斯雜訊讓 capacity 最小）**，再看兩個工程上重要的例子——**fading channel**（接收端知道 fading；傳送端、接收端都知道 fading），由後者引出 **water-filling**；接著證明 **平行高斯通道（多天線）** 的 capacity 與 water-filling 分配；最後講 water-filling 在實際（非高斯輸入）時為什麼不對，以及 **mercury/water-filling**、**two-phase water-filling**。

| 主題 | 課本 |
|---|---|
| 高斯雜訊最小化 capacity | Theorem 5.33（p. 194） |
| Fading channel（DSI、FSI） | Observation 5.35（pp. 195–197） |
| 平行高斯通道、water-filling | §5.5 Theorem 5.36（pp. 197–199） |
| 實務考量、mercury/water-filling | Observation 5.37（pp. 199–200） |


---

## 1. 為什麼高斯雜訊最難對付

[▶ 00:31](https://youtu.be/rk2pStZDrxg?t=31)

AWGN 的前提：$Y_i=X_i+N_i$，一個 block 一個 block 使用，雜訊 i.i.d.。接著思考：如果雜訊不是高斯呢？

**加性、和輸入獨立的雜訊**下，
$$I(X;Y)=h(Y)-h(N).$$
- $h(N)$ 是量測出來的、不能用工程設計改變，只能對抗。雜訊的 differential entropy **越大**，扣掉越多，能傳的越少——它就是越難對付的雜訊。
- 【口頭】Differential entropy 的物理意義：做 uniform quantization 時精確度的**調整量**（可正可負，例如 −2、−3）。$h(Y)\ge h(N)$ 一定成立（$Y$ 比 $N$ 更難了解：$N$ 要調 −2，$Y$ 就要調 −3 這種意思）。
- 同 variance 下高斯的 $h$ 最大，所以直覺上高斯雜訊最難對付。Theorem 5.33 把它嚴謹化：雜訊不是高斯，我們會很高興，因為傳輸量會比較高。

**比較要公平**：兩個雜訊要有**相同的能量**（variance $\sigma^2$）。一個是任意分布的 $Z$，一個是高斯 $Z_g$。「好對付」的定義：在哪個雜訊下可以傳得更多（最大 reliable transmission rate，和方法無關）。

【口頭】延伸思考：兩者錯誤率都趨近 0，誰趨近的速度比較快？這是更細的問題（error exponent），可以一步一步探討。

---

## 2. Theorem 5.33 的證明

[▶ 06:42](https://youtu.be/rk2pStZDrxg?t=402)

**記號**【口頭】：$I(X;Y)$ 用冒號——兩邊角色不對等（就像 Proakis 把 channel impulse response 寫成 $h(t;\tau)$：$t$ 是當下時間、$\tau$ 是路徑延遲）。數學上 mutual information 是「輸入分布」和「轉移分布」的函數，兩個 argument 用逗號：$I(f_X,f_{Y|X})$。輸入分布可以看成一個向量 $(p_1,p_2,p_3)$，和為 1；轉移分布是更高維的向量。

**證明**（課本 p. 194）：輸入都用**高斯** $f_{X_g}$（因為它是高斯雜訊下的最佳輸入，右邊那一項就正好是高斯雜訊的 capacity）。令 $Y_g=X_g+Z_g$ 為高斯輸出，$Y=X_g+Z$。

1. 加性雜訊：$f_{Y_g|X_g}(y|x)=f_{Z_g}(y-x)$（給定 $x$ 得到 $y$ 的機率，就是 $z=y-x$ 的機率）。
2. 寫出 $I(f_{X_g},f_{Y_g|X_g})=\iint f_{X_g}(x)f_{Z_g}(y-x)\log_2\frac{f_{Z_g}(y-x)}{f_{Y_g}(y)}\,dx\,dy$。
3. **關鍵換項**：$\log_2\frac{f_{Z_g}(y-x)}{f_{Y_g}(y)}$ 是「高斯除以高斯」再取 log，只剩下常數和**二次項（second moment）**。因為 $Z$ 和 $Z_g$ 有**相同的 second moment**，所以把外面對 $f_{Z_g}$ 的積分換成對 $f_Z$ 的積分，數值不變：
$$I(f_{X_g},f_{Y_g|X_g})=\iint f_{X_g}(x)f_Z(y-x)\log_2\frac{f_{Z_g}(y-x)}{f_{Y_g}(y)}\,dx\,dy.$$
4. 兩個 mutual information 相減，前面積分的權重都一樣，log 可以合併：
$$I(f_{X_g},f_{Y_g|X_g})-I(f_{X_g},f_{Y|X})=\iint f_{X_g}(x)f_Z(y-x)\log_2\frac{f_{Z_g}(y-x)f_Y(y)}{f_{Y_g}(y)f_Z(y-x)}\,dx\,dy.$$
5. **Fundamental inequality** $\ln u\le u-1$：上式 $\le\frac1{\ln2}\iint f_{X_g}(x)f_Z(y-x)\left(\frac{f_{Z_g}(y-x)f_Y(y)}{f_{Y_g}(y)f_Z(y-x)}-1\right)dx\,dy$。分母裡的 $f_{X_g}f_Z$ 和前面的權重消掉，剩下 $\iint f_{X_g}(x)f_{Z_g}(y-x)\frac{f_Y(y)}{f_{Y_g}(y)}dx\,dy=\int f_Y(y)dy=1$，所以整個 $=1-1=0$。
6. 因此 $I(f_{X_g},f_{Y|X})\ge I(f_{X_g},f_{Y_g|X_g})=\frac12\log_2\left(1+\frac P{\sigma^2}\right)$；capacity 是取 sup，只會更大：
$$C(P)\ge I(f_{X_g},f_{Y|X})\ge\frac12\log_2\left(1+\frac P{\sigma^2}\right).\qquad\blacksquare$$

【口頭】
- 一碰到不等式：相減、帶公式、裡面一定有 log，再用 fundamental inequality 或 log-sum inequality 把 log 拿掉——幾乎所有證明都這樣做。這不是背的，log 函數的處理就是 information theory 的核心（三大公設推出的唯一函數就是 log，機率倒數取 log 就是資訊量）。
- 這和 detection／estimation 課裡做 likelihood ratio test 取 log 的概念類似（雜訊都是高斯）。
- 為什麼 information theory 在 1948、49 年之後變成顯學：它給通訊工程很多以前解釋不了的事情一個好解釋。

---

## 3. Fading channel：接收端知道 A

[▶ 15:54](https://youtu.be/rk2pStZDrxg?t=954)

**模型**（Observation 5.35，p. 195）：$Y_i=A_iX_i+Z_i$。$A_i$ 是 fading 係數（i.i.d.，通常 Rayleigh 或 Rician），$Z_i$ 是高斯背景雜訊，彼此獨立、也和輸入獨立。$A_i$ 是隨機變數時，capacity 一般**不知道**；要加很強的假設才能算。

**情形 1：decoder side information（DSI）**——接收端**完全知道**每一次的 $A_i$（例如 $A_i=0.8$，接收端 100% 知道是 0.8），傳送端不知道。
- 【口頭】這個假設非常強烈、做不到：$A$ 每次傳輸都不一樣（這次 0.3、被衰減很多，下次 0.8），接收端都要知道。
- 把 $(A,Y)$ 都當成輸出：
$$I(X;A,Y)=I(X;A)+I(X;Y|A)=I(X;Y|A),$$
  因為 $X$ 和 $A$ 獨立（你傳什麼，和通道把你放大縮小的建設性／破壞性干涉無關），$I(X;A)=0$。
- $I(X;Y|A)=h(Y|A)-h(Y|X,A)=h(Y|A)-h(Z)$：$X$、$A$ 都知道時，$Y$ 的自由度只剩 $Z$。給定 $A$，讓 $X$ 是高斯，$Y$ 就是高斯，$h(Y|A)$ 最大。
- 結果（課本 (5.4.17)）：
$$C_{DSI}(P)=E_A\left[\frac12\log_2\left(1+\frac{A^2P}{\sigma^2}\right)\right].$$
  【口頭】很多論文上常見的公式。$A$ 可能是 0.2、0.3、0.4……各有機率，長期下來出現的次數符合機率，所以取期望值。

**Pilot／training 的代價**【口頭】[▶ 19:00](https://youtu.be/rk2pStZDrxg?t=1140)：實際上接收端要知道 $A$，傳送端要送 training sequence（pilot，例如 +1 −1 +1 −1），接收端拿來估計。真正達到的傳輸量是「資料那段的傳輸量 ÷ 總長度」，而且 pilot 也要花能量。
- 有人做過模擬：假設 7 個 bit 的 pilot 就能 100% 估到 $A$，後面 15 個 bit 達到 capacity；和「不做 training、直接用 22 個 bit 找最好的送法（電腦硬找、一個一個試）」比，後者還比較好——即使前者還假設了 perfect estimation（實際上做不到）。
- 但電腦硬找的方法離 **non-coherent capacity** 還有一段很大的距離。
- $C_{DSI}$ 是理想狀況下的目標（可能達不到）；後續有人研究 $A$ 估計有誤差時會減損多少。

---

## 4. Fading 讓 capacity 變小（Jensen）

[▶ 24:38](https://youtu.be/rk2pStZDrxg?t=1478)

比較 $Y=AX+Z$ 和沒有 fading 的 $Y=X+Z$：沒有 $A$、沒有變異，capacity 應該比較大。

**證明**（課本 (5.4.18)）：$\log$ 是 concave，用 **Jensen's inequality**（先代函數再取期望值 $\le$ 先取期望值再代函數）：
$$C_{DSI}(P)=E_A\left[\frac12\log_2\left(1+\frac{A^2P}{\sigma^2}\right)\right]\le\frac12\log_2\left(1+\frac{E[A^2]P}{\sigma^2}\right)=\frac12\log_2\left(1+\frac P{\sigma^2}\right)=C_G(P).$$
- 假設 $E[A^2]=1$：能量不滅——通道有時放大、有時縮小，但不會讓你平均送 1 瓦、平均收到 2 瓦。
- 【口頭】所以 attenuation 確實是比較差的 channel，理論上給了量化指標。
- 【口頭】順帶提：所有 capacity(-cost) function 都是 concave——這是第五代行動通訊可以進來的原因：time sharing（30% 時間用能量 1 的最好方法、70% 時間用能量 2 的）拉的直線不會是最好的，合起來一起考量一定比較好。

---

## 5. 傳送端也知道 A：water-filling 出現

[▶ 26:38](https://youtu.be/rk2pStZDrxg?t=1598)

**情形 2：full side information（FSI）**——傳送端、接收端**都**知道 $A$（更不可能：要有又快又可靠的 feedback 把 $A$ 拉回傳送端）。
- DSI 時傳送端不知道 $A$，modulation 和 coding 是固定的，只有 receiver 結構可以隨 $A$ 變。FSI 時傳送端可以調整：$A=0.3$ 用這個方法傳，$A=0.8$ 用另一個方法傳。

**sup 和期望值的順序**【口頭】：
- DSI：$\sup$ 放在最外面（輸入分布只能固定一個，不隨 $A$ 變），期望值在裡面。
- FSI：最好的輸入可以隨 $A$ 改變，所以**先取 sup、最後再取期望值**：
$$C_{FSI}(P)=E_A\left[\sup_{p(\cdot):\,E_A[p(A)]=P}\frac12\log_2\left(1+\frac{A^2p(A)}{\sigma^2}\right)\right]=E_A\left[\frac12\log_2\left(1+\frac{A^2p^*(A)}{\sigma^2}\right)\right],$$
$$p^*(a)=\max\left\{0,\ \frac1\lambda-\frac{\sigma^2}{a^2}\right\},\qquad\lambda\text{ 由 }E_A[p^*(A)]=P\text{ 決定}.$$
- 最好的輸入還是**高斯**（mean 設 0 無所謂，differential entropy 重要的是 variance），只是**能量 $p(A)$ 隨 $A$ 調整**。
- 【口頭】理論學者會把「傳送端／接收端知不知道」的各種組合都假設一遍（傳送端知道、接收端不知道最奇怪），從中得到對實作有幫助的觀察。

**圖形解釋（graphical interpretation）**【口頭】[▶ 30:45](https://youtu.be/rk2pStZDrxg?t=1845)：
- 畫 $\frac{\sigma^2}{a^2}$ 對 $a$ 的曲線：$a$ 越大越小，當成「臉盆的底」。
- 倒水，水面高度是 $\frac1\lambda$；水深 $\frac1\lambda-\frac{\sigma^2}{a^2}$ 就是分配的能量。$A$ 大，能量多；$A$ 小，能量少。
- 平均能量是 $P$：例如送 1 萬次，300 次是這個 $a$、200 次是那個 $a$……每種用多少能量、乘上出現比例再平均，就是水的總面積（加權）$=P$，用它解出水面高度。
- 底比水面高的地方（$A$ 太小）**完全不送**——把傳送器關掉，送了也沒幫助。學者做出來時大家很高興，好像得到一個 guideline。
- 為什麼是 $\frac{\sigma^2}{a^2}$：兩端都知道 $a$，把 $Y=aX+Z$ 除以 $a$ 得 $\frac Ya=X+\frac Za$，新雜訊能量是 $\frac{\sigma^2}{a^2}$。**通道越乾淨，越要多用**——有好幾條路，好走的多走。而且有量化：雜訊差兩倍，能量也有對應的補償比例（水深 + 底 = 常數）。
- 【口頭】這個結果後來被推翻了（見第 8 節），但它是很漂亮的數學結果。

---

## 6. 平行高斯通道：Theorem 5.36

[▶ 34:50](https://youtu.be/rk2pStZDrxg?t=2090)

【口頭】多天線系統：四支天線，每支天線被干擾的程度不同；總能量是 $P$，要怎麼分給四個 channel？Water-filling：把每個 channel 的雜訊排出來，倒水，總水量 $P$（例如 2 瓦），水深就是各 channel 分到的 $P_i$。每個 bin **寬度是 1**（面積 = 能量）；考慮使用率或複雜度可以加權重，那是延伸。【口頭】這是 80 年代很有名的結果。


（課本 Fig. 5.1：$P=P_1+P_2+P_4$，第 3 個 channel 的底 $\sigma_3^2$ 高過水面 $\theta$，分不到能量。）

**Theorem 5.36（uncorrelated parallel Gaussian channels 的 capacity）**（p. 198）：$k$ 個雜訊互不相關的平行高斯通道，總功率限制 $P$，
$$C(P)=\sum_{i=1}^k\frac12\log_2\left(1+\frac{P_i}{\sigma_i^2}\right),\qquad P_i=\max\{0,\ \theta-\sigma_i^2\},\qquad\sum_{i=1}^kP_i=P.$$
由獨立的高斯輸入 $X_i\sim\mathcal N(0,P_i)$ 達到。（高斯的 uncorrelated 就是 independent。）

**證明 第一步：化成功率分配問題**（課本 pp. 198–199）
$$\begin{aligned}
I(X^k;Y^k)&=h(Y^k)-h(Y^k|X^k)=h(Y^k)-h(Z^k)&&(\text{平移不變、}Z\text{ 和 }X\text{ 獨立})\\
&=h(Y^k)-\sum_ih(Z_i)&&(\text{雜訊彼此獨立})\\
&\le\sum_ih(Y_i)-\sum_ih(Z_i)&&(\text{independence bound：個別 quantization 相加一定比較大})\\
&\le\sum_i\frac12\log_2\left(1+\frac{P_i}{\sigma_i^2}\right)&&(E[X_i^2]=P_i\text{ 時 }Y_i\text{ 高斯最大}),
\end{aligned}$$
等號成立：$X_i$ 彼此獨立且 $X_i\sim\mathcal N(0,P_i)$。
- 【口頭】Mutual information、capacity 這兩個名詞都是 Shannon 在 1948 年取的；以前沒有人想到傳輸會有一個界線。後來 mutual information 被很多領域拿去用。

---

## 7. 用 KKT 找最好的功率分配

[▶ 39:30](https://youtu.be/rk2pStZDrxg?t=2370)

剩下的問題：在 $\sum_iP_i=P$、$P_i\ge0$ 下 maximize $\sum_i\frac12\log_2\left(1+\frac{P_i}{\sigma_i^2}\right)$。

**為什麼要 Lagrange／KKT**【口頭】：原問題 $\min f(x)$ 受限於 $g(x)\le0$、$h(x)=0$，集合變形，不能直接用微分（微分等於 0 的點不見得在集合裡）。Lagrange 換一個函數、把限制拿掉，就可以用微積分令微分為 0；但這樣解出來可能是 suboptimal。**KKT 條件**保證這樣解出來的就是原問題的最佳解。
- 這裡全部符合：把目標加負號變成 **convex** 的 minimization；等式限制 $\sum P_i-P=0$ 是線性；不等式限制 $-P_i\le0$ 也是線性（convex）。

**Lagrangian**（乘子 $\nu$ 對等式、$\lambda_i$ 對 $-P_i\le0$）：
$$L=-\sum_i\frac12\log_2\left(1+\frac{P_i}{\sigma_i^2}\right)-\sum_i\lambda_iP_i+\nu\left(\sum_iP_i-P\right).$$
- 互補鬆弛（complementary slackness）：$\lambda_iP_i=0$，即 $P_i>0\Rightarrow\lambda_i=0$；$P_i=0\Rightarrow\lambda_i\ge0$。
- 對 $P_i$ 偏微分：$\frac{\partial}{\partial P_i}\frac12\log_2\left(1+\frac{P_i}{\sigma_i^2}\right)=\frac1{2\ln2}\cdot\frac1{P_i+\sigma_i^2}$。所以
$$P_i>0:\ -\frac1{2\ln2}\frac1{P_i+\sigma_i^2}+\nu=0\ \Rightarrow\ P_i+\sigma_i^2=\frac1{2\nu\ln2}=:\theta\ (\text{常數});$$
$$P_i=0:\ \lambda_i=\nu-\frac1{2\ln2\,\sigma_i^2}\ge0\ \Rightarrow\ \sigma_i^2\ge\theta.$$
- 合起來就是 $P_i=\max\{0,\theta-\sigma_i^2\}$：**分配的能量 + 雜訊 = 常數（水面）**。∎

【口頭】寫完數學就做完了；但更厲害的人會想到畫一個圖讓人很清楚理解——**graphical interpretation** 非常重要。Water-filling 的結論：雜訊比較小的 channel（less noisy）要分 **more power**——定性；而且有定量：雜訊 1 倍和 2 倍，能量可能 2:1 分配（加起來都是 3）。

---

## 8. Water-filling 真的對嗎：mercury／water-filling

[▶ 44:06](https://youtu.be/rk2pStZDrxg?t=2646)

【口頭】後來有人模擬，發現實際照 water-filling 做，好像得不到好結果。理論完全正確、數學也對，但很怪。

- 問題出在**假設**：$\frac12\log(1+\text{SNR})$ 很漂亮、可以微分，才得到「$P+\sigma^2$ = 常數」；但它是建立在**高斯輸入**上。實際用的輸入不是高斯，例如限制成 **BPSK**（只送 ±1，設計 ±1 的序列）。
- 實作的感覺反而是 **SNR proportional**（equal SNR）：雜訊 1 倍和 2 倍，分配 1 和 2，讓大家的 SNR 都一樣，結果比較好——和 water-filling 方向相反。

**BPSK 時重算**：$Y=X+Z$，$X\in\{\pm1\}$。$I=h(Y)-h(Z)$ 這步仍然對，但 $h(Y)$ 不再是高斯。這是 symmetric channel，uniform 輸入（±1 各 1/2）達到 capacity；代進去算出的 $h(Y)$ 是很醜的公式，仍然可以微分。畫圖會發現兩端的極端行為：
- 能量大時，比較像 SNR proportional；
- 能量小時，比較像 water-filling——所以 water-filling 也沒有全錯。

> ⚠️ 逐字稿缺字／口誤：[▶ 48:09](https://youtu.be/rk2pStZDrxg?t=2889) 老師說「Sergio Verdú 他們……在 2016 年」，後面 [▶ 49:41](https://youtu.be/rk2pStZDrxg?t=2981) 又說「2006 年 Sergio Verdú 他們做的」。課本參考文獻 [250] 是 A. Lozano, A.M. Tulino, S. Verdú, *Optimum power allocation for parallel Gaussian channels with arbitrary input distributions*, IEEE Trans. IT 52(7), **2006**。應為 2006。

**Mercury/water-filling**（Lozano–Tulino–Verdú 2006，課本 Observation 5.37，pp. 199–200）：
- 原本的 water-filling：排好 $\sigma_1^2,\dots,\sigma_4^2$，倒水。
- 新的做法要**倒兩次**：先在每個 bin 倒適量的**水銀**（調整 bin 的高度），再倒水。水銀和水不相溶、比水重，所以可以當「預先調整高度」。水銀的量和 mutual information 的微分有關（論文裡用一個函數 $G$ 的形式表示；課本說是透過 mutual information 和 MMSE 的關係得到）。
- 意思是：channel 的「高度」不只由 $\sigma^2$ 決定，還有非高斯輸入帶來的因素——把實作和理論再拉近一點。
- 【課本補充】當總功率 $P$ 很小時，最佳策略近似 **equal SNR**：比較吵的 channel 反而要分**比較多**的功率。

> ⚠️ 待確認：逐字稿 [▶ 48:09](https://youtu.be/rk2pStZDrxg?t=2889) 說「能量夠大時用 proportional，能量小時傾向 water-filling」；課本 Observation 5.37 說「$P$ 很小時近似 equal SNR principle」。兩者方向相反，兩邊都列出，需再確認。

**Two-phase water-filling**（老師團隊 2012，課本 [400] Wang, Chen, Wang, IEEE Trans. IT 58(6), 2012）[▶ 49:41](https://youtu.be/rk2pStZDrxg?t=2981)：
- Verdú 他們針對 BPSK、QPSK 輸入，但仍是**高斯雜訊**。有些通道（例如光學）不是高斯雜訊。
- 這時 mercury/water-filling 不 work：高斯雜訊時預先調整**永遠往上**（倒水銀只會墊高）；但 Laplacian 等非高斯雜訊，高度可能要**拉高也可能降低**。
- 改名 **two-phase water-filling**：第一階段定出雜訊高度並拉高或降低（調整量和雜訊有關），第二階段倒水，水面告訴你每個 channel 該用多少能量。

【口頭】教訓：理論結果和經驗 mismatch 時，數學常常是對的，出錯的常是**假設**。高斯輸入只是一個指標，大家還在用是因為數學上最容易處理。第六章會給 BPSK 下的 capacity 公式，會看到它真的很醜。

【課本補充】課本最後強調：實際數位通訊重要的是「在可接受的小錯誤率（例如 bit error ≤ $10^{-5}$）下的有效傳輸率」；研究者用 channel capacity 當設計準則，是為了讓分析可行、得到簡單的參考方案。

---

## 9. 一頁速查表

**Thm 5.33（高斯雜訊最難對付）**：同 variance $\sigma^2$ 的加性雜訊，$C(P)\ge\frac12\log_2(1+\frac P{\sigma^2})$。
- 關鍵一步：都用高斯輸入；$\log\frac{f_{Z_g}}{f_{Y_g}}$ 只有二次項，$Z$、$Z_g$ second moment 相同 ⇒ 可把權重 $f_{Z_g}$ 換成 $f_Z$；相減後用 $\ln u\le u-1$，積分 $=1-1=0$。

**Fading** $Y=AX+Z$，$E[A^2]=1$
- DSI（接收端知道 $A$）：$C_{DSI}=E_A\left[\frac12\log_2(1+\frac{A^2P}{\sigma^2})\right]\le C_G$（Jensen，log concave）。
- FSI（兩端都知道）：$C_{FSI}=E_A\left[\frac12\log_2(1+\frac{A^2p^*(A)}{\sigma^2})\right]$，$p^*(a)=\max\{0,\frac1\lambda-\frac{\sigma^2}{a^2}\}$。
- 差別：DSI 是 sup 在外（輸入固定），FSI 是 sup 在內（輸入隨 $A$ 調）。

**平行高斯通道（Thm 5.36）**
- $C(P)=\sum_i\frac12\log_2(1+\frac{P_i}{\sigma_i^2})$，$P_i=\max\{0,\theta-\sigma_i^2\}$，$\sum P_i=P$。
- 證明：$I\le\sum h(Y_i)-\sum h(Z_i)$（independence bound）→ 功率分配；KKT：$P_i>0\Rightarrow P_i+\sigma_i^2=\theta$。
- 圖：底高 $\sigma_i^2$、寬 1 的 bin，倒水量 $P$；底高過水面的 channel 不送。

**實務**：非高斯（BPSK 等）輸入下 water-filling 不是最佳 → mercury/water-filling（高斯雜訊，先倒水銀墊高）；非高斯雜訊 → two-phase water-filling（可升可降）。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 相關的平行高斯通道（先對角化再 water-filling）、非高斯雜訊、band-limited 波形通道 | 第 26 集（§5.6–5.8） |
| BPSK 輸入下的 capacity 公式 | 第 31 集（§6.6 Shannon limit） |
| Reverse water-filling（rate-distortion 對高斯 source 的對偶） | 第 29 集（第 6 章） |

---

## 附：本集一句話總結

> **同能量的加性雜訊中高斯最難對付；fading 只會讓 capacity 變小，而若兩端都知道通道狀況、或有多個平行高斯通道，最好的功率分配就是「倒水」——雜訊越小的通道分越多、太吵的乾脆關掉；但這只對高斯輸入成立，實際 BPSK 時要先倒水銀（或兩階段調整）再倒水。**

---

## ⚠️ 待確認清單

1. [▶ 48:09](https://youtu.be/rk2pStZDrxg?t=2889) 老師說高能量時 SNR proportional、低能量時像 water-filling；課本 Observation 5.37 說 $P$ 很小時近似 equal SNR。方向相反，待確認。

---

*筆記依據陳伯寧老師「消息理論」Lec25 錄影逐字稿（whisper large-v3-turbo，51:43）與 Alajaji & Chen 課本 §5.4–5.5 整理。*
