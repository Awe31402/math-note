---
course: 高等統計學（數理統計續）
episode: 4
lecture: Lec04（第三週 1/2）
date: 待補
video: https://youtu.be/9LkLNEAiXXQ
notes: Hogg 8th ed. §4.2 信賴區間（Definition 4.2.1，p. 238）、樞紐量（pivot）；附錄 標準常態分配表
---

# 第 4 集 · 第三週 (1/2)：查標準常態表；信賴區間的定義與意義；樞紐量法 [▶ 影片](https://youtu.be/9LkLNEAiXXQ)

← 上一集：[03](03-two-order-statistics-joint-pdf-t-distribution.md) ｜ [總目錄](../README.md) ｜ 下一集：[05](05-normal-mean-ci-sigma-known-unknown-chi-square-table.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 4 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（1:03:42，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §4.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「信賴區間」→「信奈區間／性愛區間／心愛區間／信賴期間」，「pivotal quantity」→「pubal quantity／Pubular Quantity」，「樞紐量」→「輸扭亮」，「cover」→「carble」，「機率」→「激勵」。[▶ 32:00](https://youtu.be/9LkLNEAiXXQ?t=1920) 起一段、[▶ 37:16](https://youtu.be/9LkLNEAiXXQ?t=2236) 前後有少量幻聽字（「法定人數不足」「以上で終わります」），忽略。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 為什麼點估計不夠](#1-為什麼點估計不夠)
- [2. 標準常態的記號 z_α](#2-標準常態的記號-z_α)
- [3. 查表](#3-查表)
- [4. 常用的 z 值（要背）](#4-常用的-z-值要背)
- [5. 信賴區間的定義](#5-信賴區間的定義)
- [6. 信賴區間的意義：隨機區間 vs 觀察到的區間](#6-信賴區間的意義隨機區間-vs-觀察到的區間)
- [7. 樞紐量法](#7-樞紐量法)
- [8. 預告：常態平均數的信賴區間](#8-預告常態平均數的信賴區間)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/9LkLNEAiXXQ?t=0) 新的一章，專門講**信賴區間**（confidence interval）。

| 主題 | 課本 |
|---|---|
| $z_\alpha$ 記號、查標準常態表 | 附錄表 |
| 信賴區間的定義與意義 | Definition 4.2.1，p. 238 |
| 樞紐量（pivotal quantity）法 | §4.2 |

---

## 1. 為什麼點估計不夠

[▶ 00:30](https://youtu.be/9LkLNEAiXXQ?t=30)

- 統計問題：$X_1,\dots,X_n$ iid $f(x;\theta)$，$\theta$ 是**未知的常數**。
- 點估計 $\hat\theta(X_1,\dots,X_n)$ 是隨機變數，有分配。
- [▶ 02:35](https://youtu.be/9LkLNEAiXXQ?t=155) 連續型時 $P(\hat\theta=\theta)=0$：不可能相等。
- [▶ 03:35](https://youtu.be/9LkLNEAiXXQ?t=215) 點估計也不是沒道理：UMVUE、一致性（$n$ 夠大時幾乎沒差）。
- [▶ 05:06](https://youtu.be/9LkLNEAiXXQ?t=306) 但統計是**推論**（inference），講任何東西都要有**信心**（confidence）。點估計相等的機率是 0，信心是 0。
- [▶ 05:36](https://youtu.be/9LkLNEAiXXQ?t=336) 用一個點不可能，那用一個**區間**總可以吧——就有信心了。

---

## 2. 標準常態的記號 z_α

[▶ 06:07](https://youtu.be/9LkLNEAiXXQ?t=367) 信心是一種機率，所以要會算標準常態的機率。

$Z\sim N(0,1)$：$f_Z(z)=\frac{1}{\sqrt{2\pi}}e^{-z^2/2}$，$z\in\mathbb{R}$。

> **記號**（[▶ 07:11](https://youtu.be/9LkLNEAiXXQ?t=431)）：$z_\alpha$ 是使 $P(Z>z_\alpha)=\alpha$ 的點（它**以上**的機率是 $\alpha$）。

- 老師說這個符號其實有點不太對，但大家習慣這樣寫。
- [▶ 07:41](https://youtu.be/9LkLNEAiXXQ?t=461) 標準常態對 0 對稱，所以 $P(Z<-z_\alpha)=\alpha$。

[▶ 08:44](https://youtu.be/9LkLNEAiXXQ?t=524) 我們比較常用 $z_{\alpha/2}$：信賴區間通常講 $100(1-\alpha)\%$，希望**中間**的機率是 $1-\alpha$，外面一共 $\alpha$，對稱所以兩邊各 $\alpha/2$：
$$P\left(-z_{\alpha/2}<Z<z_{\alpha/2}\right)=1-\alpha.$$

只要查 $z_{\alpha/2}$，$-z_{\alpha/2}$ 就是它的負號。

[▶ 10:48](https://youtu.be/9LkLNEAiXXQ?t=648) 本來要算 $\int_{-z_{\alpha/2}}^{z_{\alpha/2}}\frac{1}{\sqrt{2\pi}}e^{-z^2/2}dz$，但這積不出來，要用數值方法，很麻煩。所以**查表**。

---

## 3. 查表

[▶ 11:49](https://youtu.be/9LkLNEAiXXQ?t=709) 課本附錄的表叫 **cumulative normal distribution**（累積常態分配），就是**分配函數**：

$$\Phi(x)=\int_{-\infty}^x\frac{1}{\sqrt{2\pi}}e^{-t^2/2}dt=P(Z\le x).$$

**怎麼查**（[▶ 13:53](https://youtu.be/9LkLNEAiXXQ?t=833)）：左邊一欄是 $x$ 的整數和第一位小數（0.0、0.1、……），上面一列是第二位小數（.00、.01、…….09），交叉處是 $\Phi(x)$。

**例**（[▶ 14:24](https://youtu.be/9LkLNEAiXXQ?t=864)）：$P(Z\le 1.33)$：左邊找 1.3，上面找 .03，得 $0.9082$。

- $P(Z\ge 1.33)=1-0.9082=0.0918$。
- [▶ 16:33](https://youtu.be/9LkLNEAiXXQ?t=993) 對稱：$P(Z\le-1.33)=P(Z\ge 1.33)=0.0918$。

---

## 4. 常用的 z 值（要背）

[▶ 17:05](https://youtu.be/9LkLNEAiXXQ?t=1025) 做信賴區間、檢定時，我們要的是「中間機率是多少」的那個點。**反查**：表裡面找機率，讀出 $x$。

| 中間機率 $1-\alpha$ | 每邊 $\alpha/2$ | 查 $\Phi=1-\alpha/2$ | $z_{\alpha/2}$ |
|---|---|---|---|
| 0.80 | 0.10 | 0.90 | 1.28 |
| 0.90 | 0.05 | 0.95 | 1.645 |
| 0.95 | 0.025 | 0.975 | 1.96 |
| 0.99 | 0.005 | 0.995 | 2.58 |
| 0.9973 | 0.00135 | 0.99865 | 3.00 |

- [▶ 19:41](https://youtu.be/9LkLNEAiXXQ?t=1181) 0.95 不會剛好在表裡：0.9495（1.64）和 0.9505（1.65）中間取 1.645。寫 1.65 或 1.64 也沒關係。

【口頭】[▶ 22:15](https://youtu.be/9LkLNEAiXXQ?t=1335) 參加外面的考試，這些都要背：考題會說「找 80%、90% 的信賴區間」，不記就不會寫。考統計所比較理論的，可以直接寫 $z_{0.05}$ 不用代數字；考比較應用的就要背。

---

## 5. 信賴區間的定義

[▶ 23:47](https://youtu.be/9LkLNEAiXXQ?t=1427)

> **定義（信賴區間）**（課本 Definition 4.2.1，p. 238）：$X_1,\dots,X_n$ 是來自 $f(x;\theta)$ 的隨機樣本，$0<\alpha<1$。若兩個**統計量** $T_1=T_1(X_1,\dots,X_n)$、$T_2=T_2(X_1,\dots,X_n)$ 滿足
> $$P_\theta(T_1<\theta<T_2)=1-\alpha,\qquad\textbf{對所有 }\theta,$$
> 則隨機區間 $(T_1,T_2)$ 叫 $\theta$ 的 **$100(1-\alpha)\%$ 信賴區間**。

- [▶ 25:22](https://youtu.be/9LkLNEAiXXQ?t=1522) $T_1,T_2$ 是統計量（隨機樣本的函數、不含 $\theta$），是隨機變數，所以 $(T_1,T_2)$ 是**隨機區間**（random interval）。
- [▶ 25:53](https://youtu.be/9LkLNEAiXXQ?t=1553) 下標 $\theta$：當 $\theta$ 是對的。因為不知道 $\theta$，所以**每個 $\theta$** 都要成立。
- [▶ 26:53](https://youtu.be/9LkLNEAiXXQ?t=1613) $1-\alpha=0.9$ 就是 90%；0.99 就是 99%。
- **為什麼叫信賴**：雖然不知道 $\theta$，但知道隨機區間**涵蓋**（cover）$\theta$ 的機率是 $1-\alpha$。這就是信心。

**怎麼算這個機率**（[▶ 29:58](https://youtu.be/9LkLNEAiXXQ?t=1798)）：$\{T_1<\theta<T_2\}$ 是一個事件，是 $(x_1,\dots,x_n)$ 的集合（讓 $\theta$ 落在 $T_1,T_2$ 中間的那些點）。機率＝joint pdf 在這個集合上積分。

【口頭】[▶ 28:28](https://youtu.be/9LkLNEAiXXQ?t=1708) 通常**不說「$\theta$ 落在區間裡」**：$\theta$ 是固定的常數，不會跑來跑去。要說「**隨機區間涵蓋 $\theta$** 的機率是 $1-\alpha$」。

---

## 6. 信賴區間的意義：隨機區間 vs 觀察到的區間

[▶ 32:00](https://youtu.be/9LkLNEAiXXQ?t=1920)

**觀察之後**（[▶ 27:55](https://youtu.be/9LkLNEAiXXQ?t=1675)）：樣本觀察到 $x_1,\dots,x_n$，代進去得 $t_1=T_1(\mathbf x)$、$t_2=T_2(\mathbf x)$，是**常數區間**。仍叫 $\theta$ 的 $100(1-\alpha)\%$ 信賴區間。

**但意義不同**（[▶ 33:38](https://youtu.be/9LkLNEAiXXQ?t=2018)）：

| | $(T_1,T_2)$（大寫） | $(t_1,t_2)$（小寫） |
|---|---|---|
| 是什麼 | 隨機區間 | 常數區間（例如 $(0.8,1.2)$） |
| 涵蓋 $\theta$ 的機率 | $1-\alpha$ | **0 或 1** |

[▶ 35:43](https://youtu.be/9LkLNEAiXXQ?t=2143) 常數區間已經固定，$\theta$ 是固定的未知數：要嘛在裡面、要嘛不在，不會「有 0.9 的機率在裡面」。

**那 $1-\alpha$ 是什麼意思？**（[▶ 38:00](https://youtu.be/9LkLNEAiXXQ?t=2280)）

- 想像可以**重複抽樣**很多次（像做模擬 simulation）。每抽一次就算出一個 $(t_1,t_2)$。
- 每一個 $(t_1,t_2)$ 涵蓋 $\theta$ 的機率是 0 或 1。
- 但在很多個 $(t_1,t_2)$ 裡，大約有 $100(1-\alpha)\%$ 個**真的涵蓋** $\theta$（例如 90%）。
- [▶ 39:32](https://youtu.be/9LkLNEAiXXQ?t=2372) $1-\alpha$ 越大，你找到的那一個區間涵蓋 $\theta$ 的信心就越大。

【口頭】[▶ 41:13](https://youtu.be/9LkLNEAiXXQ?t=2473) 讀一個新觀念，一開始都比較辛苦。不管統計或數學，都不是用背的，要了解背後的意義。

---

## 7. 樞紐量法

[▶ 41:45](https://youtu.be/9LkLNEAiXXQ?t=2505) 怎麼找 $T_1,T_2$？建造方式很多，最好的一個是**樞紐量**（pivotal quantity）。

【口頭】[▶ 43:21](https://youtu.be/9LkLNEAiXXQ?t=2601) 台灣（補習班）好像翻成「樞紐量」。

> **定義（樞紐量）**（[▶ 44:22](https://youtu.be/9LkLNEAiXXQ?t=2662)）：隨機樣本和參數的函數
> $$Q=q(X_1,\dots,X_n;\theta)$$
> 若它的**分配不依賴 $\theta$**，就叫樞紐量。

- [▶ 44:52](https://youtu.be/9LkLNEAiXXQ?t=2692) 它**不是**統計量（裡面有 $\theta$）。
- 它是隨機變數的函數，所以是隨機變數，有分配。
- [▶ 46:23](https://youtu.be/9LkLNEAiXXQ?t=2783) $X_1,\dots,X_n$ 的分配和 $\theta$ 有關；但這個函數的分配和 $\theta$ 無關。
- **例**（[▶ 47:26](https://youtu.be/9LkLNEAiXXQ?t=2846)）：$X\sim N(\mu,\sigma^2)$，$\frac{X-\mu}{\sigma}\sim N(0,1)$，分配裡沒有參數。（這只是單一 $X$ 的例子；樞紐量要的是隨機樣本的函數。）

**為什麼有用：一定找得到 $a,b$**（[▶ 48:27](https://youtu.be/9LkLNEAiXXQ?t=2907)）

- $Q$ 的 pdf $f_Q(q)$ 不含 $\theta$，積分是 1，所以一定找得到常數 $a,b$：
$$P_\theta\left(a<Q<b\right)=1-\alpha,\qquad\forall\theta.$$

**反例**（[▶ 49:27](https://youtu.be/9LkLNEAiXXQ?t=2967)）：$X\sim N(\mu,1)$。找不到**固定**的 $a,b$ 讓 $P(a<X<b)\equiv 1-\alpha$ 對所有 $\mu$ 成立：$\mu=\mu_1$ 時 $a,b$ 要在這裡，$\mu=\mu_2$ 時要跑到那裡……因為 $X$ 的分配和 $\mu$ 有關。但如果是 $N(0,1)$，取 $a=-z_{\alpha/2}$、$b=z_{\alpha/2}$ 就對所有 $\mu$ 成立，因為裡面沒有參數。

**一對一改寫成 $T_1<\theta<T_2$**（[▶ 54:33](https://youtu.be/9LkLNEAiXXQ?t=3273)）

- 不是每個樞紐量都有用。要的是：存在兩個**統計量** $T_1,T_2$，使得
$$a<q(\mathbf X;\theta)<b\iff T_1(\mathbf X)<\theta<T_2(\mathbf X).$$
- [▶ 56:09](https://youtu.be/9LkLNEAiXXQ?t=3369) 若且唯若 ⇒ 兩個事件**相等** ⇒ 機率相同：
$$P_\theta(T_1<\theta<T_2)=P_\theta(a<Q<b)=1-\alpha,\quad\forall\theta.$$
- 所以 $(T_1,T_2)$ 就是 $\theta$ 的 $100(1-\alpha)\%$ 信賴區間。

[▶ 60:15](https://youtu.be/9LkLNEAiXXQ?t=3615) 這是最普遍的方法，很多問題都能做。

【口頭】[▶ 62:52](https://youtu.be/9LkLNEAiXXQ?t=3772) 要花時間了解什麼是信賴區間、什麼是樞紐量法。這些觀念清楚，後面的方法都很簡單。

---

## 8. 預告：常態平均數的信賴區間

[▶ 60:15](https://youtu.be/9LkLNEAiXXQ?t=3615) 每個常見分配都有參數，我們都想找它的信賴區間：常態的 $\mu,\sigma^2$；Bernoulli／二項的 $p$；Poisson 的 $\lambda$。

[▶ 62:21](https://youtu.be/9LkLNEAiXXQ?t=3741) 從最簡單的開始：$X_1,\dots,X_n$ 來自 $N(\mu,\sigma^2)$，找 $\mu$ 的信賴區間。分兩種：$\sigma$ **已知**、$\sigma$ **未知**。（有時有兩個常態母體，要兩個 mean 差的信賴區間。）下次講。

---

## 9. 一頁速查表

**$z_\alpha$**：$P(Z>z_\alpha)=\alpha$；$P(-z_{\alpha/2}<Z<z_{\alpha/2})=1-\alpha$。

**常用值**：$z_{0.10}=1.28$，$z_{0.05}=1.645$，$z_{0.025}=1.96$，$z_{0.005}=2.58$，$z_{0.00135}=3$。

**查表**：表給 $\Phi(x)=P(Z\le x)$；$z_{\alpha/2}$ 就是 $\Phi=1-\alpha/2$ 的 $x$。

**信賴區間**：統計量 $T_1,T_2$，$P_\theta(T_1<\theta<T_2)=1-\alpha$，$\forall\theta$。

- 隨機區間涵蓋 $\theta$ 的機率是 $1-\alpha$。
- 觀察到的 $(t_1,t_2)$ 涵蓋 $\theta$ 的機率是 0 或 1；重複抽樣時約 $100(1-\alpha)\%$ 的區間涵蓋 $\theta$。

**樞紐量法**

1. 找 $Q=q(\mathbf X;\theta)$，分配不含 $\theta$。
2. 找 $a,b$：$P(a<Q<b)=1-\alpha$。
3. 把 $a<Q<b$ 改寫成 $T_1<\theta<T_2$（要若且唯若）。
4. $(T_1,T_2)$ 就是信賴區間。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 樞紐量法 | 下一集：常態 $\mu$（$\sigma$ 已知用 $Z$、未知用 $t$）；$\sigma^2$（用卡方） |
| $z_{\alpha/2}$ | 大樣本信賴區間、檢定 |

---

## 附：本集一句話總結

> **點估計等於 $\theta$ 的機率是 0、沒有信心，所以改找兩個統計量讓隨機區間 $(T_1,T_2)$ 涵蓋 $\theta$ 的機率對所有 $\theta$ 都是 $1-\alpha$；觀察到的區間涵蓋與否只有 0 或 1，$1-\alpha$ 是重複抽樣時涵蓋的比例；建造方法是找分配不含 $\theta$ 的樞紐量 $Q$，由 $P(a<Q<b)=1-\alpha$ 改寫成 $T_1<\theta<T_2$。**

---

*筆記依據「高等統計學」Lec04 錄影逐字稿（whisper large-v3-turbo，1:03:42）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
