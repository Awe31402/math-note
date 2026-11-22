---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 31
lecture: Lec31 6.6 Shannon limit of communication systems（2/2）
date: 待補
video: https://youtu.be/Bvvfphtesl0
notes: Alajaji & Chen §6.6 Example 6.39–6.40（pp. 255–258）；後半預告第二部分（information spectrum，課本沒有，只依逐字稿）
---

# 第 31 集 · Lec31 §6.6：Shannon limit（下）與第一部分總結、information spectrum 預告 [▶ 影片](https://youtu.be/Bvvfphtesl0)

← 上一集：[30](30-lossy-joint-source-channel-coding.md) ｜ [總目錄](README.md) ｜ 下一集：[32](32-generalized-information-measures.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 31 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（27:40，whisper large-v3-turbo）＋ 課本 §6.6（pp. 255–258）；後半（第 5–8 節）課本沒有，只依逐字稿
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「lossy」聽成「Lawsey／Law C」，「McEliece」聽成「McLease」，「cosh」聽成「cos h」，「Hamming」聽成「Hemming」，「bit error」聽成「bit array」，「rate-1/2、1/3」聽成「21-code、3-code、E3Co、二一扣」，「LDPC」聽成「LDP code／LDCB code」，「Gallager」聽成「Gallagher」，「MacKay」聽成「Mckay」，「Berrou」聽成「Beroux」，「Turbo code」聽成「TurboCo」，「Rayleigh fading」聽成「relate fading」，「MATLAB」聽成「MateLab」，「stationary ergodic」聽成「stational, erratic／Stationary Guarded／Stational Ergatic」，「complementary CDF」聽成「Complimentary／Compromised CDF」，「Te Sun Han」聽成「提升漢」，「Shannon」聽成「懸人」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. BPSK-AWGN capacity 公式的來源](#1-bpsk-awgn-capacity-公式的來源)
- [2. LDPC 與 Turbo code 的故事](#2-ldpc-與-turbo-code-的故事)
- [3. Rayleigh fading channel 的 Shannon limit](#3-rayleigh-fading-channel-的-shannon-limit)
- [4. 第一部分總結：一切靠大數法則](#4-第一部分總結一切靠大數法則)
- [5. 沒有大數法則時：看整個分布](#5-沒有大數法則時看整個分布)
- [6. 壓縮：entropy density 的 complementary CDF](#6-壓縮entropy-density-的-complementary-cdf)
- [7. 傳輸：information density 的分布](#7-傳輸information-density-的分布)
- [8. Separation theorem revisited](#8-separation-theorem-revisited)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

第一部分（第一到六章）的總結：補完 BPSK-AWGN 的 Shannon limit（公式來源、LDPC／Turbo 的歷史），加上 Rayleigh fading 的例子。接著預告**第二部分**：當資料**沒有大數法則**（不是 i.i.d.、不是 stationary ergodic）時，要看的是 $\frac1n\log\frac1{P(Z^n)}$（或 information density）的**整個分布**；從它的 complementary CDF 就能讀出壓縮、傳輸的極限，而且 **separation 可能不成立**。

| 主題 | 來源 |
|---|---|
| BPSK-AWGN 的 Shannon limit | Example 6.39、Table 6.2（pp. 255–257） |
| Rayleigh fading（DSI）的 Shannon limit | Example 6.40、Table 6.3（pp. 257–258） |
| 第二部分預告：information spectrum | 逐字稿（課本沒有） |

---

## 1. BPSK-AWGN capacity 公式的來源

[▶ 00:00](https://youtu.be/Bvvfphtesl0?t=0)

【口頭】Lossy information transmission theorem 是整個第一部分的總結精華。上次的例子：binary input（BPSK）的 AWGN capacity，相當實際。
- 這個公式比較早出現在 70 年代 **McEliece** 的一份報告裡（不是發表的論文），因為它相當簡單。
- Capacity = 輸入輸出 mutual information 的最大值；輸入是 ±1 加白色高斯雜訊。接收端 ±1 的兩個分布只是平移 ⇒ symmetric channel ⇒ 最好的輸入是 uniform。用 $\frac12,\frac12$ 代進去直接算。
- 積分積不出來，只能把公式寫下來。裡面的 $\cosh x=\frac12(e^x+e^{-x})$：$\frac12$ 來自機率 $\frac12$、$\frac12$；$e^{\pm x}$ 來自高斯指數的**一次項**——指數裡有二次、一次、零次項，二次和零次兩邊一樣可以提出去，只剩中間的一次項，所以出現 cosh。
- 只有一層積分，畫圖軟體可以很精確地描點。把功率換成 $E_b$（每個 information bit 的能量）和 $R_{sc}$（code rate：一次 channel 傳輸帶幾個 information symbol），畫 $E_b/N_0$ 的圖。

【課本補充】課本這個公式引的是 [63] S.A. Butman, R.J. McEliece, *The ultimate limits of binary coding for a wideband Gaussian channel*, JPL DSN Progress Report 42–22, 1974。

**判斷條件**：$R(D)<\frac1{R_{sc}}C$。Binary input、Hamming distortion ⇒ $D$ 是 bit error rate。
- 一般有線、無線通訊的經驗法則：$10^{-5}$ 是必須達到的目標。
- Rate 1/2：**0.19 dB**；降速到 1/3：**−0.495 dB**（課本 −0.496）。負的 dB 代表傳送能量可以**低於**雜訊能量（0 dB 是相等；dB = $10\log_{10}$）。
- 理論結果 1948 年就確定了，人類花了 50 年才達到。

---

## 2. LDPC 與 Turbo code 的故事

[▶ 04:37](https://youtu.be/Bvvfphtesl0?t=277)

【口頭】
- **LDPC（Low-Density Parity-Check）code**：一個線性碼，parity-check 矩陣裡 1 的個數很少，所以叫 low density。Shannon 理論出來不久就發明了，發明者是 MIT 的 **Gallager**（課程介紹的參考書之一的作者），在他的博士論文裡提出；當時電腦沒辦法模擬，所以只是理論。那本論文現在 MIT Press 還買得到，很便宜。
- **1998 年 MacKay**：英國學者，不是通訊學者，是 computer science、寫軟體的。他在一堆很舊的論文裡重新找到這個東西、拿來模擬，發現效果非常好，甚至比 Turbo code 還好。論文裡寫的是「**rediscover** LDPC code」。到 1998 年已經可以在離 Shannon limit 0.0 幾 dB 達到 $10^{-5}$。
- **Turbo code（1993）**：Berrou 他們發現的，也沒有理論依據。Shannon 說碼夠長、隨機亂取都會很好，他就把碼拉得很長（$n$ 大約 18 萬，rate 1/3）。在 0.9 dB 達到 $10^{-5}$，離 Shannon limit 0.7 dB 以內。第一次發表時大家都懷疑（沒有解釋為什麼這麼好），但大家回去模擬，事實勝於雄辯，才開始思考為什麼。
- 第四代、第五代行動通訊的 data channel 保護碼都還是 **LDPC**——現在能找到最好的碼。

> ⚠️ 逐字稿缺字：[▶ 07:12](https://youtu.be/Bvvfphtesl0?t=432) 發表 Turbo code 的研討會聽成「德國的 WOM」。課本參考文獻 [44] 是 Berrou, Glavieux, Thitimajshima 發表在 **IEEE ICC（International Conference on Communications）** 的論文；地點課本沒寫。碼長「18 萬」的算術見第 30 集（$65536\times3=196{,}608$）。

【課本補充】課本的 LDPC 參考文獻：Gallager [133]（IRE Trans. IT, 1962）、[134]（MIT Press, 1963）；MacKay–Neal [251]（Electron. Lett., 1997）。

【口頭】圖的價值：曲線左邊不存在、右邊存在，曲線就是 Shannon limit；rate 越快（例如 4/5），需要的 SNR 越多。

---

## 3. Rayleigh fading channel 的 Shannon limit

[▶ 08:14](https://youtu.be/Bvvfphtesl0?t=494)

因為是 **separation**（$R(D)$ 只和 source 有關、$C$ 只和雜訊有關），可以只換右邊的 channel。【口頭】今天也會告訴你為什麼現在的傳輸管道會違反 separation principle。

**Example 6.40**（p. 257）：binary uniform source，**BPSK、Rayleigh fading**（$f_A(a)=2ae^{-a^2}$，$a>0$），**DSI**（接收端知道 fading 振幅）。
- $C_{DSI}$ 是期望值，有**兩層積分**：
$$C_{DSI}(\gamma_b)=1-\sqrt{\frac{R_{sc}\gamma_b}\pi}\int_0^\infty\int_{-\infty}^\infty f_A(a)\,e^{-R_{sc}\gamma_b(y+a)^2}\log_2\left(1+e^{4R_{sc}\gamma_bya}\right)dy\,da.$$
- 【口頭】一層積分 MATLAB 這類數值軟體都能畫得很精確；兩層積分需要一點技巧（會有 numerically unstable 的狀態），但都可以克服。

**Table 6.3**（Rayleigh fading、DSI，dB）：

| $R_{sc}$ | $D_{SL}=0$ | $10^{-5}$ | $10^{-4}$ | $10^{-3}$ | $10^{-2}$ |
|---|---|---|---|---|---|
| 1/3 | 0.489 | 0.487 | 0.479 | 0.412 | −0.066 |
| 1/2 | 1.830 | 1.829 | 1.817 | 1.729 | 1.107 |
| 2/3 | 3.667 | 3.664 | 3.647 | 3.516 | 2.627 |
| 4/5 | 5.936 | 5.932 | 5.904 | 5.690 | 4.331 |

（課本表格最後一欄印成 $10^{-3}$，依數值趨勢應為 $10^{-2}$。）

【口頭】
- Rate 1/2、$10^{-5}$：fading 要 **1.829 dB**，純 AWGN 只要 0.186 dB，多了 1 dB 多。其實也沒多多少——若接收端能完美偵測 fading，1 點多 dB 就能做到。
- 但現在離 1.829 dB 還很遠（好幾 dB 以上），而且「完美偵測 channel」本身就做不到。可能再過幾十年才知道怎麼在 fading channel 上做到。

---

## 4. 第一部分總結：一切靠大數法則

[▶ 10:48](https://youtu.be/Bvvfphtesl0?t=648)

【口頭】整個 Shannon 理論的精神：**大數法則**——$n$ 個觀察代入一個函數取平均，$n$ 夠大時一定趨近一個常數（希望是它的期望值）：
$$\frac1n\sum_{i=1}^nf(Z_i)\to E[f(Z)].$$
- i.i.d. 時會發生（一般資料分析很重要的假設）；可以擴展到 stationary ergodic。只要有這個行為，Shannon 的定理都對。

---

## 5. 沒有大數法則時：看整個分布

[▶ 11:48](https://youtu.be/Bvvfphtesl0?t=708)

【口頭】70、80 年代開始思考：如果這件事沒發生呢？
- 例：$Z_1,\dots,Z_n$ stationary 但**不 ergodic**，平均會收斂到一個**隨機變數**（某個值有某個機率、另一個值有另一個機率）。
- 民調的例子：打 1000 通電話，支持記 1、不支持記 0，平均就是支持度。你算 30%、他算 50%，**都是對的**——資料本來就不符合大數法則：每個人之間是 dependent，人會受別人影響。
- 就像從牛頓力學推廣到相對論，希望把原來的定理推廣，完整解釋現在的現象。

**對資料壓縮，那個函數是什麼**：information 是機率倒數取 log，所以
$$\frac1n\log_2\frac1{P_{Z^n}(Z^n)}.$$
- i.i.d. 時它是 $\frac1n\sum\log\frac1{P(Z_i)}$：variance 是 $\frac1n\mathrm{Var}$（$n$ 個 variance 相加、分母 $n^2$），PDF 越來越窄、越來越尖；CDF 變成在期望值（entropy）處跳起來的 **step function**。
- 不 i.i.d. 時不能拆成乘積，但 $n$ 很大時它的**極限分布**仍然存在（stationary、non-stationary、time-varying 都有一個 distribution），只是**散開**了。
- 這是數學結果，問題是怎麼和**操作**扯上關係。

---

## 6. 壓縮：entropy density 的 complementary CDF

[▶ 15:27](https://youtu.be/Bvvfphtesl0?t=927)

畫 $\frac1n\log_2\frac1{P(Z^n)}$ 極限分布的 **complementary CDF**（$1-$CDF）。【口頭】結果非常漂亮，而且完全解釋過去的現象：
- 橫軸是壓縮率 $R$，縱軸讀到的值就是用這個壓縮率時**最好能達到的錯誤率**——存在一個操作的碼做得到。
- 錯誤率要求 $10^{-5}$，對到的橫軸位置就是**壓縮極限**。只要把 complementary CDF 畫出來，就完全知道能做到什麼程度。

**檢查古典情形**（i.i.d.／stationary ergodic）：complementary CDF 是在 entropy 處從 1 掉到 0 的階梯。
- 錯誤率要求 $10^{-3}$ 或 $10^{-1}$，壓縮極限都是 **entropy**——完全正確。
- 壓得比 entropy 小，錯誤率就是 1——這就是 **strong converse**。
- 【口頭】這個證明**不用 typical set**，而且更簡單。

【口頭】做資料統計的啟示：看你統計的那個量本身的分布。i.i.d. 就收斂到一點；沒有就散開。把「散開的機率」和「真正的操作」之間的量化關係找清楚，就有完整的解釋。關鍵是找**對的量**——機率倒數取 log，正是操作上的 information 量。

---

## 7. 傳輸：information density 的分布

[▶ 19:00](https://youtu.be/Bvvfphtesl0?t=1140)

雜訊不再是白色高斯，而是 dependent 的 stationary 高斯，甚至 non-stationary。看第 28 集講過的量：
$$\frac1n\log_2\frac{P_{X^nY^n}(X^n,Y^n)}{P_{X^n}(X^n)P_{Y^n}(Y^n)}.$$
- 獨立時拆成每個時間的和，取 log 變相加，大數法則 ⇒ 收斂到期望值 = **mutual information**。（joint 的 information 量扣掉兩個個別的——Shannon 的觀念：傳送端和接收端的連動共識越大，傳輸量越大。）
- 古典情形 CDF 是在 $I$ 處的 step：rate 比 capacity 小（例如 capacity 2.1、rate 1.9）錯誤率可以任意小；rate 2.3 錯誤率就是 1——strong converse。
- 一般情形：畫它的分布。錯誤率要求 $10^{-5}$，對到的就是最好的傳輸量；要求 $10^{-4}$、$10^{-3}$，速度可以再提升。
- 錯誤率一定要是 0（任意小）：就是分布的**左端**，記作 $\underline I(X;Y)$（inf-information rate）；速度超過分布的**右端** $\bar I(X;Y)$（sup-information rate），錯誤率都是 1。古典情形兩者合在一起（step function）。
- 這個量叫 **information density**——density 指的是機率密度。

【口頭】這是 90 年代之後很重要、很漂亮的結果，完全涵蓋古典理論；這種 spectrum 式的解釋，和操作真的是同一件事。Te Sun Han 說過一句話：你想對了，證明就非常簡單，比傳統的更簡單。

---

## 8. Separation theorem revisited

[▶ 23:12](https://youtu.be/Bvvfphtesl0?t=1392)

**古典**：source 的 complementary CDF 是 entropy 處的階梯，channel 的是 capacity 處的階梯。只要 entropy < capacity，在中間選一個速度傳：壓縮錯誤率 0、傳輸錯誤率也 0。兩個點的決定完全無關——**separation**。

**一般情形**（90 年代的經典論文「separation theorem revisited」）：
- Source 的 $\frac1n\log\frac1{P(Z^n)}$ 不能寫成 product distribution，但 complementary CDF 一定畫得出來；channel 的 information density 也一樣。
- 選一個傳輸速度，最好的錯誤率就是**兩邊的面積（尾巴機率）加起來**；找讓左右面積最小的速度就是最好的。
- 兩條曲線**相交**時就**不能 separation**。論文解釋了為什麼以前可以 separation，以及傳輸管道是 non-stationary、或只有 stationary 沒有 ergodic（沒有大數法則）時，怎麼從統計量詮釋實際操作。

【課本補充】課本參考文獻 [394] S. Vembu, S. Verdú, Y. Steinberg, *The source-channel separation theorem revisited*, IEEE Trans. IT；[172] T.S. Han, *Information-Spectrum Methods in Information Theory*（Springer, 2003）；[396] Verdú & Han, *A general formula for channel capacity*（IEEE Trans. IT 40(4)）。

【口頭】
- 這個解釋走得很前面：現在還沒有真正能掌握很不穩定的傳輸管道，做法仍是對付 AWGN、希望把 fading 完全偵測出來。
- 但這種狀態會越來越明顯：傳送速度要求越來越高（早期在美國撥接上網 2400、9600 bps 就很高興；現在 Gbps 起跳，要求 10 Gbps），前後雜訊的相依性會非常強。
- 就像 Shannon 當年給出 rate 1/2、$10^{-5}$ 要 0.19 dB，花了 50 年才達到；這個 spectrum 的極限可能就是未來的目標。目前比較少人做這方面。

---

## 9. 一頁速查表

**BPSK-AWGN Shannon limit**（$10^{-5}$）：rate 1/2 **0.186 dB**、1/3 **−0.496 dB**。公式：uniform ±1 輸入的 $I$，cosh 來自高斯指數的一次項。

**Rayleigh fading + DSI**（$10^{-5}$）：rate 1/2 **1.829 dB**、1/3 0.487 dB；兩層積分。

**碼的歷史**：Gallager 1962 提出 LDPC → Turbo 1993（0.9 dB，差 0.7 dB）→ MacKay 1998 rediscover LDPC（差 0.0 幾 dB）→ 4G／5G data channel 用 LDPC。

**第二部分預告（information spectrum）**
- 古典：$\frac1n\log\frac1{P(Z^n)}\to H$、$\frac1n\log\frac{P(X^n,Y^n)}{P(X^n)P(Y^n)}\to I$（大數法則；CDF 是 step）。
- 一般：看極限分布。壓縮率 $R$ 的最佳錯誤率 = entropy density 的 complementary CDF 在 $R$ 的值；錯誤率 0 的傳輸極限是 information density 分布的左端 $\underline I$，超過右端 $\bar I$ 錯誤率為 1。
- Separation：古典時兩個階梯分得開就行；一般時錯誤率 = 兩邊尾巴面積之和，曲線相交就不能 separation。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 廣義的 information 量（inf／sup information rate、spectrum） | 第 32 集（第二部分第 1 章） |
| 一般 source 的壓縮定理（complementary CDF） | 第 33 集（第 2 章） |
| 隨機過程的隨機性量度 | 第 34 集（第 3 章） |
| 一般 channel 的 coding theorem（information density 的左端） | 第 35 集（第 4 章） |

---

## 附：本集一句話總結

> **第一部分的終點是 Shannon limit 表——AWGN 上 rate 1/2 要 0.186 dB、Rayleigh fading 要 1.829 dB，LDPC 已逼近前者；而第一部分的一切都靠大數法則，第二部分要處理沒有大數法則的情形：那時看的是 $\log\frac1P$ 或 information density 的整個分布，從它的 complementary CDF 直接讀出壓縮與傳輸的極限，separation 也不再保證成立。**

---

*筆記依據陳伯寧老師「消息理論」Lec31 錄影逐字稿（whisper large-v3-turbo，27:40）與 Alajaji & Chen 課本 §6.6 整理。*
