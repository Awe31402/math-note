---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 22
lecture: Lec 11-1 Spectral Representation — Factorization and Innovations
date: 待補
video: https://youtu.be/OMs-MoVs2Kk
notes: Papoulis & Pillai 4th ed. §11-1 Factorization and Innovations（式 (11-1)–(11-9)，pp. 499–502；Example 11-1–11-4）；§9-4 式 (9-203)–(9-207)，pp. 423–424
---

# 第 22 集 · Lec 11-1：頻譜分解與創新過程——最小相位系統、regular process、有理頻譜的分解步驟、最小相位 = 最小群延遲 [▶ 影片](https://youtu.be/OMs-MoVs2Kk)

← 上一集：[21](21-matched-filter-tapped-delay-line-smoothing-poisson-sum.md) ｜ [總目錄](README.md) ｜ 下一集：[23](23-state-variables-finite-order-processes-continuous.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 22 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（1:16:16，whisper large-v3-turbo）＋ Papoulis §11-1（pp. 499–502）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「因式分解」→「音式分解」，「factor」→「Factor」，「innovation」→「Innovation」，「minimum phase」→「minimum phase／meanum phase／minum phase」，「pole」→「por／Pore／paw」，「zero」→「0／Gio」，「BIBO」→「BIBO」，「causal」→「cozzo／cordal」，「stable」→「stable」，「analytic」→「Analytic」，「Paley–Wiener」→「Pettie Weiner／Pelly-Weiner／Payley-Winer／Panel Vinal」，「bandlimited」→「Banded Limited」，「rational spectrum」→「rational spectrum」，「regular」→「Regular」，「whitening filter」→「Whitening／whightening filter」，「approximation」→「Approsmation」，「Kronecker delta」→「Chroniker Delta」，「unit circle」→「unicircle」，「group delay」→「group delay」，「arctangent」→「arctensin」，「magnitude response」→「magnitude／medicative／megic response」，「無理數」→「五里數」，「共軛」→「共二」，「左／右半平面」→「左半邊／右半邊」，「exponential」→「exponential」，「Cover」→「Cover」，「discrete」→「discreet」。以下一律用正確的字。

> **接上一集**：第 9 章有最重要的系統觀定理（基本定理、Theorem 9-2、9-4），第 10 章討論各種訊號。第 11 章 **Spectral Representation**（頻譜表示）討論頻譜本身的性質。§11-1 直接切到比較進階的重點：**factorization**（頻譜的因式分解）和 **innovation**（創新過程）。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 動機：我們看到的過程都是白雜訊經過濾波器](#1-動機我們看到的過程都是白雜訊經過濾波器)
- [2. 定義：最小相位系統、stable、causal、regular](#2-定義最小相位系統stablecausalregular)
- [3. 名詞：innovation、innovation filter、whitening filter](#3-名詞innovationinnovation-filterwhitening-filter)
- [4. Paley–Wiener 條件](#4-paleywiener-條件)
- [5. 有理頻譜的分解（連續時間）](#5-有理頻譜的分解連續時間)
  - [5.1 系統化步驟](#51-系統化步驟)
  - [5.2 例子](#52-例子)
  - [5.3 驗證因果、穩定：時域脈衝響應](#53-驗證因果穩定時域脈衝響應)
  - [5.4 Whitening filter 是不是 stable？（微分器的爭議）](#54-whitening-filter-是不是-stable微分器的爭議)
- [6. 離散時間](#6-離散時間)
  - [6.1 定義與 Paley–Wiener](#61-定義與-paleywiener)
  - [6.2 證明：可積時兩種 Paley–Wiener 等價](#62-證明可積時兩種-paleywiener-等價)
  - [6.3 有理頻譜的分解與例子](#63-有理頻譜的分解與例子)
- [7. 為什麼叫最小相位：最小群延遲](#7-為什麼叫最小相位最小群延遲)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 動機、定義 | [▶ 00:00](https://youtu.be/OMs-MoVs2Kk?t=0) | §11-1 開頭，式 (11-1)–(11-3)，p. 499 |
| Paley–Wiener | [▶ 16:01](https://youtu.be/OMs-MoVs2Kk?t=961) | 式 (11-4)，p. 500 |
| 有理頻譜分解、例子 | [▶ 20:07](https://youtu.be/OMs-MoVs2Kk?t=1207) | 式 (11-5)、Example 11-1–11-3，pp. 500–501 |
| 離散時間 | [▶ 41:42](https://youtu.be/OMs-MoVs2Kk?t=2502) | 式 (11-6)–(11-9)、Example 11-4，pp. 501–502 |
| 最小相位 = 最小延遲 | [▶ 64:16](https://youtu.be/OMs-MoVs2Kk?t=3856) | 無（老師的證明） |

---

## 1. 動機：我們看到的過程都是白雜訊經過濾波器

[▶ 01:01](https://youtu.be/OMs-MoVs2Kk?t=61)

- **Factorization**（因式分解）：國中學過，例如 $24=3\times8$，3 和 8 是 factor。這裡要對**頻譜**做因式分解。
- **Innovation**：一個起始的觸發點。系統的輸入會給一個 innovation。

> **一句話的動機**：給一個 WSS 過程 $X(t)$，希望把它表示成**最小相位系統** $L(\omega)$ 的輸出，輸入是**白雜訊**。

**為什麼**【口頭】：
- 觀察任何系統時，你看到的隨機過程都是透過某種濾波器 $L$ 被你觀察到的（你設計的、或它本來就經過的）；最原始的起始點是**白雜訊**。
- 假設濾波器是線性的：輸出頻譜 = 輸入頻譜 × $|L|^2$。輸入是單位強度的白雜訊（頻譜高度 1），所以
$$S_{XX}(\omega)=|L(\omega)|^2.$$
- 自然觀察到的過程，頻譜都是**某個量的平方**。所以要做因式分解：16 是 $4\times4$、4 是 $2\times2$，這是看得到的；3 寫成 $\sqrt3\times\sqrt3$，如果只允許整數（像國中的因式分解）就不行。所以要探討：**怎麼把頻譜分解成某個東西的絕對值平方**。

**最小相位**的直觀【口頭】：希望濾波器從輸入到輸出的延遲越短越好。自然界的東西都用最省力的方式（水往低處流，走最短路徑）。訊號流過時走延遲最小的路徑。所以最小相位真正的物理意義是**最小延遲**（minimum group delay）；叫「相位」是因為延遲由相位決定（第 7 節證明）。

例：聲音的模型（做語音的人）：聲帶當作白雜訊，經過口腔的形狀（濾波器），輸出就是聲音。所有口腔發出的聲音都是 regular process。

---

## 2. 定義：最小相位系統、stable、causal、regular

[▶ 05:36](https://youtu.be/OMs-MoVs2Kk?t=336)

> **最小相位系統** (minimum-phase system)：系統 $L$ **和它的倒數 $1/L$** 都是**因果** (causal) 而且**穩定** (stable) 的。

- **因果**：現在的輸出只跟現在和過去的輸入有關，不跟未來有關。實際的濾波器都是因果的，非因果的做不出來。
- **穩定**（BIBO 意義，bounded input, bounded output）：輸入有界，輸出一定有界。物理上：輸入能量有限，輸出不可能無限——不然就沒有能源問題了。老師說大家不見得修過控制，所以還是給定義。
- **穩定的數學條件**：所有的 **pole**（極點）都在複數平面的**左半邊**。
  - 例：$\frac{s+1}{(s-2)(s+3)}$。$s=2$ 時衝到無限大，像一根杆子 (pole) 翹起來；$s=-3$ 也是 pole。$s=-1$ 代進去等於 0，叫 **zero**（零點）。名詞是象形的。

> **Regular process**：最小相位系統 $L$ 以白雜訊 $I(t)$ 為輸入時的輸出。數學上：功率頻譜可以分解成
> $$S(\omega)=|L(\omega)|^2,$$
> 而且 $L(s)$（$s=j\omega$）在**右半平面** analytic。

- **regular** 就是經常的（像和學生的 regular meeting，每週固定見面）。regular process 是**正常狀況下觀察得到的**（用濾波器觀察到的輸出）；觀察不到的叫 irregular。
- **analytic**（可分析的）：數學上兩種情況比較難分析——衝到無限大（無限大是概念，不能分析），或有不定值 (indeterminate)。0 的倒數也可能衝到無限大。所以 $L$ 和 $1/L$ 都要 analytic，**pole 和 zero 都不能在右半平面**。

【課本補充】Papoulis p. 499：最小相位的意義——$L(s)$ 因果、脈衝響應 $l(t)$ 能量有限；$\Gamma(s)=1/L(s)$ 因果、脈衝響應 $\gamma(t)$ 能量有限。等價地，$L(s)$ 和 $1/L(s)$ 在右半平面 $\text{Re}\,s>0$ analytic。regular process 和白雜訊**線性等價**：
$$I(t)=\int_0^\infty\gamma(\alpha)X(t-\alpha)d\alpha,\qquad X(t)=\int_0^\infty l(\alpha)I(t-\alpha)d\alpha,\qquad E\{X^2\}=\int_0^\infty l^2(t)dt<\infty\qquad\text{(11-1), (11-2)}.$$
$$S(s)=L(s)L(-s),\qquad S(\omega)=|L(j\omega)|^2\qquad\text{(11-3)}.$$

**最小相位的意義（預告）**：對所有因果、穩定、**magnitude response**（$|H(\omega)|$）相同的濾波器，最小相位系統的延遲最小。例：輸入 $x(t)$ 輸出 $x(t-2)$ 是延遲 2，頻譜上就是 $e^{-j2\omega}$。老師說：設計濾波器的人最喜歡最小群延遲——輸入到輸出本來 10 ns，能設計成 8 ns、功能完全一樣，反應比較快，當然比較好。

---

## 3. 名詞：innovation、innovation filter、whitening filter

[▶ 13:54](https://youtu.be/OMs-MoVs2Kk?t=834)

- 輸入白雜訊 $I$：$R_{II}(\tau)=\delta(\tau)$，$S_{II}=1$。
- 輸出：$S_{XX}(\omega)=|L(\omega)|^2$，時域 $X=l*I$。
- 能做出來的功率頻譜：**實數**（沒有虛數的能量）、**正的**、**偶函數**（左右對稱；不對稱表示時域是複數）、**面積有限**（不能做能量無限的訊號）。

| 名詞 | 是什麼 |
|---|---|
| **innovation**（創新過程） | 輸入 $I$——輸出 $X$ 最早的源頭、最早的發想 |
| **innovation filter** | $L(\omega)$：讓輸入變成輸出 |
| **whitening filter**（白化濾波器） | $1/L(\omega)$：把 $X$ 通過它就回到白雜訊 |

---

## 4. Paley–Wiener 條件

[▶ 16:01](https://youtu.be/OMs-MoVs2Kk?t=961)

> **Paley–Wiener 條件**（連續時間）：
> $$\int_{-\infty}^{\infty}\frac{|\log S(\omega)|}{1+\omega^2}\,d\omega<\infty\qquad\text{(11-4)}.$$
> 滿足它，$S(\omega)$ 就能分解成 $|L|^2$（$L$ 最小相位）。

- 以前（第 15 集）的物理意義：頻譜都是正的、**沒有一整段區域是 0**；有一段是 0，條件就 fail。
- 老師比較兩者：因為 $\frac{1}{1+\omega^2}\le1$，所以 $\int\frac{|\log S|}{1+\omega^2}\le\int|\log S|$——後者有限則前者一定有限，反之不一定。
- 但 Paley–Wiener 只是**充分條件**，不是 if and only if，所以不能下太強的結論。

⚠️ 待確認：老師口述說這個條件「比較強」，但依上面的不等式，加權後的條件反而是比較容易滿足（被未加權的推出）；老師的原意待確認。

**例：帶限過程** [▶ 18:35](https://youtu.be/OMs-MoVs2Kk?t=1115)：頻譜在外面是 0，$\log0=-\infty$，**絕對違反** Paley–Wiener。那為什麼討論這麼多帶限過程？因為那是近似，方便設計；實際上任何帶限過程都做不出來。（Paley–Wiener 只是充分條件，不能用它**證明**帶限過程不是 regular，但心中大概很清楚做不出來。）

【課本補充】p. 500：頻譜由譜線組成（或帶限）時不滿足 (11-4)，這種過程是**可預測的** (predictable)；一般來說分解 $S(\omega)$ 不簡單，下面討論重要特例。

---

## 5. 有理頻譜的分解（連續時間）

[▶ 20:07](https://youtu.be/OMs-MoVs2Kk?t=1207) 研究題目：給一個想要的功率頻譜 $S_{XX}(\omega)$，設計一個濾波器（實作做得出來：穩定、因果）產生它，就是把它分解成 $|L|^2$。

非線性系統沒有「輸出頻譜 = 輸入頻譜 × $|H|^2$」的性質，所以只討論線性系統。一般情況很難，**系統化步驟只對有理頻譜有效**（呼應上一集：把要估計的訊號用多項式逼近）。

> **有理頻譜** (rational spectrum)：兩個多項式的比，而且是 $\omega^2$ 的函數（偶函數，只有偶次項）：
> $$S(\omega)=\frac{A(\omega^2)}{B(\omega^2)}\qquad\text{(11-5)}.$$

### 5.1 系統化步驟

[▶ 22:11](https://youtu.be/OMs-MoVs2Kk?t=1331)

**Step 1：換到 $s$ 平面。** $s=j\omega$，$s^2=-\omega^2$：
$$S(s)=\frac{A(-s^2)}{B(-s^2)}.$$

**Step 2：找根**（因式分解就是找根；分子的根是 zero、分母的根是 pole）。兩個觀察：
1. $S$ 是 $s^2$ 的函數（左右對稱），所以 **$s_i$ 是根 ⇒ $-s_i$ 也是根**。
2. 實係數多項式，根是實數或**共軛複數**：$3+2j$ 是根 ⇒ $3-2j$ 也是根。

所以「舉一反三」：例如 $1+j$ 是根，則 $-1-j$、$1-j$、$-1+j$ 都是根。**根對虛軸對稱**。

**Step 3：分兩組。** 根分成**左半平面** ($\text{Re}\,s_i<0$) 和**右半平面** ($\text{Re}\,s_i>0$) 兩組，完全對稱、個數相等（虛軸上的根一定是重根，各分一個）。右半平面不能有不可分析的點，所以取左邊那組：
$$S(s)=\frac{N(s)N(-s)}{D(s)D(-s)},\qquad L(s)=\frac{N(s)}{D(s)}\quad\text{（只用左半平面的根）},\qquad L^2(0)=S(0).$$

### 5.2 例子

**Example 11-1** [▶ 26:45](https://youtu.be/OMs-MoVs2Kk?t=1605)：$S(\omega)=\frac{N}{\alpha^2+\omega^2}$。
$$S(s)=\frac{N}{\alpha^2-s^2}=\frac{N}{(|\alpha|+s)(|\alpha|-s)}.$$
只有 pole，兩個左右對稱：$s=\pm|\alpha|$。取左半邊 $s=-|\alpha|$（老師加絕對值，強調在左半邊；左半邊才是因果的）：
$$L(s)=\frac{\sqrt N}{|\alpha|+s}.$$
驗證：$|L(j\omega)|^2=\frac{N}{\alpha^2+\omega^2}$。所以這個過程是 regular。

**Example 11-2** [▶ 28:17](https://youtu.be/OMs-MoVs2Kk?t=1697)：$S(\omega)=\frac{49+25\omega^2}{\omega^4+10\omega^2+9}$（分子二次、分母四次）。
$$S(s)=\frac{49-25s^2}{(1-s^2)(9-s^2)},\qquad L(s)=\frac{7+5s}{(1+s)(3+s)}.$$
兩個 zero、四個 pole，共六個根，分成左右各三個，取左半平面的。

**Example 11-3** [▶ 39:08](https://youtu.be/OMs-MoVs2Kk?t=2348)：$S(\omega)=\frac{25}{\omega^4+1}$（根有無理數，老師故意舉不那麼剛好的例子）。
$$S(s)=\frac{25}{s^4+1}=\frac{25}{(s^2+\sqrt2s+1)(s^2-\sqrt2s+1)},\qquad L(s)=\frac{5}{s^2+\sqrt2s+1}.$$

### 5.3 驗證因果、穩定：時域脈衝響應

[▶ 29:18](https://youtu.be/OMs-MoVs2Kk?t=1758) 上面只說明可以分解，還沒說明因果、穩定。因果在時域看得比較清楚（課本沒做，老師做了）。

**Example 11-1**：令 $j\omega'=\alpha+j\omega$，積分變成 $\frac{1}{j\omega'}$ 的形式。用 extended Fourier transform 的觀念：$\frac{1}{j\omega}$ 是**積分器**——輸入 $\delta$，輸出 $\int_{-\infty}^{t}\delta(u)du$。delta 在 $u=0$ 有脈衝，積分範圍沒過 0 是 0，過了 0 就是 1，也就是單位階梯 $U(t)$。所以
$$l(t)=\sqrt N\,e^{-|\alpha|t}U(t).$$
- $t<0$ 都是 0 → **因果**。根一定要在左半平面，才有這個結果。
- $e^{-(\text{正數})t}$，總積分、總能量有限 → **穩定**（頻譜上也看得到）。

**Example 11-2**：拆成部分分式（高中數學常做）：
$$L(s)=\frac{7+5s}{(1+s)(3+s)}=\frac{1}{1+s}+\frac{4}{3+s}\ \Rightarrow\ l(t)=\left(e^{-t}+4e^{-3t}\right)U(t).$$
（以下係數由部分分式求得，補上：$\frac{7+5s}{(1+s)(3+s)}$ 在 $s=-1$ 的留數 $\frac{2}{2}=1$，在 $s=-3$ 的留數 $\frac{-8}{-2}=4$。）因果、穩定。只要是分式，一定可以這樣分析。

**Example 11-3**：根是共軛複數 $s=-\frac{1}{\sqrt2}\pm\frac{j}{\sqrt2}$。一樣拆成兩個一次式的倒數，係數 $a$、$b$ 是共軛複數；共軛使實部對消、虛部留下，出現一個 $\sin$：
$$l(t)=5\sqrt2\,e^{-t/\sqrt2}\sin\frac{t}{\sqrt2}\,U(t).$$
（係數由 $\frac{1}{(s+a)^2+b^2}\leftrightarrow\frac{e^{-at}\sin bt}{b}U(t)$、$a=b=\frac1{\sqrt2}$ 補上。）

### 5.4 Whitening filter 是不是 stable？（微分器的爭議）

[▶ 33:27](https://youtu.be/OMs-MoVs2Kk?t=2007) 課本忽略的問題：定義要求 $1/L$（whitening filter）也因果穩定。Pole、zero 互換，還是在左半平面；但它真的是因果穩定嗎？

**Example 11-1 的 whitening filter**：
$$\frac{1}{L(\omega)}=\frac{|\alpha|+j\omega}{\sqrt N}.$$
常數項是 $\delta$；$j\omega$ 是**微分器**。

**各種觀點**【口頭】（老師說沒有標準答案，見仁見智，持開放態度）：
- **理論上**：有些書寫積分器、微分器都**不是 stable**——輸入有界，微分後若有瞬間跳躍會衝到無限大。這就違反定義了。
- **pole 在無限大**：$\frac{N}{\alpha+j\omega}$ 的倒數在 $\omega\to\infty$ 時衝到無限大，有人說它有一個 pole 在無限大（教控制的老師可能不同意「pole 在無限大」這種說法，但網路上也有人這樣說）。如果承認，就符合「微分器 unstable」。
- **實作上**：無限大是概念，不會發生。做任何系統，使用的頻率絕對不在無限大（3–4 GHz、5G 的 70 GHz……不會做到無限大）。永遠在有限的頻率範圍看系統，所以它其實是 stable 的。
- **做線路的人**：老師問過做系統、做線路的人，他們認為積分器、微分器是 stable 的，因為實作上很容易讓它 stable——例如用 OP amp 做時串一個電阻，就是近似的 stable 積分器。
- **課本**：沒說明，但顯然把無限大的點不當 pole，所以把這些例子當成 regular process。Example 11-3 也是二次式除以一次式（倒過來後），理論上無限遠有 pole，實作上沒關係。

---

## 6. 離散時間

### 6.1 定義與 Paley–Wiener

[▶ 42:42](https://youtu.be/OMs-MoVs2Kk?t=2562) 文字上完全一樣，只是「左半平面」換成「單位圓」。

> **離散最小相位系統**：$L(z)$ 和 $1/L(z)$ 都因果穩定，也就是在單位圓**外部** $|z|>1$ analytic。
> **離散穩定**：所有 pole 都在**單位圓 (unit circle) 內部**（學過控制的同學應該知道，離散系統看 $z$ 平面）。
> **離散 regular process**：
> $$S(z)=L(z)L(1/z),\qquad S\left(e^{j\omega}\right)=\left|L\left(e^{j\omega}\right)\right|^2\qquad\text{(11-6)}.$$
> zero 和 pole 都不能在單位圓外面。

- 輸入白雜訊的自相關是 Kronecker delta（$\delta[m]$，是 1 或 0），頻譜是 1。
- 記號 $L(\omega)$ 和 $L(e^{j\omega})$ 完全相同，不刻意區分。

【課本補充】(11-7)、(11-8)：$I[n]=\sum_{k\ge0}\gamma[k]X[n-k]$，$X[n]=\sum_{k\ge0}l[k]I[n-k]$，$E\{X^2[n]\}=\sum l^2[k]<\infty$。

> **離散 Paley–Wiener 條件**（積分只在 $(-\pi,\pi)$）：
> $$\int_{-\pi}^{\pi}\left|\log S(\omega)\right|d\omega<\infty\qquad\text{(11-9)}.$$
> 若 $S$ 可積（有限能量），它化簡成第 15 集的 $\int_{-\pi}^{\pi}\log S(\omega)\,d\omega>-\infty$ (9-203)。

### 6.2 證明：可積時兩種 Paley–Wiener 等價

[▶ 47:55](https://youtu.be/OMs-MoVs2Kk?t=2875)

- **⇒**（好證）：$\int|\log S|<\infty$ ⇒ 不取絕對值有正有負，一定不會衝到 $-\infty$。
- **⇐**（老師證這個方向）：$S$ 可積、$\int\log S>-\infty$ ⇒ $\int|\log S|<\infty$。

**關鍵：把絕對值拿掉。** $\log a>0$ 若 $a>1$；$<0$ 若 $a<1$。所以
$$\int|\log S|=-\int_{S<1}\log S+\int_{S\ge1}\log S=-\int\log S+2\int_{S\ge1}\log S.$$
（負的部分加負號就是絕對值；整個區域積分時正的部分要補兩倍。）

再用**基本不等式** $\log x\le x-1$（老師說這是通訊領域最常用的不等式，Cover 的資訊理論書叫它 Fundamental Inequality）：
$$2\int_{S\ge1}\log S\le2\int_{S\ge1}(S-1)\le2\int S<\infty.$$
兩項都有限，得證。 ∎

**重要定理**（第 9 章 p. 424 先提到，第 11 章才講由來）【課本補充】(9-205)–(9-207)：

> 存在唯一的函數 $H(z)=\sum_{k\ge0}h_kz^{-k}$，$h_0>0$，和它的倒數在 $|z|>1$ analytic（最小相位），$\sum|h_k|^2<\infty$，且 $S(\omega)=|H(e^{-j\omega})|^2$ a.e.——**若且唯若 $S(\omega)$ 和 $\log S(\omega)$ 都可積**。

老師說：所以要判斷一個過程是不是 regular，這是 if and only if 的條件——$S$ 可積、$\log S$ 的絕對值可積，兩個都成立就是 regular；因為在單位圓外面若有點，濾波器就可能非因果或不穩定。

### 6.3 有理頻譜的分解與例子

[▶ 54:07](https://youtu.be/OMs-MoVs2Kk?t=3247) 實數過程的頻譜是偶函數，所以是 $e^{j\omega}$ 和 $e^{-j\omega}$ 的對稱函數，也就是 **$\cos\omega$ 的函數**（$\cos\omega=\frac{z+z^{-1}}{2}$）：
$$S(z)=\frac{A\left(\frac{z+z^{-1}}2\right)}{B\left(\frac{z+z^{-1}}2\right)}.$$

**根的性質**：
1. $z_i$ 是根 ⇒ $\frac{1}{z_i}$ 也是根（代進去 $z+z^{-1}$ 一樣）。
2. 實係數 → 共軛也是根。

例：$2+j$ 是根 ⇒ $2-j$、$\frac{1}{2+j}$、$\frac{1}{2-j}$ 都是根。根**對單位圓對稱**，四個四個出現；兩個在外面就有兩個在裡面。分成 **inside**（$|z_i|<1$）和 **outside** 兩組，取 inside：
$$S(z)=\frac{N(z)N(1/z)}{D(z)D(1/z)},\qquad L(z)=\frac{N(z)}{D(z)},\qquad L^2(1)=S(1).$$

**Example 11-4** [▶ 58:13](https://youtu.be/OMs-MoVs2Kk?t=3493)：$S(\omega)=\frac{5-4\cos\omega}{10-6\cos\omega}$。

1. 代 $\cos\omega=\frac{z+z^{-1}}{2}$（分子分母係數除以 2）：
$$S(z)=\frac{5-2(z+z^{-1})}{10-3(z+z^{-1})}=\frac{2(z-\frac12)(z-2)}{3(z-\frac13)(z-3)}.$$
   根：$\frac12$ 和 2（互為倒數）、$\frac13$ 和 3。純實數，沒有共軛。
2. 取單位圓內的 $\frac12$、$\frac13$：
$$L(z)=\frac{2z-1}{3z-1}=\frac{2-z^{-1}}{3-z^{-1}}.$$

**驗證因果、穩定**（課本只給結果，老師驗證）：
- 喜歡用 $z^{-1}$ 為單位：$z^{-1}$ 就是延遲一格，$\frac{1}{1-a}=1+a+a^2+\cdots$ 展開成 $z^{-1},z^{-2},\dots$ 就能實作。
- 拆成「常數 + 常數／$(1-\frac13z^{-1})$」：$L(z)=\frac{1}{3}\cdot\frac{2-z^{-1}}{1-\frac13z^{-1}}$。展開：

以下係數**不是逐字稿內容**，依展開補上（老師口述了 $n=0$ 是 $1-\frac13=\frac23$，後面「$3^{-2},3^{-3},\dots$」；符號由計算得出）：
$$l[0]=\frac23,\qquad l[n]=-3^{-(n+1)}\ (n\ge1).$$
$n<0$ 都是 0 → 因果；指數衰減 → 穩定。

- **Whitening filter** $\frac{1}{L(z)}=\frac{3-z^{-1}}{2-z^{-1}}$ 也是一次除一次，同樣拆解、展開，也是因果穩定。離散的情況**沒有**連續時間微分器、積分器那種問題，比較好。

所以這個有理頻譜是 regular，完全符合條件。

---

## 7. 為什麼叫最小相位：最小群延遲

[▶ 64:16](https://youtu.be/OMs-MoVs2Kk?t=3856) 控制理論早就建立了。現在證明：對所有因果、穩定、**magnitude response 相同**的濾波器，最小相位系統的**延遲最小**。

**延遲 = 相位的微分**：濾波器 $e^{-j\omega n}$ 輸出 $X(t-n)$，延遲 $n$。$n$ 就是轉移函數相位（argument）$-\omega n$ 對 $\omega$ 微分再加負號：
$$\tau_g(\omega)=-\frac{d}{d\omega}\arg H(\omega)\quad\text{（群延遲，group delay）}.$$
（講延遲講正的，所以加負號。）

**單一個 zero**：$H(z)=1-z_iz^{-1}$。喜歡用 $z^{-1}$：輸出 $Y[t]=X[t]-z_iX[t-1]$，$z^{-1}$ 就是延遲一格，實作簡單。

令 $z_i=re^{j\theta_i}$，$z^{-1}=e^{-j\omega}$：$H=1-re^{-j(\omega-\theta_i)}$。

- 求相位時，可以把整個除以常數（老師的例子：$3e^{j20°}$ 除以 2 變 $1.5e^{j20°}$，角度不變），不影響角度。
- 相位 $=\arctan\frac{\text{虛部}}{\text{實部}}$，$\arctan$ 可以微分（$\frac{d}{dx}\tan^{-1}x=\frac{1}{1+x^2}$，要記得）。老師說細節是純數學步驟，留在講義上，用數學軟體也能得到。

結果（以下由上述步驟推導補上，和老師口述的形式一致）：
$$\tau_g(\omega)=\frac{r-\cos(\omega-\theta_i)}{r+r^{-1}-2\cos(\omega-\theta_i)}.$$

**選根**：magnitude response 固定時，舉一反三的四個點（$z_i$、$1/z_i$、共軛、共軛的倒數）都不能動，只能選哪兩個。
- 分母 $r+r^{-1}-2\cos(\cdot)$：$r$ 和 $\frac1r$ 代進去一樣（自己跟自己的倒數），是常數。
- **唯一能改變的是分子的 $r$**：要延遲最小，選 $r$ 小的——**單位圓內的那兩個點**。

**數值例**：$z_i$ 半徑 $\frac12$、角度 $\frac\pi3$，舉一反三四點（兩點在半徑 2、兩點在半徑 $\frac12$，角度 $\pm\frac\pi3$）。畫四條群延遲曲線：底下那兩條（單位圓內）永遠比上面兩條小；$z_i$ 和 $z_i^*$ 的兩條只是平移（對有的頻率大、有的小）。

**多個 zero**：線性系統的轉移函數是相乘，可以拆成好多個串接。相位相加、延遲相加（微分是線性的，可累加：2 ns + 3 ns = 5 ns）。每一級都選延遲最小的，串起來就最小。所以 inside group 絕對符合最小相位的要求。

**pole**：$H=\frac{1}{1-z_iz^{-1}}$。分子取絕對值的平方是實數，不影響角度，步驟和 zero 一模一樣，只差正號變負號，後面是常數。老師說同樣選讓延遲最小的那兩點，因此這個系統化的選法得到最小延遲，所以叫 minimum group delay，和 minimum phase 是同一件事。

⚠️ 待確認：以下**不是逐字稿內容**，是依上式推論的——pole 的群延遲是 $-\frac{r-\cos(\cdot)}{r+r^{-1}-2\cos(\cdot)}$，若只比較這個式子，$r$ 大（單位圓外）的 pole 群延遲反而比較小；但因果實現下單位圓外的 pole 會**不穩定**，所以因果穩定的系統 pole 必須都在單位圓內，比較時真正能選的只有 zero 的位置。老師說「pole 也選延遲最小的那兩點」，嚴格說應理解為「在因果穩定的前提下」。

---

## 8. 一頁速查表

### 定義

| 名詞 | 意義 |
|---|---|
| 最小相位 | $L$ 和 $1/L$ 都因果、穩定；連續：pole、zero 在左半平面；離散：在單位圓內 |
| regular | $S=\lvert L\rvert^2$，$L$ 最小相位（白雜訊經最小相位濾波器的輸出） |
| innovation／innovation filter／whitening filter | $I$／$L$／$1/L$ |

### Paley–Wiener

- 連續：$\int\frac{|\log S|}{1+\omega^2}<\infty$；離散：$\int_{-\pi}^{\pi}|\log S|<\infty$。
- 離散、$S$ 可積時 ⇔ $\int\log S>-\infty$。關鍵：$\int|\log S|=-\int\log S+2\int_{S\ge1}\log S$，$\log x\le x-1$。
- 離散：可分解（最小相位）⇔ $S$、$\log S$ 都可積。帶限過程不滿足。

### 有理頻譜分解

| | 連續 | 離散 |
|---|---|---|
| 形式 | $S=\frac{A(\omega^2)}{B(\omega^2)}$，$s=j\omega$ | $S$ 是 $\cos\omega=\frac{z+z^{-1}}2$ 的有理式 |
| 根的對稱 | $s_i\to-s_i$、共軛（對虛軸對稱） | $z_i\to1/z_i$、共軛（對單位圓對稱） |
| 取哪組 | 左半平面 | 單位圓內 |

- 例：$\frac{N}{\alpha^2+\omega^2}\to L=\frac{\sqrt N}{|\alpha|+s}$，$l=\sqrt Ne^{-|\alpha|t}U(t)$；$\frac{49+25\omega^2}{\omega^4+10\omega^2+9}\to\frac{7+5s}{(1+s)(3+s)}$；$\frac{25}{\omega^4+1}\to\frac{5}{s^2+\sqrt2s+1}$；$\frac{5-4\cos\omega}{10-6\cos\omega}\to\frac{2z-1}{3z-1}$。

### 最小延遲

$\tau_g=-\frac{d}{d\omega}\arg H$；單一 zero：$\tau_g=\frac{r-\cos(\omega-\theta)}{r+r^{-1}-2\cos(\omega-\theta)}$，選 $r<1$ 延遲最小；串接延遲相加。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 有理頻譜、$z^{-1}$ 延遲實作 | 下一集：§11-2 有限階系統與狀態變數 |
| innovation、whitening | §13-2 預測（Wiener–Kolmogorov） |
| Paley–Wiener、可預測過程 | §11-4、§13-2 |
| 最小相位 | §12 附錄 12A 最小相位函數 |

---

## 附：本集一句話總結

> **我們看到的隨機過程，都是白雜訊（innovation）經過濾波器的輸出，所以頻譜要能分解成 $|L|^2$；要求 $L$ 和 $1/L$ 都因果穩定（最小相位）的就是 regular process——有理頻譜的分解步驟是找根、利用對稱性分兩組、只取左半平面（離散：單位圓內）的根，而這樣選出來的濾波器在所有同 magnitude response 的因果穩定濾波器中延遲最小。**

---

## ⚠️ 待確認清單

1. [▶ 17:34](https://youtu.be/OMs-MoVs2Kk?t=1054) 老師說加權的 Paley–Wiener 條件「比較強」，但依不等式它反而較易滿足；原意待確認。
2. [▶ 74:34](https://youtu.be/OMs-MoVs2Kk?t=4474) pole 的群延遲比較：依式子單位圓外的 pole 延遲較小，但不穩定；老師「pole 也選延遲最小的」應指因果穩定的前提，待確認。
3. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 11-1 錄影逐字稿（whisper large-v3-turbo，1:16:16）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
