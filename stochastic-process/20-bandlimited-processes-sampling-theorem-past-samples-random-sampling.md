---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 20
lecture: Lec 10-5 Random Walks and Other Applications — Bandlimited Processes and Sampling Theory
date: 待補
video: https://youtu.be/t-Txwz6vj8E
notes: Papoulis & Pillai 4th ed. §10-5 Bandlimited Processes and Sampling Theory（式 (10-187)–(10-216)，pp. 476–483；Theorem 10-8、10-9、10-10、10-11、Example 10-5、Random Sampling）
---

# 第 20 集 · Lec 10-5：帶限過程（可微、變化慢）、隨機取樣定理、只用過去樣本就能預測、Papoulis 取樣展開、隨機取樣 [▶ 影片](https://youtu.be/t-Txwz6vj8E)

← 上一集：[19](19-cyclostationary-processes-time-average-pam.md) ｜ [總目錄](README.md) ｜ 下一集：[21](21-matched-filter-tapped-delay-line-smoothing-poisson-sum.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 20 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（1:11:14，whisper large-v3-turbo）＋ Papoulis §10-5（pp. 476–483）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「bandlimited」→「Band Limited／Bender Limited／Banner Limited／Banelimited／ban limit」，「Paley–Wiener」→「Pettie Weiner／Pelly-Winer」，「wide-sense stationary」→「Widescent Stationary」，「Taylor」→「Tiler／泰勒」，「mean-square differentiable」→「msdifferentiable」，「transfer function」→「transfer function」，「時域」→「tine domain／tidal 面／Title 面」，「頻譜」→「頻補／平譜」，「interpolation」→「interpretation／interpellation」，「sinc」→「sync」，「Fourier series」→「Fourier series／Fullier series」，「Papoulis」→「Propolis／popolis」，「binomial」→「binomial」，「polynomial」→「polynomial」，「regular process」→「regular process」，「Nyquist rate」→「Niquid Rate」，「aliasing」→「aliasing」，「Poisson」→「poison／Portone」，「unbiased estimator」→「unbiased estimator」，「complex conjugate」→「compress／complete conjugate」，「weighting」→「waiting」，「實數」→「時數」，「負數平面」＝「複數平面」。以下一律用正確的字。

> **接上一集**：上一集講循環平穩和時間平均。§10-5 講通訊特別重視的**帶限過程**，以及和它密切相關的**取樣定理**。老師的主軸是一個技巧：**兩個轉移函數相等的濾波器，輸出（均方意義下）一定相等**——取樣定理、只用過去樣本、Papoulis 展開，全部用這個技巧證明。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 帶限過程的定義](#1-帶限過程的定義)
- [2. 帶限過程處處可微、有 Taylor 展開](#2-帶限過程處處可微有-taylor-展開)
  - [2.1 證明 $R$ 任意階可微](#21-證明-r-任意階可微)
  - [2.2 核心技巧：轉移函數相等的濾波器](#22-核心技巧轉移函數相等的濾波器)
- [3. 帶限過程變化很慢](#3-帶限過程變化很慢)
- [4. 隨機取樣定理](#4-隨機取樣定理)
- [5. 只用過去的樣本就能預測（completeness with past samples）](#5-只用過去的樣本就能預測completeness-with-past-samples)
  - [5.1 敘述](#51-敘述)
  - [5.2 證明：二項式濾波器](#52-證明二項式濾波器)
  - [5.3 討論](#53-討論)
- [6. Papoulis 取樣展開](#6-papoulis-取樣展開)
- [7. 非均勻取樣（老師的補充）](#7-非均勻取樣老師的補充)
- [8. 隨機取樣](#8-隨機取樣)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 定義、可微、Taylor | [▶ 00:00](https://youtu.be/t-Txwz6vj8E?t=0) | 式 (10-187)–(10-193)，pp. 476–477 |
| 變化慢 | [▶ 11:49](https://youtu.be/t-Txwz6vj8E?t=709) | 式 (10-194)、(10-195)，pp. 477–478 |
| 隨機取樣定理 | [▶ 18:02](https://youtu.be/t-Txwz6vj8E?t=1082) | Theorem 10-9，式 (10-197)，p. 478 |
| 過去樣本 | [▶ 24:40](https://youtu.be/t-Txwz6vj8E?t=1480) | Example 10-5、Theorem 10-10，pp. 478–480 |
| Papoulis 取樣展開 | [▶ 39:02](https://youtu.be/t-Txwz6vj8E?t=2342) | Theorem 10-11，式 (10-203)–(10-208)，pp. 480–481 |
| 非均勻取樣、隨機取樣 | [▶ 55:51](https://youtu.be/t-Txwz6vj8E?t=3351) | 式 (10-209)–(10-216)，pp. 481–483 |

---

## 1. 帶限過程的定義

[▶ 00:30](https://youtu.be/t-Txwz6vj8E?t=30) 為什麼通訊特別重視帶限？任何通訊傳輸都由政府單位管控、分配頻段（台灣是 NCC）。例：從 1.8 GHz 開始的某一段分配給某家公司經營；FM 廣播分配給中廣 200 kHz。你必須保證訊號在這個頻段裡。【口頭】

> **帶限過程** (bandlimited process，BL)：功率頻譜在 $|\omega|>\sigma$ 時為 0，**而且功率有限**：
> $$\bar S(\omega)=0\ (|\omega|>\sigma),\qquad\bar R(0)<\infty\qquad\text{(10-187)}.$$

- 從**能量**（功率頻譜）上定義。
- 這是數學上的簡化：實作上不可能有任何訊號頻譜在外面是 0，因為一旦是 0 就違反 Paley–Wiener 判準（第 15 集）。
- 頭上一橫：不假設 WSS，用的是**時間平均**功率頻譜。早上可能沒局限在頻段內，但一整天平均要達到。
- **綠框**：多加 $\bar R(0)<\infty$（平均功率有限），這叫 **energy signal**。實作上合理（不可能產生無限大能量的訊號）。一般書上沒寫，但很多定理的證明其實用到了，所以老師特別講清楚。

---

## 2. 帶限過程處處可微、有 Taylor 展開

[▶ 03:37](https://youtu.be/t-Txwz6vj8E?t=217) 從理論角度，為什麼喜歡帶限訊號？**它有 Taylor 展開**，因為它**均方可微**。全部都在均方意義下（能量意義下）——不關心三階、四階，只關心到二階。

### 2.1 證明 $R$ 任意階可微

**Step 1：** 自相關是功率頻譜的反轉換，帶限所以只積 $(-\sigma,\sigma)$：
$$R(\tau)=\frac1{2\pi}\int_{-\sigma}^{\sigma}S(\omega)e^{j\omega\tau}d\omega,\qquad R(0)=\frac1{2\pi}\int_{-\sigma}^{\sigma}S(\omega)\,d\omega<\infty.$$

**Step 2：** 微分 $n$ 次 = 通過 $n$ 次微分器。Theorem 9-4：輸出頻譜 = 輸入頻譜 × $|j\omega|^{2n}=\omega^{2n}$。老師說：Theorem 9-2、9-4、基本定理是系統觀最重要的定理，將來都要變直觀。

**Step 3：** 雖然 $\omega\to\infty$ 時 $\omega^{2n}$ 無限大，但只積 $(-\sigma,\sigma)$，最大是 $\sigma^{2n}$：
$$\frac1{2\pi}\int\omega^{2n}S(\omega)\,d\omega\le\sigma^{2n}\cdot\frac1{2\pi}\int_{-\sigma}^{\sigma}S(\omega)\,d\omega=\sigma^{2n}R(0)<\infty.$$

**Step 4：** 時域可不可以微分，跟頻域乘 $\omega^{2n}$ 的總積分是不是有限有關（第 12 集，特性函數和時域的關係一樣）。所以 $R(\tau)$ 可以微分 $n$ 次，$n$ 任意：均方意義下 $X^{(n)}(t)$ 都存在。

【課本補充】式 (10-190)、(10-191)：$R^{(n)}(\tau)=\frac1{2\pi}\int_{-\sigma}^{\sigma}(j\omega)^nS(\omega)e^{j\omega\tau}d\omega$；所以 BL 過程的自相關是**整函數** (entire function)，任意階導數處處存在。課本也指出：本節所有恆等式都是均方意義。

### 2.2 核心技巧：轉移函數相等的濾波器

[▶ 08:43](https://youtu.be/t-Txwz6vj8E?t=523)

> **Theorem 10-8**：BL 過程 $X(t)$ 分別通過系統 $T_1(\omega)$、$T_2(\omega)$ 得到 $W_1$、$W_2$。若 $T_1(\omega)=T_2(\omega)$（$|\omega|\le\sigma$），則 $W_1(t)=W_2(t)$（均方）。

證明（課本）：$W_1-W_2$ 是 $X$ 通過 $T_1-T_2$ 的輸出，$E|W_1-W_2|^2=\frac1{2\pi}\int_{-\sigma}^{\sigma}S(\omega)|T_1-T_2|^2d\omega=0$。

老師說：這個技巧後面會一直重複用到。**同一個轉移函數用不同方式寫，送同一個隨機過程進去，輸出一定一樣。**

**Taylor 展開**：$e^{j\omega\tau}$ 是確定的函數，一定有 Taylor 展開：
$$\underbrace{e^{j\omega\tau}}_{\text{紅色濾波器}}=\underbrace{\sum_{n=0}^{\infty}\frac{\tau^n}{n!}(j\omega)^n}_{\text{藍色濾波器}}.$$
- 紅色：頻譜上相位旋轉 = 時域平移（golden rule），輸出 $X(t+\tau)$（頻率正，往左平移）。
- 藍色：$(j\omega)^n$ 就是微分 $n$ 次，輸出 $\sum\frac{\tau^n}{n!}X^{(n)}(t)$（均方意義下存在）。

所以
$$X(t+\tau)=\sum_{n=0}^{\infty}X^{(n)}(t)\frac{\tau^n}{n!}\qquad\text{(10-192)}.$$

> **觀念 1**：任何帶限訊號都可微（均方意義），而且有 Taylor 展開。

**直觀**【口頭】：不能微分的訊號，像轉角不平滑（雖然連續）；二次不可微一定有轉角。可微代表很平滑 (smooth)。帶限訊號有各階微分，所以**非常平滑，絕對沒有尖銳的角**，不會瞬間跳躍、瞬間改變方向。

---

## 3. 帶限過程變化很慢

[▶ 12:52](https://youtu.be/t-Txwz6vj8E?t=772) 既然平滑，兩個時間 $t$ 和 $t+\tau$ 之間的改變不會太劇烈：

> $$E|X(t+\tau)-X(t)|^2\le\sigma^2\tau^2R(0)\qquad\text{(10-194)}.$$

**解讀**【口頭】：
- 10 點到 10 點 01 分的改變量，最多是時間差（1 分鐘）的平方乘一個常數。
- 常數是 $\sigma^2R(0)$：**頻寬 $\sigma$ 越窄，改變越小**（非常平滑）；**能量 $R(0)$ 越強，允許的改變越大**。非常合理。
- 這個上界其實很鬆，真正的變化比這還小。
- 老師說：證明定理時數學重要，但更重要的是能產生直覺、能用口語了解結果。例如當評審時，看到有人說「大頻寬的訊號變化量反而小、小頻寬反而大」，直覺就知道不對，一定量錯了或有沒講清楚的機制。
- 課本假設實數過程，其實證明沒用到，複數也對；只要帶限都對。

**證明（濾波器技巧）**：

1. $Y(t)=X(t+\tau)-X(t)$ 是 $X$ 通過線性濾波器 $H(\omega)=e^{j\omega\tau}-1$ 的輸出（相位旋轉 → 平移；減 1 → 乘 1 不變再減掉）。老師說：將來都要這樣想，這是濾波器觀點的非常大的優點。
2. 輸出功率 = 輸出頻譜的總積分 = 輸入頻譜 × $|H|^2$：
$$E|Y|^2=\frac1{2\pi}\int_{-\sigma}^{\sigma}S(\omega)\left|e^{j\omega\tau}-1\right|^2d\omega,\qquad\left|e^{j\omega\tau}-1\right|^2=2(1-\cos\omega\tau)=4\sin^2\frac{\omega\tau}{2}.$$
3. 用 $|\sin\theta|\le|\theta|$：$4\sin^2\frac{\omega\tau}2\le\omega^2\tau^2\le\sigma^2\tau^2$（帶限，$|\omega|\le\sigma$）。
4. $E|Y|^2\le\sigma^2\tau^2R(0)$。 ∎

【課本補充】(10-195)：等價寫法 $2[R(0)-R(\tau)]\le\sigma^2\tau^2R(0)$；課本的推導用 $1-\cos\omega\tau=2\sin^2\frac{\omega\tau}2\le\frac{\omega^2\tau^2}{2}$，得到更緊的 $R(0)-R(\tau)\le\frac{\sigma^2\tau^2}{2}R(0)$。

---

## 4. 隨機取樣定理

[▶ 18:02](https://youtu.be/t-Txwz6vj8E?t=1082) 加一個字叫 **stochastic** sampling theorem：大學部通訊原理講的取樣定理是**確定**訊號；現在是隨機過程，等號是**均方意義**（左右相減絕對值平方的期望值為 0）。

> **隨機取樣定理** (Theorem 10-9)：$X(t)$ 帶限（頻寬 $\sigma$），$T=\frac\pi\sigma$（Nyquist 間隔）。則對每個 $t$、$\tau$：
> $$X(t+\tau)=\sum_{n=-\infty}^{\infty}X(t+nT)\,\frac{\sin\sigma(\tau-nT)}{\sigma(\tau-nT)}\qquad\text{(10-197)}.$$

- 以 $t$ 為基準點，$t+\tau$ 是連續的值；用 $t$ 加一倍、兩倍、三倍 $T$ 的樣本描述 $t+\tau$ 的行為。內插函數是 $\tau$ 的函數。（和數位通訊只看整數點的描述略不同。）
- $T$ 不能亂取，是頻寬的倒數乘 $\pi$（用 $\omega$ 不是 $f$，所以多一個 $\pi$）。

**證明（兩個濾波器）**：

1. **左邊**：濾波器 $e^{j\omega\tau}$，輸出 $X(t+\tau)$。
2. **右邊**：把 $e^{j\omega\tau}$（看成 $\omega$ 的函數，$\tau$ 是參數）在 $(-\sigma,\sigma)$ 上展開成**傅立葉級數**：
$$e^{j\omega\tau}=\sum_na_ne^{jnT\omega},\qquad a_n=\frac1{2\sigma}\int_{-\sigma}^{\sigma}e^{j\omega\tau}e^{-jnT\omega}d\omega=\frac{\sin\sigma(\tau-nT)}{\sigma(\tau-nT)}\quad(|\omega|\le\sigma).$$
   每一項 $e^{jnT\omega}$ 是平移 $nT$，輸出 $X(t+nT)$；係數 $a_n$ 就是 sinc 內插函數。
3. 兩個轉移函數在 $|\omega|\le\sigma$ 完全相等（外面不在乎，因為頻譜是 0），由 Theorem 10-8，輸出相等。 ∎

老師說：用這個觀點，取樣定理的證明兩三行就結束了。（傅立葉級數的週期：課本系統把頻率限制在 $(-\sigma,\sigma)$，取樣間隔 $T=\pi/\sigma$；數位通訊時是 $(-\pi,\pi)$、間隔 1，這裡只是延伸。）

---

## 5. 只用過去的樣本就能預測（completeness with past samples）

[▶ 24:40](https://youtu.be/t-Txwz6vj8E?t=1480) 對隨機過程來說很重要的觀點（確定訊號沒有這個結果）。

**確定訊號的取樣定理**：中間的值可以插掉，只要白色的樣本點，用內插就能毫無誤差地重建。但要重建某一點，需要**過去所有**和**未來所有**的樣本——無限多個（可數）。觀念很棒，實作上不可能：未來還沒發生；過去也是無限多個。

**隨機過程不一樣**：**只要過去的樣本就夠精準，完全不需要知道未來**。理論依據：想知道某一點，只要把過去的樣本累積下來，未來的完全不用知道。對實作是很好的定理。

### 5.1 敘述

> **定理**：$X(t)$ 帶限（頻寬 $\sigma$），取樣間隔 $T_0=\frac{T}{3}=\frac{\pi}{3\sigma}$（比需要的密 3 倍）。給任何 $\varepsilon>0$，存在 $n$ 和係數 $a_1,\dots,a_n$，使
> $$E\left|X(t)-\sum_{k=1}^{n}a_kX(t-kT_0)\right|^2<\varepsilon.$$

- 只用**過去**的 $n$ 個樣本（$k=1,\dots,n$），而且是**有限**個，就能讓誤差小於你要的範圍。
- 為什麼密 3 倍？為了讓證明簡單。老師說實際上不需要：有別的、比較複雜的證明，第二個條件可以拿掉（課本 Theorem 10-10：任何 $T_0<T$ 都可以）。
- 老師的應用聯想【口頭】：machine learning／deep learning 就是在精煉 learning 的技巧——拿到大量數據，快速抽取資訊做 learning。這個定理是最基礎的理論依據：對帶限訊號，用過去學到的足夠樣本，可以精準預測未來，只要時間平均功率頻譜存在。如果這個不對，做 learning 就沒有用了，你一定要得到未來的樣本才能預測。

### 5.2 證明：二項式濾波器

[▶ 29:46](https://youtu.be/t-Txwz6vj8E?t=1786)

**Step 1：誤差是濾波器的輸出。** 令 $\hat X(t)=\sum_ka_kX(t-kT_0)$，誤差
$$Y(t)=X(t)-\hat X(t)$$
是 $X$ 通過 $H(\omega)=1-\sum_{k=1}^na_ke^{-jk\omega T_0}$ 的輸出（減延遲 = 對負角度旋轉）。老師說他很喜歡這個觀點，因為給直觀、不用手算。只要找到係數就好；怎麼找，會影響將來設計有限階 (finite order) 濾波器的直觀。

**Step 2：誤差功率。** 誤差能任意小，是在功率上：
$$E|Y|^2=\frac1{2\pi}\int_{-\sigma}^{\sigma}S(\omega)|H(\omega)|^2d\omega.$$
帶限是重點：外面是 0，濾波器在 $|\omega|>\sigma$ 長什麼樣不用管，**只要在 $|\omega|\le\sigma$ 讓 $|H|^2$ 很小**，例如 $|H|^2\le\frac{\varepsilon}{R(0)}$，則
$$E|Y|^2\le\frac{\varepsilon}{R(0)}\cdot\frac{1}{2\pi}\int S=\varepsilon.$$
（頻譜有值的地方濾波器好小好小，外面不管。）

**Step 3：選二項式濾波器** (binomial filter)。老師說任何多項式都可以設計（$z=e^{-j\omega T_0}$ 的 $n$ 次多項式），他有一年考試就考用不同的設計：
$$H(\omega)=\left(1-e^{-j\omega T_0}\right)^n=\sum_{k=0}^{n}(-1)^k\binom nke^{-jk\omega T_0}.$$
（$k=0$ 項是 1，所以 $a_k=-(-1)^k\binom nk$。）

**Step 4：驗證夠小。** $|1-e^{-j\omega T_0}|=2\left|\sin\frac{\omega T_0}{2}\right|$，所以
$$|H(\omega)|^2=\left(2\sin\frac{\omega T_0}{2}\right)^{2n}.$$
$|\omega|<\sigma$ 時 $\frac{|\omega|T_0}{2}<\frac{\sigma}{2}\cdot\frac{\pi}{3\sigma}=\frac\pi6$，$\sin\frac\pi6=\frac12$，所以 $2\left|\sin\frac{\omega T_0}2\right|<1$。小於 1 的數的 $2n$ 次方，$n\to\infty$ 時趨於 0。要多小就多小，只要 $n$ 夠大；而且知道 $n$ 要多大。 ∎

老師說：證明有觀念的好處是不用記 step by step，記觀念：誤差是濾波器的輸出、線性設計、找一個對的多項式；用到的真正性質就是帶限（只看那個頻帶）。

【課本補充】Example 10-5（p. 479）就是這個證明：$\hat X(t)=nX(t-T_0)-\binom n2X(t-2T_0)+\cdots$，$E\{y^2\}=\frac1{2\pi}\int_{-\sigma}^{\sigma}S(\omega)\left(2\sin\frac{\omega T_0}2\right)^{2n}d\omega$（10-200）；只在 $T_0<T/3$ 時成立；而且係數 $\binom nk\to\infty$。Theorem 10-10（任意 $T_0<T$）的證明要用 Weierstrass 逼近定理和 Fejér–Riesz 分解定理，細節不簡單。

### 5.3 討論

[▶ 36:29](https://youtu.be/t-Txwz6vj8E?t=2189)

**能不能讓誤差等於 0？** 直觀上不可能：
- 要讓濾波器在某個區間**完全等於 0**，會違反 Paley–Wiener 判準。（Paley–Wiener 是充分條件，不能反推；但觀念上它有一點「必要」的味道。）
- 設計一個在某地方完全是 0 的濾波器也很不合理，只能讓它無限小。
- 第 11 章會講 **regular process**（regular 就是經常的、平常碰得到的，像指導教授的 regular meeting）：真正做得出來的過程，功率頻譜可以拆成兩項的平方。我們看到的任何隨機過程，都有一個起始點經過一個濾波器才看到，所以不會有誤差為 0 的結果。

【課本補充】p. 480：係數 $a_k$ 在 $\varepsilon\to0$ 時趨於無限大，因為找不到指數和 $P(\omega)$ 使 $|1-P(\omega)|=0$ 在整個區間成立，否則違反 Paley–Wiener 條件 (9-203)。

**取樣間隔**：理論上 $T_0$ 只要比 $\pi/\sigma$ 稍微小一點就可以，但濾波器就不是二項式了，要選別的形式（不唯一）。最好降到 $\pi/\sigma$，應該不能再改善——老師說目前沒有人能完整證明：頻寬 $\sigma$ 時，取樣比 Nyquist 慢到底夠不夠，除非有額外條件。

---

## 6. Papoulis 取樣展開

[▶ 39:02](https://youtu.be/t-Txwz6vj8E?t=2342) Papoulis 提供另一個可能性：**取樣可以更慢**——每 $N$ 個週期才取一次，但每次用 $N$ 個不同的方式（$N$ 個濾波器）取 $N$ 個值。**總數一樣**，只是可以在同一個時間取。

老師的比喻：過去每個時間點取一個；現在 $N=2$ 時跳著取，但同一點用兩個方式得到兩個值（$y_1,y_2$）。就像「每七天讀七個小時，不要每天讀一個小時」（但人還是會累）。也提供一個想法：同一點用不同方法觀察多次，但隔久一點再觀察，結果一樣。老師說：研究其實沒有限制，但證完要詮釋它在操作上有沒有意義 (operational meaning)，這比較重要。

> **Papoulis 取樣展開** (Theorem 10-11)：$X(t)$ 帶限（頻寬 $\sigma$），通過 $N$ 個線性系統 $H_1(\omega),\dots,H_N(\omega)$ 得到 $Y_1,\dots,Y_N$。令
> $$c=\frac{2\sigma}{N},\qquad\bar T=\frac{2\pi}{c}=NT.$$
> 若 $P_k(\omega,\tau)$ 是下列多元一次聯立方程式的解（$\omega\in(-\sigma,-\sigma+c)$）：
> $$H_1(\omega+mc)P_1(\omega,\tau)+\cdots+H_N(\omega+mc)P_N(\omega,\tau)=e^{jmc\tau},\quad m=0,1,\dots,N-1,$$
> 令 $p_k(\tau)=\frac1c\int_{-\sigma}^{-\sigma+c}P_k(\omega,\tau)e^{j\omega\tau}d\omega$，則
> $$X(t+\tau)=\sum_{n=-\infty}^{\infty}\left[Y_1(t+n\bar T)p_1(\tau-n\bar T)+\cdots+Y_N(t+n\bar T)p_N(\tau-n\bar T)\right].$$

- 把頻寬 $2\sigma$ 切成 $N$ 塊（$c=2\sigma/N$，$N=2,3,4$），每塊頻寬變小，需要的取樣間隔就變大 $\bar T=NT$——可以一陣子不做事，一次做很多。
- 內插函數不再是 sinc，要另外取。
- 前面用二項式；Papoulis 比較聰明，取一組聯立方程式：先選 $H$，再解 $P$。行列式不為 0 就一定有解（可能用 MATLAB 解）。解出來可能沒有乾淨的 closed form，但一定存在，照畫就是。
- 只要在一個寬度 $c$ 的區間 $(-\sigma,-\sigma+c)$ 解，其他是平移（右邊的式子是週期的）。

**記號的提醒** [▶ 45:37](https://youtu.be/t-Txwz6vj8E?t=2737)：傅立葉級數的時域變數是 $n$（離散），頻譜是 $\omega$；$k$ 和 $\tau$ 都只是參數（第 $k$ 組、以 $\tau$ 為基準）。課本寫的時候把 $n$ 代 0 寫得很快，你可能要花點時間想；老師在投影片右邊紅字補了原來的公式。

**證明**：同一個觀點——兩個濾波器。
- 左邊：$e^{j\omega\tau}$，輸出 $X(t+\tau)$。
- 右邊：$Y_k(t+n\bar T)$ 是 $X$ 通過 $H_k(\omega)e^{jn\bar T\omega}$ 的輸出，所以右邊是 $X$ 通過 $\sum_kH_k(\omega)\sum_np_k(\tau-n\bar T)e^{jn\bar T\omega}$。
- 由傅立葉級數，$\sum_np_k(\tau-n\bar T)e^{jn\bar T\omega}=P_k(\omega,\tau)e^{j\omega\tau}$；把頻帶切成 $N$ 塊（$\omega=\theta+mc$），每一塊代入，用 $e^{jn\bar T\cdot mc}=1$（整數倍的 $2\pi$），就變成聯立方程式的第 $m$ 式乘 $e^{j\omega\tau}$，等於 $e^{j\omega\tau}$。
- 兩個轉移函數在 $|\omega|\le\sigma$ 相等，輸出相等。 ∎

老師說這是很巧妙的定理，一個新的觀點。

**討論**：
- $N=1$：回到原來的取樣定理。
- $N>1$：**總數沒有減少**。到目前為止的定理，總數都沒有減少——Nyquist rate 好像是一個基本門檻，減少就沒辦法精確恢復。

---

## 7. 非均勻取樣（老師的補充）

[▶ 55:51](https://youtu.be/t-Txwz6vj8E?t=3351)【口頭】

- 取樣定理還有很多變化版本。這裡都是**均勻取樣** (uniform sampling)：按一定週期取樣，實作容易（機械性的動作）。
- 也有人做**非均勻** (non-uniform) 取樣：總數一樣，中間可以挪動，在某些方面有好的效果。
- 取樣定理不只用在通訊訊號。例：**網路管理**（老師做過一陣子）——偵測網路是不是壅塞、要不要即時處置。最簡單：每 10 秒取樣一次網路流量。有人說：每 20 秒取兩次、每 30 秒取三次，但不一定切在中間；曾經有人用**黃金分割**取樣，有好處（黃金分割有數學上的意義）。每分鐘取樣 6 次，怎麼分布可以設計，會有額外好處，但系統比較複雜。
- 網路管理、控制、sensing 監控都可以動態調整，不用永遠 10 秒一次。

---

## 8. 隨機取樣

[▶ 59:23](https://youtu.be/t-Txwz6vj8E?t=3563) 每分鐘只要 6 個樣本，怎麼取？一種是固定的（例如黃金分割，週期性地有密有疏）；另一種是**隨機**的：每分鐘隨機產生 6 個時間（例如 6、8、20、32、54 秒），下一分鐘再丟一次骰子。有沒有理論上的好處？

**背景**：等距取樣 $nT$，頻譜會重複（週期化），產生 **aliasing error**。

**隨機取樣**：取樣時間 $\mathbf{t}_i$ 是平均密度 $\lambda$ 的 **Poisson 點**（粗體，表示隨機）。對確定的訊號 $f(t)$，估計它的傅立葉轉換 $F(\omega)$：
$$\mathbf{P}(\omega)=\frac1\lambda\sum_if(\mathbf{t}_i)e^{-j\omega\mathbf{t}_i}\qquad\text{(10-210)}.$$

> **結論**：$\mathbf{P}(\omega)$ 是 $F(\omega)$ 的**不偏估計** (unbiased estimate)，而且
> $$E\{\mathbf{P}(\omega)\}=F(\omega),\qquad\text{Var}\{\mathbf{P}(\omega)\}=\frac{E}{\lambda},\quad E=\int f^2(t)\,dt\qquad\text{(10-211)}.$$
> 所以 $\lambda\to\infty$（取樣越密）時估計越來越準，變異數以 $\frac1\lambda$ 趨於 0。

**證明（很乾淨，一頁）**：

**Step 1：取樣 = 乘一串脈衝。** 令 Poisson 脈衝串 $Z(t)=\sum_i\delta(t-\mathbf{t}_i)$，則
$$\mathbf{P}(\omega)=\frac1\lambda\int f(t)Z(t)e^{-j\omega t}dt.$$

**Step 2：平均。** $Z$ 是 Poisson 計數過程的**微分**（第 11 集）。由基本定理，輸出平均 = 輸入平均的微分：$E[Z]=\frac{d}{dt}(\lambda t)=\lambda$。所以
$$E\{\mathbf{P}(\omega)\}=\frac1\lambda\int f(t)\lambda e^{-j\omega t}dt=F(\omega).$$

**Step 3：變異數。** 不偏估計時，變異數 = 二階動差 − 真值的平方（detection／estimation 會教：$E|\hat\theta-\theta|^2=E|\hat\theta|^2-|\theta|^2$）。所以只要算 $E|\mathbf{P}|^2$：
$$E|\mathbf{P}(\omega)|^2=\frac1{\lambda^2}\iint f(t_1)f(t_2)R_{ZZ}(t_1,t_2)e^{-j\omega(t_1-t_2)}dt_1dt_2.$$
（$Z$ 是實數，共軛拿掉時指數的正負號要對應調整。）

**Step 4：$R_{ZZ}$。** 微分器輸入輸出的自相關關係是微分兩次；Poisson 計數的 $R=\lambda\min(t_1,t_2)+\lambda^2t_1t_2$，微分兩次：
$$R_{ZZ}(t_1,t_2)=\lambda^2+\lambda\,\delta(t_1-t_2).$$

**Step 5：** 代入：$\lambda^2$ 那項得 $\lambda^2|F(\omega)|^2$；$\lambda\delta$ 那項得 $\lambda\int f^2$。除以 $\lambda^2$ 再減 $|F|^2$：
$$\text{Var}\{\mathbf{P}(\omega)\}=\frac1\lambda\int f^2(t)\,dt=\frac E\lambda\to0.$$ ∎

**意義**【口頭】：
- 不需要均勻，只要（平均上）相當於均勻分布就可以；$\lambda$ 是單位時間取樣幾次。只要把握重點——平均每分鐘 6 個樣本就夠了——不用掌控精準的位置。
- 為什麼非均勻有好處？如果訊號本身在機率上不均勻、不集中：機率堆積的部分要多取樣，機率少的部分少取樣。例如發現有異常時多取樣，沒有異常時少取樣。
- **重要**：整個證明**沒有用到帶限**！隨機取樣可能突破這個限制，只要取樣越來越密就有 guideline。和均勻取樣在操作上是完全不一樣的想法。

⚠️ 待確認：老師口述時用 $X$ 和 $X(\omega)$（像是把訊號當隨機過程），課本 (10-209)–(10-211) 的 $f(t)$ 是**確定**訊號，隨機性只來自 Poisson 取樣時間；筆記照課本寫。

【課本補充】(10-215)：要估計得好，需要 $|F(\omega)|\gg\sqrt{E/\lambda}$。Example 10-6：$f(t)$ 是 $(-a,a)$ 內的正弦和 $\sum c_ke^{j\omega_kt}$，$F(\omega_k)\approx2ac_k$，$E\approx2a\sum|c_k|^2$；只要 $\sum|c_i|^2\ll2a\lambda|c_k|^2$，$\mathbf{P}(\omega_k)\approx F(\omega_k)$。**用隨機取樣，即使平均速率 $\lambda$ 很小，只要觀察區間 $2a$ 夠長，就能偵測任何頻率的譜線**。

---

## 9. 一頁速查表

### 帶限過程（$S=0$ 於 $|\omega|>\sigma$，$R(0)<\infty$）

- 任意階均方可微：$\frac1{2\pi}\int\omega^{2n}S\le\sigma^{2n}R(0)$。
- Taylor：$X(t+\tau)=\sum X^{(n)}(t)\frac{\tau^n}{n!}$（$e^{j\omega\tau}=\sum\frac{(j\omega\tau)^n}{n!}$）。
- 變化慢：$E|X(t+\tau)-X(t)|^2\le\sigma^2\tau^2R(0)$（$|e^{j\omega\tau}-1|^2=4\sin^2\frac{\omega\tau}2\le\omega^2\tau^2$）。
- **核心技巧**：$T_1=T_2$（$|\omega|\le\sigma$）⇒ 輸出均方相等。

### 取樣

| 定理 | 公式 | 關鍵 |
|---|---|---|
| 隨機取樣定理 | $X(t+\tau)=\sum X(t+nT)\frac{\sin\sigma(\tau-nT)}{\sigma(\tau-nT)}$，$T=\frac\pi\sigma$ | $e^{j\omega\tau}$ 在 $(-\sigma,\sigma)$ 的傅立葉級數 |
| 過去樣本 | $E\lvert X(t)-\sum_{k=1}^na_kX(t-kT_0)\rvert^2<\varepsilon$ | $H=(1-e^{-j\omega T_0})^n$，$\lvert H\rvert^2=(2\sin\frac{\omega T_0}2)^{2n}$，$T_0=\frac{\pi}{3\sigma}$ 時 $<1$ |
| Papoulis 展開 | $N$ 個濾波器、間隔 $\bar T=NT$ | 解聯立方程式求 $P_k$；總樣本數不變 |
| 隨機取樣 | $\mathbf{P}(\omega)=\frac1\lambda\sum f(\mathbf{t}_i)e^{-j\omega\mathbf{t}_i}$ | 不偏；$\text{Var}=E/\lambda$；$R_{ZZ}=\lambda^2+\lambda\delta$；不需帶限 |

- 誤差不能為 0（Paley–Wiener）；係數 $a_k\to\infty$。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Poisson 求和公式（aliasing 的根源） | 下一集：附錄 10A |
| 雜訊中的確定訊號 | 下一集：§10-6 matched filter |
| regular process、Paley–Wiener、頻譜分解 | §11-1（第 22 集） |
| 用過去樣本預測 | §13-2 預測（第 39–40 集） |

---

## 附：本集一句話總結

> **帶限過程非常平滑（任意階均方可微、有 Taylor 展開、$E|X(t+\tau)-X(t)|^2\le\sigma^2\tau^2R(0)$）；只要兩個濾波器在頻帶內轉移函數相等，輸出就均方相等——用這一招可以證明隨機取樣定理、證明只用有限個過去樣本就能任意精準地預測（二項式濾波器），以及 Papoulis 的 $N$ 通道取樣展開；而 Poisson 隨機取樣甚至不需要帶限，就能不偏地估計頻譜，變異數 $E/\lambda$。**

---

## ⚠️ 待確認清單

1. [▶ 59:53](https://youtu.be/t-Txwz6vj8E?t=3593) 隨機取樣：老師口述用 $X$（像隨機過程），課本是確定訊號 $f(t)$；筆記照課本。
2. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 10-5 錄影逐字稿（whisper large-v3-turbo，1:11:14）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
