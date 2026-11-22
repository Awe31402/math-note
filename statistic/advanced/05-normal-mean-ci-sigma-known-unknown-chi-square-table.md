---
course: 高等統計學（數理統計續）
episode: 5
lecture: Lec05（第三週 2/2）
date: 待補
video: https://youtu.be/8F6dasFDbUc
notes: Hogg 8th ed. §4.2 常態平均數的信賴區間（$t$ 區間 Example 4.2.1；$\sigma$ 已知的 $z$ 區間）；附錄 卡方分配表
---

# 第 5 集 · 第三週 (2/2)：常態平均數 $\mu$ 的信賴區間（$\sigma$ 已知／未知）；查卡方表 [▶ 影片](https://youtu.be/8F6dasFDbUc)

← 上一集：[04](04-standard-normal-table-confidence-interval-pivotal-quantity.md) ｜ [總目錄](../README.md) ｜ 下一集：[06](06-variance-ci-difference-of-means-ci.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 5 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（44:54，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §4.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「信賴區間」→「系列期間／信奈期間」，「pivotal quantity」→「Puberth／Puptal／Pubital Quantity」，「卡方」→「卡簧」，「variance」→「valence」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 情形 1：σ 已知](#1-情形-1σ-已知)
- [2. 樞紐量的關鍵：能一對一改寫](#2-樞紐量的關鍵能一對一改寫)
- [3. 情形 2：σ 未知](#3-情形-2σ-未知)
- [4. 對照記法](#4-對照記法)
- [5. 查卡方表](#5-查卡方表)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

$X_1,\dots,X_n$ 來自 $N(\mu,\sigma^2)$，找 $\mu$ 的信賴區間。分兩種情形：

| 情形 | 樞紐量 | 分配 | 信賴區間 |
|---|---|---|---|
| $\sigma=\sigma_0$ 已知 | $\dfrac{\bar X-\mu}{\sigma_0/\sqrt n}$ | $N(0,1)$ | $\bar X\pm z_{\alpha/2}\dfrac{\sigma_0}{\sqrt n}$ |
| $\sigma$ 未知 | $\dfrac{\bar X-\mu}{S/\sqrt n}$ | $t(n-1)$ | $\bar X\pm t_{\alpha/2}(n-1)\dfrac{S}{\sqrt n}$ |

最後學查卡方表（下次 $\sigma^2$ 的信賴區間要用）。

---

## 1. 情形 1：σ 已知

[▶ 01:02](https://youtu.be/8F6dasFDbUc?t=62) 有些問題 $\sigma$ 真的知道，$\sigma=\sigma_0$：$X_i$ iid $N(\mu,\sigma_0^2)$。

**Step 1：找樞紐量**（[▶ 02:04](https://youtu.be/8F6dasFDbUc?t=124)）。估 $\mu$ 的 UMVUE 是 $\bar X$，所以用 $\bar X$ 來建造。

- $\bar X\sim N\left(\mu,\frac{\sigma_0^2}{n}\right)$。
- [▶ 03:09](https://youtu.be/8F6dasFDbUc?t=189) $\bar X$ 本身**不是**樞紐量：它的分配含未知的 $\mu$。（而且 $\bar X$ 也不含參數，它是統計量。）
- [▶ 04:09](https://youtu.be/8F6dasFDbUc?t=249) 標準化：
$$Q=\frac{\bar X-\mu}{\sigma_0/\sqrt n}\sim N(0,1).$$
是樣本和 $\mu$ 的函數，分配**不含參數** ⇒ 樞紐量。

**Step 2：找 $a,b$**（[▶ 05:12](https://youtu.be/8F6dasFDbUc?t=312)）。標準常態對稱，取 $a=-z_{\alpha/2}$、$b=z_{\alpha/2}$（查表，跟參數無關）：
$$1-\alpha=P\left(-z_{\alpha/2}\le Z\le z_{\alpha/2}\right)=P_\mu\left(-z_{\alpha/2}\le\frac{\bar X-\mu}{\sigma_0/\sqrt n}\le z_{\alpha/2}\right).$$

[▶ 07:46](https://youtu.be/8F6dasFDbUc?t=466) 右邊的下標 $\mu$：$\bar X$ 減掉的是真正的 mean 才會是標準常態。不知道 $\mu$，所以任何 $\mu$ 是對的時候，這裡放同一個 $\mu$。對所有 $\mu$ 成立。

**Step 3：改寫成 $\mu$ 在中間**（[▶ 09:16](https://youtu.be/8F6dasFDbUc?t=556)）

1. 乘上 $\frac{\sigma_0}{\sqrt n}>0$：$-z_{\alpha/2}\frac{\sigma_0}{\sqrt n}\le\bar X-\mu\le z_{\alpha/2}\frac{\sigma_0}{\sqrt n}$。
2. 右邊不等式：$-\mu$ 搬到右邊、右邊那項搬到左邊：$\mu\ge\bar X-z_{\alpha/2}\frac{\sigma_0}{\sqrt n}$。
3. 左邊不等式：$\mu\le\bar X+z_{\alpha/2}\frac{\sigma_0}{\sqrt n}$。

$$1-\alpha=P_\mu\left(\bar X-z_{\alpha/2}\frac{\sigma_0}{\sqrt n}\le\mu\le\bar X+z_{\alpha/2}\frac{\sigma_0}{\sqrt n}\right),\qquad\forall\mu\in\mathbb{R}.$$

**Step 4：確認是統計量**（[▶ 11:50](https://youtu.be/8F6dasFDbUc?t=710)）：$\bar X$ 是樣本的函數；$z_{\alpha/2}$ 查表；$\sigma_0$ 已知；$n$ 是樣本數。兩端都不含未知參數 ⇒ 統計量。

> **結果**（[▶ 13:53](https://youtu.be/8F6dasFDbUc?t=833)）：$\sigma$ 已知時，$\mu$ 的 $100(1-\alpha)\%$ 信賴區間是
> $$\left(\bar X-z_{\alpha/2}\frac{\sigma_0}{\sqrt n},\ \bar X+z_{\alpha/2}\frac{\sigma_0}{\sqrt n}\right).$$

[▶ 13:23](https://youtu.be/8F6dasFDbUc?t=803) $\mu$ 的參數空間是 $(-\infty,\infty)$：不管 $\mu$ 是多少，涵蓋機率都是 $1-\alpha$。

---

## 2. 樞紐量的關鍵：能一對一改寫

[▶ 14:56](https://youtu.be/8F6dasFDbUc?t=896)

- 從 $-z_{\alpha/2}\le Q\le z_{\alpha/2}$ 到 $T_1\le\mu\le T_2$，每一步都可以換過來、換回去（若且唯若），所以兩個事件相同，機率相同。
- [▶ 15:58](https://youtu.be/8F6dasFDbUc?t=958) 有些樞紐量（分配不含參數）**沒辦法**這樣改寫，就沒用。
- 任何樞紐量都找得到 $a,b$；問題是能不能改寫成「參數在中間、統計量在兩邊」。

【口頭】[▶ 16:59](https://youtu.be/8F6dasFDbUc?t=1019) 做過一兩題就很清楚。信賴區間其實是最簡單的，沒有多少理論，只是要熟悉不同的問題；一開始的觀念要建立起來。

---

## 3. 情形 2：σ 未知

[▶ 17:59](https://youtu.be/8F6dasFDbUc?t=1079) 大部分情況 $\sigma$ 不知道，$\mu$、$\sigma^2$ 都是參數。

**沒用的樞紐量**（[▶ 18:29](https://youtu.be/8F6dasFDbUc?t=1109)）：$\frac{\bar X-\mu}{\sigma/\sqrt n}\sim N(0,1)$，分配不含參數，是樞紐量。但改寫到最後，兩端會含 $\sigma$（未知），**不是統計量**。轉換不過來，沒用。

**有用的樞紐量**（[▶ 20:31](https://youtu.be/8F6dasFDbUc?t=1231)）。上學期證過：

- $\bar X\sim N(\mu,\sigma^2/n)$；
- $\frac{(n-1)S^2}{\sigma^2}\sim\chi^2(n-1)$，$S^2=\frac{1}{n-1}\sum(X_i-\bar X)^2$；
- $\bar X$ 和 $S^2$ **獨立**。

[▶ 21:31](https://youtu.be/8F6dasFDbUc?t=1291) 用上一集的 $t$ 分配：標準常態 ÷ $\sqrt{\text{卡方}/\text{自由度}}$，兩者獨立：
$$T=\frac{\dfrac{\bar X-\mu}{\sigma/\sqrt n}}{\sqrt{\dfrac{(n-1)S^2}{\sigma^2}\Big/(n-1)}}=\frac{\bar X-\mu}{S/\sqrt n}\sim t(n-1).$$

（分母根號裡 $n-1$ 消掉，$\sigma^2$ 開根號和分子的 $\sigma$ 消掉。）

- [▶ 24:03](https://youtu.be/8F6dasFDbUc?t=1443) $t$ 分配只和自由度 $n-1$ 有關，不含 $\mu,\sigma^2$ ⇒ 分配不含參數。
- 是樣本（$\bar X$、$S$）和 $\mu$ 的函數 ⇒ **樞紐量**，而且有用。

**$t_{\alpha/2}$**（[▶ 25:36](https://youtu.be/8F6dasFDbUc?t=1536)）：$t$ 分配也對 0 對稱（$f_T(-t)=f_T(t)$）。$t_{\alpha/2}(n-1)$：以上機率 $\alpha/2$；$-t_{\alpha/2}$ 以下也是 $\alpha/2$；中間 $1-\alpha$。

**改寫**（[▶ 27:44](https://youtu.be/8F6dasFDbUc?t=1664)）：$S>0$，乘過去、移項，同情形 1：

> **結果**（[▶ 30:19](https://youtu.be/8F6dasFDbUc?t=1819)）：$\sigma$ 未知時，$\mu$ 的 $100(1-\alpha)\%$ 信賴區間是
> $$\left(\bar X-t_{\alpha/2}(n-1)\frac{S}{\sqrt n},\ \bar X+t_{\alpha/2}(n-1)\frac{S}{\sqrt n}\right).$$

兩端只有 $\bar X$、$S$、查表值、$n$，沒有 $\mu,\sigma^2$ ⇒ 統計量。

---

## 4. 對照記法

[▶ 32:05](https://youtu.be/8F6dasFDbUc?t=1925)

| | $\sigma$ 已知 | $\sigma$ 未知 |
|---|---|---|
| 樞紐量 | $\frac{\bar X-\mu}{\sigma_0/\sqrt n}\sim N(0,1)$ | $\frac{\bar X-\mu}{S/\sqrt n}\sim t(n-1)$ |
| 查表 | $z_{\alpha/2}$ | $t_{\alpha/2}(n-1)$ |
| 標準差位置 | $\sigma_0$ | 換成 $S$ |
| 區間 | $\bar X\pm z_{\alpha/2}\frac{\sigma_0}{\sqrt n}$ | $\bar X\pm t_{\alpha/2}\frac{S}{\sqrt n}$ |

【口頭】很好記，但要會自己導。

---

## 5. 查卡方表

[▶ 34:39](https://youtu.be/8F6dasFDbUc?t=2079) 下次要找 $\sigma^2$ 的信賴區間，要用卡方。

**表是什麼**（[▶ 35:18](https://youtu.be/8F6dasFDbUc?t=2118)）：課本附錄的 chi-square distribution 表給**累積**（分配函數）：
$$F(u)=P\left(\chi^2(n)\le u\right)=\int_0^u\frac{1}{\Gamma(n/2)2^{n/2}}x^{n/2-1}e^{-x/2}\,dx.$$
（卡方大於 0，所以從 0 積。）表的左欄是自由度 $n$，上列是累積機率，交叉處是 $u$。

**記號**（[▶ 38:30](https://youtu.be/8F6dasFDbUc?t=2310)）：$\chi^2_{0.05}(10)$ 表示自由度 10 的卡方，**以下**機率是 0.05 的點。

⚠️ 注意：這裡卡方的下標是「**以下**的機率」，和上一集 $z_\alpha$（以上的機率）方向相反。這是老師這堂課的用法；課本用法請對照課本表頭。

**例**（[▶ 39:31](https://youtu.be/8F6dasFDbUc?t=2371)）：自由度 10。

- $\chi^2_{0.05}(10)$：左欄找 10，上列找 0.05 → **3.94**。
- $\chi^2_{0.95}(10)$：以下 0.95，也就是以上 0.05 → **18.3**。

$$P\left(3.94\le\chi^2(10)\le 18.3\right)=0.95-0.05=0.90.$$

[▶ 43:35](https://youtu.be/8F6dasFDbUc?t=2615) 要中間 0.90：找以下 0.05 和以下 0.95 的點。要中間 0.95：找以下 0.025 和以下 0.975 的點。卡方**不對稱**，兩個點都要查。

下次講 $\sigma^2$ 的信賴區間。

---

## 6. 一頁速查表

**常態 $\mu$ 的信賴區間**

- $\sigma$ 已知：$\bar X\pm z_{\alpha/2}\frac{\sigma_0}{\sqrt n}$（樞紐量 $\frac{\bar X-\mu}{\sigma_0/\sqrt n}\sim N(0,1)$）。
- $\sigma$ 未知：$\bar X\pm t_{\alpha/2}(n-1)\frac{S}{\sqrt n}$（樞紐量 $\frac{\bar X-\mu}{S/\sqrt n}\sim t(n-1)$）。

$t$ 樞紐量的關鍵一步：
$$\frac{\bar X-\mu}{S/\sqrt n}=\frac{(\bar X-\mu)/(\sigma/\sqrt n)}{\sqrt{\frac{(n-1)S^2}{\sigma^2}/(n-1)}},\quad\text{分子 }N(0,1)\text{、分母 }\sqrt{\chi^2(n-1)/(n-1)}\text{、獨立}.$$

**沒用的樞紐量**：$\sigma$ 未知時 $\frac{\bar X-\mu}{\sigma/\sqrt n}$ 改寫後兩端含 $\sigma$，不是統計量。

**卡方表**：給 $P(\chi^2(n)\le u)$。$\chi^2_{0.05}(10)=3.94$，$\chi^2_{0.95}(10)=18.3$。不對稱，兩端都要查。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 卡方表 | 下一集：$\sigma^2$ 的信賴區間（樞紐量 $\frac{(n-1)S^2}{\sigma^2}$） |
| $t$ 區間 | 兩個常態母體平均數差的信賴區間；$t$ 檢定 |

---

## 附：本集一句話總結

> **常態平均數 $\mu$ 的信賴區間：$\sigma$ 已知時用樞紐量 $\frac{\bar X-\mu}{\sigma_0/\sqrt n}\sim N(0,1)$ 得 $\bar X\pm z_{\alpha/2}\sigma_0/\sqrt n$；$\sigma$ 未知時用 $\frac{\bar X-\mu}{S/\sqrt n}\sim t(n-1)$（靠 $\bar X\perp S^2$）得 $\bar X\pm t_{\alpha/2}S/\sqrt n$；卡方表給左尾機率，不對稱，兩端都要查。**

---

*筆記依據「高等統計學」Lec05 錄影逐字稿（whisper large-v3-turbo，44:54）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
