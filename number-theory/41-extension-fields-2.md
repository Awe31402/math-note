---
course: Number Theory（2021 秋，線上錄影）
episode: 41
lecture: 2021-11-10 第 2 部
date: 2021-11-10
video: https://youtu.be/Rh0Q54CQNxg
notes: 講者講義 Cook《Lecture Notes for Abstract Algebra I》（2018）§4.9 Lecture 29（p. 166–167）：Example 4.9.9、Definition 4.9.10、Example 4.9.11–4.9.16、Definition 4.9.17
---

# 第 41 集 · 分裂體、代數元與超越元（Extension Fields, Part 2） [▶ 影片](https://youtu.be/Rh0Q54CQNxg)

← 上一集：[40-extension-fields-1](40-extension-fields-1.md) ｜ [總目錄](README.md) ｜ 下一集：[42-irreducible-polynomial-simple-extensions-1](42-irreducible-polynomial-simple-extensions-1.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 41 集（2021-11-10 第 2 部，接第 40 集）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（17:35，自動字幕）＋ 講者講義 §4.9
> **標記說明**：
> - `【口頭】` 講者口頭補充，講義沒有
> - `【講義補充】` 講者講義有、課堂沒講
> - `【課堂討論】` 講者問、學生答
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字，依講義補

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. x⁴ − 5x² + 6：不同的擴張體都能給根](#1-x--5x--6不同的擴張體都能給根)
- [2. 分裂體（先提一下）](#2-分裂體先提一下)
- [3. 代數元與超越元](#3-代數元與超越元)
- [4. 例子](#4-例子)
- [5. π 和 e](#5-π-和-e)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

接第 40 集的例子 $x^4-5x^2+6$，然後定義**代數元**和**超越元**。

---

## 1. x⁴ − 5x² + 6：不同的擴張體都能給根

[▶ 00:03](https://youtu.be/Rh0Q54CQNxg?t=3)（講義 Example 4.9.9）

$f(x) = x^4-5x^2+6 = (x^2-3)(x^2-2)$ 在 $\mathbb{Q}$ 上可約，但 $x^2-3$、$x^2-2$ 在 $\mathbb{Q}$ 上不可約。

**用 $x^2-3$**：$\mathbb{Q}[x]/\langle x^2-3\rangle = \{a+b\alpha\}$，$\alpha^2-3 = 0$，所以 $f(\alpha) = 0$。$\alpha$ 扮演 $\sqrt3$，**這就是 $\mathbb{Q}(\sqrt3)$**（同構意義下）[▶ 01:04](https://youtu.be/Rh0Q54CQNxg?t=64)。

**用 $x^2-2$**：$\mathbb{Q}[x]/\langle x^2-2\rangle\cong\mathbb{Q}(\sqrt2)$，$\beta^2-2 = 0$，$f(\beta) = 0$。

講者 [▶ 01:36](https://youtu.be/Rh0Q54CQNxg?t=96)：**同一個多項式，可能有不同的擴張體**都能給它一個根。

**兩個一起加**：$\mathbb{Q}(\alpha,\beta) = \mathbb{Q}(\sqrt2,\sqrt3)$，包含 $\mathbb{Q}$、$\sqrt2$、$\sqrt3$ 的最小的體。在這裡 $f$ **完全分解** [▶ 02:41](https://youtu.be/Rh0Q54CQNxg?t=161)：
$$f(x) = (x-\sqrt3)(x+\sqrt3)(x-\sqrt2)(x+\sqrt2).$$

> 【講義補充】Example 4.9.9（p. 166）的寫法：
> - 在 $\mathbb{Q}(\alpha)[x]$ 裡（$\alpha^2 = 2$）：$f(x) = (x+\alpha)(x-\alpha)(x^2-3)$；
> - 在 $\mathbb{Q}(\beta)[x]$ 裡（$\beta^2 = 3$）：$f(x) = (x^2-2)(x+\beta)(x-\beta)$。
> - $\mathbb{Q}(\alpha)$ 是體，可以再做 $\mathbb{Q}(\alpha)[t]/\langle t^2-3\rangle$，在裡面 $f(t) = (t+\alpha)(t-\alpha)(t+\beta)(t-\beta)$。
>
> （講義的 $\alpha,\beta$ 分別對應 $\sqrt2,\sqrt3$，跟課堂相反；不影響內容。）

---

## 2. 分裂體（先提一下）

[▶ 03:12](https://youtu.be/Rh0Q54CQNxg?t=192)

**分裂**（split）：多項式寫成一次式的乘積（可以重複）。讓多項式完全分解的體叫**分裂體**（splitting field）。

- $\mathbb{Q}(\sqrt3)$ 或 $\mathbb{Q}(\sqrt2)$ **單獨都不是** $f$ 的分裂體：各自還剩 $x^2-2$ 或 $x^2-3$。要兩個都加才能完全分解。（⚠️ 逐字稿缺字：字幕是「on their lonesome **are** a splitting field」，依前後文應是「are **not**」。）
- 每個多項式在 $\mathbb{C}$ 上都分裂：**代數基本定理**。
- $\mathbb{R}$ 上有不可約的二次式，像第 40 集的 $x^2+4x+5$。

講者 [▶ 04:29](https://youtu.be/Rh0Q54CQNxg?t=269)：分裂體完整的討論是講 **Galois 理論**時的事，「這學期不講，你們安全了。但它其實沒那麼糟」。

> 以下**不是逐字稿內容**，是補分裂體的精確說法：$f$ 在 $F$ 上的分裂體是讓 $f$ 分裂成一次式的**最小**擴張體（由 $f$ 的所有根生成）。所以 $\mathbb{C}$ 讓 $x^4-5x^2+6$ 分裂，但它的分裂體（在 $\mathbb{Q}$ 上）是 $\mathbb{Q}(\sqrt2,\sqrt3)$。

---

## 3. 代數元與超越元

[▶ 05:04](https://youtu.be/Rh0Q54CQNxg?t=304)

> **定義**（講義 Definition 4.9.10）：$E$ 是 $F$ 的擴張體，$\alpha\in E$。
> - 若存在**非零** $f(x)\in F[x]$ 使 $f(\alpha) = 0$，就說 $\alpha$ 在 $F$ 上是**代數的**（algebraic over $F$）。
> - 不是代數的，叫**超越的**（transcendental over $F$）。

講者 [▶ 06:47](https://youtu.be/Rh0Q54CQNxg?t=407)：代數、超越**都要指明基體**。不說基體沒意義——但大家常常不說，因為心裡有特定的情境（第 5 節）。

> 【講義補充】講義（p. 166）：「我有時候會忘記說基體。這不明智，因為同一個數依情境可以是代數的也可以是超越的。」

---

## 4. 例子

**體裡的元素在自己上面都是代數的**（Ex 4.9.11）[▶ 07:20](https://youtu.be/Rh0Q54CQNxg?t=440)：$\alpha\in F$，$f(x) = x-\alpha\in F[x]$，$f(\alpha) = 0$。

**$i$ 在 $\mathbb{R}$ 上是代數的**（Ex 4.9.12）[▶ 08:00](https://youtu.be/Rh0Q54CQNxg?t=480)：$f(x) = x^2+1$，$f(i) = 0$。

【課堂討論】講者問：$\mathbb{R}$ 可以換成什麼？學生：$\mathbb{C}$。講者：對，也可以換成 $\mathbb{Q}$——$x^2+1$ 本身就是有理係數多項式。「這裡有個定理可以講，但我還沒講到那個定理。」

**$\sqrt2$ 在 $\mathbb{Q}(\sqrt3)$ 上是代數的**（Ex 4.9.13）[▶ 09:32](https://youtu.be/Rh0Q54CQNxg?t=572)：$x^2-2$ 的係數在 $\mathbb{Q}(\sqrt3)$ 裡。其實 $\sqrt2$ 在 $\mathbb{Q}$ 上就是代數的，$\sqrt3$ 只是「櫥窗裝飾」。

**$\alpha = 2+\sqrt{1+\sqrt3}$ 在 $\mathbb{Q}$ 上是代數的**（Ex 4.9.15，課堂叫例 13）[▶ 10:46](https://youtu.be/Rh0Q54CQNxg?t=646)：

要找一個有理係數多項式以它為根。講者給中級代數班的建議：「**把根號孤立出來**。根號的天敵是什麼？平方。」

$$\alpha-2 = \sqrt{1+\sqrt3}\ \Rightarrow\ (\alpha-2)^2 = 1+\sqrt3\ \Rightarrow\ (\alpha-2)^2-1 = \sqrt3\ \Rightarrow\ \left[(\alpha-2)^2-1\right]^2 = 3.$$

展開 $(x-2)^2-1 = x^2-4x+3$：
$$f(x) = (x^2-4x+3)^2-3 = x^4-8x^3+22x^2-24x+6.$$

⚠️ 逐字稿缺字：講者在課堂上邊算邊改，字幕的中間步驟和結果是「$x^4-4x^3+18x^2-24x+6$」，係數聽不清楚；依講義 Example 4.9.15（p. 167），正確結果是 $x^4-8x^3+22x^2-24x+6$（已驗算：$(x^2-4x+3)^2 = x^4-8x^3+22x^2-24x+9$）。

【口頭】[▶ 11:17](https://youtu.be/Rh0Q54CQNxg?t=677) 算到一半講者岔題：Facebook 一直推一個很蠢的政治人物馬克杯給他，他想買給很討厭那人的媽媽，21 塊錢，結果結帳時運費要再 6 塊，「你對我來說已經死了，我才不花快 30 塊買一個馬克杯」。

> 【講義補充】講義（p. 167）：
> - **Example 4.9.14**：$d\in\mathbb{Z}$，$\sqrt d$ 是 $x^2-d$ 的根，所以在 $\mathbb{Q}$ 上是代數的。$\mathbb{Q}(\sqrt d)$ 可能是實的或複的擴張；若 $d = n^2$，$\sqrt d = n\in\mathbb{Q}$，$\mathbb{Q}(\sqrt d) = \mathbb{Q}$。
> - 「由有限次加、減、乘和開正根造出來的數都是代數數，因為我們可以像這樣**一再平方或立方**，有系統地消掉根號。」

---

## 5. π 和 e

[▶ 14:52](https://youtu.be/Rh0Q54CQNxg?t=892)

【課堂討論】講者問：什麼是不是代數的元素？有沒有有理係數多項式以 $\pi$ 為根？學生：「必須是有限的？」講者：對，多項式——有沒有**有限多個**係數，使 $\pi$ 的那個組合等於 0？**沒有。**

- 講者：「我沒辦法當場證明。」可以證明 $\pi$ 是無理數；$\pi$ 在 $\mathbb{Q}$ 上**不是代數的**也能證，「但我不覺得這容易，大概能花整堂課仔細證」。$e$ 也一樣。
- **$\pi$ 和 $e$ 在 $\mathbb{Q}$ 上是超越的**（Ex 4.9.16）[▶ 16:37](https://youtu.be/Rh0Q54CQNxg?t=997)。
- **但 $\pi$ 和 $e$ 在 $\mathbb{R}$ 上是代數的**：體裡的元素在自己上面都是代數的（$x-\pi$）。

**大家說「$\pi$ 是超越數」是什麼意思？** [▶ 17:07](https://youtu.be/Rh0Q54CQNxg?t=1027) 指的是**相對於 $\mathbb{Q}$**，這是數論學家的預設。「但要懂，代數和超越是**角度問題**。」

> 【講義補充】
>
> **Definition 4.9.17**（p. 167）：$x\in\mathbb{C}$ 在 $\mathbb{Q}$ 上是代數的，叫**代數數**（algebraic number）；不是的叫**超越數**（transcendental number）。
>
> Example 4.9.16 說證明 $\pi$、$e$ 的超越性「需要我們花很大力氣」，有些微積分二的課本（Salas、Hille、Etgen）的習題給了證明的一大部分。

講者最後：「謝謝大家，希望你們不介意我打斷講義去深入……」（第 40 集的雙曲數和同構驗證。）

---

## 6. 一頁速查表

**同一個多項式可以有不同的擴張體給根**：$x^4-5x^2+6 = (x^2-2)(x^2-3)$，$\mathbb{Q}(\sqrt2)$、$\mathbb{Q}(\sqrt3)$ 各給一對根；在 $\mathbb{Q}(\sqrt2,\sqrt3)$ 裡完全分解。

**分裂體**：讓多項式分解成一次式乘積的（最小）擴張體。$\mathbb{C}$ 上每個多項式都分裂（代數基本定理）。

**代數 / 超越**（一定要說基體）

| 元素 | 基體 | 代數？ | 多項式 |
|---|---|---|---|
| $\alpha\in F$ | $F$ | 代數 | $x-\alpha$ |
| $i$ | $\mathbb{R}$、$\mathbb{Q}$ | 代數 | $x^2+1$ |
| $\sqrt2$ | $\mathbb{Q}$、$\mathbb{Q}(\sqrt3)$ | 代數 | $x^2-2$ |
| $2+\sqrt{1+\sqrt3}$ | $\mathbb{Q}$ | 代數 | $x^4-8x^3+22x^2-24x+6$ |
| $\pi$、$e$ | $\mathbb{R}$ | 代數 | $x-\pi$ |
| $\pi$、$e$ | $\mathbb{Q}$ | **超越** | 不存在（證明很難） |

**找多項式的方法**：孤立根號 → 平方 → 重複。**關鍵一步**：$[(\alpha-2)^2-1]^2 = 3$。

**代數數** = 在 $\mathbb{Q}$ 上代數的複數；「超越數」預設相對於 $\mathbb{Q}$。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 超越元 ⇔ 求值映射單射；$\mathbb{Q}[\pi]$ 像多項式 | 第 42 集 |
| 最小多項式 $\mathrm{irr}(\alpha,F)$、$\deg(\alpha,F)$ | 第 42–43 集 |
| $F(\alpha)$ 的基底 $1,\alpha,\dots,\alpha^{n-1}$ | 第 42–43 集 |
| 代數擴張、$[E:F]$ | 第 44–45 集 |
| 分裂體、Galois 理論 | 本課沒講 |

---

## 附：本集一句話總結

> **同一個多項式可以在不同的擴張體裡得到根，例如 $x^4-5x^2+6$ 在 $\mathbb{Q}(\sqrt2)$ 和 $\mathbb{Q}(\sqrt3)$ 各有一對根，兩個都加進來才完全分解。一個元素若是某個非零 $F$ 係數多項式的根，就是在 $F$ 上「代數的」，否則是「超越的」——這永遠要看基體：$\pi$ 在 $\mathbb{R}$ 上是代數的，在 $\mathbb{Q}$ 上是超越的。**

---

*筆記依據 James S. Cook「Number Theory」2021-11-10 第 2 部錄影逐字稿（YouTube 自動字幕，17:35）與講者講義《Lecture Notes for Abstract Algebra I》（2018）§4.9 整理。*
