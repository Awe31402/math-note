---
course: 統計學（數理統計，數學系）
episode: 9
lecture: Lec09
date: 待補
video: https://youtu.be/DtPqAsjGvKQ
notes: Hogg 8th ed. §2.2 二元變換；§4.1 隨機樣本（Definition 4.1.1，p. 226）、統計量（Definition 4.1.2，p. 226）；§2.4 Theorem 2.4.5 獨立 ⇔ joint mgf 可分解（p. 122）
---

# 第 9 集 · Lec09：變換例題 $X_1\pm X_2$；隨機樣本、參數、統計量；mgf 與獨立 [▶ 影片](https://youtu.be/DtPqAsjGvKQ)

← 上一集：[08](08-multivariate-transformation-jacobian.md) ｜ [總目錄](../README.md) ｜ 下一集：[10](10-independence-lemmas-chi-square-sum-xbar-normal.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 9 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（1:04:06，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §2.2、§2.4、§4.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `【課堂討論】` 講者問、學生答
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「iid」→「RID」，「Jacobian」→「吃過餅／夾殼餅／夾科病」，「反函數」→「法然數／法藍素」，「parameter $\theta$」→「seta／sitter」，「Lemma」→「LEMA」，「若且唯若」→「弱解為弱／弱且微弱」，「random sample」→「rand ensemble」，「joint」→「Join／Jone」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 例題：iid U(0,1)，求 X₁＋X₂ 與 X₁−X₂ 的分配](#1-例題iid-u01求-x₁x₂-與-x₁x₂-的分配)
  - [1.1 joint pdf 與範圍 A](#11-joint-pdf-與範圍-a)
  - [1.2 一對一、反函數、Jacobian](#12-一對一反函數jacobian)
  - [1.3 範圍 B：把四條邊映過去](#13-範圍-b把四條邊映過去)
  - [1.4 joint pdf 與 marginal pdf](#14-joint-pdf-與-marginal-pdf)
  - [1.5 只給一個 Y 的時候](#15-只給一個-y-的時候)
- [2. 機率的名詞 vs 統計的名詞](#2-機率的名詞-vs-統計的名詞)
- [3. 隨機樣本](#3-隨機樣本)
- [4. 參數](#4-參數)
- [5. 統計量](#5-統計量)
- [6. 統計推論](#6-統計推論)
- [7. mgf 的三個用途；joint mgf](#7-mgf-的三個用途joint-mgf)
- [8. 定理：獨立 ⇔ joint mgf＝個別 mgf 相乘](#8-定理獨立--joint-mgf個別-mgf-相乘)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本對應 |
|---|---|
| 二元變換的完整例題 | §2.2 |
| 隨機樣本＝iid 隨機變數 | Definition 4.1.1，p. 226 |
| 參數、統計量 | Definition 4.1.2，p. 226 |
| 統計推論 | §4.1 |
| joint mgf；獨立 ⇔ mgf 可分解 | Theorem 2.4.5，p. 122 |

---

## 1. 例題：iid U(0,1)，求 X₁＋X₂ 與 X₁−X₂ 的分配

[▶ 00:31](https://youtu.be/DtPqAsjGvKQ?t=31)

> **題目**：$X_1,X_2$ iid $\sim U(0,1)$。令 $Y_1=X_1+X_2$，$Y_2=X_1-X_2$。求 $Y_1,Y_2$ 的分配。

- 為什麼只寫一個分配？因為 i.d.（同分配），兩個一樣，寫一個就好。
- [▶ 02:32](https://youtu.be/DtPqAsjGvKQ?t=152) 兩個變成兩個 → 用上一集的變換公式：
$$f_{Y_1,Y_2}(y_1,y_2)=f_{X_1,X_2}\left(w_1(y_1,y_2),w_2(y_1,y_2)\right)|J|.$$

[▶ 03:33](https://youtu.be/DtPqAsjGvKQ?t=213) 從公式看出要做的事：

1. 找 $X_1,X_2$ 的 joint pdf。
2. 確認一對一（要用反函數）。
3. 找 $X_1,X_2$ 的範圍 $A$（space），才能找 $Y_1,Y_2$ 的範圍 $B$。
4. 算 Jacobian，得 joint pdf。
5. 積掉一個得另一個的 marginal pdf。

### 1.1 joint pdf 與範圍 A

[▶ 05:06](https://youtu.be/DtPqAsjGvKQ?t=306)

- **獨立** ⇒ joint pdf＝個別 pdf 相乘：$f(x_1,x_2)=f_{X_1}(x_1)f_{X_2}(x_2)$。
- **同分配**，都是 $U(0,1)$：$f(x)=\frac{1}{1-0}=1$，$0<x<1$；其他是 0。

[▶ 07:11](https://youtu.be/DtPqAsjGvKQ?t=431) 兩個相乘：兩個都是 1 才是 1；有一個是 0 就是 0。

$$f(x_1,x_2)=\begin{cases}1, & 0<x_1<1,\ 0<x_2<1\\ 0, & \text{其他}\end{cases}$$

$$A=\{(x_1,x_2): 0<x_1<1,\ 0<x_2<1\}\quad(\text{單位正方形}).$$

### 1.2 一對一、反函數、Jacobian

[▶ 09:15](https://youtu.be/DtPqAsjGvKQ?t=555) **技巧**：確認一對一和找反函數可以**同時做**。給定 $y_1,y_2$（不管是多少），解 $x_1,x_2$：

$$\begin{cases}y_1=x_1+x_2\\ y_2=x_1-x_2\end{cases}$$

- 兩式相加：$2x_1=y_1+y_2$ ⇒ $x_1=\frac{y_1+y_2}{2}$。
- 兩式相減：$2x_2=y_1-y_2$ ⇒ $x_2=\frac{y_1-y_2}{2}$。

[▶ 10:48](https://youtu.be/DtPqAsjGvKQ?t=648) 不管 $y_1,y_2$ 是多少，只解得**一組**解 ⇒ 一對一。（解出兩組以上就不是一對一。）

**Jacobian**（[▶ 12:19](https://youtu.be/DtPqAsjGvKQ?t=739)）：
$$J=\det\begin{pmatrix}\frac12 & \frac12\\[1mm] \frac12 & -\frac12\end{pmatrix}=-\frac14-\frac14=-\frac12,\qquad |J|=\frac12.$$

### 1.3 範圍 B：把四條邊映過去

[▶ 14:24](https://youtu.be/DtPqAsjGvKQ?t=864) $A$ 是正方形。做法：把四條邊映過去，得到四條線，夾在中間的就是 $B$。

| $A$ 的邊 | 代入 | $(y_1,y_2)$ 平面上的線 |
|---|---|---|
| $x_1=0$ | $y_1=x_2$，$y_2=-x_2$ | $y_2=-y_1$ |
| $x_1=1$ | $y_1=1+x_2$，$y_2=1-x_2$ | $y_1+y_2=2$ |
| $x_2=0$ | $y_1=x_1$，$y_2=x_1$ | $y_2=y_1$ |
| $x_2=1$ | $y_1=x_1+1$，$y_2=x_1-1$ | $y_1-y_2=2$ |

$B$ 是頂點 $(0,0)$、$(1,1)$、$(2,0)$、$(1,-1)$ 的正方形（轉了 45°）：

$$B=\{(y_1,y_2): |y_2|<y_1,\ |y_2|<2-y_1\}.$$

### 1.4 joint pdf 與 marginal pdf

[▶ 19:14](https://youtu.be/DtPqAsjGvKQ?t=1154) 代入：在 $B$ 裡 $f_{X_1,X_2}(w_1,w_2)=1$，乘 $|J|=\frac12$：

$$f_{Y_1,Y_2}(y_1,y_2)=\begin{cases}\frac12, & (y_1,y_2)\in B\\ 0, & \text{其他}\end{cases}$$

**$Y_1$ 的 marginal pdf**（[▶ 20:15](https://youtu.be/DtPqAsjGvKQ?t=1215)）：$y_1\in(0,2)$，但不能一次積完，要在 $y_1=1$ 切開：

- $0<y_1<1$：$y_2$ 從下邊 $y_2=-y_1$ 積到上邊 $y_2=y_1$：
$$f_{Y_1}(y_1)=\int_{-y_1}^{y_1}\frac12\,dy_2=y_1.$$
- $1\le y_1<2$：$y_2$ 從 $y_2=y_1-2$ 積到 $y_2=2-y_1$：
$$f_{Y_1}(y_1)=\int_{y_1-2}^{2-y_1}\frac12\,dy_2=2-y_1.$$
- 其他：0。

**$Y_2$ 的 marginal pdf**（[▶ 22:51](https://youtu.be/DtPqAsjGvKQ?t=1371)）：$y_2\in(-1,1)$，在 $y_2=0$ 切開：

- $-1<y_2<0$：$y_1$ 從 $-y_2$ 積到 $2+y_2$：$f_{Y_2}(y_2)=\frac12(2+2y_2)=1+y_2$。
- $0\le y_2<1$：$y_1$ 從 $y_2$ 積到 $2-y_2$：$f_{Y_2}(y_2)=\frac12(2-2y_2)=1-y_2$。
- 其他：0。

（兩個都是三角形分配。驗算：$\int_0^1y\,dy+\int_1^2(2-y)\,dy=\frac12+\frac12=1$。✓）

[▶ 24:23](https://youtu.be/DtPqAsjGvKQ?t=1463) 【口頭】變數轉換考試通常考這種類型。每題有自己的技巧，但公式和步驟都一樣，要會。

### 1.5 只給一個 Y 的時候

[▶ 24:53](https://youtu.be/DtPqAsjGvKQ?t=1493)

- 題目常只給 $Y_1$，沒給 $Y_2$。那 $Y_2$ 要**自己定**，讓它一對一。
- [▶ 25:54](https://youtu.be/DtPqAsjGvKQ?t=1554) 可以定很多種不同的 $Y_2$，得到的 joint pdf 不一樣，但最後 $Y_1$ 的 pdf **一定一樣**。
- [▶ 26:24](https://youtu.be/DtPqAsjGvKQ?t=1584) 變換的方法有很多：分配函數法、mgf 法、這個公式。老師說比較常用的是 mgf 法；這種公式題是外面考試常考的，練習會不會做變換。

---

## 2. 機率的名詞 vs 統計的名詞

[▶ 26:54](https://youtu.be/DtPqAsjGvKQ?t=1614) 【口頭】老師畫了一個圓圓的東西：中文叫西瓜，英文叫 watermelon，台語、客家話各有叫法。同一個東西，不同環境有不同名字。（老師的小孩五年級要去美國一年時問：「美國人真的不會講國語嗎？」）

[▶ 28:30](https://youtu.be/DtPqAsjGvKQ?t=1710) 統計和機率常用同一個東西但名字不同。機率從數學角度取名，而且機率不只統計在用（工業工程、機械、電子都用）。前面講的多是機率；現在開始講統計，有些東西會換名字。

---

## 3. 隨機樣本

[▶ 29:34](https://youtu.be/DtPqAsjGvKQ?t=1774)

- 「iid 隨機變數」是**機率**名詞：獨立（joint pdf＝marginal 相乘）、同分配（pdf 完全重疊）。很數學，沒有統計意義。
- [▶ 31:07](https://youtu.be/DtPqAsjGvKQ?t=1867) 統計把它叫 **random sample（隨機樣本）**。

> **定義（隨機樣本）**（課本 Definition 4.1.1，p. 226）：$X_1,\dots,X_n$ iid ⇔ $X_1,\dots,X_n$ 是一組隨機樣本。

**為什麼要「隨機」**（[▶ 31:39](https://youtu.be/DtPqAsjGvKQ?t=1899)）【口頭】：

- 推新產品（手機、化妝品）前，先抽一些人試用。10 個裡 6 個說好，大概能賣；只有 1、2 個說好，可能有副作用，賣了會虧。
- 不能找自己家族的人（姓陳的找陳家人，大家都說好）；新竹市選市長，不能只在眷村抽，得到 100% 支持也不準。這是**偏的樣本**。
- [▶ 33:11](https://youtu.be/DtPqAsjGvKQ?t=1991) 隨機：新竹市 40 萬人，**每個人被抽到的機會一樣** → 同分配。這次抽和下次抽**沒關係** → 獨立。
- 不能這次抽新竹市、下次抽新竹縣：母體不同，分配不同。

【口頭】寫統計時盡量用「隨機樣本」，寫機率時盡量用「iid 隨機變數」，但實際上常換來換去。

**隨機樣本的 joint pdf**（[▶ 35:45](https://youtu.be/DtPqAsjGvKQ?t=2145)）：$X_1,\dots,X_n$ 是來自 pdf $f_0(x)$ 的隨機樣本。

1. 獨立 ⇒ $f(x_1,\dots,x_n)=f_1(x_1)f_2(x_2)\cdots f_n(x_n)$。
2. 同分配 ⇒ $f_1=\cdots=f_n=f_0$。

$$f(x_1,\dots,x_n)=\prod_{i=1}^{n}f_0(x_i).$$

「相乘」來自 I（獨立）；「都是 $f_0$」來自 i.d.；裡面是 $x_1,\dots,x_n$ 不同的值（同分配但發生的值不同）。

---

## 4. 參數

[▶ 39:29](https://youtu.be/DtPqAsjGvKQ?t=2369)

進入統計後，pdf 不再寫 $f(x)$，而寫

$$f(x;\theta).$$

- 函數 $f$ 的**形式是知道的**，但裡面有個 $\theta$ 是**未知的常數**。
- [▶ 41:01](https://youtu.be/DtPqAsjGvKQ?t=2461) $\theta$ 叫**參數**（parameter）。

例：

| 分配 | 參數（可能未知） |
|---|---|
| $N(\mu,\sigma^2)$ | $\mu$、$\sigma^2$ |
| Poisson$(\lambda)$ | $\lambda$ |
| $b(n,p)$ | $p$ |
| $\Gamma(\alpha,\beta)$ | $\alpha$、$\beta$ |

常態 pdf 的公式我們會寫，但裡面的 $\mu,\sigma^2$ 不知道。

[▶ 43:05](https://youtu.be/DtPqAsjGvKQ?t=2585) 【口頭】**為什麼有統計**：如果分配完全知道，要什麼都有（例如 $P(a<X<b)$ 積分就好），就不需要統計。統計就是因為不完全知道 pdf 長什麼樣子。

---

## 5. 統計量

[▶ 43:36](https://youtu.be/DtPqAsjGvKQ?t=2616)

$n$ 個隨機變數是 $n$ 維的東西。做統計通常要把它**濃縮、簡化**：取一個函數。

> **定義（統計量，statistic）**（課本 Definition 4.1.2，p. 226）：隨機樣本 $X_1,\dots,X_n$ 的函數 $T=g(X_1,\dots,X_n)$，**裡面不含未知參數**。

- [▶ 44:08](https://youtu.be/DtPqAsjGvKQ?t=2648) 中文叫**統計量**。statistics（加 s）是統計學；也可以是兩個以上統計量的複數。

**是統計量的例子**：

- **樣本平均數**（sample mean，[▶ 44:39](https://youtu.be/DtPqAsjGvKQ?t=2679)）：
$$\bar X=\frac1n\sum_{i=1}^nX_i.$$
- **樣本變異數**（sample variance，[▶ 45:10](https://youtu.be/DtPqAsjGvKQ?t=2710)）：
$$S^2=\frac{1}{n-1}\sum_{i=1}^n\left(X_i-\bar X\right)^2.$$
  為什麼除以 $n-1$ 不是 $n$？有些書除以 $n$。老師統一除以 $n-1$，理由後面講。
- **指示函數**（indicator function，[▶ 45:42](https://youtu.be/DtPqAsjGvKQ?t=2742)）：$I(X_1\ge 0)$，$X_1\ge 0$ 時是 1，否則是 0。只用到 $X_1$ 也沒關係，還是 $X_1,\dots,X_n$ 的函數。

**不是統計量的例子**（[▶ 46:43](https://youtu.be/DtPqAsjGvKQ?t=2803)）：
$$\frac1n\sum_{i=1}^n(X_i-\mu)^2,$$
因為 $\mu$ 是未知參數。

---

## 6. 統計推論

[▶ 47:48](https://youtu.be/DtPqAsjGvKQ?t=2868) 【口頭】我們一直在做準備，還沒講到統計的核心。核心是：隨機變數的分配裡有不知道的參數 $\theta$，**怎麼去了解 $\theta$**。

- 現在的統計學常叫 *Statistical Inference*（統計推論）。
- [▶ 48:49](https://youtu.be/DtPqAsjGvKQ?t=2929) 推論：只給你一點點東西（一組樣本），用它推論背後不知道的東西。
- 例：想知道新竹市民對某產品的偏好，抽 100 人。100 人不等於全體，但要用它了解整個**母體**（population）。
- 推論有很多方法（所以 inferences 加 s）；用**機率**的觀點做推論。講到推論時才是正式講統計。

---

## 7. mgf 的三個用途；joint mgf

[▶ 49:50](https://youtu.be/DtPqAsjGvKQ?t=2990)

| | 用途 | 狀態 |
|---|---|---|
| 1 | 生成動差：$M^{(k)}(0)=E(X^k)$ | 已證 |
| 2 | 導出分配：mgf 和分配一對一 | 已講 |
| 3 | 判斷隨機變數是否**獨立** | 本集 |

**joint mgf**（[▶ 53:24](https://youtu.be/DtPqAsjGvKQ?t=3204)）：$n$ 個隨機變數，每個配一個 $t_i$：

$$M_{X_1,\dots,X_n}(t_1,\dots,t_n)=E\left(e^{t_1X_1+\cdots+t_nX_n}\right).$$

取期望值是對 $X_1,\dots,X_n$ 做 $n$ 重積分，積完 $x_i$ 就不見了，剩下 $t_1,\dots,t_n$ 的函數。

---

## 8. 定理：獨立 ⇔ joint mgf＝個別 mgf 相乘

[▶ 54:57](https://youtu.be/DtPqAsjGvKQ?t=3297)

> **Lemma**（課本 Theorem 2.4.5，p. 122）：
> $$X_1,X_2\text{ 獨立}\iff M_{X_1,X_2}(t_1,t_2)=M_{X_1}(t_1)M_{X_2}(t_2)\quad\text{對所有 }t_1,t_2.$$

用途：要證獨立，就證 mgf 可分解；已知獨立，joint mgf 就是相乘。

**證明（⇒）**（[▶ 56:32](https://youtu.be/DtPqAsjGvKQ?t=3392)）：設獨立，$f(x_1,x_2)=f_{X_1}(x_1)f_{X_2}(x_2)$。

$$M_{X_1,X_2}(t_1,t_2)=\iint e^{t_1x_1+t_2x_2}f(x_1,x_2)\,dx_1dx_2=\iint e^{t_1x_1}f_{X_1}(x_1)\cdot e^{t_2x_2}f_{X_2}(x_2)\,dx_1dx_2.$$

被積函數拆成「只有 $x_1$」×「只有 $x_2$」，範圍都是 $(-\infty,\infty)$，拆成兩個積分相乘：

$$=\int e^{t_1x_1}f_{X_1}(x_1)\,dx_1\cdot\int e^{t_2x_2}f_{X_2}(x_2)\,dx_2=M_{X_1}(t_1)M_{X_2}(t_2).$$

**證明（⇐）**（[▶ 60:06](https://youtu.be/DtPqAsjGvKQ?t=3606)）：設 $M_{X_1,X_2}(t_1,t_2)=M_{X_1}(t_1)M_{X_2}(t_2)$。右邊寫成積分再合併：

$$M_{X_1}(t_1)M_{X_2}(t_2)=\iint e^{t_1x_1+t_2x_2}\,f_{X_1}(x_1)f_{X_2}(x_2)\,dx_1dx_2.$$

- 左邊是 joint pdf $f(x_1,x_2)$ 的 joint mgf。
- 右邊是 $f_{X_1}(x_1)f_{X_2}(x_2)$（也是一個 pdf）的 joint mgf。
- [▶ 62:07](https://youtu.be/DtPqAsjGvKQ?t=3727) 兩個分配的 mgf 相同 ⇒ 分配相同（mgf 和分配一對一）⇒ $f(x_1,x_2)=f_{X_1}(x_1)f_{X_2}(x_2)$ ⇒ 獨立。∎

【課本補充】這裡用的是**多變數** mgf 的唯一性（joint mgf 決定 joint 分配）。課本 Theorem 2.4.5 的證明也這樣寫，並說明它是單變數唯一性定理的推廣。

【口頭】這個證明要自己會證一遍。

---

## 9. 一頁速查表

**變換題步驟**：joint pdf（獨立就相乘）→ 範圍 $A$ → 解反函數（唯一解＝一對一）→ $J$ → 四條邊映過去得 $B$ → $f_Y=f_X(w)|J|$ → 分段積掉另一個。

**例題結果**（$X_1,X_2$ iid $U(0,1)$）：

- $x_1=\frac{y_1+y_2}2$，$x_2=\frac{y_1-y_2}2$，$|J|=\frac12$；$f_{Y_1,Y_2}=\frac12$ on $B$（頂點 $(0,0),(1,1),(2,0),(1,-1)$）。
- $f_{Y_1}(y)=y$（$0<y<1$），$2-y$（$1\le y<2$）。
- $f_{Y_2}(y)=1+y$（$-1<y<0$），$1-y$（$0\le y<1$）。

**名詞**

| 機率 | 統計 |
|---|---|
| iid 隨機變數 | 隨機樣本 |

- 隨機樣本 joint pdf：$\prod_{i=1}^nf(x_i;\theta)$。
- 參數 $\theta$：pdf 形式已知、裡面未知的常數。
- 統計量：樣本的函數、**不含未知參數**。$\bar X$、$S^2=\frac{1}{n-1}\sum(X_i-\bar X)^2$ 是；$\frac1n\sum(X_i-\mu)^2$ 不是。

**joint mgf 與獨立**：$X_1\perp X_2\iff M(t_1,t_2)=M_{X_1}(t_1)M_{X_2}(t_2)$。

- ⇒：被積函數可分離 → 兩個積分相乘。
- ⇐：兩邊是兩個分配的 joint mgf → mgf 唯一性 → joint pdf＝marginal 相乘。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 隨機樣本、統計量 | 之後所有統計推論 |
| $\bar X$、$S^2$ | 抽樣分配（常態母體下的 $\bar X$、$S^2$） |
| 獨立 ⇔ mgf 可分解 | 獨立隨機變數之和的 mgf＝mgf 相乘 |

---

## 附：本集一句話總結

> **用變換公式求出兩個獨立均勻變數的和與差都是三角形分配；統計把 iid 隨機變數叫隨機樣本、把 pdf 裡未知的常數叫參數、把不含參數的樣本函數叫統計量；兩個隨機變數獨立若且唯若 joint mgf 等於個別 mgf 相乘。**

---

*筆記依據「統計學」Lec09 錄影逐字稿（whisper large-v3-turbo，1:04:06）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
