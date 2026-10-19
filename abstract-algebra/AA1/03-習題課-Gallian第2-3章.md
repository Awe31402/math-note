---
course: Abstract Algebra I (Fall 2016)
episode: 3
lecture: 習題課
date: 2016-09-01
video: https://www.youtube.com/watch?v=z9q0ak87srA
notes: 無直接對應（Gallian 第 2、3 章習題）
---

# 第 3 集 · 習題課：Gallian 第 2、3 章 [▶ 影片](https://www.youtube.com/watch?v=z9q0ak87srA&list=PLBY4G2o7DhF0JCgapYKrqibGaJuvV4Gkb)

← 上一集：[[02-L2-模運算與子群]] ｜ [總目錄](../README.md) ｜ 下一集：[[04-L3-中心-中心化子-二面體群]] →

## 本集概要

學生點題，老師現場解。重點如下：
- **襪子—鞋子性質** $(ab)^{-1}=b^{-1}a^{-1}$ 的證明，以及 $(ab)^{-2}\neq b^{-2}a^{-2}$ 的反例。
- 兩個「條件 ⇒ 交換群」的證明技巧：$(ab)^2=a^2b^2$，以及 $ab=ca\Rightarrow b=c$。
- 從不完整的 $U(91)$ 找出缺少的元素；$U(15)$ 的循環子群。
- 附帶澄清：**單位元素的階是 1**（回答上一集學生的問題）。

> ⚠️ 題號說明：課堂用的是 Gallian **第 5 版**，題號和我們手上的第 10 版不同。下面每題都附上第 10 版對應的題號（找得到的話）。

---

## 筆記

### 題 1：襪子—鞋子性質 [▶ 00:30](https://youtu.be/z9q0ak87srA?t=30)

**題目**（第 10 版 Ch.2 #26，p.55）：說明 $(ab)^{-1}=b^{-1}a^{-1}$ 與穿脫鞋襪的類比；找出 $(ab)^{-2}\neq b^{-2}a^{-2}$ 的例子。

