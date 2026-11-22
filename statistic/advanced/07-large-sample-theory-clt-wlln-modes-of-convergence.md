---
course: 高等統計學（數理統計續）
episode: 7
lecture: Lec07（第四週 2/2）
date: 待補
video: https://youtu.be/3SlBH7haSyw
notes: Hogg 8th ed. §5.1 依機率收斂、WLLN（Theorem 5.1.1）、連續函數保持收斂（Theorem 5.1.4，p. 323）；§5.2 依分配收斂（Definition 5.2.1，p. 327；Theorem 5.2.1，p. 332）；§5.3 中央極限定理（Theorem 5.3.1，p. 341）
---

# 第 7 集 · 第四週 (2/2)：大樣本理論——中央極限定理、弱大數法則、三種收斂的強弱 [▶ 影片](https://youtu.be/3SlBH7haSyw)

← 上一集：[06](06-variance-ci-difference-of-means-ci.md) ｜ [總目錄](../README.md) ｜ 下一集：[08](08-slutsky-approximate-ci-mean-proportion.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 7 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（33:23，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §5.1–5.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「收斂」→「縮鏈／縮練／solid」，「機率收斂」→「基力收斂」，「中央極限定理」→「中央極限子定理」，「Large Sample」→「大學問號（開頭）」，「近似」→「近視」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 大樣本理論](#1-大樣本理論)
- [2. 中央極限定理](#2-中央極限定理)
- [3. 為什麼要依分配收斂：建造信賴區間](#3-為什麼要依分配收斂建造信賴區間)
- [4. 弱大數法則](#4-弱大數法則)
- [5. 連續函數保持依機率收斂](#5-連續函數保持依機率收斂)
- [6. 依機率收斂 vs 依分配收斂](#6-依機率收斂-vs-依分配收斂)
- [7. 幾乎必然收斂](#7-幾乎必然收斂)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

建造**近似信賴區間**前，先整理需要的大樣本理論。

| 主題 | 課本 |
|---|---|
| 中央極限定理（CLT） | Theorem 5.3.1，p. 341 |
| 弱大數法則（WLLN） | Theorem 5.1.1 |
| $Y_n\xrightarrow{P}a$、$g$ 連續 ⇒ $g(Y_n)\xrightarrow{P}g(a)$ | Theorem 5.1.4，p. 323 |
| 依機率收斂 ⇒ 依分配收斂 | Theorem 5.2.1，p. 332 |
| 幾乎必然收斂 | （課本未詳述） |

---

## 1. 大樣本理論

[▶ 00:30](https://youtu.be/3SlBH7haSyw?t=30)

- 隨機樣本 $X_1,\dots,X_n$，$n$ 叫**樣本大小**（sample size）。
- **大樣本**：$n$ 很大，也就是 $n\to\infty$。
- [▶ 01:32](https://youtu.be/3SlBH7haSyw?t=92) **大樣本理論**（large sample theory）：所有考慮 $n\to\infty$ 的理論，就是各種**收斂**（convergence）。

---

## 2. 中央極限定理

[▶ 02:34](https://youtu.be/3SlBH7haSyw?t=154)

> **中央極限定理**（central limit theorem，CLT）（課本 Theorem 5.3.1，p. 341）：$X_1,\dots,X_n$ 是隨機樣本，來自**某個**分配，mean $\mu$、variance $\sigma^2$（$0<\sigma^2<\infty$），則
> $$\frac{\bar X-\mu}{\sigma/\sqrt n}\xrightarrow{D}N(0,1).$$

- [▶ 03:05](https://youtu.be/3SlBH7haSyw?t=185) $\mu$ 是 $\bar X$ 的 mean；$\sigma/\sqrt n$ 是 $\bar X$ 的標準差（$\text{Var}\bar X=\sigma^2/n$）。所以這就是「$\bar X$ 減掉 mean 除以標準差」。
- [▶ 03:36](https://youtu.be/3SlBH7haSyw?t=216) 這是一串**隨機變數**的收斂。講過兩種：依機率收斂、**依分配收斂**（上面寫 $D$）。

> **依分配收斂**（convergence in distribution）（課本 Definition 5.2.1，p. 327）：$X_n\xrightarrow{D}X$ 指
> $$F_{X_n}(x)\to F_X(x)\quad\text{在 }F_X\text{ 的每個連續點 }x.$$
> 「分配函數收斂到分配函數。」

[▶ 05:09](https://youtu.be/3SlBH7haSyw?t=309) 標準常態的分配函數在**每一點**都連續，所以 CLT 是對**所有** $x$：
$$P\left(\frac{\bar X-\mu}{\sigma/\sqrt n}\le x\right)\to\Phi(x)=\int_{-\infty}^x\frac{1}{\sqrt{2\pi}}e^{-t^2/2}dt,\quad\forall x.$$

---

## 3. 為什麼要依分配收斂：建造信賴區間

[▶ 06:43](https://youtu.be/3SlBH7haSyw?t=403) 【口頭】每個東西都有用。講依分配收斂的目的就是**建造信賴區間**。

[▶ 07:43](https://youtu.be/3SlBH7haSyw?t=463)

1. $Z\sim N(0,1)$：
$$1-\alpha=P(-z_{\alpha/2}<Z\le z_{\alpha/2})=\Phi(z_{\alpha/2})-\Phi(-z_{\alpha/2}).$$
2. [▶ 09:16](https://youtu.be/3SlBH7haSyw?t=556) 由 CLT，$W_n=\frac{\bar X-\mu}{\sigma/\sqrt n}$ 的分配函數在**同一點**會很接近 $\Phi$（$n$ 夠大）：
$$P(W_n\le z_{\alpha/2})\approx\Phi(z_{\alpha/2}),\qquad P(W_n\le-z_{\alpha/2})\approx\Phi(-z_{\alpha/2}).$$
3. [▶ 11:23](https://youtu.be/3SlBH7haSyw?t=683) 相減：$P(-z_{\alpha/2}<W_n\le z_{\alpha/2})\approx 1-\alpha$。
4. 分母乘過去、移項：
$$P\left(\bar X-z_{\alpha/2}\frac{\sigma}{\sqrt n}\le\mu\le\bar X+z_{\alpha/2}\frac{\sigma}{\sqrt n}\right)\approx 1-\alpha.$$

這就是建造信賴區間的方式（$\approx$：近似，不是相等）。

[▶ 12:58](https://youtu.be/3SlBH7haSyw?t=778) 但後面的近似信賴區間不是完全靠這樣（這裡還有 $\sigma$ 未知的問題），還需要別的理論。

---

## 4. 弱大數法則

[▶ 13:28](https://youtu.be/3SlBH7haSyw?t=808) Large numbers 的 numbers 就是 $n$（樣本數）。

> **弱大數法則**（WLLN）：隨機樣本，mean $\mu$、variance $\sigma^2<\infty$ ⇒ $\bar X\xrightarrow{P}\mu$，即
> $$P(|\bar X-\mu|\ge\epsilon)\to 0,\quad\forall\epsilon>0.$$

- [▶ 15:04](https://youtu.be/3SlBH7haSyw?t=904) $\bar X$ 和 $\mu$ 距離比很小的數還大的機率趨近 0：最後幾乎相等。
- [▶ 15:36](https://youtu.be/3SlBH7haSyw?t=936) 證明（上學期）：$E\bar X=\mu$，$\text{Var}\bar X=\sigma^2/n\to 0$。

---

## 5. 連續函數保持依機率收斂

[▶ 16:37](https://youtu.be/3SlBH7haSyw?t=997) 經常用的定理：

> **定理**（課本 Theorem 5.1.4，p. 323）：$Y_n\xrightarrow{P}a$（$a$ 是常數），$g$ 在 $a$ **連續**，則
> $$g(Y_n)\xrightarrow{P}g(a).$$

- [▶ 17:38](https://youtu.be/3SlBH7haSyw?t=1058) 證明用高等微積分裡連續函數的性質，不困難，有些統計書有。
- **例**（[▶ 18:38](https://youtu.be/3SlBH7haSyw?t=1118)）：由 WLLN，$\bar X\xrightarrow{P}\mu$，所以
  - $\bar X^2\xrightarrow{P}\mu^2$（平方連續；三次方、四次方都行）；
  - $e^{\bar X}\xrightarrow{P}e^\mu$（可微 ⇒ 連續）；
  - $\cos^2\bar X\xrightarrow{P}\cos^2\mu$。

---

## 6. 依機率收斂 vs 依分配收斂

[▶ 19:40](https://youtu.be/3SlBH7haSyw?t=1180)

| | 定義 |
|---|---|
| $X_n\xrightarrow{P}X$ | $P(\lvert X_n-X\rvert>\epsilon)\to 0$，$\forall\epsilon>0$（等價：$P(\lvert X_n-X\rvert\le\epsilon)\to 1$） |
| $X_n\xrightarrow{D}X$ | $F_{X_n}(x)\to F_X(x)$，在 $F_X$ 的連續點 |

依機率收斂：$X_n$ 和 $X$ 的差比無限小的數還小，機率趨近 1，幾乎沒有距離。

【課堂討論】[▶ 22:58](https://youtu.be/3SlBH7haSyw?t=1378) 老師問：微積分裡「連續」和「可微」哪個比較強？學生答：可微比較強（可微一定連續，連續不一定可微）。那這兩種收斂哪個強？

> **定理**（課本 Theorem 5.2.1，p. 332）：$X_n\xrightarrow{P}X$ ⇒ $X_n\xrightarrow{D}X$。反過來不一定。

**依機率收斂比較強**。

---

## 7. 幾乎必然收斂

[▶ 24:51](https://youtu.be/3SlBH7haSyw?t=1491) 給參考，不用背，本課不會用到。

**先看依機率收斂的事件**（[▶ 25:22](https://youtu.be/3SlBH7haSyw?t=1522)）：$X_n,X$ 都是 $S\to\mathbb{R}$ 的函數，事件 $\{|X_n-X|>\epsilon\}$ 是樣本點 $s$ 的集合：$|X_n(s)-X(s)|>\epsilon$ 的那些點。

> **幾乎必然收斂**（almost surely，a.s.；也叫 almost everywhere）（[▶ 27:27](https://youtu.be/3SlBH7haSyw?t=1647)）：
> $$P\left(\left\{s\in S:\ \lim_{n\to\infty}X_n(s)=X(s)\right\}\right)=1.$$

- [▶ 29:00](https://youtu.be/3SlBH7haSyw?t=1740) 給定一個 $s$，$X_n(s)$ 是一個實數數列（微積分的數列）。要求它的極限**等於** $X(s)$。
- 兩個函數不可能每一點都相等；但讓極限相等的那些點要多到機率是 1：「幾乎全部」。
- [▶ 30:35](https://youtu.be/3SlBH7haSyw?t=1835) 比依機率收斂強：依機率收斂只說差比無限小還小的機率趨近 1，不保證相等；a.s. 要求極限**相等**。

**強弱**（[▶ 31:35](https://youtu.be/3SlBH7haSyw?t=1895)）：
$$X_n\xrightarrow{a.s.}X\ \Rightarrow\ X_n\xrightarrow{P}X\ \Rightarrow\ X_n\xrightarrow{D}X.$$

【口頭】[▶ 32:08](https://youtu.be/3SlBH7haSyw?t=1928) 數學很好的人讀統計可以專做這種研究，做不完：別人證了依分配收斂，你證它其實依機率收斂；別人證了依機率收斂，你證 a.s.。越強表示越接近，越好。

---

## 8. 一頁速查表

**CLT**：$\dfrac{\bar X-\mu}{\sigma/\sqrt n}\xrightarrow{D}N(0,1)$（任何分配，$\sigma^2<\infty$）。

**用法**：$P\left(-z_{\alpha/2}<\frac{\bar X-\mu}{\sigma/\sqrt n}\le z_{\alpha/2}\right)\approx 1-\alpha$ → 近似信賴區間。

**WLLN**：$\bar X\xrightarrow{P}\mu$。

**連續函數**：$Y_n\xrightarrow{P}a$、$g$ 在 $a$ 連續 ⇒ $g(Y_n)\xrightarrow{P}g(a)$。

**三種收斂**

| | 定義 | 強弱 |
|---|---|---|
| a.s. | $P(\lim X_n=X)=1$ | 最強 |
| 依機率 | $P(\lvert X_n-X\rvert>\epsilon)\to 0$ | 中 |
| 依分配 | $F_{X_n}\to F_X$（連續點） | 最弱 |

a.s. ⇒ P ⇒ D。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| CLT、WLLN、連續函數 | 下一集：Slutsky 型結果，$\sigma$ 換成 $S$ 的近似信賴區間 |
| 依分配收斂 | 二項比例 $p$ 的近似信賴區間 |

---

## 附：本集一句話總結

> **大樣本理論就是 $n\to\infty$ 的各種收斂：中央極限定理說 $\frac{\bar X-\mu}{\sigma/\sqrt n}$ 依分配收斂到 $N(0,1)$，可用來建造近似信賴區間；弱大數法則說 $\bar X\xrightarrow{P}\mu$，連續函數保持依機率收斂；三種收斂的強弱是 a.s. ⇒ 依機率 ⇒ 依分配。**

---

*筆記依據「高等統計學」Lec07 錄影逐字稿（whisper large-v3-turbo，33:23）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
