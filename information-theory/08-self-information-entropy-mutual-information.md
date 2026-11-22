---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 8
lecture: "Lec08 Chapter 2: Information Measures for Discrete Systems: 2.1.1 Self-information …"
date: 待補
video: https://youtu.be/YH7bXbiPgZI
notes: Alajaji & Chen §2.1–2.3（pp. 5–20，Theorem 2.1–Theorem 2.21），§2.4 開頭（Lemma 2.22，p. 20）
---

# 第 8 集 · Lec08 第 2 章：self-information、entropy、chain rule、mutual information [▶ 影片](https://youtu.be/YH7bXbiPgZI)

← 上一集：[07](07-ergodicity-law-of-large-numbers-clt.md) ｜ [總目錄](README.md) ｜ 下一集：[09](09-data-processing-fano-inequality.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 8 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（59:36，whisper large-v3-turbo）＋ 課本 §2.1–2.4（pp. 5–20）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「Shannon」聽成「Shanon／Shenon」，「量度」聽成「良度」，「公設」聽成「公社」，「倒數」聽成「導數」，「monotone」聽成「Molotonic／Morotone」，「negative information」聽成「food information」，「floor function」聽成「flower function」，「實數」聽成「時數」，「nats」聽成「nets」，「Blahut」聽成「Breha」，「斜率」聽成「斜律」，「Venn diagram」聽成「Vin Diagram／Van Diagram」，「約定俗成」聽成「約定成熟」，「旁聽／攔截」聽成「導彈」，「independence bound」聽成「independent bound／bond」，「bound on mutual information」聽成「about on mutual information」，「memoryless」聽成「Memories」，「lemma」聽成「Lama／Lema」。開頭 [00:00]「邰威老師成為的」是亂碼。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Self-information 的三個公設](#1-self-information-的三個公設)
- [2. Theorem 2.1 的證明](#2-theorem-21-的證明)
- [3. Self-information 的意義與 entropy](#3-self-information-的意義與-entropy)
- [4. Fundamental inequality](#4-fundamental-inequality)
- [5. Entropy 的上下界](#5-entropy-的上下界)
- [6. Log-sum inequality](#6-log-sum-inequality)
- [7. Joint entropy 與 conditional entropy](#7-joint-entropy-與-conditional-entropy)
- [8. Chain rule](#8-chain-rule)
- [9. Conditioning never increases entropy](#9-conditioning-never-increases-entropy)
- [10. Mutual information](#10-mutual-information)
- [11. Conditional mutual information 與 chain rule](#11-conditional-mutual-information-與-chain-rule)
- [12. 多個隨機變數：chain rule 與 independence bound](#12-多個隨機變數chain-rule-與-independence-bound)
- [13. Bound on mutual information](#13-bound-on-mutual-information)
- [14. 預告：data processing inequality](#14-預告data-processing-inequality)
- [15. 一頁速查表](#15-一頁速查表)
- [16. 與後續集數的連結](#16-與後續集數的連結)

---

## 0. 這堂課要做什麼

正式進入第 2 章：從 Shannon 的三個公設證明 self-information 一定是 $-\log p$，定義 entropy、joint／conditional entropy、mutual information，並證明它們的性質都**符合工程直覺**。

【口頭】證明的萬用口訣：**要證 $A\le B$，就證 $B-A\ge0$；把 $\log$ 的項合在一起，再用 fundamental inequality 或 log-sum inequality 把 $\log$ 拿掉。**兩年後細節忘了，記得這句話就夠。

| 主題 | 課本 |
|---|---|
| 三個公設、Theorem 2.1 | §2.1.1（pp. 5–7） |
| Entropy | §2.1.2 Definition 2.2（p. 8） |
| FI、非負、上界、log-sum | §2.1.3 Lemma 2.4–2.7（pp. 10–12） |
| Joint／conditional entropy、chain rule | §2.1.4 Definition 2.8–Corollary 2.11（pp. 12–14） |
| Conditioning reduces entropy 等 | §2.1.5 Lemma 2.12–2.14（pp. 14–16） |
| Mutual information | §2.2 Lemma 2.15–2.16（pp. 16–18） |
| 多變數 chain rule、independence bound | §2.3 Theorem 2.17–2.21（pp. 18–20） |

---

## 1. Self-information 的三個公設

[▶ 00:00](https://youtu.be/YH7bXbiPgZI?t=0)

**Information measure**：要量化「這件事給你多少 information」。先講**離散系統**（0、1 的數位世界）。

- 我們傳的都是 **event（事件）**，而且是**還沒發生**的事。丟骰子之前才有 information；丟完是 3 點，大家都知道了，就沒有 information。
- 事件還沒發生，但知道機率（例如銅板正反各 0.5），問：它發生之後我預期得到多少 information？

設事件 $E$ 的機率 $p_E$，self-information $I(E)=I(p_E)$。三個公設（課本 pp. 5–6）：

1. **$I(p)$ 對 $p$ 嚴格遞減**。機率越低，真的發生時得到的 information 越大；99.9% 會發生的事真的發生了，你不會 surprise。
2. **$I(p)$ 對 $p$ 連續**：機率從 0.99 降到 0.98，information 只變一點點。
3. **獨立事件可加**：$I(p_1\times p_2)=I(p_1)+I(p_2)$。這是**決定性**的條件——相乘變相加就是 log 的行為。

【口頭】
- 這次投影片把第 2、3 條和之前的順序對調了。
- 本來還有第 4 條「$I\ge0$」：你不可能得到負的 information（不會讓人從很有知識變得知識變少）。後來發現在三個公設下它**自動成立**，所以拿掉——公設越少越好。
- 第二部分會講近代結果：程式的複雜度也是 entropy，裡面都隱含這種概念。

---

## 2. Theorem 2.1 的證明

[▶ 05:03](https://youtu.be/YH7bXbiPgZI?t=303)

**Theorem 2.1**（p. 6）：定義在 $p\in[0,1]$、滿足 (1) 單調遞減 (2) 連續 (3) $I(p_1p_2)=I(p_1)+I(p_2)$ 的函數，**只有**
$$I(p)=-c\cdot\log_bp,$$
$c>0$ 是常數，底數 $b>1$。

$b$、$c$ 可以任意取，只是單位不同。一般 $b=2$，單位叫 **bit**。

**證明分三步**（老師：「數學不難，難的是觀念的突破」）：先證 $p=\frac1n$（整數分之一），再證 $p$ 是有理數，最後證 $p$ 是實數。第 2 條公設（連續）只在第三步用到。

**Step 1：$I\left(\frac1n\right)=-c\log_2\frac1n=c\log_2n$**，$n=1,2,3,\dots$ [▶ 06:36](https://youtu.be/YH7bXbiPgZI?t=396)

- $n=1$：由公設 3，$I(1)=I(1\cdot1)=I(1)+I(1)$，所以 $I(1)=0=-c\log_21$。
- $n>1$：對任意正整數 $r$，存在非負整數 $k$ 使
$$n^k\le2^r<n^{k+1}.$$
  （$k=\lfloor r/\log_2n\rfloor$。$n=1$ 時分母 $\log_21=0$，$k$ 不存在，所以 $n=1$ 要另外證。）
- 取倒數再用公設 1（遞減）：
$$I\left(\frac1{n^k}\right)\le I\left(\frac1{2^r}\right)<I\left(\frac1{n^{k+1}}\right).$$
- 用公設 3（$k$ 個 $\frac1n$ 相乘 → $k$ 個 $I(\frac1n)$ 相加）：
$$k\,I\left(\tfrac1n\right)\le r\,I\left(\tfrac12\right)<(k+1)\,I\left(\tfrac1n\right).$$
- 因為 $n\ge2$，$\frac1n<1$，由**嚴格**遞減 $I(\frac1n)>I(1)=0$，可以除過去：
$$\frac kr\le\frac{I(1/2)}{I(1/n)}<\frac{k+1}r.$$
- 另一方面，對 $n^k\le2^r<n^{k+1}$ 取 $\log_2$：$k\log_2n\le r<(k+1)\log_2n$，所以
$$\frac kr\le\frac1{\log_2n}<\frac{k+1}r.$$
- 兩個數都落在長度 $\frac1r$ 的區間 $\left[\frac kr,\frac{k+1}r\right)$ 裡，所以
$$\left|\frac{I(1/2)}{I(1/n)}-\frac1{\log_2n}\right|<\frac1r.$$
左邊不是 $r$ 的函數，$r$ 又可以任意大，所以兩者相等：$I\left(\frac1n\right)=I\left(\frac12\right)\log_2n$。令 $c=I\left(\frac12\right)>0$ 即得。

【口頭】每個條件都調得剛剛好：如果把嚴格遞減弱化成 non-increasing，證明就不 work，因為要 $I(\frac1n)>0$ 才能除。做研究時，公設也是因為證明需要才慢慢調出來的。

**Step 2：有理數 $p=\frac rs$** [▶ 10:49](https://youtu.be/YH7bXbiPgZI?t=649)：由公設 3，
$$I\left(\frac1s\right)=I\left(\frac rs\cdot\frac1r\right)=I\left(\frac rs\right)+I\left(\frac1r\right)$$
$$\Rightarrow I\left(\frac rs\right)=I\left(\frac1s\right)-I\left(\frac1r\right)=c\log_2s-c\log_2r=-c\log_2\frac rs.$$

**Step 3：實數 $p$** [▶ 11:20](https://youtu.be/YH7bXbiPgZI?t=680)：用有理數從左右兩邊逼近 $p$，由公設 2（連續），左極限 = 右極限 = $-c\log_2p$。

---

## 3. Self-information 的意義與 entropy

[▶ 11:51](https://youtu.be/YH7bXbiPgZI?t=711)

取 $c=1$、$b=2$：
- 機率 $\frac12$ 的事件發生，得到 $-\log_2\frac12=1$ bit；
- 機率 $\frac14$ 的事件發生，得到 2 bit，是前者的兩倍。

【口頭】工程就是要**量化**，不能只講定性。

**Uncertainty 的說法** [▶ 12:54](https://youtu.be/YH7bXbiPgZI?t=774)：還沒發生，所以不確定（uncertainty）；發生了，就學到了。
$$\text{the amount of information gained}=\text{the amount of uncertainty lost}.$$

**Entropy** [▶ 13:24](https://youtu.be/YH7bXbiPgZI?t=804)：很多事件，不知道哪個會發生，就看期望值——**expected self-information**。

**Definition 2.2**（p. 8）：
$$H(X)=-\sum_{x\in\mathcal X}P_X(x)\log_2P_X(x)=E\left[-\log_2P_X(X)\right].$$
- 單位：以 2 為底叫 **bits**；以 $e$ 為底叫 **nats**（natural logarithm）。
- 二元 $(p,1-p)$：**binary entropy function** $h_b(p)=-p\log_2p-(1-p)\log_2(1-p)$。
- 為了方便，假設字母集 $\mathcal X$ 是有限的。

**$E[f(X)]$ 的寫法** [▶ 27:47](https://youtu.be/YH7bXbiPgZI?t=1667)：$f(a)=\log_2\frac1{P_X(a)}$ 是一個函數，$f(X)$ 是新的隨機變數，entropy 就是它的期望值。【口頭】這個寫法到 90 年代開始發酵，和第二部分非常有關，要熟悉。

---

## 4. Fundamental inequality

[▶ 15:24](https://youtu.be/YH7bXbiPgZI?t=924)

**Lemma 2.4（Fundamental inequality, FI）**（p. 10）：對 $x>0$、$D>1$，
$$\log_D(x)\le\log_D(e)\cdot(x-1),$$
等號成立 **iff** $x=1$。令 $y=\frac1x$ 得
$$\log_D(y)\ge\log_D(e)\left(1-\frac1y\right).$$
自然對數時就是 $1-\frac1x\le\ln x\le x-1$。

【口頭】
- 用途：取總和時 $\log$ 的和很難加，把 $\log$ 換成 $x-1$ 或 $1-\frac1x$ 就變成多項式的和。
- 不用證明，畫圖就知道：直線 $x-1$ 在 $\ln x$ 的上方，在 $x=1$ 相切。
- 1970 年前（Blahut 的書）沒有這個名詞，直接用；Cover 的書以後（90 年代）才單獨列為 fundamental inequality。
- 底數 $D$ 時要乘上斜率 $\log_D(e)$。
- 只寫一邊就夠：$\log x\le x-1$ 代 $\frac1x$ 就得另一邊。**一定要記得等號只在 $x=1$**。

---

## 5. Entropy 的上下界

**Lemma 2.5（非負）**（p. 10）[▶ 16:25](https://youtu.be/YH7bXbiPgZI?t=985)：$H(X)\ge0$，等號 iff $X$ 是 deterministic。
- 證明：$0\le P_X(x)\le1$ ⇒ $\log_2\frac1{P_X(x)}\ge0$，正數的期望值 $\ge0$。等號 iff 某個 $P_X(x)=1$。
- **Convention**：$0\cdot\log\frac10=0$（工程上用極限解釋：$\varepsilon\log\frac1\varepsilon\to0$）。這是消息理論最常用的約定。
- 【口頭】明天 100% 下雨，那「明天下雨」對你不是新鮮事，information 是 0——完全符合直覺。數學家可以假設一堆公設玩（例如投影幾何），但要解釋工程現象，結果一定要符合工程的解釋。

**Lemma 2.6（上界）**（p. 11）[▶ 18:57](https://youtu.be/YH7bXbiPgZI?t=1137)：$X$ 取值在有限集合 $\mathcal X$，則
$$H(X)\le\log_2|\mathcal X|,$$
等號 iff $X$ 均勻分布（$P_X(x)=\frac1{|\mathcal X|}$）。

**證明**（照口訣：相減、合併 log、用 FI）：
$$\begin{aligned}
\log_2|\mathcal X|-H(X)&=\log_2|\mathcal X|\sum_xP_X(x)+\sum_xP_X(x)\log_2P_X(x)\\
&=\sum_xP_X(x)\log_2\left[|\mathcal X|\,P_X(x)\right]\\
&\ge\sum_xP_X(x)\log_2(e)\left(1-\frac1{|\mathcal X|P_X(x)}\right)\\
&=\log_2(e)\left(\sum_xP_X(x)-\sum_x\frac1{|\mathcal X|}\right)=\log_2(e)(1-1)=0.
\end{aligned}$$
- 第一行的技巧：乘上 $\sum_xP_X(x)=1$，讓兩項的 summation 可以合併。
- 不等號用 FI（$\log y\ge\log e\,(1-\frac1y)$），等號 iff $|\mathcal X|P_X(x)=1$，即均勻分布。

【口頭】例：骰子 6 面，不管機率如何，$H\le\log_26$ bit；每面 $\frac16$ 時最大。約人明天吃飯，對方說「去不去各 50%」，最難預測，發生時給你最大的驚訝量。

【課本補充】$\log|\mathcal X|$ 也叫 Hartley function／Hartley entropy；Hartley 最早提出不管內容地量測 information（p. 11 註 4）。

---

## 6. Log-sum inequality

[▶ 24:12](https://youtu.be/YH7bXbiPgZI?t=1452)

**Lemma 2.7（log-sum inequality）**（p. 11）：非負數 $a_1,\dots,a_n$、$b_1,\dots,b_n$，
$$\sum_{i=1}^na_i\log_D\frac{a_i}{b_i}\ \ge\ \left(\sum_{i=1}^na_i\right)\log_D\frac{\sum_{i=1}^na_i}{\sum_{i=1}^nb_i},$$
等號 iff $\frac{a_i}{b_i}$ 是與 $i$ 無關的常數（$=\frac{\sum a_j}{\sum b_j}$）。
- Convention：$0\log0=0$、$0\log\frac00=0$、$a\log\frac a0=\infty$（$a>0$），用連續性（極限）解釋。

【口頭】「先取 log 再 sum」≥「先 sum 再 log」——又是兩個操作對調。它讓你在 summation 裡不用處理 log，有時比 FI 更直接。Cover 的書大多用 log-sum 證，早期的書大多用 FI 證；任何定理兩種都能證。

**證明**（用 FI，課本 p. 12）：令 $a=\sum a_i$、$b=\sum b_i$。
$$\begin{aligned}
\sum_ia_i\log_D\frac{a_i}{b_i}-a\log_D\frac ab&=a\sum_i\frac{a_i}a\log_D\left(\frac{a_i}{b_i}\cdot\frac ba\right)\qquad\left(\text{用 }\textstyle\sum_i\frac{a_i}a=1\right)\\
&\ge a\log_D(e)\sum_i\frac{a_i}a\left(1-\frac{b_i\,a}{a_i\,b}\right)\\
&=a\log_D(e)\left(\sum_i\frac{a_i}a-\sum_i\frac{b_i}b\right)=0.
\end{aligned}$$
等號 iff $\frac{a_i}{b_i}\cdot\frac ba=1$ 對所有 $i$。

【課本補充】也可以用 Jensen（p. 12）：取 $f(t)=t\log_Dt$（strictly convex），$\alpha_i=\frac{b_i}{\sum b_j}$、$t_i=\frac{a_i}{b_i}$，則 $\sum\alpha_if(t_i)\ge f(\sum\alpha_it_i)$。

---

## 7. Joint entropy 與 conditional entropy

[▶ 26:16](https://youtu.be/YH7bXbiPgZI?t=1576)

Shannon 原本要研究 information transmission：$X$ 傳給 $Y$。傳送前不知道 $X$ 送什麼、$Y$ 收到什麼。

**Definition 2.8（joint entropy）**（p. 13）：$X$、$Y$ 合起來的 information 量。由三個公設，唯一的形式是
$$H(X,Y)=-\sum_{(x,y)}P_{X,Y}(x,y)\log_2P_{X,Y}(x,y)=E\left[-\log_2P_{X,Y}(X,Y)\right].$$

**Definition 2.9（conditional entropy）**（p. 13）[▶ 28:18](https://youtu.be/YH7bXbiPgZI?t=1698)：已經告訴你 $X$（例如 $X=0$），因為有雜訊，$Y$ 還是不確定。先算給定 $X=x$ 時的 entropy，再對 $X$ 取期望值：
$$H(Y|X)=\sum_xP_X(x)\left(-\sum_yP_{Y|X}(y|x)\log_2P_{Y|X}(y|x)\right)=\sum_xP_X(x)H(Y|X=x)=E\left[-\log_2P_{Y|X}(Y|X)\right].$$
寫大寫 $X$ 代表最後還要對 $X$ 取期望值。

【課本補充】課本（p. 14）的名詞：通道輸入 $X$、輸出 $Y$ 時，$H(X|Y)$ 叫 **equivocation**——接收端看輸入的不確定性（第 1 集提過這個字）；$H(Y|X)$ 叫 **prevarication**——傳送端看輸出的不確定性。$H(X|Y)=0$ 表示看到 $Y$ 之後 $X$ 就確定了。

---

## 8. Chain rule

[▶ 30:22](https://youtu.be/YH7bXbiPgZI?t=1822)

**Theorem 2.10（chain rule for entropy）**（p. 13）：
$$H(X,Y)=H(X)+H(Y|X).$$
**證明**：$P_{X,Y}(x,y)=P_X(x)P_{Y|X}(y|x)$，相乘取 log 變相加：
$$H(X,Y)=E[-\log_2P_{X,Y}]=E[-\log_2P_X(X)]+E[-\log_2P_{Y|X}(Y|X)]=H(X)+H(Y|X).$$

**物理意義**（【口頭】）：先量 $X$，再量「給定 $X$ 之後 $Y$ 剩下的不確定性」，兩者相加就是共有的。例：$H(X,Y)=3$ bit、$H(X)=2$ bit，則 $H(Y|X)=1$ bit。用 Venn diagram 畫：兩個圈的聯集是 $H(X,Y)$，$H(X)$ 是一個圈，剩下的那塊是 $H(Y|X)$——完全符合集合的概念，表示這個量度好像真的是對的。

因為 $H(X,Y)=H(Y,X)$，
$$H(X)+H(Y|X)=H(Y)+H(X|Y)\ \Rightarrow\ H(X)-H(X|Y)=H(Y)-H(Y|X).\qquad(2.1.7)$$

**Corollary 2.11**（p. 14）[▶ 32:29](https://youtu.be/YH7bXbiPgZI?t=1949)：$H(X,Y|Z)=H(X|Z)+H(Y|X,Z)$。
【口頭】三者的情形：$X$ 要傳給 $Y$，$Z$ 可能是竊聽者（security）、干擾者，或幫助傳輸的 side information。

---

## 9. Conditioning never increases entropy

[▶ 33:30](https://youtu.be/YH7bXbiPgZI?t=2010)

**Lemma 2.12**（p. 14）：
$$H(X|Y)\le H(X),$$
等號 iff $X$、$Y$ 獨立。

**意義**（【口頭】）：先告訴你額外的訊息，你對 $X$ 的了解只會增加，不確定性只會減少。**Side information 永遠有幫助**；只有 side information 和你要分析的事完全獨立時才沒有幫助。

**證明**（用 log-sum）[▶ 34:33](https://youtu.be/YH7bXbiPgZI?t=2073)：
$$\begin{aligned}
H(X)-H(X|Y)&=\sum_{x,y}P_{X,Y}(x,y)\log_2\frac{P_{X|Y}(x|y)}{P_X(x)}
=\sum_{x,y}P_{X,Y}(x,y)\log_2\frac{P_{X|Y}(x|y)P_Y(y)}{P_X(x)P_Y(y)}\\
&=\sum_{x,y}P_{X,Y}(x,y)\log_2\frac{P_{X,Y}(x,y)}{P_X(x)P_Y(y)}
\ge\left(\sum_{x,y}P_{X,Y}\right)\log_2\frac{\sum_{x,y}P_{X,Y}(x,y)}{\sum_{x,y}P_X(x)P_Y(y)}=1\cdot\log_2\frac11=0.
\end{aligned}$$
- 技巧：分子分母各乘 $P_Y(y)$，讓 log 裡的分子和前面的係數都是 $P_{X,Y}$，才能套 log-sum 的 $a\log\frac ab$ 形式。【口頭】這一步只是為了「湊」。
- 等號 iff $\frac{P_{X,Y}}{P_XP_Y}$ 是常數；機率總和是 1，常數就是 1，即獨立。

**Lemma 2.13**（p. 15）[▶ 36:03](https://youtu.be/YH7bXbiPgZI?t=2163)：$X$、$Y$ 獨立 ⇒ $H(X,Y)=H(X)+H(Y)$。（chain rule + $H(Y|X)=H(Y)$。）一般有 $H(X,Y)\le H(X)+H(Y)$。

**Lemma 2.14（conditional entropy 是 lower additive）**（p. 15）[▶ 36:34](https://youtu.be/YH7bXbiPgZI?t=2194)：
$$H(X_1,X_2|Y_1,Y_2)\le H(X_1|Y_1)+H(X_2|Y_2),$$
等號 iff $P_{X_1,X_2|Y_1,Y_2}=P_{X_1|Y_1}P_{X_2|Y_2}$。
【課本補充】證明：chain rule 得 $H(X_1|Y_1,Y_2)+H(X_2|X_1,Y_1,Y_2)$，再兩次用「conditioning 降低 entropy」拿掉多餘的條件。

【口頭】這些基本性質會常用，**不要記公式，記感覺**。

---

## 10. Mutual information

[▶ 37:05](https://youtu.be/YH7bXbiPgZI?t=2225)

用集合的概念：$X$ 的圈和 $Y$ 的圈有交集——傳送前兩端**共有的不確定性**。傳輸要用這個共有的部分來傳（第 3 集的例子）。

**定義**（Shannon 想到的；課本 (2.2.1)，p. 16 寫成第一個等式）：
$$I(X;Y):=H(X)+H(Y)-H(X,Y)=H(X)-H(X|Y)=H(Y)-H(Y|X).$$
- 兩塊相加有重疊，重疊的部分加了兩次，扣掉整個聯集一次，就是交集——**共識**。
- 由 (2.1.7)，$I(X;Y)=I(Y;X)$，**對稱**。【口頭】所以有人用 reverse channel 做研究：$X$ 送到 $Y$ 和 $Y$ 送到 $X$ 是同一件事。例：加性高斯通道 $Y=X+N$，也可以寫 $X=Y-N$，$-N$ 還是零均值高斯。

**Lemma 2.15**（pp. 16–17）：
1. $\displaystyle I(X;Y)=\sum_{x,y}P_{X,Y}(x,y)\log_2\frac{P_{X,Y}(x,y)}{P_X(x)P_Y(y)}$。
   - 【口頭】分母是「當作獨立」、分子是「合在一起」。比值越大（log 越大），$X$、$Y$ 越相關、共識越多、能傳越多；比值接近 1，兩端幾乎獨立、沒有共識，很難溝通。
2. $I(X;Y)=I(Y;X)=H(Y)-H(Y|X)$。
3. $I(X;Y)=H(X)+H(Y)-H(X,Y)$。
4. **$I(X;Y)\le H(X)$**，等號 iff $X$ 是 $Y$ 的函數（$X=f(Y)$）。
   - 【口頭】送的訊息量 ≥ 能送過去的量，因為有雜訊。等號：收到 $Y$ 帶進 $f$ 就百分之百知道 $X$（例如 $Y=2$ ⇒ $X=1$），所有訊息都送得過去。
5. **$I(X;Y)\ge0$**，等號 iff $X$、$Y$ 獨立（Lemma 2.12 的直接結果）。收到的東西和送的東西統計獨立，就什麼都送不過去。
6. **$I(X;Y)\le\min\{\log_2|\mathcal X|,\log_2|\mathcal Y|\}$**。
   - 證明：$I=H(X)-H(X|Y)\le H(X)\le\log_2|\mathcal X|$（$H(X|Y)\ge0$ 加 Lemma 2.6）；另一邊同理。
   - 【口頭】例：傳送端 3 bit（8 種狀況），接收端量化成只有 0、1。收到的只有兩種，不可能分辨 8 種，最多送 1 bit。接收端的可能性要夠多，訊息才可能完全送過去。

**Fig. 2.2**（p. 17）：Venn diagram——$H(X,Y)$ 是聯集；$H(X|Y)$、$I(X;Y)$、$H(Y|X)$ 是由左到右三塊。

---

## 11. Conditional mutual information 與 chain rule

[▶ 44:15](https://youtu.be/YH7bXbiPgZI?t=2655)

**Conditional mutual information**（(2.2.2)，p. 17）：已知 $Z$ 時 $X$、$Y$ 的共同不確定性
$$I(X;Y|Z):=H(X|Z)-H(X|Y,Z).$$

**Lemma 2.16（chain rule for mutual information）**（p. 17）：定義 $I(X;Y,Z):=H(X)-H(X|Y,Z)$，則
$$I(X;Y,Z)=I(X;Y)+I(X;Z|Y)=I(X;Z)+I(X;Y|Z).$$
證明：$H(X)-H(X|Y,Z)=\left[H(X)-H(X|Y)\right]+\left[H(X|Y)-H(X|Y,Z)\right]$。

**記號**（【口頭】）：分號左邊是傳送端、右邊是接收端，這是約定俗成；用分號而不是逗號，是因為兩邊不對等。

**談判的比喻**（【口頭】）：$X$ 要同時和 $Y$、$Z$ 溝通，像金正恩和川普（加上幕僚）談判，接收端人比較多。可以先 $X$ 和 $Y$ 私下溝通，再和 $Z$ 溝通「$Y$ 已經知道之後剩下的部分」。例：總共能傳 3 bit，$X$、$Y$ 之間有 2 bit 共識，和 $Z$ 就只剩 1 bit，不會多出來。也可以先和 $Z$ 溝通。另外也可以寫成 $I(X;Y|Z)$ 加上重疊的部分，用 Venn diagram 說明。

---

## 12. 多個隨機變數：chain rule 與 independence bound

[▶ 46:49](https://youtu.be/YH7bXbiPgZI?t=2809)

連續傳送：$X_1,\dots,X_n$ 送出去，收到 $Y_1,\dots,Y_n$。記號 $X^n:=(X_1,\dots,X_n)$，$X^{i-1}:=(X_1,\dots,X_{i-1})$。【口頭】這是消息理論特有的寫法，別的領域不一定這樣寫。

**Theorem 2.17（chain rule for entropy）**（p. 18）：
$$H(X_1,\dots,X_n)=\sum_{i=1}^nH(X_i|X_{i-1},\dots,X_1)=\sum_{i=1}^nH(X_i|X^{i-1}).$$
（反覆用兩個變數的 chain rule，即歸納法。）先量 $X_1$，再量給定 $X_1$ 的 $X_2$，再量給定 $X_1,X_2$ 的 $X_3$……

**Theorem 2.18**：加上條件 $Y$ 也成立。

**Theorem 2.19（chain rule for mutual information）**（p. 19）：
$$I(X_1,\dots,X_n;Y)=\sum_{i=1}^nI(X_i;Y|X_{i-1},\dots,X_1).$$
【口頭】一序列 $X_1,X_2,X_3$ 循序送：先送 $X_1$；送 $X_2$ 時 $X_1$ 已經送過去了，所以是 given $X_1$……循序送不會有資料損失，符合工程概念。

**Theorem 2.20（independence bound on entropy）**（p. 19）：
$$H(X_1,\dots,X_n)\le\sum_{i=1}^nH(X_i),$$
等號 iff 所有 $X_i$ 互相獨立。
- 證明：chain rule 後每項用「conditioning 降低 entropy」：$H(X_i|X^{i-1})\le H(X_i)$。
- 等號 iff 每個 $X_i$ 和 $(X_{i-1},\dots,X_1)$ 獨立。

**「和過去獨立」就夠** [▶ 50:22](https://youtu.be/YH7bXbiPgZI?t=3022)：
- 課本 p. 19 註 8：「$X_i$ 和 $(X_{i-1},\dots,X_1)$ 獨立，對所有 $i$」**等價於**「全部互相獨立」（可用 $P_{X^n}=\prod_iP_{X_i|X^{i-1}}$ 證明，留作習題）。
- 【口頭】兩種說法數學上等價，但思維不同。$X$ 代表一個操作（這個時間點送 0 或 1）。操作上只要「今天的決定和前兩天獨立」就好，不用去考慮「今天要和明天獨立」——明天還沒發生。這是 causal 的想法。做理論就是要培養對這種小差異的敏感度。

---

## 13. Bound on mutual information

[▶ 52:56](https://youtu.be/YH7bXbiPgZI?t=3176)

**Theorem 2.21**（p. 20）：若 $\{(X_i,Y_i)\}$ 滿足**條件獨立假設**
$$P_{Y^n|X^n}=\prod_{i=1}^nP_{Y_i|X_i},$$
則
$$I(X_1,\dots,X_n;Y_1,\dots,Y_n)\le\sum_{i=1}^nI(X_i;Y_i),$$
等號 iff $\{X_i\}$ 互相獨立。

**證明**（課本 p. 20）：
- Independence bound：$H(Y^n)\le\sum_iH(Y_i)$。
- 條件獨立：$H(Y^n|X^n)=E\left[-\log_2\prod_iP_{Y_i|X_i}\right]=\sum_iH(Y_i|X_i)$。
- 相減：$I(X^n;Y^n)=H(Y^n)-H(Y^n|X^n)\le\sum_i\left[H(Y_i)-H(Y_i|X_i)\right]=\sum_iI(X_i;Y_i)$。

**意義**（【口頭】）：
- 一群人一起開會溝通，鬧哄哄每個人都有意見，送出的訊息量少；不如 $X_1$ 和 $Y_1$、$X_2$ 和 $Y_2$ 分別溝通，總量更大。
- 條件獨立假設的意思：**不同時間的雜訊彼此獨立**（第 2 個時間送 $X_2$ 收到 $Y_2$ 的錯誤，和第 1 個時間無關）。AWGN、memoryless channel 都是這樣。
- 等號成立要兩個條件：(1) 雜訊在時間上獨立（上面的假設）；(2) 要送的訊息 $X_1,X_2,\dots$ 在時間上也獨立。兩者都成立時，分開一個一個送和合在一起送，總量一樣。

> 老師口述時把「雜訊在時間上獨立」也說成等號成立的條件之一，並提到「如果雜訊是 dependent，總傳送量還是會比較大」。課本的寫法是：雜訊時間獨立是定理的**前提**，等號 iff $X_i$ 獨立。這裡照課本寫。

---

## 14. 預告：data processing inequality

[▶ 56:34](https://youtu.be/YH7bXbiPgZI?t=3394)

**Data processing lemma／inequality**（課本 Lemma 2.22，p. 20；下一集講證明）：資料經過處理，information 只會減少，不會增加。

圖：source $U$ →（encoder）→ $X$ →（channel，加雜訊）→ $Y$ →（decoder）→ $V$。則
$$I(U;V)\le I(X;Y).$$
- $Y\to V$ 這種轉換叫 processing；encoding、decoding、modulation 都是 processing。處理越多，能傳的訊息量只會越少。
- 【口頭】那為什麼還要處理？老師自己加了一句：**處理後的 information 形式比較 useful**。例如把 0、1 轉成 5V、0V 的電壓，後面的線路比較好處理。
- 證明牽涉 Markov chain——這就是 Markov process 在消息理論裡重要的原因。（影片在這裡結束。）

---

## 15. 一頁速查表

**Theorem 2.1**：遞減 + 連續 + $I(p_1p_2)=I(p_1)+I(p_2)$ ⇒ $I(p)=-c\log_bp$。
- 關鍵：$n^k\le2^r<n^{k+1}$ ⇒ $\frac kr\le\frac{I(1/2)}{I(1/n)},\frac1{\log_2n}<\frac{k+1}r$ ⇒ 差 $<\frac1r$ ⇒ 相等；有理數用可加性，實數用連續性。

**Entropy**：$H(X)=E[-\log_2P_X(X)]$；bits（底 2）、nats（底 $e$）；$h_b(p)$。

**兩把去 log 的刀**
- FI：$\log_D(e)(1-\frac1x)\le\log_Dx\le\log_D(e)(x-1)$，等號 iff $x=1$。
- Log-sum：$\sum a_i\log\frac{a_i}{b_i}\ge(\sum a_i)\log\frac{\sum a_i}{\sum b_i}$，等號 iff $a_i/b_i$ 常數。
- 口訣：證 $B-A\ge0$，合併 log，套 FI 或 log-sum。

**界**：$0\le H(X)\le\log_2|\mathcal X|$（下：deterministic；上：uniform，證明用 FI 於 $|\mathcal X|P_X(x)$）。

**Conditional／joint**
- $H(Y|X)=\sum_xP_X(x)H(Y|X=x)$；chain rule $H(X,Y)=H(X)+H(Y|X)$（相乘取 log 變相加）。
- $H(X|Y)\le H(X)$（log-sum，分子分母乘 $P_Y$），等號 iff 獨立。
- $H(X_1,X_2|Y_1,Y_2)\le H(X_1|Y_1)+H(X_2|Y_2)$。

**Mutual information**
- $I(X;Y)=H(X)+H(Y)-H(X,Y)=H(X)-H(X|Y)=\sum P_{XY}\log\frac{P_{XY}}{P_XP_Y}$，對稱。
- $0\le I(X;Y)\le\min\{H(X),H(Y)\}\le\min\{\log|\mathcal X|,\log|\mathcal Y|\}$；$I=0$ iff 獨立；$I=H(X)$ iff $X=f(Y)$。
- $I(X;Y|Z)=H(X|Z)-H(X|Y,Z)$；$I(X;Y,Z)=I(X;Y)+I(X;Z|Y)$。

**多變數**
- $H(X^n)=\sum H(X_i|X^{i-1})\le\sum H(X_i)$（等號 iff 獨立；「和過去獨立」就等價）。
- $I(X^n;Y)=\sum I(X_i;Y|X^{i-1})$。
- 若 $P_{Y^n|X^n}=\prod P_{Y_i|X_i}$：$I(X^n;Y^n)\le\sum I(X_i;Y_i)$，等號 iff $X_i$ 獨立。

---

## 16. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Data processing inequality、Markov chain | 第 9 集（§2.4） |
| Fano 不等式（用 $H(X|Y)$ 界錯誤率） | 第 9 集（§2.5） |
| Divergence（$I$ 是 $P_{XY}$ 和 $P_XP_Y$ 的 divergence） | 第 10 集（§2.6） |
| $I(X;Y)$ 對輸入分布 concave | 第 11 集（§2.7） |
| Entropy = 最好的壓縮率 | 第 12 集（第 3 章） |
| Bound on mutual information（memoryless channel） | 第 16–18 集（converse 證明） |
| $C=\max_{P_X}I(X;Y)$ | 第 16–19 集（第 4 章） |

---

## 附：本集一句話總結

> **三個公設逼出唯一的 $I(p)=-\log p$；它的期望值 entropy、以及 joint／conditional entropy、mutual information，全部都能畫成 Venn diagram，而每個性質（非負、uniform 最大、side information 有幫助、共識不超過任一方）都吻合工程直覺——這證明 Shannon 找到的是「對的」量。**

---

*筆記依據陳伯寧老師「消息理論」Lec08 錄影逐字稿（whisper large-v3-turbo，59:36）與 Alajaji & Chen 課本 §2.1–2.4 整理。*
