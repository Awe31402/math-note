---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 31
lecture: Lecture 31
date: 2023-04-19
video: https://youtu.be/BAfWfszOV4M
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §5.10–5.11（書頁 253–268，PDF 頁 272–287）
---

# 第 31 集 · 反微分算子（Green 函數）與 Fourier 變換 [▶ 影片](https://youtu.be/BAfWfszOV4M)

← 上一集：[30-separation-of-variables-sturm-liouville](30-separation-of-variables-sturm-liouville.md) ｜ [總目錄](README.md) ｜ 下一集：[32-fourier-transform-distributions](32-fourier-transform-distributions.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 31 集
> **講者**：James Cook（⚠️ 待確認，見第 01 集）
> **來源**：YouTube 自動字幕逐字稿（59:51）＋ Debnath & Mikusiński §5.10–5.11
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯，依課本修正

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. §5.10 反微分算子與 Green 函數（快速帶過）](#1-510-反微分算子與-green-函數快速帶過)
- [2. Fourier 變換的定義](#2-fourier-變換的定義)
- [3. 【Q&A】L¹ 與 L² 的差別](#3-qal¹-與-l²-的差別)
- [4. 例一：$e^{-\alpha|x|}$](#4-例一e-alphax)
- [5. 例二：Gauss 函數](#5-例二gauss-函數)
- [6. 基本性質：線性、連續、一致收斂](#6-基本性質線性連續一致收斂)
- [7. 平移、位移、縮放、共軛](#7-平移位移縮放共軛)
- [8. 微分變乘法：$\mathcal F\{f'\}=i\omega\hat f$](#8-微分變乘法mathcal-fficomegahat-f)
- [9. 摺積定理](#9-摺積定理)
- [10. 延拓到 L²、Parseval／Plancherel](#10-延拓到-l²parsevalplancherel)
- [11. 對稱極限（主值）](#11-對稱極限主值)
- [12. 反變換與「對偶」的困惑](#12-反變換與對偶的困惑)
- [13. 預告](#13-預告)
- [14. 一頁速查表](#14-一頁速查表)
- [15. 與後續集數的連結](#15-與後續集數的連結)

---

## 0. 這堂課要做什麼

講者說上次已把 Sturm–Liouville 系統「自帶一套解的世界和幾何」講得差不多了；這次先**很快**帶過 §5.10（反微分算子、Green 函數），然後把時間花在 §5.11 Fourier 變換。[▶ 00:39](https://youtu.be/BAfWfszOV4M?t=39)

| 主題 | 課本位置 |
|---|---|
| Green 函數、積分算子 $T$ | Theorem 5.10.1–5.10.4，pp. 253–257 |
| Fourier 變換定義與例子 | Definition 5.11.1、Example 5.11.2，pp. 258–259 |
| 線性、連續、一致收斂、Riemann–Lebesgue | Theorem 5.11.3–5.11.6，pp. 259–261 |
| 平移／位移／縮放／共軛 | Theorem 5.11.7，p. 261 |
| 微分、摺積 | Theorem 5.11.9–5.11.11，pp. 262–263 |
| L² 延拓、Parseval、反變換 | Definition 5.11.13 – Corollary 5.11.20，pp. 264–267 |

【口頭】講者說 Fourier 變換是「標準數學課程裡最被虧待的主題」：對工程極重要，而它的抽象版本（在群上做 Fourier 分析）到今天仍是研究題目。[▶ 08:47](https://youtu.be/BAfWfszOV4M?t=527)

---

## 1. §5.10 反微分算子與 Green 函數（快速帶過）

[▶ 00:39](https://youtu.be/BAfWfszOV4M?t=39)

**想法**：要解 $Lu=f$（$u$ 滿足邊界條件），若能找到反算子 $L^{-1}$，答案就是 $u=L^{-1}f$。

【口頭】講者提醒這「有點騙人」：微分算子通常不是一對一（齊次方程 $Lu=0$ 有非零解），所以嚴格說只能談「一類解」——$L^{-1}f$ 給特解，再加上齊次解。[▶ 02:22](https://youtu.be/BAfWfszOV4M?t=142)

**Green 函數**（Green's function）就是讓解寫成積分的那個核：

$$u(x)=(L^{-1}f)(x)=\int_a^b G(x,t)\,f(t)\,dt .$$

【口頭】積分範圍不一定是 $[a,b]$；別的情境可能是無窮積分，「這沒有刻在石頭上」。[▶ 03:29](https://youtu.be/BAfWfszOV4M?t=209)

【課本補充】Theorem 5.10.1 的條件：$\lambda=0$ 不是正則 Sturm–Liouville 系統
$$Lu=\frac{d}{dx}\left(p(x)\frac{du}{dx}\right)+q(x)u=f(x),\qquad a_1u(a)+a_2u'(a)=0,\quad b_1u(b)+b_2u'(b)=0$$
的本徵值（$p,q$ 連續實值、$p>0$）。這時解唯一，並可寫成上面的積分，其中 $G(x,t)=G(t,x)$（對稱）。

定義積分算子
$$(Tf)(x)=\int_a^b G(x,t)f(t)\,dt .\tag{5.85}$$

講者唸過三個定理：[▶ 04:41](https://youtu.be/BAfWfszOV4M?t=281)

- **Theorem 5.10.2**：$T$ 是從 $L^2([a,b])$ 到 $C([a,b])$ 的**自伴緊緻**算子。
  - 【課本補充】證明三步：緊緻來自 Example 4.8.4（積分算子）；$G(x,t)=G(t,x)$ 所以自伴（Example 4.4.6）；$G$ 連續所以 $Tf$ 連續。
- **Theorem 5.10.3**：若 $0$ 不是 S–L 系統的本徵值，則 $0$ 也不是 $T$ 的本徵值。
- **Theorem 5.10.4**：$\lambda$ 是 $L$ 的本徵值 ⟺ $1/\lambda$ 是 $T$ 的本徵值；而且本徵函數相同。[▶ 07:03](https://youtu.be/BAfWfszOV4M?t=423)

$$Lu=\lambda u\quad\Longleftrightarrow\quad Tu=\frac1\lambda u .$$

【口頭】「一點也不意外」：有限維也一樣，可逆矩陣 $A$ 有本徵值 2，則 $A^{-1}$ 有本徵值 $\tfrac12$。[▶ 08:07](https://youtu.be/BAfWfszOV4M?t=487)

【課本補充】證明的關鍵一步：若 $Lf=\lambda f$，由 Theorem 5.10.1 得 $f=T(\lambda f)=\lambda Tf$，所以 $Tf=\frac1\lambda f$。

講者也說不打算在這裡做細節，「只做到讓下一節說得通」。

---

## 2. Fourier 變換的定義

[▶ 09:52](https://youtu.be/BAfWfszOV4M?t=592)

**Definition 5.11.1**：設 $f\in L^1(\mathbb R)$（Lebesgue 可積）。$f$ 的 **Fourier 變換**（Fourier transform）是

$$\hat f(\omega)=\mathcal F\{f(x)\}(\omega)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{-i\omega x}f(x)\,dx .$$

$|e^{-i\omega x}|=1$，所以 $f\in L^1$ 就保證這個積分存在。兩種記號 $\hat f$、$\mathcal F\{f\}$ 都會用。

---

## 3. 【Q&A】L¹ 與 L² 的差別

[▶ 11:12](https://youtu.be/BAfWfszOV4M?t=672)

一位學生讀到課本 p. 258：「這個積分**不能**拿來當 $L^2(\mathbb R)$ 上的定義，因為不是每個 $L^2$ 函數都可積；但可以把 Fourier 變換從 $L^1\cap L^2$ 延拓到 $L^2$。」學生問：到底哪些函數在 $L^2$ 卻不在 $L^1$？

講者和學生一起回去看第 2 章的定義（Definition 2.13.1，p. 74；$L^1$ 的定義約在 p. 45）。[▶ 14:05](https://youtu.be/BAfWfszOV4M?t=845)

講者的例子：[▶ 16:40](https://youtu.be/BAfWfszOV4M?t=1000)

- 像 $\dfrac1{|x|}$ 這種函數：在無窮遠處 $\int\frac1{|x|}$ 發散，但平方後 $\frac1{x^2}$ 收斂。
- 講者自己說「這不是完全對的例子」，因為 $\frac1{|x|}$ 在 0 附近也會出問題。

以下**不是逐字稿內容**，是依課本的定義推論的：一個乾淨的例子是
$$f(x)=\begin{cases}0,&|x|<1\\[2pt] \dfrac1{|x|},&|x|\ge1\end{cases}$$
這時 $\int_{\mathbb R}|f|=2\int_1^\infty\frac{dx}{x}=\infty$，但 $\int_{\mathbb R}|f|^2=2\int_1^\infty\frac{dx}{x^2}=2<\infty$。所以 $f\in L^2(\mathbb R)$，但 $f\notin L^1(\mathbb R)$。

學生也提到兩個方向都有反例（$L^1\not\subset L^2$、$L^2\not\subset L^1$）。講者補充：p. 88 的 Problem 32 是一個「Lebesgue 不可積，但廣義 Riemann 積分收斂」的函數；他說那和 Fresnel 函數有關，在光學裡會出現。[▶ 18:21](https://youtu.be/BAfWfszOV4M?t=1101)

---

## 4. 例一：$e^{-\alpha|x|}$

[▶ 19:31](https://youtu.be/BAfWfszOV4M?t=1171)

**Example 5.11.2(a)**：設 $\alpha>0$，求 $\mathcal F\{e^{-\alpha|x|}\}$。

**第 1 步：把絕對值拆開。**
$$\mathcal F\{e^{-\alpha|x|}\}=\frac1{\sqrt{2\pi}}\int_{-\infty}^0 e^{x(\alpha-i\omega)}\,dx+\frac1{\sqrt{2\pi}}\int_0^\infty e^{-x(\alpha+i\omega)}\,dx .$$

**第 2 步：直接積。**
$$=\frac1{\sqrt{2\pi}}\left[\frac{e^{x(\alpha-i\omega)}}{\alpha-i\omega}\right]_{-\infty}^{0}+\frac1{\sqrt{2\pi}}\left[\frac{-e^{-x(\alpha+i\omega)}}{\alpha+i\omega}\right]_{0}^{\infty}.$$

因為 $\alpha>0$，$x\to-\infty$ 時 $|e^{x(\alpha-i\omega)}|=e^{\alpha x}\to0$；$x\to\infty$ 時 $|e^{-x(\alpha+i\omega)}|=e^{-\alpha x}\to0$。所以只剩 $x=0$ 的項：
$$=\frac1{\sqrt{2\pi}}\left(\frac1{\alpha-i\omega}+\frac1{\alpha+i\omega}\right).$$

**第 3 步：通分。** 分母 $(\alpha-i\omega)(\alpha+i\omega)=\alpha^2+\omega^2$，分子 $(\alpha+i\omega)+(\alpha-i\omega)=2\alpha$（$i\omega$ 互相抵消）：
$$\boxed{\mathcal F\{e^{-\alpha|x|}\}=\frac{2\alpha}{\sqrt{2\pi}\,(\alpha^2+\omega^2)}=\sqrt{\frac2\pi}\,\frac{\alpha}{\alpha^2+\omega^2}}$$

（講者寫的是左邊那個形式；兩者相等，因為 $\frac{2}{\sqrt{2\pi}}=\sqrt{\frac2\pi}$。）[▶ 23:04](https://youtu.be/BAfWfszOV4M?t=1384)

---

## 5. 例二：Gauss 函數

[▶ 23:53](https://youtu.be/BAfWfszOV4M?t=1433)

**Example 5.11.2(b)**：設 $\alpha>0$，求 $\mathcal F\{e^{-\alpha x^2}\}$。

**第 1 步：合併指數，配方。**
$$-\alpha x^2-i\omega x=-\alpha\left(x^2+\frac{i\omega}{\alpha}x\right)=-\alpha\left(x+\frac{i\omega}{2\alpha}\right)^2+\alpha\left(\frac{i\omega}{2\alpha}\right)^2 .$$
因為 $i^2=-1$，最後一項是 $\alpha\cdot\frac{-\omega^2}{4\alpha^2}=-\frac{\omega^2}{4\alpha}$。[▶ 25:46](https://youtu.be/BAfWfszOV4M?t=1546)

**第 2 步：把常數提出來。**
$$\hat f(\omega)=\frac1{\sqrt{2\pi}}\,e^{-\omega^2/(4\alpha)}\int_{-\infty}^{\infty}\exp\left(-\alpha\left(x+\frac{i\omega}{2\alpha}\right)^2\right)dx .$$

**第 3 步：Gauss 積分。** 令 $u=x+\frac{i\omega}{2\alpha}$；這只是平移，所以 $du=dx$。[▶ 27:42](https://youtu.be/BAfWfszOV4M?t=1662)
$$\int_{-\infty}^{\infty}e^{-\alpha u^2}\,du=\sqrt{\frac\pi\alpha}.$$

**第 4 步：化簡。**
$$\hat f(\omega)=\frac1{\sqrt{2\pi}}\sqrt{\frac{\pi}{\alpha}}\,e^{-\omega^2/(4\alpha)}=\boxed{\frac1{\sqrt{2\alpha}}\,e^{-\omega^2/(4\alpha)}}$$

以下**不是逐字稿內容**，是依複變積分推論的：第 3 步的平移是往**虛軸方向**平移，$du=dx$ 只說明了形式上的換元。嚴格的理由是對 $e^{-\alpha z^2}$ 沿長方形圍道積分，兩條直邊在 $|x|\to\infty$ 時趨於 0，所以水平線 $\operatorname{Im}z=\frac{\omega}{2\alpha}$ 上的積分等於實軸上的積分。

【口頭】重點：Gauss 函數的 Fourier 變換**還是 Gauss 函數**。這回答了一個問題：「什麼函數變換之後形式不變？」答案是 Gauss。[▶ 28:25](https://youtu.be/BAfWfszOV4M?t=1705)

【口頭】講者接著想把 $\alpha$ 換成純虛數（$-\alpha=i\beta$），算 $e^{i\beta x^2}$ 類函數的變換，但算到一半說「我不確定這對不對」，為了趕時間就放下了。[▶ 29:35](https://youtu.be/BAfWfszOV4M?t=1775)

以下**不是逐字稿內容**，是依定義推論的：$|e^{i\beta x^2}|=1$，這個函數**不在** $L^1(\mathbb R)$，所以 Definition 5.11.1 不能直接用；上面的公式在 $\operatorname{Re}\alpha\le0$ 時不能直接套。

---

## 6. 基本性質：線性、連續、一致收斂

[▶ 30:54](https://youtu.be/BAfWfszOV4M?t=1854)

- **Theorem 5.11.3（線性）**：$\mathcal F(\alpha f+\beta g)=\alpha\,\mathcal F(f)+\beta\,\mathcal F(g)$。
- **Theorem 5.11.4**：可積函數的 Fourier 變換是**連續函數**。
  - 【課本補充】關鍵一步：
  $$\left|\hat f(\omega+\lambda)-\hat f(\omega)\right|\le\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}\left|e^{-i\lambda x}-1\right|\,|f(x)|\,dx ,$$
  被積函數被 $2|f|$ 控制，且 $\lambda\to0$ 時逐點趨於 0，用 Lebesgue 控制收斂定理得到結果。
- **Theorem 5.11.5**：若 $\|f_n-f\|_1\to0$，則 $\hat f_n\to\hat f$ **一致**收斂。[▶ 32:11](https://youtu.be/BAfWfszOV4M?t=1931)
  - 證明一行：$\displaystyle\sup_\omega|\hat f_n(\omega)-\hat f(\omega)|\le\frac1{\sqrt{2\pi}}\int|f_n-f|=\frac1{\sqrt{2\pi}}\|f_n-f\|_1\to0$。
  - 【口頭】講者強調：左邊（$L^1$ 收斂）不是一致收斂，右邊卻是。

【課本補充】**Theorem 5.11.6（Riemann–Lebesgue 引理）**：$f\in L^1(\mathbb R)$ ⟹ $\displaystyle\lim_{|\omega|\to\infty}\hat f(\omega)=0$。課本總結：Theorem 5.11.3–5.11.6 說明 $\mathcal F$ 是從 $L^1(\mathbb R)$ 到 $C_0(\mathbb R)$ 的連續線性算子。課堂上沒講這條。

---

## 7. 平移、位移、縮放、共軛

[▶ 33:31](https://youtu.be/BAfWfszOV4M?t=2011)

**Theorem 5.11.7**：設 $f\in L^1(\mathbb R)$。

| 性質 | 公式 |
|---|---|
| (a) 平移（translation） | $\mathcal F\{e^{i\alpha x}f(x)\}=\hat f(\omega-\alpha)$ |
| (b) 位移（shifting） | $\mathcal F\{f(x-x_0)\}=\hat f(\omega)\,e^{-i\omega x_0}$ |
| (c) 縮放（scaling） | $\mathcal F\{f(\alpha x)\}=\dfrac1\alpha\hat f\left(\dfrac\omega\alpha\right)$，$\alpha>0$ |
| (d) 共軛（conjugate） | $\mathcal F\{\overline{f(x)}\}=\overline{\mathcal F\{f(-x)\}}$ |

(a) 的推導：$\mathcal F\{e^{i\alpha x}f\}(\omega)=\frac1{\sqrt{2\pi}}\int e^{-i(\omega-\alpha)x}f(x)\,dx=\hat f(\omega-\alpha)$。

【口頭】和 Laplace 變換類比：**虛指數之於 Fourier 變換，就像實指數之於 Laplace 變換**（Laplace 有 $\mathcal L\{e^{at}f\}=F(s-a)$）。[▶ 34:01](https://youtu.be/BAfWfszOV4M?t=2041)

【口頭】講者注意到 (d) 不是「共軛的變換 = 變換的共軛」，而是要多一個 $x\mapsto-x$。[▶ 35:17](https://youtu.be/BAfWfszOV4M?t=2117)

【課本補充】**Example 5.11.8（調變 Gauss 函數）**：$f(x)=e^{i\omega_0x-\frac12x^2}$ ⟹ $\hat f(\omega)=e^{-\frac12(\omega-\omega_0)^2}$。由例二（$\alpha=\tfrac12$ 給出 $e^{-\omega^2/2}$）加上平移性質 (a) 得到。

---

## 8. 微分變乘法：$\mathcal F\{f'\}=i\omega\hat f$

[▶ 35:53](https://youtu.be/BAfWfszOV4M?t=2153)

【口頭】「如果 Fourier 變換你什麼都不記，也要記住這個定理——它是 Fourier 變換的招牌動作。」講者說要「暫時不管定義域的細節」，先把推導做出來。

**Theorem 5.11.9**：設 $f$ 連續、分段可微，$f,f'\in L^1(\mathbb R)$，且 $\lim_{|x|\to\infty}f(x)=0$。則
$$\mathcal F\{f'\}=i\omega\,\mathcal F\{f\}.$$

**推導（分部積分）**：[▶ 39:12](https://youtu.be/BAfWfszOV4M?t=2352)

先寫乘積法則：
$$\frac{d}{dx}\left(e^{-i\omega x}f(x)\right)=e^{-i\omega x}f'(x)-i\omega\,e^{-i\omega x}f(x).$$
移項後積分：
$$\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{-i\omega x}f'(x)\,dx=\frac1{\sqrt{2\pi}}\left[e^{-i\omega x}f(x)\right]_{-\infty}^{\infty}+\frac{i\omega}{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{-i\omega x}f(x)\,dx .$$

邊界項為 0：$|e^{-i\omega x}f(x)|=|f(x)|\to0$，這正是定理假設 $\lim_{|x|\to\infty}f(x)=0$ 的用處。[▶ 40:54](https://youtu.be/BAfWfszOV4M?t=2454) 剩下的就是 $i\omega\hat f(\omega)$。

【口頭】講者喜歡先寫出乘積法則再積分，「確定自己沒有騙自己」；並說 Laplace 變換的定理在不太計較分析細節時，證明幾乎都只是微積分二的分部積分。[▶ 37:50](https://youtu.be/BAfWfszOV4M?t=2270)

**Corollary 5.11.10**：重複使用，
$$\mathcal F\{f^{(n)}\}=(i\omega)^n\,\mathcal F\{f\}$$
（條件：$f,\dots,f^{(n)}\in L^1$，$f^{(k)}\to0$，$k=0,\dots,n-1$）。例如 $\mathcal F\{f''\}=(i\omega)^2\hat f=-\omega^2\hat f$。

【口頭】一句話：**Fourier 變換把微分變成乘以 $i\omega$**。Laplace 變換也一樣把時域微分變成頻域乘以 $s$，只是多了初值項。[▶ 42:09](https://youtu.be/BAfWfszOV4M?t=2529)

---

## 9. 摺積定理

[▶ 42:41](https://youtu.be/BAfWfszOV4M?t=2561)

【課本補充】配合本書的定義，摺積重新定義成
$$(f*g)(x)=\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x-u)\,g(u)\,du .$$

**Theorem 5.11.11（摺積定理）**：$f,g\in L^1(\mathbb R)$ ⟹
$$\mathcal F(f*g)=\mathcal F(f)\,\mathcal F(g).$$

【口頭】用代數的話說，這是**同態**（homomorphism）性質：「摺積意義下的乘法」變成「$\omega$ 的函數的一般乘法」。[▶ 43:11](https://youtu.be/BAfWfszOV4M?t=2591)

【課本補充】證明關鍵：$h=f*g\in L^1$（Theorem 2.15.1），寫出 $\hat h$ 的二重積分，用 Fubini 交換順序，再令 $x-u=v$，就拆成 $\hat f(\omega)\hat g(\omega)$。

---

## 10. 延拓到 L²、Parseval／Plancherel

[▶ 43:44](https://youtu.be/BAfWfszOV4M?t=2624)

**Theorem 5.11.12**：$f$ 連續且在有界區間外為 0 ⟹ $\hat f\in L^2(\mathbb R)$，且 $\|\hat f\|_2=\|f\|_2$。

**Definition 5.11.13（$L^2$ 上的 Fourier 變換）**：設 $f\in L^2(\mathbb R)$，取一列緊支撐連續函數 $\varphi_n$ 使 $\|f-\varphi_n\|_2\to0$，定義
$$\hat f=\lim_{n\to\infty}\hat\varphi_n\qquad(\text{在 }L^2\text{ 範數下的極限}).$$

【口頭】講者說今天不太在意這個延拓的細節，只說重點：**用適當序列的極限來延拓**——「就像你們正在做的作業：把內積延拓到空間的完備化」。[▶ 44:18](https://youtu.be/BAfWfszOV4M?t=2658)

【課本補充】為什麼這樣定義是好的：緊支撐連續函數在 $L^2$ 中稠密；由 Theorem 5.11.12，$\|\hat\varphi_n-\hat\varphi_m\|_2=\|\varphi_n-\varphi_m\|_2$，所以 $(\hat\varphi_n)$ 是 Cauchy 列，極限存在，且不依賴所選的序列。注意 $L^2$ 收斂不是逐點收斂，所以 $L^2$ 函數的 Fourier 變換只是「幾乎處處」定義的。

**Theorem 5.11.14（Parseval 關係）**：$f\in L^2(\mathbb R)$ ⟹ $\|\hat f\|_2=\|f\|_2$。[▶ 44:51](https://youtu.be/BAfWfszOV4M?t=2691)

【口頭】課本說：在物理問題中，$\|f\|^2$ 是能量的量度，$\|\hat f\|^2$ 代表 $f$ 的「功率譜」（power spectrum）。

---

## 11. 對稱極限（主值）

[▶ 45:27](https://youtu.be/BAfWfszOV4M?t=2727)

**Theorem 5.11.15**：$f\in L^2(\mathbb R)$ ⟹
$$\hat f(\omega)=\lim_{n\to\infty}\frac1{\sqrt{2\pi}}\int_{-n}^{n}e^{-i\omega x}f(x)\,dx ,$$
收斂是在 $L^2$ 範數下。

【課本補充】證明：令 $f_n=f\cdot\mathbf 1_{(-n,n)}$，則 $\|f-f_n\|_2\to0$，所以 $\|\hat f-\hat f_n\|_2\to0$。

【口頭】講者覺得這個定理很有意思：平常 $\int_{-\infty}^{\infty}$ 必須讓上下限**分別**趨於無窮；這裡卻只用**一個** $n$ 對稱地取極限。[▶ 46:03](https://youtu.be/BAfWfszOV4M?t=2763)
- 這叫**主值**（principal value）。很多函數的廣義積分發散，主值卻有限，而且很適合用複變的方法（圍道積分）來算。[▶ 47:12](https://youtu.be/BAfWfszOV4M?t=2832)
- 講者說這也是 Fourier 變換在大學部被虧待的另一個原因：真的會用計算型複變分析的學生不多。

---

## 12. 反變換與「對偶」的困惑

[▶ 48:21](https://youtu.be/BAfWfszOV4M?t=2901)

講者說要跳過中間的引理，直接看「下一個大事件」：

**Corollary 5.11.19（反變換）**：$f\in L^1(\mathbb R)\cap L^2(\mathbb R)$ ⟹ 幾乎處處有
$$f(x)=\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{i\omega x}\hat f(\omega)\,d\omega .$$

和正變換長得幾乎一樣，只是指數的符號相反。這就是**反 Fourier 變換**（inverse Fourier transform）。[▶ 49:28](https://youtu.be/BAfWfszOV4M?t=2968)

【課本補充】$L^2$ 版本是 Theorem 5.11.18：$f(x)=\lim_{n\to\infty}\frac1{\sqrt{2\pi}}\int_{-n}^{n}e^{i\omega x}\hat f(\omega)\,d\omega$（$L^2$ 收斂）。

**Corollary 5.11.20（Duality，p. 267）**：$f\in L^1\cap L^2$ ⟹ 幾乎處處 $\mathcal F\{\mathcal F\{f(x)\}\}=f(-x)$。證明：「在 (5.95) 裡把 $x$ 換成 $-x$ 就夠了。」

【口頭】講者讀到這裡很困惑，懷疑是印錯：[▶ 50:13](https://youtu.be/BAfWfszOV4M?t=3013)
- 他認為「Fourier 變換的 Fourier 變換」說不通，因為 $\hat f$ 是 $\omega$ 的函數；他猜作者想說的是反變換。
- 他在黑板上試著推，但被「哪個是積分的啞變數、哪個 $\omega$ 是同一個」卡住。[▶ 54:49](https://youtu.be/BAfWfszOV4M?t=3289)
- 他回憶在量子場論裡看過：這種積分會冒出一個 Dirac δ 和一個 $2\pi$，兩個 $2\pi$ 抵消，「但我看不出為什麼會得到 $-x$」。最後說「我做到剛好夠讓人困惑」，沒有結論。[▶ 57:37](https://youtu.be/BAfWfszOV4M?t=3457)

以下**不是逐字稿內容**，是依 Definition 5.11.1 與 Corollary 5.11.19 推論的：課本的敘述其實是對的，不是印錯。$\hat f$ 雖然是「$\omega$ 的函數」，但它本身就是一個 $\mathbb R\to\mathbb C$ 的函數，啞變數叫什麼名字不重要，所以可以再做一次 Fourier 變換：
$$\mathcal F\{\hat f\}(x)=\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{-ix\omega}\hat f(\omega)\,d\omega .$$
把反變換公式裡的 $x$ 換成 $-x$：
$$f(-x)=\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{i\omega(-x)}\hat f(\omega)\,d\omega=\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{-ix\omega}\hat f(\omega)\,d\omega=\mathcal F\{\hat f\}(x).$$
兩式右邊完全一樣，所以 $\mathcal F\{\mathcal F\{f\}\}(x)=f(-x)$。直觀說法：正、反變換只差指數的正負號，而 $x\mapsto -x$ 正好把正負號翻過來。所以連做兩次正變換等於把函數左右翻轉，做四次就回到原函數。講者記得的 Dirac δ 和 $2\pi$，是反變換公式的「形式推導」裡會出現的東西（$\int e^{i\omega(x-y)}d\omega=2\pi\delta(x-y)$），不影響這個結論。

---

## 13. 預告

[▶ 58:52](https://youtu.be/BAfWfszOV4M?t=3532)

- 下一節 §5.12 會真的用 Fourier 變換解微分方程，留到下次。
- 講者打算下週三考第 3、4 章，大概做成 take-home（帶回家考），「因為我們沒時間了」。

---

## 14. 一頁速查表

| 項目 | 公式／內容 | 關鍵一步 |
|---|---|---|
| Green 函數 | $u=L^{-1}f=\int_a^bG(x,t)f(t)\,dt$ | 需要 0 不是 S–L 本徵值 |
| 積分算子 $T$ | 自伴、緊緻，$L^2\to C$ | $G(x,t)=G(t,x)$；$G$ 連續 |
| 本徵值對應 | $Lu=\lambda u\iff Tu=\frac1\lambda u$ | $f=T(\lambda f)$ |
| Fourier 變換 | $\hat f(\omega)=\frac1{\sqrt{2\pi}}\int e^{-i\omega x}f(x)\,dx$ | $f\in L^1$ |
| $L^2\setminus L^1$ 例 | $\frac1{|x|}$（$|x|\ge1$），0（$|x|<1$） | $\int\frac1x=\infty$，$\int\frac1{x^2}<\infty$ |
| 例一 | $e^{-\alpha|x|}\mapsto\sqrt{\frac2\pi}\frac{\alpha}{\alpha^2+\omega^2}$ | 拆成兩半，$\frac1{\alpha-i\omega}+\frac1{\alpha+i\omega}$ |
| 例二 | $e^{-\alpha x^2}\mapsto\frac1{\sqrt{2\alpha}}e^{-\omega^2/(4\alpha)}$ | 配方；$\int e^{-\alpha u^2}=\sqrt{\pi/\alpha}$ |
| 連續 | $\hat f$ 連續 | 控制收斂 |
| 一致收斂 | $\|f_n-f\|_1\to0\Rightarrow\hat f_n\rightrightarrows\hat f$ | $\sup|\hat f_n-\hat f|\le\frac1{\sqrt{2\pi}}\|f_n-f\|_1$ |
| Riemann–Lebesgue | $\hat f(\omega)\to0$，$|\omega|\to\infty$ | （課本） |
| 平移 | $e^{i\alpha x}f\mapsto\hat f(\omega-\alpha)$ | 合併指數 |
| 位移 | $f(x-x_0)\mapsto e^{-i\omega x_0}\hat f$ | 換元 |
| 縮放 | $f(\alpha x)\mapsto\frac1\alpha\hat f(\omega/\alpha)$ | 換元 $u=\alpha x$ |
| 共軛 | $\overline{f(x)}\mapsto\overline{\mathcal F\{f(-x)\}}$ | |
| 微分 | $f^{(n)}\mapsto(i\omega)^n\hat f$ | 分部積分；邊界項因 $f\to0$ 消失 |
| 摺積 | $\mathcal F(f*g)=\hat f\hat g$（$*$ 帶 $\frac1{\sqrt{2\pi}}$） | Fubini |
| $L^2$ 延拓 | $\hat f=\lim\hat\varphi_n$ | 稠密＋等距 ⟹ Cauchy |
| Parseval | $\|\hat f\|_2=\|f\|_2$ | 能量＝功率譜 |
| 主值 | $\hat f=\lim_n\frac1{\sqrt{2\pi}}\int_{-n}^n$ | $f\mathbf 1_{(-n,n)}\to f$ in $L^2$ |
| 反變換 | $f(x)=\frac1{\sqrt{2\pi}}\int e^{i\omega x}\hat f\,d\omega$ | |
| 對偶 | $\mathcal F\{\mathcal F\{f\}\}(x)=f(-x)$ | 反變換公式中 $x\to-x$ |

---

## 15. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 微分變乘法、摺積定理 | 第 32 集：用 Fourier 變換解微分方程（§5.12） |
| Dirac δ、主值 | 第 32 集：分佈（第 6 章） |
| Gauss 函數、Fourier 變換是酉算子 | 第 33–34 集：量子力學（位置與動量表象、測不準原理） |

---

## 附：本集一句話總結

> **Green 函數把微分算子 $L$ 反過來變成一個自伴緊緻的積分算子 $T$（本徵值從 $\lambda$ 變 $1/\lambda$）；Fourier 變換 $\hat f(\omega)=\frac1{\sqrt{2\pi}}\int e^{-i\omega x}f$ 則把微分變成乘以 $i\omega$、把摺積變成乘法、在 $L^2$ 上保持長度，Gauss 函數變換完還是 Gauss 函數，而連做兩次就把函數左右翻轉。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-04-19 錄影逐字稿（YouTube 自動字幕 59:51）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §5.10–5.11 整理。*
