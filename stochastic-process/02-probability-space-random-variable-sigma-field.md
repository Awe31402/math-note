---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 2
lecture: Lec 9-1 General Concepts — Definitions (1/7)
date: 待補
video: https://youtu.be/xcZ7YH9uW2I
notes: Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. §2-2 機率空間（Fields、Borel fields，pp. 22–23，式 (2-16)–(2-21)）、§4-1 隨機變數（pp. 72–74）
---

# 第 2 集 · Lec 9-1 (1/7)：為什麼學隨機過程、機率空間、隨機變數、σ-field [▶ 影片](https://youtu.be/xcZ7YH9uW2I)

← 上一集：[01](01-course-introduction-syllabus.md) ｜ [總目錄](README.md) ｜ 下一集：[03](03-probability-measure-cdf-sufficiency-random-vector.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 2 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（37:18，whisper large-v3-turbo）＋ Papoulis §2-2（pp. 22–24）、§4-1（pp. 72–74）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「實數」聽成「時數」，「量度」聽成「良度」，「公設」聽成「公社」，「probability measure」聽成「Probidity Major／Profit Majors」，「random variable」聽成「Brandom Variable」，「stochastic」聽成「Sketis／scatastic」，「河川」聽成「核川／核傳」，「空集合」聽成「空極核／空姐」。以下一律用正確的字，不再逐一標。

> 這一集的標題是第 9 章，但內容其實是**複習機率論的基礎**：機率空間、隨機變數、σ-field。課本對應的是第 2、4 章，不是第 9 章。投影片沒有公開，公式是從口述和課本重建的。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 名詞：random、stochastic、process](#1-名詞randomstochasticprocess)
- [2. 為什麼要學隨機過程](#2-為什麼要學隨機過程)
  - [2.1 確定模型 vs 隨機模型](#21-確定模型-vs-隨機模型)
  - [2.2 隨機過程一定跟時間有關](#22-隨機過程一定跟時間有關)
  - [2.3 統計特性要百分之百確定](#23-統計特性要百分之百確定)
- [3. 機率空間 (S, F, P)](#3-機率空間-s-f-p)
- [4. 隨機變數的定義](#4-隨機變數的定義)
  - [4.1 定義](#41-定義)
  - [4.2 為什麼一定要映射到實數](#42-為什麼一定要映射到實數)
  - [4.3 「隨機變數」既不隨機、也不是變數](#43-隨機變數既不隨機也不是變數)
- [5. 例子：正方形、三角形、菱形](#5-例子正方形三角形菱形)
- [6. Field（代數）的公設](#6-field代數的公設)
  - [6.1 三條公設和背後的道理](#61-三條公設和背後的道理)
  - [6.2 交集封閉：可以證出來](#62-交集封閉可以證出來)
  - [6.3 老師的版本 vs 課本的版本](#63-老師的版本-vs-課本的版本)
- [7. 為什麼要 σ-field](#7-為什麼要-σ-field)
  - [7.1 反例：端點是有理數的區間](#71-反例端點是有理數的區間)
  - [7.2 σ-field 的定義](#72-σ-field-的定義)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 名詞解釋、為什麼學這門課 | [▶ 00:00](https://youtu.be/xcZ7YH9uW2I?t=0) | 無（【口頭】） |
| 機率空間 (S, F, P) | [▶ 10:17](https://youtu.be/xcZ7YH9uW2I?t=617) | §2-2「Axiomatic Definition of an Experiment」，p. 23 |
| 隨機變數的定義 | [▶ 13:19](https://youtu.be/xcZ7YH9uW2I?t=799) | §4-1 Definition，p. 74 |
| Field 的公設 | [▶ 25:38](https://youtu.be/xcZ7YH9uW2I?t=1538) | §2-2 Fields，式 (2-16)–(2-19)，p. 22 |
| σ-field（Borel field） | [▶ 32:20](https://youtu.be/xcZ7YH9uW2I?t=1940) | §2-2 Borel fields，pp. 22–23 |

老師開頭就說：第 9 章是**觀念上比較難**的一章，因為要接受很抽象的概念。他會一邊介紹，一邊說明為什麼這些抽象概念重要。【口頭】

---

## 1. 名詞：random、stochastic、process

[▶ 01:03](https://youtu.be/xcZ7YH9uW2I?t=63) 老師從字典查這三個字。【口頭】

- **random**：口語裡常帶有「**每個都一樣機會**」(equal chance for each item) 的意思，也就是 uniform（均勻）。例如「random pick 一個人」，意思是十個人每人機率都是 1/10。
  - 所以看到 random 這個字，如果沒有特別說明，直覺上可以先當成 uniform。
- **stochastic**：有機率、有規律 (pattern)，**可以被分析，但不一定能精確預測** (can be analyzed, but may not be predicted precisely)。這正好是這門課的目標。
- 所以老師比較喜歡叫 **stochastic process**（隨機過程），覺得比 random process 更準。兩個名字指的是同一個東西。
- **process**：一個有目的、有系統的步驟。例如收集一大堆河川流量和空氣污染的資料，目的是找出兩者的關係。

[▶ 03:40](https://youtu.be/xcZ7YH9uW2I?t=220) 老師給的簡單定義【口頭】：

> 隨機過程是為了**方便分析一個系統** (for convenience of analyzing a system)。系統有輸入、有輸出；用隨機過程的模型，可以有規律地分析它。

他也說：理論如果達不到這個目的，就變成數學遊戲。

---

## 2. 為什麼要學隨機過程

### 2.1 確定模型 vs 隨機模型

[▶ 04:13](https://youtu.be/xcZ7YH9uW2I?t=253) 以通訊系統為例，模型可以粗分兩種【口頭】：

| | 確定模型 (deterministic model) | 隨機模型 (stochastic model) |
|---|---|---|
| 意思 | 什麼都知道：要傳的資料、雜訊，全部確定 | 有些東西不確定 |
| 例子 | 手機只為了傳 `10111` 這一串而設計；要傳 `11001` 就傳不好 | 不知道下一個要傳的是 0 還是 1 |
| 缺點 | 用途太窄，不是我們要的 | — |

重點不是「分兩類」本身，而是要想清楚：**什麼是確定的、什麼是不確定的**。

### 2.2 隨機過程一定跟時間有關

[▶ 05:43](https://youtu.be/xcZ7YH9uW2I?t=343) 老師強調關鍵字 **time dependent**（跟時間有關），他說很多書沒講清楚。【口頭】

- 系統是要**隨時間一直用**的：今天下午用、晚上用、明天早上用。電風扇要用三年，滑鼠保證用一年。
- 所以後面的定義都有一個「時間」指標 (index)：平穩 (stationary) 跟時間平移有關，遍歷 (ergodic) 也跟時間有關。

### 2.3 統計特性要百分之百確定

[▶ 06:44](https://youtu.be/xcZ7YH9uW2I?t=404)【口頭】

- 我們不知道雜訊或資料**隨時間怎麼變**，但一定要**完全知道它的統計特性**，才能做隨機過程的分析。
- 例：0 和 1 各出現 1/2。機率是確定的，但下一個是 0 還是 1 完全不確定。
- 如果連統計特性都不知道，叫 **blind system**（盲系統）。也有人研究，但很難，要犧牲效能、複雜度或傳輸速度。
- 這門課：**對機率是百分之百確定的**。

[▶ 07:46](https://youtu.be/xcZ7YH9uW2I?t=466) 通訊裡一定是隨機過程的東西：**雜訊** (noise)、**干擾** (interference)、**要傳的資料**。其他部分是你要設計的。

[▶ 08:16](https://youtu.be/xcZ7YH9uW2I?t=496) 老師說隨機過程算是工程科系的**數學基礎課**，和 detection／estimation 一樣。他在美國讀研究所時，這兩門每年都開，比較應用的課反而很少開。所以定義會很數學，要開始接受抽象的概念。【口頭】

---

## 3. 機率空間 (S, F, P)

[▶ 10:17](https://youtu.be/xcZ7YH9uW2I?t=617) 隨機變數一定要定義在一個**機率空間** (probability space) 上。機率空間有三個要素，寫成三元組 (tuple) $(S,\mathcal{F},P)$：

1. **$S$：樣本空間** (sample space)。所有可能的**結果** (outcome) 列出來。
   - 丟銅板：$S=\{\text{正面},\text{反面}\}$。
   - 丟骰子：$S=\{1,2,3,4,5,6\}$。
   - 一定要清楚列出「你能觀察到的結果是什麼」。
2. **$\mathcal{F}$：事件空間** (event space)，一般要求是 **σ-field**（第 7 節）。裡面放的是**事件** (event)。
   - 事件 = 你在機率上想看的一個結果集合。例：丟骰子出現偶數 → 事件 $\{2,4,6\}$；出現奇數 → $\{1,3,5\}$。
   - **事件一定要能量機率**。不能量機率的集合，對這門課沒有意義。
3. **$P$：機率測度** (probability measure)。對 $\mathcal{F}$ 裡的**每一個**事件，都要給一個機率。

> 老師的直覺訓練【口頭】：**一看到「$\in\mathcal{F}$」，就馬上想到「它是事件，所以它有機率」。**

【課本補充】Papoulis 的說法一樣（§2-2，p. 23「Axiomatic Definition of an Experiment」）：一個實驗由三樣東西決定——所有結果的集合 $S$、所有事件構成的 Borel field、這些事件的機率。

---

## 4. 隨機變數的定義

### 4.1 定義

[▶ 13:19](https://youtu.be/xcZ7YH9uW2I?t=799) 投影片上的定義（從口述重建）：

> **定義（隨機變數，random variable）**：設 $(S,\mathcal{F},P)$ 是機率空間。隨機變數 $X$ 是一個**實數值函數** (real-valued function)
> $$X:S\to\mathbb{R},$$
> 而且對**每一個**實數 $x$，
> $$\{\zeta\in S:\ X(\zeta)\le x\}\in\mathcal{F}.$$

第二個條件老師用紅字特別寫出來，他說有些書不寫，但他認為**非常重要**。【口頭】

這個條件在說什麼：

- 因為 $X$ 映到實數，所以 $X(\zeta)$ 可以和另一個實數 $x$ **比大小**。
- 把所有「映過去之後 $\le x$」的結果 $\zeta$ 收集起來，變成 $S$ 的一個子集。
- 這個子集**一定要在 $\mathcal{F}$ 裡**，也就是一定要是事件、一定要能量機率。
- 例：把「正面」映到 $-1$。那麼 $\{\zeta: X(\zeta)\le x\}$ 就是「映過去的數 $\le x$ 的那些銅板面」。

老師要大家記住這句話（他說下一節課大家自己就念得出來）：

> **A random variable is a real-valued function defined over a probability space.**

【課本補充】Papoulis 的定義（§4-1，p. 74）：隨機變數 $\mathbf{x}$ 是對每個結果 $\zeta$ 指定一個數 $\mathbf{x}(\zeta)$ 的規則，而且要滿足：

1. 對每一個 $x$，集合 $\{\mathbf{x}\le x\}$ 是事件。
2. $P\{\mathbf{x}=\infty\}=0$，$P\{\mathbf{x}=-\infty\}=0$。

第 1 條和老師的條件一樣。第 2 條是課本多的，因為課本允許 $\mathbf{x}$ 取 $\pm\infty$；老師直接規定映到 $\mathbb{R}$，就不需要這條。課本也強調：$\{\mathbf{x}\le x\}$ **不是一個數的集合，而是一個結果的集合**（p. 73）。

### 4.2 為什麼一定要映射到實數

[▶ 13:49](https://youtu.be/xcZ7YH9uW2I?t=829) 老師給兩個理由【口頭】：

1. **實數是最完整的數學系統**：有加、減、乘、除，有加法和乘法的反元素，可以排大小。映到實數之後，做什麼運算都沒有困難。
2. **樣本空間通常是抽象的**：銅板的正面、反面不是數字，不能加減乘除，也不能說「正面大於反面」。要拿來算，就要先**量化**，映成實數。

老師也說：目前還沒有人把隨機變數完整地推廣到非實數的世界。

### 4.3 「隨機變數」既不隨機、也不是變數

[▶ 16:26](https://youtu.be/xcZ7YH9uW2I?t=986) 老師引用另一本書第 4 頁的說法：random variable 這個名字是 **misnomer**（名不符實）。【口頭】

- **不隨機**：$X$ 是一個**確定的映射** (deterministic mapping)。給定結果 $\zeta$，$X(\zeta)$ 就固定了。隨機性全部來自「哪個 $\zeta$ 發生」，不在 $X$ 本身。
- **不是變數**：它是一個**函數** (function)、一個對應 (mapping)，從 $S$ 映到 $\mathbb{R}$。
- 原文大意：*the random variable simply maps each point (outcome) in the sample space to a real number.*
- 老師的比喻：聽過一個演講說「神聖羅馬帝國既不神聖、跟羅馬也沒關係、也不是帝國」。
- 大學部把它講成「變數」，是為了好懂；研究所要了解它的本質。到介紹隨機過程時，就會明白為什麼一定要這樣看。

⚠️ 待確認：老師沒說是哪一本書（逐字稿只有「另外一本書……第四頁」）。

老師順便建議：不要只讀一本課本，比較幾本書，不同作者對同一件事描述不同，甚至會有出入，可能會得到新想法。【口頭】

---

## 5. 例子：正方形、三角形、菱形

[▶ 21:02](https://youtu.be/xcZ7YH9uW2I?t=1262)

樣本空間是三個**抽象的形狀**，沒有結構，不能加減、不能比大小：

$$S=\{\square,\ \triangle,\ \diamond\}$$

（老師說這種抽象事件在機率裡很常見：正面反面、哪幾個國家會結盟、三個系會不會合併……）

我們關心的事件剛好四個：

$$\mathcal{F}=\big\{\varnothing,\ \{\square,\triangle\},\ \{\diamond\},\ S\big\}$$

機率測度：

| 事件 | $\varnothing$ | $\{\square,\triangle\}$ | $\{\diamond\}$ | $S$ |
|---|---|---|---|---|
| $P$ | 0 | 0.7 | 0.3 | 1 |

- $\{\square,\triangle\}$ 的意思是「正方形或三角形其中一個出現」（每次還是只出現一個）。
- 這是一個**合法的** (well-defined) 機率空間：四個事件都有機率。
- 注意：「正方形單獨出現」$\{\square\}$、「三角形單獨出現」$\{\triangle\}$ **不在** $\mathcal{F}$ 裡。意思是我們**不關心**它們，也就不用給它們機率。

### $\mathcal{F}$ 可以是空的嗎？

[▶ 18:57](https://youtu.be/xcZ7YH9uW2I?t=1137) 定義裡寫 $\mathcal{F}$ 是 **nonempty**（非空）。老師問：$\mathcal{F}$ 可以是空的嗎？【課堂討論】（老師讓同學心裡先想答案，再自己回答）

- 直觀理由：你都在研究機率了，一定有關心的事件，空的很奇怪。
- 數學上更精確：$\mathcal{F}$ **至少有兩個元素**：$\varnothing$ 和 $S$。
  - $\varnothing$：什麼都沒發生，機率 0，一定能量。
  - $S$：例如「骰子出現 1 到 6 點中任一點」，一定發生，機率 1，一定能量。
- 所以**最小的事件空間**是 $\{\varnothing,S\}$。它合法，但很 trivial（沒什麼用）。

---

## 6. Field（代數）的公設

[▶ 23:37](https://youtu.be/xcZ7YH9uW2I?t=1417) 事件空間不只是一堆集合，它要有**規則**，才有結構、才能操作。老師的比喻：政黨有黨章、交大有校規。數學上講「空間」(space)，一定有規則。【口頭】

事件空間的規則，借用代數學家的 **field**（也叫 **algebra**，代數）。

### 6.1 三條公設和背後的道理

[▶ 26:08](https://youtu.be/xcZ7YH9uW2I?t=1568) $\mathcal{F}$ 是一個 **field**，如果：

1. $\varnothing\in\mathcal{F}$ 而且 $S\in\mathcal{F}$。
2. **補集封閉** (closure under complementation)：$A\in\mathcal{F}\Rightarrow A^c\in\mathcal{F}$。
3. **有限聯集封閉** (closure under finite union)：$A,B\in\mathcal{F}\Rightarrow A\cup B\in\mathcal{F}$。

老師用同一個準則解釋三條：**事件 = 有一個機制 (mechanism) 能決定「一個結果在不在這個集合裡」**。【口頭】

1. $\varnothing$ 和 $S$：一定能決定。$\varnothing$ 裡沒有任何結果，$S$ 裡有全部結果。所以放進來。
2. 補集：能決定「誰在 $A$ 裡」，就能決定「誰不在 $A$ 裡」。
   - 回到第 5 節的例子：$\{\diamond\}$ 在 $\mathcal{F}$ 裡，它的補集 $\{\square,\triangle\}$ 也一定要在。
   - 既然知道 $P(\{\diamond\})=0.3$，就知道 $P(\{\square,\triangle\})=0.7$。想量 $\{\square,\triangle\}$，可以反過來量 $\{\diamond\}$。
3. 聯集：能決定「在不在 $A$」，也能決定「在不在 $B$」，就一定能決定「在不在 $A\cup B$」。

公設 (axiom) 是大家都同意、不用證明的。老師強調【口頭】：

- 公設**越少越好**，其他性質都從公設證出來。（像向量空間的 8 條性質，已經減到最少。）
- 公設不是永遠不能改。有人研究拿掉其中一條會怎樣（例如 π-system）。如果你發現拿掉某一條反而更好用，就大膽拿掉，但要證明它有用。

### 6.2 交集封閉：可以證出來

[▶ 30:45](https://youtu.be/xcZ7YH9uW2I?t=1845) 早期有人把「$A,B\in\mathcal{F}\Rightarrow A\cap B\in\mathcal{F}$」列為第 4 條公設，後來發現不需要，因為**可以用第 2、3 條證出來**。

**證明**（老師說「二跟三可以證第四個」；以下步驟依課本式 (2-18) 的證法補完整）：

設 $A,B\in\mathcal{F}$。

1. 由公設 2：$A^c\in\mathcal{F}$，$B^c\in\mathcal{F}$。
2. 由公設 3：$A^c\cup B^c\in\mathcal{F}$。
3. 再用公設 2：$(A^c\cup B^c)^c\in\mathcal{F}$。
4. De Morgan 定律：$(A^c\cup B^c)^c=A\cap B$。

所以 $A\cap B\in\mathcal{F}$。 ∎

老師的建議【口頭】：雖然不是公設，**還是把它當成第 4 條記住**。考試、推導時很好用：**交集、聯集全部都要在裡面**就對了。

### 6.3 老師的版本 vs 課本的版本

兩邊寫法不同（來源衝突，兩邊都寫）：

| | 老師（投影片） | Papoulis §2-2，p. 22 |
|---|---|---|
| 第 1 條 | $\varnothing\in\mathcal{F}$，$S\in\mathcal{F}$ | $\mathcal{F}$ 非空 (nonempty) |
| 第 2 條 | $A\in\mathcal{F}\Rightarrow A^c\in\mathcal{F}$ | 同，式 (2-16) |
| 第 3 條 | $A,B\in\mathcal{F}\Rightarrow A\cup B\in\mathcal{F}$ | 同，式 (2-17) |

以下**不是逐字稿內容**，是依課本式 (2-19) 的推導補的：**兩個版本等價**。

- 老師 ⇒ 課本：$\varnothing\in\mathcal{F}$，所以 $\mathcal{F}$ 非空。
- 課本 ⇒ 老師：$\mathcal{F}$ 非空，所以至少有一個 $A\in\mathcal{F}$。由 (2-16)，$A^c\in\mathcal{F}$。由 (2-17)，$A\cup A^c=S\in\mathcal{F}$。再由 (2-16)，$S^c=\varnothing\in\mathcal{F}$。

【課本補充】由兩兩聯集，用歸納法可得：**有限多個**事件的聯集、交集都在 $\mathcal{F}$ 裡。但**無限多個**就不一定（p. 22）。這正是下一節的問題。

---

## 7. 為什麼要 σ-field

[▶ 32:20](https://youtu.be/xcZ7YH9uW2I?t=1940) Field 在數學上沒問題，但工程上**常要處理極限**。【口頭】

- 系統越來越大；一支手機買了用兩年，可能被使用十萬次、百萬次。
- 長時間使用 → 行為有**極限效應**。
- 一碰到極限，field 的定義就出問題。

### 7.1 反例：端點是有理數的區間

[▶ 33:22](https://youtu.be/xcZ7YH9uW2I?t=2002) 老師說這是一個很人工 (artificial) 的例子。

- $S=\mathbb{R}$。
- $\mathcal{F}$：所有**開區間、半開區間、閉區間**，而且**兩個端點都是有理數** (rational number)。
- 老師說它是一個 field（滿足前面三條公設）。

以下**不是逐字稿內容**，是依 field 的公設推論的：嚴格說，單獨的區間對補集不封閉（例如 $[0,1]^c=(-\infty,0)\cup(1,\infty)$ 不是一個區間）。要讓它真的是 field，$\mathcal{F}$ 應該取「端點是有理數（或 $\pm\infty$）的區間的**有限聯集**」。這樣修正後，下面的反例照樣成立。

**取極限：**

令 $\pi_{(k)}$ 是圓周率 $\pi$ 截到小數點後第 $k$ 位：$\pi_{(1)}=3.1$，$\pi_{(2)}=3.14$，$\pi_{(3)}=3.141$，……。每個 $\pi_{(k)}$ 都是**有限小數，所以是有理數**。

令
$$A_k=\left[0,\ \pi_{(k)}\right],\qquad k=1,2,3,\dots$$

⚠️ 待確認：老師只說「左端是 0、右端是 π 截到第 k 位」，沒說區間開或閉；這裡用閉區間，不影響結論。

- 每個 $A_k$ 兩端都是有理數，所以 $A_k\in\mathcal{F}$。
- 取**無限多個**的聯集。因為 $\pi_{(k)}$ 遞增而且趨近 $\pi$，但每個都 $<\pi$：
$$\bigcup_{k=1}^{\infty}A_k=[0,\pi).$$
- 左端 0 是有理數，但**右端 $\pi$ 是無理數**。所以 $[0,\pi)\notin\mathcal{F}$。

結論：每個 $A_k$ 都能量機率，它們的極限卻**不能量機率**。這是 field 的缺陷。

老師說【口頭】：這看起來有點吹毛求疵，工程師可能不管，東西能用就好。但隨機過程的本質是數學，要嚴謹；理論弄嚴謹，做工程應用時也會更嚴謹。

### 7.2 σ-field 的定義

[▶ 35:25](https://youtu.be/xcZ7YH9uW2I?t=2125) 數學家定義 **σ-field**（sigma field）。和 field 只差在**第 3 條**：

> $\mathcal{F}$ 是 **σ-field**，如果：
> 1. $\varnothing\in\mathcal{F}$，$S\in\mathcal{F}$。
> 2. $A\in\mathcal{F}\Rightarrow A^c\in\mathcal{F}$。
> 3. **可數無限聯集封閉**：$A_1,A_2,\dots\in\mathcal{F}\Rightarrow\displaystyle\bigcup_{k=1}^{\infty}A_k\in\mathcal{F}$。

- 第 3 條放寬了，納進更多集合，**包含極限**。
- 有限聯集是特例：取 $A_3=A_4=\dots=\varnothing$ 就得到 $A_1\cup A_2$。所以 σ-field 一定是 field。
- 夠不夠？老師說到目前為止，工程應用用 σ-field 就夠了，所以沒有再往下推廣，但也不排除以後會。
- **事件空間 $\mathcal{F}$ 一律用 σ-field。**

【課本補充】Papoulis 叫它 **Borel field**（§2-2，p. 22）：如果 $A_1,\dots,A_n,\dots$ 是 $\mathcal{F}$ 裡的無限序列，它們的聯集和交集也都在 $\mathcal{F}$ 裡，$\mathcal{F}$ 就叫 Borel field。課本也說（p. 23）：
- 事件取成 Borel field，才能對事件的**極限**指定機率。
- 配套地，機率要多一條**可數可加性** (axiom of infinite additivity)，式 (2-21)：若 $A_1,A_2,\dots$ 兩兩互斥，則 $P(A_1\cup A_2\cup\cdots)=P(A_1)+P(A_2)+\cdots$。
- 實數線上的事件：取包含所有半直線 $x\le x_i$ 的**最小 Borel field**（p. 24）。

（老師說待會會介紹機率測度的三條規則，這一集沒講到，應該在下一集。）

最後 [▶ 36:29](https://youtu.be/xcZ7YH9uW2I?t=2189) 老師說：第一節課只是初步概念，後面會一直延伸、重複，讓大家有系統地了解隨機過程。

---

## 8. 一頁速查表

### 機率空間

$$(S,\mathcal{F},P)$$

- $S$：所有結果；$\mathcal{F}$：事件（σ-field）；$P$：每個事件的機率。
- **「$\in\mathcal{F}$」＝ 是事件 ＝ 有機率。**
- 最小的 $\mathcal{F}$：$\{\varnothing,S\}$。

### 隨機變數

$$X:S\to\mathbb{R},\qquad \{\zeta: X(\zeta)\le x\}\in\mathcal{F}\quad\forall x\in\mathbb{R}$$

- 關鍵：$\{X\le x\}$ 是**結果的集合**，要能量機率。
- 它是確定的函數，不隨機、不是變數；隨機性來自「哪個 $\zeta$ 發生」。
- 課本多一條：$P\{X=\pm\infty\}=0$。

### Field vs σ-field

| | Field（代數） | σ-field（Borel field） |
|---|---|---|
| 1 | $\varnothing,S\in\mathcal{F}$ | 同 |
| 2 | $A\in\mathcal{F}\Rightarrow A^c\in\mathcal{F}$ | 同 |
| 3 | $A\cup B\in\mathcal{F}$（有限） | $\bigcup_{k=1}^{\infty}A_k\in\mathcal{F}$（可數無限） |

- **交集封閉**（推出來的）：$A\cap B=(A^c\cup B^c)^c$，用 2 → 3 → 2。
- **非空 ⇒ $\varnothing,S\in\mathcal{F}$**：$A\cup A^c=S$，$S^c=\varnothing$。
- **Field 不夠的反例**：$A_k=[0,\pi_{(k)}]$ 端點都是有理數，但 $\bigcup_k A_k=[0,\pi)$ 右端點無理。
- σ-field ⇒ field：取 $A_3=A_4=\cdots=\varnothing$。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 機率空間 $(S,\mathcal{F},P)$ | 第 3 集起：機率測度的公設；隨機過程 $x(t,\zeta)$ 的定義 |
| 隨機變數是 $S\to\mathbb{R}$ 的函數 | 隨機過程 = 對每個 $\zeta$ 指定一個時間函數（課本 §9-1，p. 373） |
| $\{X\le x\}\in\mathcal{F}$ | 分布函數 $F(x,t)=P\{x(t)\le x\}$（課本式 (9-2)） |
| σ-field、處理極限 | 均方收斂、遍歷性（Lec 12-1，第 31–33 集） |
| time dependent | 平穩 (stationary)、遍歷 (ergodic) 的定義 |

---

## 附：本集一句話總結

> **隨機變數是定義在機率空間 $(S,\mathcal{F},P)$ 上的實數值函數，而且 $\{X\le x\}$ 一定要是事件；事件空間要用 σ-field，因為工程上要處理極限，而 field 對無限聯集不封閉。**

---

## ⚠️ 待確認清單

1. [▶ 16:26](https://youtu.be/xcZ7YH9uW2I?t=986) 老師引用「另外一本書第四頁」說 random variable 是 misnomer，沒說書名。
2. [▶ 33:53](https://youtu.be/xcZ7YH9uW2I?t=2033) 反例的 $A_k$ 是開區間還是閉區間，逐字稿沒說；筆記用閉區間（不影響結論）。
3. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 9-1 (1/7) 錄影逐字稿（whisper large-v3-turbo，37:18）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