**證明 $(ab)^{-1}=b^{-1}a^{-1}$** [▶ 02:32](https://youtu.be/z9q0ak87srA?t=152)　由結合律：
$$(ab)(b^{-1}a^{-1}) = a(bb^{-1})a^{-1} = aea^{-1} = aa^{-1} = e.$$
所以 $b^{-1}a^{-1}$ 具有「$ab$ 的反元素」的功能；又因為**反元素唯一**（L1 定理 3），它就是 $(ab)^{-1}$。$\blacksquare$

**老師的提醒** [▶ 04:13](https://youtu.be/z9q0ak87srA?t=253)：這題真正在問的是「乘積的反元素是什麼」。驗算只說明 $b^{-1}a^{-1}$ 有反元素的功能，**要靠唯一性**才能說它「就是」反元素。

**$(ab)^{-2}$ 是什麼？** [▶ 05:20](https://youtu.be/z9q0ak87srA?t=320)　照負次方的定義 $g^{-n}=(g^{-1})^n$：
$$(ab)^{-2} = \big((ab)^{-1}\big)^2 = b^{-1}a^{-1}b^{-1}a^{-1}.$$
如果 $a,b$ 交換，這會等於 $b^{-2}a^{-2}$，所以反例必須來自**非交換群**。

**反例（在 $GL(2,\mathbb{R})$ 中）** [▶ 07:35](https://youtu.be/z9q0ak87srA?t=455)
$$a=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad b=\begin{pmatrix}1&0\\1&1\end{pmatrix}$$
- $(ab)^{-2} = \begin{pmatrix}2&-3\\-3&5\end{pmatrix}$
- $b^{-2}a^{-2} = \begin{pmatrix}1&0\\-2&1\end{pmatrix}\begin{pmatrix}1&-2\\0&1\end{pmatrix} = \begin{pmatrix}1&-2\\-2&5\end{pmatrix}$

兩者不相等。

> 💬 板書的計算字幕不完整，上面兩個矩陣是我依老師選的 $a,b$ 重算的結果；$b^{-2},a^{-2}$ 與字幕念出的 $\begin{pmatrix}1&0\\-2&1\end{pmatrix}$、$\begin{pmatrix}1&-2\\0&1\end{pmatrix}$ 吻合（字幕裡兩者的對應順序不清楚）。

**怎麼想到找反例的？** [▶ 11:31](https://youtu.be/z9q0ak87srA?t=691)：需要非交換群，而目前最簡單的就是 $2\times 2$ 矩陣（二面體群明天才教）。

**類比** [▶ 12:01](https://youtu.be/z9q0ak87srA?t=721)：先穿襪子再穿鞋 $(ab)$，脫的時候要先脫鞋再脫襪 $(b^{-1}a^{-1})$。但「穿兩次再脫兩次」不等於「先脫兩次鞋再脫兩次襪」。

### 題 2：$(ab)^2=a^2b^2$ 對所有 $a,b$ 成立 ⇒ $G$ 交換 [▶ 13:02](https://youtu.be/z9q0ak87srA?t=782)

（第 10 版 Ch.2 #36 的前半，p.56）

**題目的精確敘述** [▶ 14:03](https://youtu.be/z9q0ak87srA?t=843)：課本寫法有點隨便，應該讀成「設 $G$ 為群。若 $(ab)^2=a^2b^2$ **對所有** $a,b\in G$ 成立，則 $ab=ba$ **對所有** $a,b\in G$ 成立」。

**證明** [▶ 15:04](https://youtu.be/z9q0ak87srA?t=904)　展開：$abab = aabb$。左邊乘 $a^{-1}$、右邊乘 $b^{-1}$：
$$a^{-1}(abab)b^{-1} = a^{-1}(aabb)b^{-1} \;\Rightarrow\; ebae = eabe \;\Rightarrow\; ba = ab.$$
這對所有 $a,b$ 都成立，所以 $G$ 是交換群。$\blacksquare$

**寫法建議** [▶ 17:40](https://youtu.be/z9q0ak87srA?t=1060)：不必每行都寫「對所有 $a,b\in G$」，可以最後一句話總結「上面的計算對所有 $a,b$ 成立，因此 $G$ 是交換群」。老師的評語是：這題看起來嚇人，展開後才發現自己會。

**作業提示** [▶ 18:10](https://youtu.be/z9q0ak87srA?t=1090)：作業裡那個 $\begin{pmatrix}a&a\\a&a\end{pmatrix}$ 群（見 L2）的單位元素**不是** $I$，而是 $\begin{pmatrix}\tfrac12&\tfrac12\\\tfrac12&\tfrac12\end{pmatrix}$。

**關於 Heisenberg 群類的題目** [▶ 20:22](https://youtu.be/z9q0ak87srA?t=1222)：如果你的集合不是 $GL(n)$ 的子群，那麼**矩陣的反矩陣不一定是群的反元素**。這時要直接解 $gh=e$：先找出單位元素，再對一般的 $(a,b,c)$ 解出反元素 $(x,y,z)$ 的公式。

### 題 3：$U(91)$ 少了哪個元素？ [▶ 22:53](https://youtu.be/z9q0ak87srA?t=1373)

**題目**（第 10 版 Ch.2 #23，p.54）：一位代數老師要打字員打出 9 個在模 91 乘法下構成群的整數，結果漏打一個，變成 $1, 9, 16, 22, 53, 74, 79, 81$。漏掉的是哪個？（Gallian 註明：「This really happened!」）

**方法** [▶ 25:25](https://youtu.be/z9q0ak87srA?t=1525)：既然是群，就對乘法封閉。把清單裡的元素兩兩相乘再取模 91，總會冒出不在清單上的那個。例如 $9\times 22 = 198 \equiv 16$（已在清單上），$16\times 16 = 256 \equiv 74$（也在）……一直試下去。

**答案** [▶ 27:31](https://youtu.be/z9q0ak87srA?t=1651)：**29**。

> 📘 Gallian 10th p.250 的另一題（Ch.11 #21）直接列出這個群：*"The set {1, 9, 16, 22, 29, 53, 74, 79, 81} is a group under multiplication modulo 91."*，正好印證缺的是 29。

> 💬 老師說這種「給你群的一部分，用乘法補完」的題目很適合出在考試上 [▶ 26:55](https://youtu.be/z9q0ak87srA?t=1615)。

### 題 4：若 $ab=ca \Rightarrow b=c$ 對所有 $a,b,c$ 成立，則 $G$ 交換 [▶ 27:31](https://youtu.be/z9q0ak87srA?t=1651)

**題目**：設群 $G$ 滿足「$ab=ca$ 推得 $b=c$」對所有 $a,b,c\in G$ 成立（類似「交叉消去律」）。證明 $G$ 是交換群。

**卡關過程** [▶ 29:15](https://youtu.be/z9q0ak87srA?t=1755)–36:26：老師和學生試了好幾個方向（不能直接假設 $ab=ba$；試過反證法），一度卡住。

**關鍵想法（學生提出）** [▶ 36:26](https://youtu.be/z9q0ak87srA?t=2186)　從一個恆真的式子出發：
$$a(ba) = (ab)a.$$
把它看成假設中的「$a\,\boxed{B} = \boxed{C}\,a$」，其中 $B = ba$、$C = ab$。由假設得到 $B=C$，也就是
$$ba = ab.$$
這對所有 $a,b$ 都成立，所以 $G$ 是交換群。$\blacksquare$

**技巧** [▶ 36:56](https://youtu.be/z9q0ak87srA?t=2216)：假設是一個「蘊含式」，要找出符合它前提形式的**真等式**，再巧妙地認定誰是 $B$、誰是 $C$。用 $x,y$ 等其他字母可以避免和題目的 $a,b,c$ 混淆。

### 題 5：$U(15)$ 有六個循環子群 [▶ 38:37](https://youtu.be/z9q0ak87srA?t=2317)

**預告循環子群** [▶ 39:07](https://youtu.be/z9q0ak87srA?t=2347)：在乘法群中，$\langle a\rangle = \{a, a^2, a^3,\dots\}$，直到 $a^n=e$ 為止。之後的講課會正式定義。

$U(15) = \{1,2,4,7,8,11,13,14\}$ [▶ 39:38](https://youtu.be/z9q0ak87srA?t=2378)

- $\langle 2\rangle = \{2,4,8,1\}$，$|2|=4$ [▶ 40:08](https://youtu.be/z9q0ak87srA?t=2408)。
- $\langle 4\rangle = \{4,1\}$，$|4|=2$。
- $\langle 7\rangle$：$7^2=49\equiv 4$，$7^3 \equiv 28 \equiv 13$（老師也示範寫成 $\equiv -2$），$7^4\equiv 1$，所以 $\langle 7\rangle = \{7,4,13,1\}$ [▶ 42:13](https://youtu.be/z9q0ak87srA?t=2533)。
- **算模運算的小技巧** [▶ 42:44](https://youtu.be/z9q0ak87srA?t=2564)：可以用負的代表元，例如 $28\equiv -2 \pmod{15}$，有時計算比較方便。

老師到這裡就下課了。照同樣的方法補完：

> 💬 以下是我依課堂方法補算的結果，課堂上沒有算完：
> $\langle 1\rangle=\{1\}$、$\langle 4\rangle=\{1,4\}$、$\langle 11\rangle=\{1,11\}$、$\langle 14\rangle=\{1,14\}$、$\langle 2\rangle=\langle 8\rangle=\{1,2,4,8\}$、$\langle 7\rangle=\langle 13\rangle=\{1,4,7,13\}$，**正好六個**。這也呼應老師說的「有些子群有兩個不同的生成元」[▶ 43:45](https://youtu.be/z9q0ak87srA?t=2625)。

**角括號記號** [▶ 41:09](https://youtu.be/z9q0ak87srA?t=2469)：$\langle\ \rangle$ 有專門的意思（生成的子群），列舉集合時要用大括號 $\{\ \}$。

### 附帶：單位元素的階是 1 [▶ 41:40](https://youtu.be/z9q0ak87srA?t=2500)

回應上一集學生的問題，老師現在明確說：**單位元素的階是 1**。理由是**元素的階應該等於它生成的循環子群的階**：$|2|=4$ 生成 4 階子群，$|4|=2$ 生成 2 階子群，而 $e$ 生成 $\{e\}$，階是 1。

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| 襪子—鞋子性質 | socks–shoes property | [00:30](https://youtu.be/z9q0ak87srA?t=30) |
| 反例 | counterexample | [03:00](https://youtu.be/z9q0ak87srA?t=180) |
| Heisenberg 群 | Heisenberg group | [21:53](https://youtu.be/z9q0ak87srA?t=1313) |
| 循環子群 | cyclic subgroup | [39:07](https://youtu.be/z9q0ak87srA?t=2347) |
| 生成元 | generator | [40:39](https://youtu.be/z9q0ak87srA?t=2439) |

## ⚠️ 待確認清單

1. [▶ 24:24](https://youtu.be/z9q0ak87srA?t=1464) 題 4（$ab=ca\Rightarrow b=c$）在 Gallian 第 10 版的題號：沒有找到群版本的同一題，只有第 12 章環的版本（Ch.12 #8，p.261，"Outer cancellation implies commutativity"）。
