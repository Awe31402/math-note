---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 18
lecture: Lec18 4.3 Block codes for data transmission over DMCs (3/3)
date: 待補
video: https://youtu.be/TnRthbWsjFw
notes: Alajaji & Chen §4.3 末（pp. 123–126，converse 證明、Fig. 4.5、Observation 4.12–4.13）
---

# 第 18 集 · Lec18 §4.3 (3/3)：channel coding converse、information density、三個區域 [▶ 影片](https://youtu.be/TnRthbWsjFw)

← 上一集：[17](17-channel-coding-theorem-achievability.md) ｜ [總目錄](README.md) ｜ 下一集：[19](19-calculating-channel-capacity-symmetric-kkt.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 18 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（31:22，whisper large-v3-turbo）＋ 課本 §4.3 末（pp. 123–126）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「大數法則」聽成「大樹法則」，「加性白高斯雜訊（AWGN）」聽成「相加白色高三根／香加白色高斯」，「公設」聽成「公社」，「strong converse」聽成「Trone Converse／Strone Converse」，「stationary ergodic」聽成「station-garde」，「Fano」聽成「Phenor／Phanal／Phenom」，「complementary CDF」正確，「information density」聽成「Information Bensing」，「asymptotic」聽成「asynthetic」，「coherence bandwidth」聽成「coherent bandwidth」。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 回顧：大數法則與 typical set 的配對現象](#1-回顧大數法則與-typical-set-的配對現象)
- [2. 預告：information density 的分布](#2-預告information-density-的分布)
- [3. 為什麼通訊所一定要修消息理論](#3-為什麼通訊所一定要修消息理論)
- [4. Converse 的工具：Fano 不等式](#4-converse-的工具fano-不等式)
- [5. Converse 的證明](#5-converse-的證明)
- [6. 錯誤率下界的意義](#6-錯誤率下界的意義)
- [7. 錯誤率曲線與 strong converse](#7-錯誤率曲線與-strong-converse)
- [8. 一般通道的三個區域](#8-一般通道的三個區域)
- [9. Zero-error codes 與之後的發展](#9-zero-error-codes-與之後的發展)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

把 channel coding theorem 的 **converse** 證完（用 Fano 不等式 + DPI），然後用 **information density** 的分布重新看整件事，並說明一般通道會有**三個區域**。

| 主題 | 課本 |
|---|---|
| Fano 不等式（channel coding 版） | (4.3.6)（pp. 123–124） |
| Converse 證明 | pp. 124–125 |
| Fig. 4.5、三個區域 | Observation 4.12 與註 8（p. 125） |
| Zero-error codes、編碼理論的發展 | Observation 4.13（pp. 125–126） |

---

## 1. 回顧：大數法則與 typical set 的配對現象

[▶ 00:00](https://youtu.be/TnRthbWsjFw?t=0)

【口頭】花比較多時間解釋 Shannon 的概念，因為概念最重要。工程科學裡真正抓的都是大數法則的行為。

- $(X_i,Y_i)$ 兩兩獨立（例如 AWGN）。帶進一個實數函數 $h$ 再平均，會非常接近期望值。把差 $<\delta$ 的所有 $(x^n,y^n)$ 收集起來就是一個集合——分布、$\delta$、函數一給定，這個集合就**完全確定**，是純數學的量，跟操作（coding）無關。
- Shannon 選的函數是**自己的機率**：$h=-\log P_{X^n,Y^n}$，就是 self-information，完全符合三大公設；它的期望值就是 entropy。
- **配對現象**：在這個集合裡，$x$ 和 $y$ 幾乎一對一——就像 identity channel（送 0 得 0、送 3 得 3，收到 3 就知道送 3）。這是以前機率學家沒看到的。
- $n$ 不夠大時，集合裡會有**少數**一對二、二對一的 pair（例如收到 3 可能來自 2 或 3），會出錯。所以錯誤有兩種：收到的 $y^n$ 在外面（不跟任何人 typical），或落在裡面但一對二。數量很少。
- 【口頭】換別的函數試試看就沒有這個現象——這個函數找得很好，跟三大公設有關。所以老師一開始很強調三大公設；大部分的書直接給 entropy 定義，省略了背後的思考模式。

---

## 2. 預告：information density 的分布

[▶ 05:39](https://youtu.be/TnRthbWsjFw?t=339)

【口頭】第二部分會講：**我們真正關心的不是期望值，而是這個量的機率表現**。
- 令 $\omega=-\frac1n\log P(\cdot)$（老師用 $h$、$\omega$ 表示）是一個新的實數隨機變數，分布完全由 $(X,Y)$ 決定。傳統上看期望值；90 年代發現 **$\omega$ 的分布完全決定通訊的行為**。
- 把它的 complementary CDF $\Pr[\omega>x]$ 畫出來：i.i.d. 時 $n\to\infty$ 變成一個階梯（step）——這就是 **strong converse**。雜訊不像 AWGN、彼此 dependent 時，$\omega$ 會散開，不是 strong converse；這時傳輸速度在哪裡，對應的就是最好的錯誤率。
- Shannon 的時代講的是 i.i.d.，平均趨近期望值。

---

## 3. 為什麼通訊所一定要修消息理論

[▶ 07:42](https://youtu.be/TnRthbWsjFw?t=462)

【口頭】
- 國外以通訊為主的研究所，消息理論幾乎都必修——不是每個人都要做這方面研究，而是要知道**大數法則是很多工程成功的背後道理**。現象不符合大數法則，大概就沒辦法操作；non-stationary 或 non-ergodic 的系統，每個人量的不一樣，沒辦法下結論。有大數法則，系統是封閉體系，手機今年做、明年用都沒問題。
- 老師在美國學這門課時，老師一節課一行一行抄黑板，學生一行一行抄，剛好證完下課，完全不知道在幹嘛——每一步都對，但抓不到重點。
- 要記得 1948 年論文的概念：**typical set、大數法則、random coding**；能很快說出它在做什麼、用到別的領域或研究題目，就非常成功。

---

## 4. Converse 的工具：Fano 不等式

[▶ 10:19](https://youtu.be/TnRthbWsjFw?t=619)

Converse：rate 超過 information capacity，錯誤率就不能任意小，有一個不小的下限（bounded away from zero）。

**為什麼用 Fano**（【口頭】）：Fano 不等式跟操作一點關係都沒有——不告訴你怎麼設計，只說**任何設計**（任何 $f_n$、$g_n$）在接收端的錯誤率都滿足它。Converse 要證明所有設計都不好，不可能一個一個檢查，所以需要這種對所有設計都成立的不等式。

**Channel coding 版的 Fano**（課本 (4.3.6)，pp. 123–124）：$(n,M_n)$ 碼，$W$ uniform 於 $\{1,\dots,M_n\}$，$X^n=f_n(W)$，$\hat W=g_n(Y^n)$，$\Pr[W\ne\hat W]=P_e(\mathcal C_n)$。由弱版 Fano（$h_b\le1$）：
$$H(W|Y^n)\le1+P_e(\mathcal C_n)\log_2(M_n-1)<1+P_e(\mathcal C_n)\log_2M_n.$$

**和 mutual information 的關係**（【口頭】）[▶ 12:51](https://youtu.be/TnRthbWsjFw?t=771)：
- 傳送速度和 $\frac1nI(X^n;Y^n)$ 有關（$n$ 很大，例如 6 萬個一次解）；獨立時 $\frac1nI(X^n;Y^n)=I(X;Y)$。
- $I(X;Y)=H(X)-H(X|Y)$：$H(X)$ 是要送的 information，$H(X|Y)$ 是**損失**。$H(X|Y)=0$ 時收到 $Y$ 對 $X$ 沒有不確定性，全部送過去。例：每個 $X$ 帶 2 bit，希望全部送過去，但有雜訊會損失一點。
- Fano 給 $H(X|Y)$ 一個上界，等價於給 mutual information 一個下界——對所有設計都對。

---

## 5. Converse 的證明

[▶ 14:52](https://youtu.be/TnRthbWsjFw?t=892)

（課本 pp. 124–125）任何 $(n,M_n)$ 碼：

**(1) DPI**：$W\to X^n\to Y^n$ 是 Markov chain（$W$ 先 map 到 channel symbol，收到 $Y$ 再猜回 $\hat W$），所以
$$I(W;Y^n)\le I(X^n;Y^n).$$
【口頭】經過 processing 只會損失 information，越靠近的 mutual information 越大。

**(2) 用 $C$ 上界 $I(X^n;Y^n)$**：
$$I(X^n;Y^n)\le\max_{P_{X^n}}I(X^n;Y^n)\le\max_{P_{X^n}}\sum_{i=1}^nI(X_i;Y_i)\le\sum_{i=1}^n\max_{P_{X^n}}I(X_i;Y_i)=\sum_{i=1}^n\max_{P_{X_i}}I(X_i;Y_i)=nC.$$
- 第二個 ≤：Theorem 2.21（DMC 的條件獨立）。
- 第三個 ≤：先加總再取最大 ≤ 個別取最大再加總。
- 【口頭】不管輸入角度怎麼選，$\frac1nI(X^n;Y^n)\le C$，因為 $C$ 是最大的共識。

**(3) 組合**：$W$ uniform，$\log_2M_n=H(W)$：
$$\log_2M_n=H(W|Y^n)+I(W;Y^n)\le H(W|Y^n)+I(X^n;Y^n)\le H(W|Y^n)+nC<1+P_e(\mathcal C_n)\log_2M_n+nC.$$
【口頭】要送的 entropy 希望全部送過去，但會差一點點（$H(W|Y^n)$）；帶進不等式，其實到這一步就做完了。

**(4) 解出 $P_e$**：
$$P_e(\mathcal C_n)>1-\frac{C}{\frac1n\log_2M_n}-\frac1{\log_2M_n}=1-\frac{C+\frac1n}{\frac1n\log_2M_n}.$$
這對**所有設計、所有有限 $n$** 都成立。

**(5) 漸近**：若 $\liminf\frac1n\log_2M_n=\frac C{1-\mu}$（$\mu\in(0,1)$，即 rate $R=\frac C{1-\mu}>C$、$\mu=1-\frac CR$），則對任意 $0<\varepsilon<1$，存在 $N$ 使 $n\ge N$ 時
$$\frac1n\log_2M_n\ge\frac{C+1/n}{1-(1-\varepsilon)\mu}$$
（否則這個不等式會在無限多個 $n$ 被違反，得到 $\liminf\frac1n\log_2M_n\le\frac C{1-(1-\varepsilon)\mu}<\frac C{1-\mu}$，矛盾）。於是
$$P_e(\mathcal C_n)>1-[1-(1-\varepsilon)\mu]=(1-\varepsilon)\mu>0.$$
【口頭】這部分後面就交給同學看，不會太難。∎

---

## 6. 錯誤率下界的意義

[▶ 17:26](https://youtu.be/TnRthbWsjFw?t=1046)

忽略 $\frac1n$（$n$ 很大，$nC\gg1$）：
$$P_e\gtrsim1-\frac CR.$$
- $R<C$：右邊是負的——錯誤率比負數大，沒有限制（forward part 說可以任意小）。例：capacity 0.5、設計 0.4，沒問題。
- $R>C$：右邊是 $(0,1)$ 的正數——**錯誤率不可能任意小**，所有方法都比它差，而且對有限 $n$ 也成立。

【口頭】Shannon 在 1948 年用很簡單的方法說明：傳送速度不可能超過 $C$。Fano 不等式物理上不那麼直觀，因為它對所有碼都對，大部分時候蠻 loose，但對 Shannon 來說夠了。所以 forward part 比較重要。

---

## 7. 錯誤率曲線與 strong converse

[▶ 20:02](https://youtu.be/TnRthbWsjFw?t=1202)

【口頭】Shannon 真正證明的事可以這樣看：
- $-\frac1n\log P(\cdot)$ 是 $(x^n,y^n)$ 共有 information 的平均量（這裡指 information density）。channel independent 時，它變成 i.i.d. 的和取平均，趨近期望值（就是 $C$，在最佳輸入下）。
- i.i.d. 的平均，PDF 會越來越集中；complementary CDF $\Pr[\frac1n\sum\omega_i>x]$ 在 $n\to\infty$ 時變成一個階梯。例：$\omega$ 取 0、1，1 的機率 $\frac14$，平均趨近 $\frac14$，而且非常緊。
- **錯誤率曲線就是這個 complementary CDF**：rate 小於期望值，錯誤率趨近 0；rate 一超過，錯誤率是 1。通訊傳送就有一條上帝畫的天然界線：這個通道不可能送得比它快，否則所有設計都會錯。
- 雜訊有相關性時，$\frac1n\log\frac1{P}$ 不一定收斂（除以 $n$，不是 $\sqrt n$），會**散開**（stationary 系統會給例子）。這時非常清楚：rate 在哪裡，最好的錯誤率就是曲線上對應的值。
- 這個量後來叫 **information density**：任何系統的 information density 的 CDF，完全決定你在這個系統能達到的效能。第二部分（全新的觀點）會證明。
- Shannon 時代只考慮 AWGN 這類 memoryless 通道，所以有 strong converse：rate 超過 capacity，所有方法的錯誤率都趨近 1。

> ⚠️ 待確認：[▶ 20:33](https://youtu.be/TnRthbWsjFw?t=1233) 老師這段把「information density」寫成 $\frac1n\log\frac1{P_{X^nY^n}}$（joint 的 self-information）；一般文獻的 information density 是 $\frac1n\log\frac{P_{Y^n|X^n}}{P_{Y^n}}$。逐字稿沒有唸出投影片上的完整式子，課本這一節也沒有，第二部分（第 35 集附近）再核對。

【課本補充】Fig. 4.5（p. 125）：橫軸 rate $R$。$R<C$：最好的 block code $\limsup P_e=0$；$R>C$：所有 block code $\limsup P_e>0$。p. 125 註 9：只要 $\frac1n\log M_n$ 從**下方**逼近 $C$，$C$ 就能當作漸近傳輸率達到。

---

## 8. 一般通道的三個區域

[▶ 25:40](https://youtu.be/TnRthbWsjFw?t=1540)

我們看的是 liminf；看 limsup 會怎樣？liminf 和 limsup（最小、最大的群集點）不一定相等，所以可能有**三個區域**。

**例子**（【口頭】）：你對長度是 10 的倍數特別有心得，$n=10,20,30,\dots$ 都設計得很好，$P_e(\mathcal C_{10}),P_e(\mathcal C_{20}),\dots\to0$；但 $n=15,25,35,\dots$ 沒有好設計，錯誤率不趨近 0。
- 後來真的找到這樣的通道：有些長度會卡住（例如有 fading 等現象，要超過 coherence bandwidth 才行），在某些特定長度就傳不好——**最好的設計**也只在某些 $n$ 好。例如 non-stationary、cyclo-stationary、periodic-stationary 的通道。
- 所以會有兩條界線 $C$ 和 $\bar C$：
  1. $R<C$：每個夠長的 $n$ 都有好設計，錯誤率趨近 0（sufficiently large 的概念——Shannon 講的是這個很強的要求）；
  2. $C<R<\bar C$：某些特定的 $n$ 很好、某些不好；
  3. $R>\bar C$：只要夠長，都很爛。
- Shannon 時代只講一條界線（已經非常不容易）。
- 有些論文討論 **什麼時候 strong converse 成立**——就是問什麼時候 $C=\bar C$、三個區域縮成兩個。答案之一：AWGN（白色雜訊）只有一條界線；雜訊有顏色、彼此 dependent，就可能有三個區域。

【課本補充】p. 125 註 8：對一般通道，三個區域是 $R<C_{op}$（最好的碼 $\limsup P_e=0$）、$C_{op}<R<\bar C_{op}$（最好的碼 $\limsup P_e>0$ 但 $\liminf P_e=0$）、$R>\bar C_{op}$（所有碼 $\liminf P_e>0$）。$\bar C_{op}$ 叫 **optimistic operational capacity**；DMC 時 $\bar C_{op}=C_{op}=C$，三個區域縮成兩個。$\bar C_{op}$ 有用一般化（spectral）mutual information rate 表示的公式。

---

## 9. Zero-error codes 與之後的發展

【課本補充】**Observation 4.13**（pp. 125–126）：converse 證明了 $\liminf P_e=0\Rightarrow\liminf\frac1n\log M_n\le C$。若要求**每個** $n$ 都完全沒有錯誤（$P_e=0$），則 $H(W|Y^n)=0$，
$$\log_2M_n=I(W;Y^n)\le I(X^n;Y^n)\le nC\ \Rightarrow\ \limsup\frac1n\log_2M_n\le C,$$
這比 (4.3.10) 更強。

【課本補充】p. 126：Shannon 的定理給出極限，但沒給有效的構造——在隨機碼裡搜尋好碼，複雜度隨 block length **雙重指數**成長。這催生了整個 coding theory：線性碼（Hamming、Golay、BCH、Reed–Muller、Reed–Solomon、convolutional codes）；1993 年 Berrou 等人的 Turbo code 在 memoryless 通道上實驗接近 capacity；Gallager 的 LDPC 被重新發現；2007 年 Arıkan 的 **polar code** 是第一個可證明達到 capacity 的確定性構造（下一節）。

---

## 10. 一頁速查表

**Fano（channel 版）**：$H(W|Y^n)\le1+P_e\log_2(M_n-1)<1+P_e\log_2M_n$，對任何 $(f_n,g_n)$ 成立。

**Converse 證明**
$$\log_2M_n=H(W)=H(W|Y^n)+I(W;Y^n)\le H(W|Y^n)+I(X^n;Y^n)\le1+P_e\log_2M_n+nC.$$
- DPI：$W\to X^n\to Y^n$ ⇒ $I(W;Y^n)\le I(X^n;Y^n)$。
- $I(X^n;Y^n)\le\sum I(X_i;Y_i)\le nC$（DMC）。
- ⇒ $P_e>1-\frac{C+1/n}{\frac1n\log_2M_n}$ ⇒ $R>C$ 時 $P_e>(1-\varepsilon)(1-\frac CR)>0$。
- 例：$C=10$、$R=20$ ⇒ $P_e\ge\frac12$。

**Zero-error**：$P_e=0\ \forall n$ ⇒ $\limsup\frac1n\log M_n\le C$。

**錯誤率 vs rate**
- DMC：一條界線 $C$（實際上有 strong converse：$R>C$ ⇒ $P_e\to1$）。
- 一般通道：$C\le\bar C$ 兩條界線、三個區域；$C=\bar C$ ⟺ strong converse 成立的那類通道。
- 真正決定行為的是 information density 的分布（第二部分）。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 怎麼算 $C=\max I$ | 第 19 集（§4.5） |
| 第一個可證明達到 capacity 的構造（polar code） | 第 20 集（§4.4） |
| Fano + DPI 的 converse 手法 | 第 21 集（joint source-channel converse）、第 28 集（rate-distortion converse） |
| Information density、optimistic capacity、strong converse 的一般條件 | 第 35 集（第二部分 Chapter 4） |

---

## 附：本集一句話總結

> **Converse 只需要兩個「對所有碼都成立」的不等式：DPI 讓 $\log M_n\le H(W|Y^n)+nC$，Fano 讓 $H(W|Y^n)\le1+P_e\log M_n$——合起來就是 rate 超過 $C$ 時 $P_e\ge1-C/R$；而更深的圖像是錯誤率曲線就是 information density 的分布，DMC 時它收成一條垂直的界線。**

---

## ⚠️ 待確認清單

1. [▶ 20:33](https://youtu.be/TnRthbWsjFw?t=1233) 老師口述的 information density 式子（$\frac1n\log\frac1{P_{X^nY^n}}$）和一般定義 $\frac1n\log\frac{P_{Y^n|X^n}}{P_{Y^n}}$ 不同，投影片原式待補。

---

*筆記依據陳伯寧老師「消息理論」Lec18 錄影逐字稿（whisper large-v3-turbo，31:22）與 Alajaji & Chen 課本 §4.3 整理。*
