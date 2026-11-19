---
course: Number Theory（2021 秋，線上錄影）
episode: 16
lecture: 2021-09-29 第 2 部
date: 2021-09-29
video: https://youtu.be/w47fBFeDmyw
notes: 講者照 Keith Conrad〈The Gaussian Integers〉Theorem 3.1 的證明；Jones & Jones《Elementary Number Theory》§10.2 除法的幾何證明（書頁 198，PDF 頁 213）
---

# 第 16 集 · 高斯整數除法定理的證明（Proof of Division Algorithm in Gaussian Integers Continued） [▶ 影片](https://youtu.be/w47fBFeDmyw)

← 上一集：[15-gaussian-integers-division-algorithm-1](15-gaussian-integers-division-algorithm-1.md) ｜ [總目錄](README.md) ｜ 下一集：[17-gaussian-euclid-factoring-1](17-gaussian-euclid-factoring-1.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 16 集（2021-09-29 第 2 部，接第 15 集）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（22:07，自動字幕）＋ Jones & Jones《Elementary Number Theory》§10.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `【課堂討論】` 講者問、學生答

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 修正版的整數除法演算法](#1-修正版的整數除法演算法)
- [2. 高斯整數除法定理的證明](#2-高斯整數除法定理的證明)
  - [2.1 Step 1：把 α/β 寫成 (m + ni)/N(β)](#21-step-1把-αβ-寫成-m--ninβ)
  - [2.2 Step 2：對 m、n 做修正版除法](#22-step-2對-mn-做修正版除法)
  - [2.3 Step 3：定出 γ 和 ρ](#23-step-3定出-γ-和-ρ)
  - [2.4 Step 4：估計 N(ρ)](#24-step-4估計-nρ)
- [3. 接下來要做什麼](#3-接下來要做什麼)
- [4. 一頁速查表](#4-一頁速查表)
- [5. 與後續集數的連結](#5-與後續集數的連結)

---

## 0. 這堂課要做什麼

證明第 15 集的**除法定理**（Conrad Theorem 3.1）：

> $\alpha,\beta\in\mathbb{Z}[i]$，$\beta\neq0$ ⇒ 存在 $\gamma,\rho\in\mathbb{Z}[i]$，$\alpha = \beta\gamma+\rho$，$N(\rho)\le\tfrac12N(\beta)$。

講者說他「幾乎一行一行照 Conrad，因為它太漂亮了」，而且證明「正好反映剛才例子的計算」。

| 主題 | 時間 |
|---|---|
| 修正版整數除法 | 00:01 |
| 證明 | 01:14 |
| 預告 | 17:46 |

---

## 1. 修正版的整數除法演算法

[▶ 00:01](https://youtu.be/w47fBFeDmyw?t=1)

**普通版**（第 3 集）：$bq$ 取「$a$ **左邊**最近的」$b$ 的倍數，餘數 $0\le r<|b|$。

**修正版**（modified division theorem，Conrad 的說法）：$bq$ 取「**離 $a$ 最近的**」$b$ 的倍數。餘數可能是負的，但
$$|r|\le\frac12|b|.$$

**為什麼是一半** [▶ 05:13](https://youtu.be/w47fBFeDmyw?t=313)：講者畫數線。$m$ 落在兩個相鄰的倍數 $qN$ 和 $(q+1)N$ 之間，兩者相距 $N$。**取比較近的那個**，距離一定不超過一半，$\le\frac12N$。

**例子** [▶ 06:55](https://youtu.be/w47fBFeDmyw?t=415)（第 15 集最後的例子，除以 9）：
$$34 = 9\cdot 3+7 = 9\cdot 4-2.$$
- 普通版餘數 $7$：大於 $4.5$，「不好的選擇」。
- 修正版餘數 $-2$：$|-2|\le 4.5$。✓

**這也是高斯整數除法的實際做法** [▶ 01:14](https://youtu.be/w47fBFeDmyw?t=74)：算複數的商，看小數，取最近的格點。

---

## 2. 高斯整數除法定理的證明

### 2.1 Step 1：把 α/β 寫成 (m + ni)/N(β)

[▶ 02:17](https://youtu.be/w47fBFeDmyw?t=137)

分母有理化：
$$\frac\alpha\beta = \frac{\alpha\bar\beta}{\beta\bar\beta} = \frac{\alpha\bar\beta}{N(\beta)}.$$

$\alpha\bar\beta$ 是高斯整數，寫成 $m+ni$（$m,n\in\mathbb{Z}$）：
$$\frac\alpha\beta = \frac{m+ni}{N(\beta)}.$$

### 2.2 Step 2：對 m、n 做修正版除法

[▶ 03:34](https://youtu.be/w47fBFeDmyw?t=214)

用修正版除法演算法，分別拿 $N(\beta)$ 去除 $m$ 和 $n$：存在整數 $q_1,q_2,r_1,r_2$ 使
$$m = N(\beta)\,q_1+r_1,\qquad n = N(\beta)\,q_2+r_2,\qquad |r_1|,|r_2|\le\tfrac12N(\beta).$$

【口頭】講者問大家懂不懂為什麼是「一半」，然後畫了第 1 節的數線圖。

### 2.3 Step 3：定出 γ 和 ρ

[▶ 07:57](https://youtu.be/w47fBFeDmyw?t=477)

代回去：
$$\frac\alpha\beta = \frac{N(\beta)q_1+r_1 + i\left(N(\beta)q_2+r_2\right)}{N(\beta)} = (q_1+iq_2) + \frac{r_1+ir_2}{N(\beta)}.$$

【口頭】[▶ 09:07](https://youtu.be/w47fBFeDmyw?t=547) 講者寫到一半想直接消掉 $N(\beta)$：「我不要當典型的中級代數學生，亂消。只能消它真的在的地方——那邊還有一個 $N(\beta)$，笨的是我不是你們。」

令 [▶ 09:39](https://youtu.be/w47fBFeDmyw?t=579)
$$\gamma = q_1+iq_2\in\mathbb{Z}[i].$$

把 $N(\beta) = \beta\bar\beta$ 代入，兩邊乘 $\beta$ [▶ 11:15](https://youtu.be/w47fBFeDmyw?t=675)：
$$\alpha = \beta\gamma + \frac{r_1+ir_2}{\bar\beta}.$$

令
$$\rho = \alpha-\beta\gamma = \frac{r_1+ir_2}{\bar\beta}.$$

$\rho = \alpha-\beta\gamma$ 是高斯整數（$\alpha,\beta,\gamma$ 都是），而且 $\alpha = \beta\gamma+\rho$ 成立。「代數的部分已經滿足了，現在只要證 $N(\rho)\le\frac12N(\beta)$。」

### 2.4 Step 4：估計 N(ρ)

[▶ 12:53](https://youtu.be/w47fBFeDmyw?t=773)

**Conrad 的做法**：令 $z = \rho$，則 $z\bar\beta = r_1+ir_2$。取範數，用乘性：
$$N(z)\,N(\bar\beta) = N(r_1+ir_2) = r_1^2+r_2^2.$$
而且 $N(\bar\beta) = N(\beta)$（共軛的長度一樣）。所以
$$N(\rho) = \frac{r_1^2+r_2^2}{N(\beta)}.$$

【課堂討論】[▶ 14:30](https://youtu.be/w47fBFeDmyw?t=870) 講者一度想對 $\frac{1}{\bar\beta}$ 直接取範數，說「範數對倒數也有意義」；學生建議上下同乘 $\beta$，把分母變成整數 $N(\beta)$ 再算，結果一樣。

**代入估計** [▶ 17:06](https://youtu.be/w47fBFeDmyw?t=1026)：$|r_1|,|r_2|\le\frac12N(\beta)$，所以 $r_1^2,r_2^2\le\frac14N(\beta)^2$。
$$N(\rho)\le\frac{\frac14N(\beta)^2+\frac14N(\beta)^2}{N(\beta)} = \frac12N(\beta).\ \blacksquare$$

**這跟例子對得上**：第 15 集取 $\gamma$ 的方式（$\alpha/\beta$ 的實部、虛部各取最近的整數），就是這裡對 $m,n$ 做修正版除法——因為 $\frac{m}{N(\beta)}$ 最近的整數就是 $q_1$。

> 【課本補充】§10.2（p. 198）的證明是**幾何的**：$\beta$ 的倍數組成邊長 $|\beta|$ 的正方形格子，任何點到最近格點的距離最多是半條對角線 $|\beta|/\sqrt2$，所以 $N(\rho) = |\rho|^2\le\frac12|\beta|^2$。課本說「代數證明也可以」——本集就是代數證明。兩者的關係：代數證明裡「實部、虛部各差不超過一半」，就是幾何裡「點在正方形內，橫向、縱向離最近格點各不超過半邊」。

---

## 3. 接下來要做什麼

[▶ 17:46](https://youtu.be/w47fBFeDmyw?t=1066)

講者預告：

1. 更多高斯整數除法的例子。
2. 高斯整數的**互質**、**Euclid 演算法**、**gcd**、**Bézout 定理**，「越來越多整除的結果」。
3. 應用到 $4n+1$ 型的質數 [▶ 18:48](https://youtu.be/w47fBFeDmyw?t=1128)：奇質數不是 $4n+1$ 就是 $4n+3$。
   - $4n+1$ 型的質數**能**寫成 $a^2+b^2$。
   - $4n+3$ 型的質數**不能**寫成兩平方和（第 13 集證過）。
   - 講者：「希望我沒記反，我最討厭把定理完全記反了。」（沒記反。）
4. **一個數寫成兩平方和的方法有好幾種** [▶ 19:49](https://youtu.be/w47fBFeDmyw?t=1189)：講者說會學到一種計算技巧，「可以造出一個數，能用 10 種不同方式寫成兩平方和，而且我能控制是哪幾種」。

【課堂討論】[▶ 20:22](https://youtu.be/w47fBFeDmyw?t=1222) 學生問：是普通的自然數嗎？講者：是，用高斯整數來造。他試著舉例 $68 = 8^2+2^2$，但想不出第二種寫法，「我幹嘛自己編，Conrad 有例子」。

> 以下**不是逐字稿內容**，是補一個例子：$68$ 其實只有一種寫法（$68 = 2^2+8^2$）。有兩種寫法的最小例子之一是 $65 = 1^2+8^2 = 4^2+7^2$，而 $65 = 5\cdot 13$ 正是兩個 $4n+1$ 型質數的乘積。第 19–21 集會解釋為什麼。

---

## 4. 一頁速查表

**修正版整數除法**：取離 $m$ 最近的 $N$ 的倍數，$m = Nq+r$，$|r|\le\frac12N$。例：$34 = 9\cdot 4-2$。

**高斯整數除法定理的證明**

1. $\dfrac\alpha\beta = \dfrac{\alpha\bar\beta}{N(\beta)} = \dfrac{m+ni}{N(\beta)}$。
2. 修正版除法：$m = N(\beta)q_1+r_1$，$n = N(\beta)q_2+r_2$，$|r_j|\le\frac12N(\beta)$。
3. $\gamma = q_1+iq_2$，$\rho = \alpha-\beta\gamma = \dfrac{r_1+ir_2}{\bar\beta}$。
4. **關鍵一步**：$N(\rho)N(\beta) = r_1^2+r_2^2\le\frac12N(\beta)^2$，所以 $N(\rho)\le\frac12N(\beta)$。

**幾何版**（課本）：點到正方形格子最近格點的距離 $\le$ 半條對角線 $=|\beta|/\sqrt2$。

---

## 5. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 除法定理 ⇒ Euclid 演算法、gcd、Bézout | 第 17–18 集 |
| 唯一分解、高斯質數 | 第 17–19 集 |
| $4n+1$ 型質數是兩平方和 | 第 19–21 集 |
| 一個數有幾種兩平方和寫法 | 第 19–21 集 |
| 有除法定理的環 = Euclid 整環 ⇒ PID ⇒ UFD | 第 38–39 集 |

---

## 附：本集一句話總結

> **把 $\alpha/\beta$ 寫成 $(m+ni)/N(\beta)$，對 $m,n$ 各做「取最近倍數」的修正版除法，餘數不超過 $N(\beta)$ 的一半；這兩個餘數合成的 $\rho$ 滿足 $N(\rho) = (r_1^2+r_2^2)/N(\beta)\le\frac12N(\beta)$——高斯整數的除法定理就證完了。**

---

*筆記依據 James S. Cook「Number Theory」2021-09-29 第 2 部錄影逐字稿（YouTube 自動字幕，22:07）與 Jones & Jones《Elementary Number Theory》§10.2 整理；證明照 Keith Conrad〈The Gaussian Integers〉。*
