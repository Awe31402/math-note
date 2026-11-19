---
course: Number Theory（2021 秋，線上錄影）
episode: 2
lecture: 2021-08-16 第 2 部
date: 2021-08-16
video: https://youtu.be/guJluWw1ArE
notes: Jones & Jones《Elementary Number Theory》附錄 B（書頁 244–245，PDF 頁 259–260）；§11.5 Theorem 11.3（書頁 223，PDF 頁 238）；Diophantus 的單位圓做法課本沒有
---

# 第 2 集 · 數系：性質 vs 構造（Number Systems and Their Properties vs. Construction） [▶ 影片](https://youtu.be/guJluWw1ArE)

← 上一集：[01-history-of-numbers](01-history-of-numbers.md) ｜ [總目錄](README.md) ｜ 下一集：[03-divisibility-euclid-algorithm-1](03-divisibility-euclid-algorithm-1.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 2 集（2021-08-16 第 2 部，接第 1 集）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（18:52，自動字幕）＋ Jones & Jones《Elementary Number Theory》附錄 B、§11.5
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 用矩陣乘法看複數乘法](#1-用矩陣乘法看複數乘法)
- [2. 複數「是」矩陣嗎？模型 vs 本體](#2-複數是矩陣嗎模型-vs-本體)
- [3. 為什麼在乎 R 和 C](#3-為什麼在乎-r-和-c)
- [4. C 的運算性質：子集合直接繼承](#4-c-的運算性質子集合直接繼承)
- [5. 課程前三分之一的路線](#5-課程前三分之一的路線)
- [6. Diophantus：用單位圓找畢氏三元數組](#6-diophantus用單位圓找畢氏三元數組)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

接著第 1 集最後「$i\cdot i$ 等於多少」講下去。

| 主題 | 時間 | 課本 |
|---|---|---|
| 矩陣乘法 = 複數乘法 | 00:04 | — |
| 模型 vs 本體 | 02:55 | — |
| $\mathbb{R}$、$\mathbb{C}$ 的意義；體的定義 | 04:32 | 附錄 B |
| $\mathbb{C}$ 的運算性質 | 06:42 | 附錄 B |
| 課程路線 | 10:48 | — |
| Diophantus 的單位圓做法 | 14:43 | §11.5（結果） |

---

## 1. 用矩陣乘法看複數乘法

[▶ 00:04](https://youtu.be/guJluWw1ArE?t=4)

第 1 集把 $a+ib$ 對應到矩陣 $\begin{pmatrix} a & -b\\ b & a\end{pmatrix}$，$i$ 對應到 $\begin{pmatrix} 0 & -1\\ 1 & 0\end{pmatrix}$。

**$i\cdot i$**：
$$\begin{pmatrix} 0 & -1\\ 1 & 0\end{pmatrix}\begin{pmatrix} 0 & -1\\ 1 & 0\end{pmatrix} = \begin{pmatrix} -1 & 0\\ 0 & -1\end{pmatrix} = -I.$$
$-I$ 是「負的單位矩陣」，扮演 $-1$。所以 $i^2=-1$。

**一般的乘法** [▶ 00:36](https://youtu.be/guJluWw1ArE?t=36)：

$$\begin{pmatrix} a & -b\\ b & a\end{pmatrix}\begin{pmatrix} c & -d\\ d & c\end{pmatrix} = \begin{pmatrix} ac-bd & -(ad+bc)\\ ad+bc & ac-bd\end{pmatrix}.$$

> ⚠️ 逐字稿缺字 [▶ 01:24](https://youtu.be/guJluWw1ArE?t=84)：字幕的矩陣元素很亂（「a d minus b c minus bd」「minus a d minus bc」），講者自己也說寫錯一個字被學生指正（第二個矩陣右下角應是 $c$，不是 $d$）。上式是依矩陣乘法重算的。

結果還是 $\begin{pmatrix} p & -q\\ q & p\end{pmatrix}$ 的形狀，其中 $p=ac-bd$、$q=ad+bc$。換回複數記號 [▶ 01:54](https://youtu.be/guJluWw1ArE?t=114)：

$$(a+ib)(c+id) = (ac-bd) + i\,(ad+bc).$$

這**正是**複數乘法的公式。

【口頭】講者的教學建議：有些學生會說「複數不存在，連你們自己都承認一半是 imaginary（虛的）」。講者說這些名字「很糟糕」。對付的辦法：問他承不承認「2×2 的一格一格數字」存在？承認的話，就拿這種形狀的矩陣給他看，用他「半懂」的矩陣乘法，證明複數乘法這種東西確實存在。

---

## 2. 複數「是」矩陣嗎？模型 vs 本體

[▶ 02:55](https://youtu.be/guJluWw1ArE?t=175)

講者的答案：**不是。** 「我把複數想成複數。」

他腦中的數系是一層包一層：
$$\mathbb{N}\subseteq\mathbb{Z}\subseteq\mathbb{Q}\subseteq\mathbb{R}\subseteq\mathbb{C}.$$

**為什麼不能堅持「複數就是矩陣」** [▶ 03:27](https://youtu.be/guJluWw1ArE?t=207)：如果複數**真的就是**這些矩陣，那 $\mathbb{N}\subseteq\mathbb{C}$ 就逼你也要說「自然數 $n$ 就是矩陣 $\begin{pmatrix} n & 0\\ 0 & n\end{pmatrix}$」。這太荒謬了。

**所以矩陣只是一個模型** [▶ 04:01](https://youtu.be/guJluWw1ArE?t=241)：它證明了「滿足這些規則的東西**存在**」。有了這個保證，我們就放心直接寫 $a+bi$，約定：

- 加法：實部加實部，虛部加虛部。
- 乘法：照上面的公式。

**另一個模型**：取 $\mathbb{R}^2$（實數的有序對），在上面定義一個特別的乘法，然後證明它滿足複數系統的所有公理。

（這呼應第 1 集 5.4 節：數系「是」它滿足的那組公理，具體模型只是一種實現。）

---

## 3. 為什麼在乎 R 和 C

[▶ 04:32](https://youtu.be/guJluWw1ArE?t=272)

| 數系 | 在數論裡的意義 |
|---|---|
| $\mathbb{N}$、$\mathbb{Q}$ | **丟番圖方程**（Diophantine equation）：找多項式方程的自然數解或有理數解 |
| $\mathbb{R}$ | $\mathbb{Q}$ 的**完備化**——「分析進場了」 |
| $\mathbb{C}$ | **代數基本定理**（fundamental theorem of algebra）：任何多項式在 $\mathbb{C}$ 上都能完全分解成一次因式。講者說 $\mathbb{C}$ 是「代數完備的體」 |

> **體**（field）[▶ 05:02](https://youtu.be/guJluWw1ArE?t=302)：有單位元素的**交換環**，而且**每個非零元素都有乘法反元素**。

$\mathbb{Q}$、$\mathbb{R}$、$\mathbb{C}$ 都是體。

> 【課本補充】附錄 B（p. 245）：「單位」（unit）是有乘法反元素的元素；體就是「每個非零元素都是單位」的環。課本也提到 $\mathbb{Z}_n$ 在 $n$ 是質數時是體（第 7–8 集會碰到）。完整的環定義見[第 1 集 5.2 節](01-history-of-numbers.md#52-環整環體)。

【口頭】講者問學生抽象代數有沒有教到體，「每間學校不一樣」。他說本課要「補完你們對環、體、整環的認識」，之後會仔細定義。

【口頭】[▶ 06:03](https://youtu.be/guJluWw1ArE?t=363) 中間有一段在講排課（有學生的實分析課在星期二晚上，無法改時間），跟內容無關。

---

## 4. C 的運算性質：子集合直接繼承

[▶ 06:42](https://youtu.be/guJluWw1ArE?t=402)

講者列出 $\mathbb{C}$ 的運算性質（「你們不會意外」）。對所有 $x,y,z\in\mathbb{C}$：

**加法**

| 性質 | 式子 |
|---|---|
| 交換律（commutativity） | $x+y=y+x$ |
| 結合律（associativity） | $(x+y)+z = x+(y+z)$ |
| 加法單位元素 0 | $x+0=x=0+x$ |
| 加法反元素（additive inverse） | 每個 $x$ 都有 $-x$，使 $x+(-x)=0$ |

講者說最後一條也可以叫「對取負封閉」（closure under negation）。【口頭】這四條合起來，就是說加法構成一個**交換群**（abelian group）。任何環的加法都有這個結構。

**乘法** [▶ 08:44](https://youtu.be/guJluWw1ArE?t=524)

| 性質 | 式子 |
|---|---|
| 交換律 | $xy=yx$ |
| 結合律 | $(xy)z=x(yz)$ |
| 乘法單位元素 1 | $x\cdot 1 = x = 1\cdot x$ |

**分配律**（distributive law）[▶ 09:46](https://youtu.be/guJluWw1ArE?t=586)

$$(x+y)z = xz+yz,\qquad x(y+z) = xy+xz.$$

**其他** [▶ 10:17](https://youtu.be/guJluWw1ArE?t=617)

$$-x = (-1)\cdot x,\qquad 0\cdot x = 0.$$

【口頭】「乘以 $-1$ 等於取負，這一點都不明顯」。在**抽象的環**裡，這可以從上面的公理證明出來。這類證明可能會在最後三分之一學期（抽象代數部分）當作業。

> 以下**不是逐字稿內容**，是補上「$0\cdot x=0$ 可以從公理推出來」的關鍵一步：
> $0\cdot x = (0+0)\cdot x = 0\cdot x + 0\cdot x$（用 $0+0=0$ 和分配律）。兩邊加上 $-(0\cdot x)$，得 $0 = 0\cdot x$。
> 然後 $x + (-1)x = 1\cdot x + (-1)x = (1+(-1))x = 0\cdot x = 0$，所以 $(-1)x$ 就是 $x$ 的加法反元素 $-x$。

**重點：子集合直接繼承這些性質** [▶ 08:14](https://youtu.be/guJluWw1ArE?t=494)

這些性質 $\mathbb{C}$ 都有，所以**任何 $\mathbb{C}$ 的子集合**也都有——$\mathbb{R}$、$\mathbb{Q}$、$\mathbb{Z}$、$\mathbb{N}$，還有之後會看的更有趣的例子（例如高斯整數）。

- 本課幾乎都在看 $\mathbb{C}$ 或它的子集合。
- 所以每次介紹新例子時，**只要檢查封閉性**（closure：運算的結果還在這個子集合裡），不用每次重新驗結合律、交換律、分配律。「每次都驗結合律會很煩。」

> 以下**不是逐字稿內容**，是舉例說明怎麼用：
> 要說高斯整數 $\mathbb{Z}[i]=\{a+bi : a,b\in\mathbb{Z}\}$ 是個環，只要檢查：$0,1$ 在裡面；加、減、乘的結果還在裡面。例如
> $$(a+bi)(c+di) = (ac-bd)+(ad+bc)i,$$
> $ac-bd$ 和 $ad+bc$ 還是整數，所以乘法封閉。交換律、結合律、分配律都從 $\mathbb{C}$ 繼承，不用驗。

---

## 5. 課程前三分之一的路線

[▶ 10:48](https://youtu.be/guJluWw1ArE?t=648)

【口頭】講者說前三分之一不會把大家拖進抽象環論，會盡量具體：

1. 整數、質數、整除
2. 同餘（congruence），怎麼用同餘計算
3. **RSA 加密**——第一次考試前的最後一個主題。要做加密，只需要「扎實的模運算計算」。

**課程網站** [▶ 11:49](https://youtu.be/guJluWw1ArE?t=709)：【口頭】講者展示個人網站，有辦公時間、上次教這門課的網站。舊講義「基本上是把 Stillwell 抄一遍、加幾個例子」，這次不想照著走，想「開一條新路、增加價值」，但偶爾會回去用。

---

## 6. Diophantus：用單位圓找畢氏三元數組

[▶ 14:43](https://youtu.be/guJluWw1ArE?t=883)

講者在螢幕上秀出舊講義第 1 講（「直接取自 Stillwell」），很快帶過。公式大多在螢幕上，沒唸出來。以下 Step 2–4 依講者口述的步驟重建。

### Step 1：把整數問題變成有理數問題

要找正整數 $a,b,c$ 使 $a^2+b^2=c^2$。因為找的是非零解，兩邊除以 $c^2$：

$$\left(\frac ac\right)^2+\left(\frac bc\right)^2 = 1.$$

令 $x=a/c$、$y=b/c$，問題變成：

> 在**單位圓** $x^2+y^2=1$ 上，找**座標都是有理數**的點。

【口頭】「Diophantus 的招數：解整數問題，改成找有理數解。」幾何上很漂亮。

### Step 2：從 $(-1,0)$ 畫直線

[▶ 15:45](https://youtu.be/guJluWw1ArE?t=945)

$(-1,0)$ 是圓上的有理點。設 $R=(x,y)$ 是另一個有理點，連起來的直線斜率為 $t$。

- 兩個點的座標都是有理數，所以**斜率 $t$ 也是有理數**。
- 直線方程：$y = t\,(x+1)$。

### Step 3：代回圓的方程

[▶ 16:16](https://youtu.be/guJluWw1ArE?t=976)

講者說他是配方，得到 $(x+\alpha)^2=\beta^2$ 的形式，所以 $x=-\alpha\pm\beta$（$\alpha,\beta$ 是上面算式定義的，螢幕上有，沒唸出）。

> 以下**不是逐字稿內容**，是依講者說的步驟補算：
> 把 $y=t(x+1)$ 代入 $x^2+y^2=1$：
> $$x^2+t^2(x+1)^2 = 1 \iff (1+t^2)x^2 + 2t^2x + (t^2-1) = 0.$$
> 除以 $1+t^2$ 後配方，$\alpha = \dfrac{t^2}{1+t^2}$、$\beta=\dfrac{1}{1+t^2}$：
> $$\left(x+\frac{t^2}{1+t^2}\right)^2 = \frac{t^4 - (t^2-1)(1+t^2)}{(1+t^2)^2} = \frac{1}{(1+t^2)^2}.$$
> 所以 $x = \dfrac{-t^2\pm 1}{1+t^2}$。取 $-$ 號得 $x=-1$，就是出發點；取 $+$ 號得新的點：
> $$x = \frac{1-t^2}{1+t^2},\qquad y = t(x+1) = \frac{2t}{1+t^2}.$$

### Step 4：令 $t=v/u$

[▶ 16:46](https://youtu.be/guJluWw1ArE?t=1006)

講者說「令 $t=v/u$ 代進去，再做一點手腳，就回到第 1 集學生說的那組公式」。

> 以下**不是逐字稿內容**，是補算：
> $t=v/u$ 代入，上下同乘 $u^2$：
> $$x = \frac{u^2-v^2}{u^2+v^2},\qquad y = \frac{2uv}{u^2+v^2}.$$
> 因為 $x=a/c$、$y=b/c$，取 $a=u^2-v^2$、$b=2uv$、$c=u^2+v^2$（或它們的倍數），就是第 1 集的 Euclid 公式。

> 【課本補充】§11.5 Theorem 11.3（p. 223）給出同樣的結果：$u>v$ 互質、一奇一偶時，$(u^2-v^2,\,2uv,\,u^2+v^2)$ 是本原三元數組，而且所有本原三元數組都這樣來。課本用的是**因數分解**的證法（見[第 1 集 2.2 節](01-history-of-numbers.md#22-euclid-的公式)），不是單位圓。

**講者的評語** [▶ 17:16](https://youtu.be/guJluWw1ArE?t=1036)：

- 【口頭】本課**不會**用這個方法：它對有些問題行不通，講者比較想用別的方法，所以沒有慢慢推。「花半小時可以自己推完，沒什麼驚天動地的。」
- 【口頭】真正有趣的是：**用高斯整數，這件事變得簡單得多**。第一次考試之後會做（第 15–21 集）。

**下一堂** [▶ 17:46](https://youtu.be/guJluWw1ArE?t=1066)：除法演算法、輾轉相除法。學生說學過，講者說「我會複習，確保大家在同一頁，不會無聊的」。之後由整除理論自然走到模運算。

---

## 7. 一頁速查表

**複數 = 矩陣模型**

- $a+ib \leftrightarrow \begin{pmatrix} a & -b\\ b & a\end{pmatrix}$。
- 乘法：$(a+ib)(c+id) = (ac-bd)+i(ad+bc)$。**關鍵一步**：兩個這種矩陣相乘還是這種形狀，元素正好是 $ac-bd$ 和 $ad+bc$。
- $i^2 = -I$。
- 矩陣只是**模型**，證明複數存在；複數本身不是矩陣（否則 $n$ 也要是 $nI$）。

**體**：有單位元素的交換環，每個非零元素都有乘法反元素。$\mathbb{Q},\mathbb{R},\mathbb{C}$ 是體。

**$\mathbb{C}$ 的運算性質**：加法交換、結合、有 0、有負元素；乘法交換、結合、有 1；分配律；$-x=(-1)x$，$0\cdot x=0$。

- **關鍵一步**（$0\cdot x=0$）：$0x = (0+0)x = 0x+0x$，兩邊減 $0x$。
- **子集合只要驗封閉性**，其他性質從 $\mathbb{C}$ 繼承。

**Diophantus 的單位圓做法**

1. $a^2+b^2=c^2$ ⇔ 單位圓上的有理點 $(a/c,\,b/c)$。
2. 過 $(-1,0)$、斜率 $t\in\mathbb{Q}$ 的直線 $y=t(x+1)$。
3. 交點：$x=\dfrac{1-t^2}{1+t^2}$，$y=\dfrac{2t}{1+t^2}$。
4. $t=v/u$ ⇒ $(u^2-v^2,\ 2uv,\ u^2+v^2)$。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 除法演算法、輾轉相除法 | 第 3–4 集 |
| 模運算 | 第 7–8 集 |
| RSA 加密（第一次考試前最後一個主題） | 第 13–14 集 |
| 子集合只驗封閉性（例如 $\mathbb{Z}[i]$） | 第 15 集起（高斯整數） |
| 高斯整數讓三元數組變簡單 | 第 15–21 集 |
| 環、體的正式定義；$-x=(-1)x$ 這類證明 | 第 27–28 集起 |

---

## 附：本集一句話總結

> **2×2 矩陣是複數的一個模型，證明複數存在，但複數本身不是矩陣。本課幾乎都在 $\mathbb{C}$ 的子集合裡工作，所以新例子只要驗封閉性；最後看 Diophantus 怎麼用單位圓上的有理點找出所有畢氏三元數組。**

---

*筆記依據 James S. Cook「Number Theory」2021-08-16 第 2 部錄影逐字稿（YouTube 自動字幕，18:52）與 Jones & Jones《Elementary Number Theory》附錄 B、§11.5 整理。*
