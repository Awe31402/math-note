---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 9
lecture: Lec09 2.4 Data processing inequality, 2.5 Fano's inequality
date: 待補
video: https://youtu.be/15SwirHhsqk
notes: Alajaji & Chen §2.4–2.5（pp. 20–26，Lemma 2.22–Example 2.28 及 Fano 的另一個證明）
---

# 第 9 集 · Lec09 §2.4–2.5：entropy 名字的由來、data processing inequality、Fano 不等式 [▶ 影片](https://youtu.be/15SwirHhsqk)

← 上一集：[08](08-self-information-entropy-mutual-information.md) ｜ [總目錄](README.md) ｜ 下一集：[10](10-divergence-variational-distance.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 9 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（49:30，whisper large-v3-turbo）＋ 課本 §2.4–2.5（pp. 20–26）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「Claude Shannon」聽成「Cross Shannon」，「IEEE」聽成「I3POE」，「熵」聽成「商」，「von Neumann」聽成「Van Neumann／Van Newman」，「Princeton」聽成「Prinston」，「Boltzmann」聽成「波茲曼」（正確），「公設」聽成「公社」，「倒數」聽成「導數」，「Fano」聽成「Phenos／Pheno／Phanal／Bellon／Final」，「Rényi」聽成「Rini」，「Campbell」聽成「Ron Campbell」，「錯誤率」聽成「抽率」，「Venn 圖」聽成「文式圖」，「韓太舜（Te Sun Han）」聽成「提升汉」，「preface」聽成「prefit」，「asymptotic」聽成「asynthetic」，「lemma」聽成「Lamma」。開頭 [00:00]「影哲學語言大解」、結尾「字幕志愿者」是 whisper 幻覺。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 回顧：entropy 這個名字的由來](#1-回顧entropy-這個名字的由來)
- [2. 要背的公式與兩種 mutual information 寫法](#2-要背的公式與兩種-mutual-information-寫法)
- [3. 數學量如何連上操作](#3-數學量如何連上操作)
- [4. Data processing inequality](#4-data-processing-inequality)
- [5. 給定 Z 之後，mutual information 可能變大](#5-給定-z-之後mutual-information-可能變大)
- [6. Fano 不等式：敘述與意義](#6-fano-不等式敘述與意義)
- [7. Fano 不等式的區域圖](#7-fano-不等式的區域圖)
- [8. 證明一：引進錯誤指標 E](#8-證明一引進錯誤指標-e)
- [9. 證明二：DPI + FI（可推廣的證明）](#9-證明二dpi--fi可推廣的證明)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

先回顧 entropy 和 mutual information 的由來與意義，然後講兩個重要結果：
- **Data processing inequality（DPI）**：處理只會讓 mutual information 變少。
- **Fano 不等式**：把一個純數學的量 $H(X|Y)$ 和一個純操作的量（猜錯的機率 $P_e$）連起來；之後用來證所有 **converse**。

| 主題 | 課本 |
|---|---|
| DPI 與推論 | §2.4 Lemma 2.22、Corollary 2.23–2.25（pp. 20–22） |
| $Z=X+Y$ 的例子 | p. 22 |
| Fano 不等式、區域圖 | §2.5 Lemma 2.26、Observation 2.27、Fig. 2.4（pp. 22–24） |
| 證明一、sharp、等號例子 | pp. 24–25、Example 2.28 |
| 證明二（DPI + FI） | pp. 25–26 |

---

## 1. 回顧：entropy 這個名字的由來

[▶ 00:00](https://youtu.be/15SwirHhsqk?t=0)

- Shannon 的 "A Mathematical Theory of Communication" 一開始是 Bell 實驗室內部的 journal；大家發現太經典，隔年 IRE（IEEE 的前身）的期刊邀請重新刊登。
- 出發點：**怎麼用數學定義要傳輸的 information**。三個公設 → 定義出 information。看起來像數學遊戲，但最後他證明這個數學定義和實際工程操作**完全一致**。

【口頭】名字的故事 [▶ 02:05](https://youtu.be/15SwirHhsqk?t=125)：
- entropy 不是 Shannon 取的，歷史很久，出現在熱力學和統計熱力學（最早約 1850 年）。物理上有名的公式是
$$S=k_B\log D,$$
$D$ 是可能的能量狀態數（the number of possible energy states），$k_B$ 是 Boltzmann 常數。中文叫「熵」。
- Shannon 二十幾歲就寫出證明，原本想叫它 **uncertainty**——所以很多文獻也叫 uncertainty。他對 information 的定義是「你知道我不知道、你希望告訴我的」。
- 後來他去拜訪 von Neumann。von Neumann 那時在 Princeton 高等研究院（富商捐款成立的私人研究機構，只做研究不教書；第一批聘的四人中有 Einstein 和 von Neumann）。von Neumann 建議：**不要叫 uncertainty，叫 entropy**。
- 為什麼像：若 $D$ 個狀態機率都是 $\frac1D$，每個狀態的 self-information 是 $\log D$；取期望值 $\sum\frac1D\log D=\log D$，和 $S=k_B\log D$ 成正比。
- 老師的詮釋：knowledge is power，你知道的東西是以能量的形式體現，所以 information 是能量的概念。log 的律：$\frac{d}{dx}\log x=\frac1x$——付出努力會增加，但越往高峰增加得越少；不過 $\log x\to\infty$，沒有極限。capacity $\log(1+\text{SNR})$ 也是 log。

> ⚠️ 待確認：[▶ 02:05](https://youtu.be/15SwirHhsqk?t=125)–[▶ 03:38](https://youtu.be/15SwirHhsqk?t=218) 老師說 entropy 出現在 Shannon 論文「2.6 節」的標題、Shannon「23 歲拜訪 von Neumann、24 歲拿博士」等年代細節，課本沒有記載，無法核對（第 1 集老師說的是「Section 6」）。

---

## 2. 要背的公式與兩種 mutual information 寫法

[▶ 06:44](https://youtu.be/15SwirHhsqk?t=404)

【口頭】考試**不會給公式**，entropy 和 mutual information 一定要會寫：
$$H(X)=\sum_xP_X(x)\log_2\frac1{P_X(x)},$$
$$I(X;Y)=E\left[\log_2\frac{P_{X,Y}(X,Y)}{P_X(X)P_Y(Y)}\right]=E\left[\log_2\frac{P_{Y|X}(Y|X)}{P_Y(Y)}\right].$$

- **第一種寫法**：聯合分布和「假設獨立的分布」之間的差異（log scale）。越獨立越不好。
- **第二種寫法** [▶ 08:48](https://youtu.be/15SwirHhsqk?t=528)：輸出端看到 $Y$ 的分布 $P_Y$，和給定 $X$ 後看到 $Y$ 的分布 $P_{Y|X}$ 的比值。90 年代發現它很有用。

**Output statistics 才是關鍵**（【口頭】）：
- Shannon 理論說要找最好的輸入角度 $P_X$ 讓 mutual information 最大，所以大家覺得輸入很重要。
- 但 $P_{X,Y}=P_X\,P_{Y|X}$：$P_{Y|X}$ 是自然界量出來的（不能改），$P_X$ 是你能改的。改 $P_X$ 就改了聯合分布，也就改了輸出分布 $P_Y$。
- 後來發現：**真正決定錯誤率的是輸出統計（output statistics）**。兩個不同的輸入分布（例如 1 用 80% 和 1 用 70%）經過同一個通道，有可能造成相同的 $P_Y$，這時錯誤率表現一樣。第二部分會講（90 年代的結果）。

---

## 3. 數學量如何連上操作

[▶ 11:28](https://youtu.be/15SwirHhsqk?t=688)

【口頭】
- entropy、mutual information 都是數學公式，跟操作一點關係都沒有——從沒說怎麼傳、怎麼設計。但最後能證明它們完全解釋了傳輸量和壓縮極限，所以非常有用。
- 有人專注在數學遊戲：換公設、重新定義 entropy，也很好玩。但沒跟工程問題串在一起，就只是數學遊戲。
- 例：Rényi（匈牙利數學家）定義的 Rényi entropy 一直找不到用途；到 70 年代 Campbell 發現壓縮的 cost 和碼長有關時，壓縮極限就是 Rényi entropy，才找到它的 operational meaning（第 2 集）。

---

## 4. Data processing inequality

[▶ 13:31](https://youtu.be/15SwirHhsqk?t=811)

**Lemma 2.22（data processing inequality／lemma）**（p. 21）：若 $X\to Y\to Z$，則
$$I(X;Y)\ge I(X;Z).$$

**證明**（課本 p. 21）：$X\to Y\to Z$ 表示給定 $Y$ 時 $X$、$Z$ 條件獨立，所以 $I(X;Z|Y)=0$。由 chain rule（第 8 集 Lemma 2.16），
$$I(X;Z)+I(X;Y|Z)=I(X;Y,Z)=I(X;Y)+I(X;Z|Y)=I(X;Y).$$
因為 $I(X;Y|Z)\ge0$，得 $I(X;Y)\ge I(X;Z)$，等號 iff $I(X;Y|Z)=0$。

【口頭】「$X$、$Z$ 條件獨立 ⇒ $I(X;Z|Y)=0$」可以直接寫：因為 mutual information 是「對的量」，它應該完全反映操作——兩端能溝通 iff 不獨立。

**Corollary 2.23**（p. 21）[▶ 17:05](https://youtu.be/15SwirHhsqk?t=1025)：任何函數 $g$，$X\to Y\to g(Y)$，所以
$$I(X;Y)\ge I(X;g(Y)).$$
- $Y$ 可能是很亂的資料，要整理成工程上可操作的判斷（例如送 +1 還 −1），就是 mapping／processing $g$。處理後 information 不會增加，只是 $g(Y)$ 更 useful。

**Fig. 2.3**（p. 21）：Source $U$ → Encoder → $X$ → Channel → $Y$ → Decoder → $V$，$I(U;V)\le I(X;Y)$。課本的話："By processing, we can only reduce (mutual) information, but the processed information may be in a more useful form!"

**「演化違反 DPI？」**（【口頭】）[▶ 13:31](https://youtu.be/15SwirHhsqk?t=811)：網路上有文章說生物演化違反 data processing lemma——老師傳知識給學生，經過處理應該只會損失，但人類會產生新知識。老師的回答：Shannon 的 information **只是很狹隘的 uncertainty**。學生讀了書自己推論、產生新的 information，那是另一回事；就「把我知道、你不知道的傳給你」這個量來說，處理只會讓它消失，不會增加。所以 information 的定義要講清楚。

**Corollary 2.24**（p. 21）[▶ 17:36](https://youtu.be/15SwirHhsqk?t=1056)：若 $X\to Y\to Z$，則 $I(X;Y|Z)\le I(X;Y)$。
- 意義：$Z$ 對 $X$ 的了解**完全來自** $Y$。【口頭】就像我完全不認識你，對你的了解全是第三者轉述的——那我提供的意見對「你和第三者」之間的溝通是多餘的。

**Corollary 2.25**（p. 22）[▶ 23:42](https://youtu.be/15SwirHhsqk?t=1422)：若 $X_1\to X_2\to\cdots\to X_n$，則對 $1\le i\le j\le k\le l\le n$，
$$I(X_i;X_l)\le I(X_j;X_k).$$
靠得越近，能傳的越多；靠得越遠，中間經過傳遞（處理）就消失一些。

---

## 5. 給定 Z 之後，mutual information 可能變大

[▶ 18:36](https://youtu.be/15SwirHhsqk?t=1116)

如果**不是** Markov chain（$Z$ 也直接接觸 $X$），$Z$ 可能幫忙溝通，也可能拖累，看 $Z$ 用什麼角度介入。所以 $I(X;Y|Z)$ 可能比 $I(X;Y)$ 大，也可能小。

**怎麼造例子**（【口頭】）：讓 $I(X;Y)=0$（$X$、$Y$ 獨立，不能溝通），再造一個 $Z$ 跟兩邊都相關，把它們串起來：$Z=X+Y$。

**例子**（課本 p. 22）：$X$、$Y$ 是獨立、等機率的 0/1 隨機變數，$Z=X+Y$（實數加法），$Z\in\{0,1,2\}$：
- $0+0=0$；$0+1=1+0=1$；$1+1=2$。四種情形等機率。

計算：
$$I(X;Y|Z)=H(X|Z)-H(X|Y,Z)=H(X|Z).$$
- $H(X|Y,Z)=0$：知道 $Y$ 和 $Z$，$X=Z-Y$ 完全確定（例如 $Y=1$、$Z=2$ ⇒ $X=1$）。
- $Z=0$ ⇒ $X=Y=0$，沒有不確定性：$H(X|Z=0)=0$。
- $Z=2$ ⇒ $X=Y=1$：$H(X|Z=2)=0$。
- $Z=1$ ⇒ $X$ 是 0 或 1 各半：$H(X|Z=1)=1$ bit。$P_Z(1)=\frac24=\frac12$。

$$H(X|Z)=P_Z(0)\cdot0+P_Z(1)\cdot1+P_Z(2)\cdot0=0.5\text{ bits}>0=I(X;Y).$$

【口頭】原本每次送 0 bit（$X$、$Y$ 獨立，完全不能溝通）；透過 $Z$，每次平均能帶 0.5 bit，送兩次帶一個。Information theory 給我們操作上的 guideline：怎麼讓傳輸和計算能進行。

---

## 6. Fano 不等式：敘述與意義

[▶ 24:12](https://youtu.be/15SwirHhsqk?t=1452)

【口頭】Fano 是 MIT 教授。Fano 不等式**從來沒有正式發表過**：是他 1950 年在 MIT 上課的講義裡推的，大家覺得很棒才抽出來。他 1961 年出了一本 information theory 的書，裡面有這個不等式。

**Lemma 2.26（Fano's inequality）**（p. 22）：$X$、$Y$ 是（一般相關的）兩個隨機變數，字母集 $\mathcal X$ **有限**，$\mathcal Y$ 可以可數無限。$\hat X:=g(Y)$ 是看到 $Y$ 後對 $X$ 的估計，$g:\mathcal Y\to\mathcal X$。錯誤率 $P_e:=\Pr[\hat X\ne X]$。則
$$H(X|Y)\le h_b(P_e)+P_e\log_2(|\mathcal X|-1),$$
$h_b(x)=-x\log_2x-(1-x)\log_2(1-x)$ 是 binary entropy function。

**意義**（【口頭】）：
- **左邊是純數學的量**：看到 $Y$ 之後對 $X$ 還有多少不了解。從公設來，跟操作無關。
- **右邊是純操作的量**：看到 $Y$，用某個策略（policy）$g$ 去猜 $X$（例如在 0、1、2、3 中猜），猜錯的機率 $P_e$。$h_b$ 裡是「猜對 or 猜錯」；第二項是 $P_e$ 乘上 $\log(\text{可能數}-1)$，例如 4 種可能就是 $\log_23$。
- **最漂亮的地方**：右邊和**你怎麼猜無關**（universal）。猜得好、猜得爛都滿足它，所以它給出極限。
- **用途**：證明 **converse**。achievability 只要證存在一個方法；converse 要證全世界所有設計都做不到，很難。Fano 不等式涵蓋所有 $g$，正好拿來證 converse。

**物理意義** [▶ 30:26](https://youtu.be/15SwirHhsqk?t=1826)：
- $P_e=0$（百分之百猜對）：右邊 $h_b(0)+0=0$，所以 $H(X|Y)=0$——看到 $Y$ 對 $X$ 完全沒有不確定性。符合直覺：完全了解才能百分之百做對決定。
- 【課本補充】Observation 2.27（p. 23）：$P_e=0$ 時 $\hat X=g(Y)=X$（w.p. 1），所以 $H(X|Y)=H(g(Y)|Y)=0$。

---

## 7. Fano 不等式的區域圖

[▶ 31:26](https://youtu.be/15SwirHhsqk?t=1886)

**Fig. 2.4**（p. 23）：橫軸 $P_e$、縱軸 $H(X|Y)$，邊界是 $f(P_e):=h_b(P_e)+P_e\log_2(|\mathcal X|-1)$。
- $f$ 在 $P_e=\frac{|\mathcal X|-1}{|\mathcal X|}$ 時達到最大值 $\log_2|\mathcal X|$；$P_e=1$ 時 $f(1)=\log_2(|\mathcal X|-1)$。
- 允許的 $(P_e,H(X|Y))$ 在曲線下方（斜線區）：工程上做得到的都在這裡。

**下界** [▶ 31:56](https://youtu.be/15SwirHhsqk?t=1916)：$H(X|Y)$ 一定時，不管怎麼猜，$P_e$ 有一個下界——由「$Y$ 對 $X$ 的數學性了解」完全決定。而且這**不是漸近的**，是百分之百對的。

**上界也有**（【口頭】）：若 $\log_2(|\mathcal X|-1)<H(X|Y)\le\log_2|\mathcal X|$，$P_e$ 也有上界——就算亂猜，想錯到 100% 也不可能。
- 比喻：考 1000 題是非題，想考 0 分很難，每題都要猜錯；每題都猜對當然也難。對這件事完全不了解時，你沒辦法刻意讓錯誤率 100%。

【課本補充】Observation 2.27（pp. 23–24）的精確敘述：
- 當 $\log_2(|\mathcal X|-1)<H(X|Y)\le\log_2|\mathcal X|$：
$$0<\inf\{a:f(a)\ge H(X|Y)\}\le P_e\le\sup\{a:f(a)\ge H(X|Y)\}<1.$$
- 當 $0<H(X|Y)\le\log_2(|\mathcal X|-1)$：只有下界 $P_e\ge\inf\{a:f(a)\ge H(X|Y)\}>0$。
- 結論：$H(X|Y)$ 離 0 有距離 ⇒ $P_e$ 也離 0 有距離。
- 較弱但簡單的版本：$h_b(P_e)\le1$ 得 $H(X|Y)\le1+P_e\log_2(|\mathcal X|-1)$，即 $P_e\ge\frac{H(X|Y)-1}{\log_2(|\mathcal X|-1)}$（$|\mathcal X|>2$）。

---

## 8. 證明一：引進錯誤指標 E

[▶ 33:56](https://youtu.be/15SwirHhsqk?t=2036)

【口頭】很聰明、很 tricky，一頁就證完；但針對性強，**不容易推廣**，也**看不出等號何時成立**。

**證明**（課本 p. 24）：定義新的隨機變數
$$E:=\begin{cases}1,&g(Y)\ne X\ (\text{猜錯})\\0,&g(Y)=X\ (\text{猜對})\end{cases}$$
它的期望值就是 $P_e$；它把「操作」藏在一個隨機變數裡。

用 conditional entropy 的 chain rule（$Y$ 一直是 given），兩種順序量 $(E,X)$：
$$H(E,X|Y)=H(X|Y)+H(E|X,Y)=H(E|Y)+H(X|E,Y).$$

逐項處理：
1. $H(E|X,Y)=0$：知道 $X$ 和 $Y$，就知道 $g(Y)$ 是否等於 $X$，$E$ 完全確定。
2. $H(E|Y)\le H(E)=h_b(P_e)$：conditioning 不增加 entropy；$E$ 是二元、機率 $(P_e,1-P_e)$。
3. $H(X|E,Y)$：
$$H(X|E,Y)=\Pr[E=0]\,H(X|Y,E=0)+\Pr[E=1]\,H(X|Y,E=1)\le(1-P_e)\cdot0+P_e\log_2(|\mathcal X|-1).$$
   - $E=0$ 時 $X=g(Y)$，完全確定，entropy 0。
   - $E=1$ 時 $X\ne g(Y)$，只剩 $|\mathcal X|-1$ 種可能，entropy 最多 $\log_2(|\mathcal X|-1)$（uniform 時最大）。例：送 0、猜錯，只剩 1、2、3。

合起來：$H(X|Y)=H(E|Y)+H(X|E,Y)-0\le h_b(P_e)+P_e\log_2(|\mathcal X|-1)$。∎

**Sharp vs tight** [▶ 39:33](https://youtu.be/15SwirHhsqk?t=2373)：
- 等號在某些情形會成立，所以 Fano 不等式**不能再改善**。
- 課本 p. 24 註 9：bound 在**某些特定情形**達到叫 **sharp**；在**所有情形**都達到叫 **tight**。Fano 是 sharp，不是 tight。【口頭】sharp 像瞬間跳起來的尖峰。都是 worst case 考量，大部分情形等號不成立。

【課本補充】等號條件（p. 25）：$H(E|Y)=H(E)$（$E$ 和 $Y$ 獨立）且 $H(X|Y,E=1)=\log_2(|\mathcal X|-1)$（$P_{X|Y}(\cdot|y)$ 在 $\mathcal X\setminus\{g(y)\}$ 上均勻）。

【課本補充】**Example 2.28**（p. 25）：$X$、$Y$ 獨立，都在 $\{0,1,2\}$ 上均勻，$g(y)=y$。
$$P_e=\Pr[Y\ne X]=1-\sum_{x=0}^2P_X(x)P_Y(x)=1-3\cdot\tfrac19=\tfrac23.$$
$$h_b\left(\tfrac23\right)+\tfrac23\log_2(3-1)=H(X|Y)=H(X)=\log_23.$$
（驗算：$h_b(\frac23)=\log_23-\frac23$，加上 $\frac23\cdot1$ 得 $\log_23$。）

---

## 9. 證明二：DPI + FI（可推廣的證明）

[▶ 40:03](https://youtu.be/15SwirHhsqk?t=2403)

【口頭】這是「正統」的證明：照口訣「相減、把 log 拿掉」，比較長，但**一招闖天下**，而且**完全知道等號何時成立**。課本習題 26、27 題（別的書沒有）就用這個方法推廣，例如 **list estimator**（讓你猜三次，有一次對就算對）的 Fano 不等式。

**卡在哪裡** [▶ 40:35](https://youtu.be/15SwirHhsqk?t=2435)：$X$ 有限，$Y$ 可能無限甚至連續（例如 $X=\pm1$，$Y$ 是實數）。$X$ 和 $Y$ 的空間不對稱，沒辦法直接「相減、合併 summation、拿掉 log」。

**小技巧**：$X\to Y\to\hat X$ 是 Markov chain，而 $\hat X=g(Y)$ 和 $X$ **在同一個空間**（都有 $|\mathcal X|$ 種可能）。由 DPI：
$$I(X;Y)\ge I(X;\hat X)\ \Rightarrow\ H(X)-H(X|Y)\ge H(X)-H(X|\hat X)\ \Rightarrow\ H(X|Y)\le H(X|\hat X).$$
所以只要證 $H(X|\hat X)\le h_b(P_e)+P_e\log_2(|\mathcal X|-1)$ 就好，而這可以用傳統方法。

【口頭】這門課有很多這種小技巧，但很多老師不特別強調。做研究時，怎麼變化題目讓一個技巧能用上，這種思維很有用。

**計算** [▶ 43:43](https://youtu.be/15SwirHhsqk?t=2623)（課本 pp. 25–26）：
$$P_e=\sum_{x}\sum_{\hat x\ne x}P_{X,\hat X}(x,\hat x),\qquad1-P_e=\sum_xP_{X,\hat X}(x,x)$$
（錯誤率 = 非對角線的和；正確率 = 對角線的和。例：$X=\pm1$，送 −1 猜 +1、送 +1 猜 −1 就是錯。）

把 $H(X|\hat X)$ 拆成非對角線和對角線兩部分，$h_b(P_e)$、$P_e\log_2(|\mathcal X|-1)$ 也用上面的和寫出來，相減後合併 log：
$$\begin{aligned}
&H(X|\hat X)-h_b(P_e)-P_e\log_2(|\mathcal X|-1)\\
&=\sum_x\sum_{\hat x\ne x}P_{X,\hat X}(x,\hat x)\log_2\frac{P_e}{P_{X|\hat X}(x|\hat x)(|\mathcal X|-1)}+\sum_xP_{X,\hat X}(x,x)\log_2\frac{1-P_e}{P_{X|\hat X}(x|x)}\\
&\le\log_2(e)\sum_x\sum_{\hat x\ne x}P_{X,\hat X}(x,\hat x)\left[\frac{P_e}{P_{X|\hat X}(x|\hat x)(|\mathcal X|-1)}-1\right]+\log_2(e)\sum_xP_{X,\hat X}(x,x)\left[\frac{1-P_e}{P_{X|\hat X}(x|x)}-1\right]\\
&=\log_2(e)\left[\frac{P_e}{|\mathcal X|-1}\sum_x\sum_{\hat x\ne x}P_{\hat X}(\hat x)-P_e\right]+\log_2(e)\left[(1-P_e)\sum_xP_{\hat X}(x)-(1-P_e)\right]\\
&=\log_2(e)\left[\frac{P_e}{|\mathcal X|-1}(|\mathcal X|-1)-P_e\right]+\log_2(e)\left[(1-P_e)-(1-P_e)\right]=0.
\end{aligned}$$
- 不等號：每個 log 用 FI $\log x\le\log(e)(x-1)$。
- $P_{X,\hat X}(x,\hat x)/P_{X|\hat X}(x|\hat x)=P_{\hat X}(\hat x)$；$\sum_x\sum_{\hat x\ne x}P_{\hat X}(\hat x)=(|\mathcal X|-1)\sum_{\hat x}P_{\hat X}(\hat x)=|\mathcal X|-1$。

**等號** [▶ 47:14](https://youtu.be/15SwirHhsqk?t=2834)：FI 的等號 iff log 裡的數是 1：
$$P_{X|\hat X}(x|\hat x)(|\mathcal X|-1)=P_e\ (\hat x\ne x),\qquad P_{X|\hat X}(x|x)=1-P_e.$$
可以刻意造出這種很特殊的情形。

**推廣**（【口頭】）：$P_e$ 是「$\hat x$ 不在某集合」的和、$1-P_e$ 是「$\hat x$ 在某集合」的和——把對角線換成任意集合，同樣的步驟就能推廣到 list decoding、分 group 猜等情形。Fano 原本的策略是把接收端分成「猜對（例如 $\{0\}$）」和「猜錯（$\{1,2,3\}$）」兩塊；如果改成猜它在哪個 group，形式還是對，怎麼證？相減、把 log 拿掉，就證完了。

【口頭】幾年後你一定寫不出這個證明（老師說他也寫不出來），但會記得邏輯：**相減，把 log 拿掉**。為什麼算到最後剛好是 0？因為它是**對的量**。韓太舜（Shannon Award 得主）書的 preface 開宗明義寫：在 information theory 裡，只要你想對了、找到對的量，後面的證明數學上都很簡單。老師認為這句話非常經典。

---

## 10. 一頁速查表

**兩種 mutual information 寫法**（要背）
$I(X;Y)=E\left[\log\frac{P_{XY}}{P_XP_Y}\right]=E\left[\log\frac{P_{Y|X}}{P_Y}\right]$；$P_{XY}=P_XP_{Y|X}$，$P_X$ 可設計、$P_{Y|X}$ 是自然界。

**DPI**
- $X\to Y\to Z$ ⇒ $I(X;Y)\ge I(X;Z)$。關鍵：$I(X;Z|Y)=0$ + chain rule $I(X;Z)+I(X;Y|Z)=I(X;Y)$。
- $I(X;Y)\ge I(X;g(Y))$；$I(U;V)\le I(X;Y)$（encoder–channel–decoder）。
- $X\to Y\to Z$ ⇒ $I(X;Y|Z)\le I(X;Y)$；鏈上 $I(X_i;X_l)\le I(X_j;X_k)$（$i\le j\le k\le l$）。
- 非 Markov 時可能變大：$X,Y$ i.i.d. Bern(1/2)，$Z=X+Y$ ⇒ $I(X;Y|Z)=H(X|Z)=\frac12\cdot1=0.5>0$。

**Fano**
- $H(X|Y)\le h_b(P_e)+P_e\log_2(|\mathcal X|-1)$，對**任何**估計 $g$ 成立 → converse 的工具。
- 證明一：$E=\mathbf 1\{g(Y)\ne X\}$；$H(X|Y)=H(E|Y)+H(X|E,Y)-H(E|X,Y)\le h_b(P_e)+P_e\log(|\mathcal X|-1)$。
- 證明二：DPI 得 $H(X|Y)\le H(X|\hat X)$，再拆對角／非對角、用 FI。
- $P_e=0\Rightarrow H(X|Y)=0$；$H(X|Y)>0\Rightarrow P_e$ 有正下界；$H(X|Y)>\log(|\mathcal X|-1)$ 時 $P_e$ 也有 $<1$ 的上界。
- 弱版：$P_e\ge\frac{H(X|Y)-1}{\log_2(|\mathcal X|-1)}$。
- Sharp（某些情形等號）≠ tight（所有情形等號）。例：$X,Y$ 獨立均勻於 $\{0,1,2\}$、$g(y)=y$ ⇒ $P_e=\frac23$，等號成立。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Divergence（第一種 MI 寫法的一般化） | 第 10 集（§2.6） |
| Fano 不等式證 converse | 第 12 集（source coding converse）、第 18 集（channel coding weak converse） |
| DPI | 第 18 集、第 21 集（joint source-channel coding converse）、第 28 集 |
| Output statistics | 第 35 集（第二部分 Chapter 4） |

---

## 附：本集一句話總結

> **處理只會讓 mutual information 變少（但形式更有用）；而 Fano 不等式用一個與猜法無關的界，把數學量 $H(X|Y)$ 和操作量 $P_e$ 綁在一起——只要 $H(X|Y)$ 不趨近 0，任何人的錯誤率都不可能趨近 0，這就是所有 converse 的基礎。**

---

## ⚠️ 待確認清單

1. [▶ 02:05](https://youtu.be/15SwirHhsqk?t=125) 老師說 entropy 出現在 Shannon 論文「2.6 節」標題（第 1 集說 Section 6），以及 Shannon 拜訪 von Neumann 的年齡、拿博士的年齡等細節，課本沒有記載。

---

*筆記依據陳伯寧老師「消息理論」Lec09 錄影逐字稿（whisper large-v3-turbo，49:30）與 Alajaji & Chen 課本 §2.4–2.5 整理。*
