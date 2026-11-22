---
course: 高等統計學（數理統計續）
episode: 20
lecture: Lec20（第十一週 1/2）
date: 待補
video: https://youtu.be/VbnrF6d9m5w
notes: Hogg 8th ed. §8.3.1 常態平均數的 LRT（單樣本 t 檢定）；§3.6.2 F 分配（p. 212）
---

# 第 20 集 · 第十一週 (1/2)：LRT 化成 t 檢定；「心裡要先知道最後用什麼」；兩變異數相等的問題與 F 分配 [▶ 影片](https://youtu.be/VbnrF6d9m5w)

← 上一集：[19](19-lrt-examples-exponential-normal-mean.md) ｜ [總目錄](../README.md) ｜ 下一集：[21](21-f-table-variance-ratio-ci-test.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 20 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（約 28 分鐘，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §3.6.2、§8.3.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「variance」→「Valence／Violence」，「信賴區間」→「心態期間／信貸區間／心愛期間」，「follow」→「扶寵」，「$\chi^2$」→「卡方」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 心裡要先知道最後會用什麼](#1-心裡要先知道最後會用什麼)
- [2. 例三續：Λ 化成 t 統計量](#2-例三續λ-化成-t-統計量)
- [3. 兩個平均數比較前：變異數要相等](#3-兩個平均數比較前變異數要相等)
- [4. F 分配](#4-f-分配)
- [5. 一頁速查表](#5-一頁速查表)
- [6. 與後續集數的連結](#6-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| $N(\theta_1,\theta_2)$，$H_0:\theta_1=0$ 的 LRT ⇒ $t$ 檢定 | §8.3.1 |
| 為什麼要檢定 $\sigma_1^2=\sigma_2^2$ | §8.3.2 前置 |
| F 分配定義 | §3.6.2，p. 212 |

---

## 1. 心裡要先知道最後會用什麼

[▶ 02:34](https://youtu.be/VbnrF6d9m5w?t=154) 【口頭】做任何問題，心裡原本就要有「答案」：知道最後一定會用什麼統計量來檢定。因為隨便弄一個統計量，你不會知道它的分配；推導半天，最後一定要變成你熟悉的那個。

| 情形 | 關心 | 最後一定會用 | $H_0$ 下的分配 |
|---|---|---|---|
| $N(\theta_1,1)$（變異數已知） | 平均數，$H_0:\theta_1=0$ | $\frac{\bar X-\theta_1}{1/\sqrt n}=\sqrt n\bar X$ | $N(0,1)$ |
| $N(0,\sigma^2)$（平均數已知為 0） | 變異數，$H_0:\sigma^2=1$ | $\sum\frac{X_i^2}{\sigma^2}=\sum X_i^2$ | $\chi^2(n)$ |
| $N(\mu,\sigma^2)$ 都未知 | 變異數，$H_0:\sigma^2=1$ | $\frac{(n-1)S^2}{\sigma^2}=(n-1)S^2$ | $\chi^2(n-1)$ |
| $N(\mu,\sigma^2)$ 都未知 | 平均數，$H_0:\mu=0$ | $\frac{\bar X-\mu}{S/\sqrt n}=\frac{\bar X}{S/\sqrt n}$ | $t(n-1)$ |
| $\sigma^2$ 已知 | 平均數 | $\frac{\bar X-\mu}{\sigma/\sqrt n}$ | $N(0,1)$ |

- [▶ 05:06](https://youtu.be/VbnrF6d9m5w?t=306) 平均數已知為 0 時，絕對不會用 $(n-1)S^2/\sigma^2$——$S^2$ 是因為 $\mu$ 不知道才用的。
- [▶ 06:39](https://youtu.be/VbnrF6d9m5w?t=399) 不管找的是 MP、UMP 還是 LRT，推到最後一定是你熟悉的那一種。所以常態隨機變數怎麼化成 $\chi^2$、標準常態、$t$，都要熟悉。
- [▶ 07:10](https://youtu.be/VbnrF6d9m5w?t=430) 大家會的就只有這些分配；出別的，出題的人自己也不會。

---

## 2. 例三續：Λ 化成 t 統計量

[▶ 00:30](https://youtu.be/VbnrF6d9m5w?t=30) 接上一集：$X_1,\dots,X_n$ iid $N(\theta_1,\theta_2)$，
$$H_0:\theta_1=0,\ \theta_2>0\quad\text{vs}\quad H_1:\theta_1\ne 0,\ \theta_2>0,$$
$$\Lambda=\left[\frac{\sum(x_i-\bar x)^2}{\sum x_i^2}\right]^{n/2}\le\lambda_0.$$

[▶ 07:40](https://youtu.be/VbnrF6d9m5w?t=460) 關心 $\theta_1$（平均數），$\theta_2$ 不知道 ⇒ 目標：$\frac{\bar X}{S/\sqrt n}\sim t(n-1)$（$H_0$ 下）。

**一連串一對一轉換**：

1. [▶ 02:03](https://youtu.be/VbnrF6d9m5w?t=123) 取 log 再取指數，等價於
$$\frac{\sum(x_i-\bar x)^2}{\sum x_i^2}\le c_0.$$
2. [▶ 10:47](https://youtu.be/VbnrF6d9m5w?t=647) 分母用 $\sum x_i^2=\sum(x_i-\bar x)^2+n\bar x^2$，上下除以 $\sum(x_i-\bar x)^2$：
$$\frac{1}{1+\dfrac{n\bar x^2}{\sum(x_i-\bar x)^2}}\le c_0.$$
3. [▶ 11:49](https://youtu.be/VbnrF6d9m5w?t=709) 移項：
$$\frac{n\bar x^2}{\sum(x_i-\bar x)^2}\ge\frac1{c_0}-1\equiv c_1.$$
4. [▶ 12:50](https://youtu.be/VbnrF6d9m5w?t=770) 分母除以 $n-1$ 變成 $S^2$（兩邊乘 $n-1$）：
$$\frac{\bar x^2}{s^2/n}\ge(n-1)c_1\equiv c_2,\qquad s^2=\frac{\sum(x_i-\bar x)^2}{n-1}.$$
5. [▶ 14:21](https://youtu.be/VbnrF6d9m5w?t=861) 左邊是 $\left|\frac{\bar x}{s/\sqrt n}\right|^2$，開根號：
$$\left|\frac{\bar x}{s/\sqrt n}\right|\ge\sqrt{c_2}\equiv c.$$

**找 $c$**（[▶ 15:52](https://youtu.be/VbnrF6d9m5w?t=952)）：$H_0$ 為真時 $\frac{\bar X}{S/\sqrt n}\sim t(n-1)$，對稱於 0：
$$\alpha=P\left(|t(n-1)|\ge c\right)\Rightarrow c=t_{\alpha/2}(n-1)\ (\text{查表}).$$

> **LRT 拒絕域**（[▶ 17:27](https://youtu.be/VbnrF6d9m5w?t=1047)）：
> $$\left|\frac{\bar x}{s/\sqrt n}\right|\ge t_{\alpha/2}(n-1).$$
> 這就是單樣本雙邊 **$t$ 檢定**。

【口頭】[▶ 14:51](https://youtu.be/VbnrF6d9m5w?t=891) 這個過程不是那麼容易，要一步一步練過才知道。[▶ 17:27](https://youtu.be/VbnrF6d9m5w?t=1047) 學過信賴區間、檢定，處理過很多種問題之後，碰到什麼問題就知道一定會用什麼：變異數知道／不知道時用什麼；處理變異數時平均數知道／不知道用什麼。

---

## 3. 兩個平均數比較前：變異數要相等

[▶ 18:27](https://youtu.be/VbnrF6d9m5w?t=1107) 統計最有興趣的是平均數。一個平均數：檢定它等於多少、找信賴區間；兩個平均數：想知道是否相等。

**設定**（[▶ 18:58](https://youtu.be/VbnrF6d9m5w?t=1138)）：$X_1,\dots,X_n$ iid $N(\mu_1,\sigma_1^2)$，$Y_1,\dots,Y_m$ iid $N(\mu_2,\sigma_2^2)$，兩組獨立。關心 $H_0:\mu_1=\mu_2$，或 $\mu_1-\mu_2$ 的信賴區間。

[▶ 19:29](https://youtu.be/VbnrF6d9m5w?t=1169) 必須假設 $\sigma_1^2=\sigma_2^2=\sigma^2$，不然沒有公式。書上通常直接寫 $\sigma^2$。

**問題**（[▶ 20:30](https://youtu.be/VbnrF6d9m5w?t=1230)）：怎麼知道兩個變異數相等？

- 實際不相等卻當作相等去做，整個假設是錯的：
  - 檢定：你以為顯著水準是 $\alpha$，實際型一錯誤機率可能不是 $\alpha$。
  - [▶ 21:30](https://youtu.be/VbnrF6d9m5w?t=1290) 信賴區間：你以為 95%，實際涵蓋 $\mu_1-\mu_2$ 的機率不是 0.95。
- [▶ 22:31](https://youtu.be/VbnrF6d9m5w?t=1351) 所以要**先**檢定 $\frac{\sigma_1^2}{\sigma_2^2}=1$（或找它的信賴區間）。接受 $H_0$ 就相信兩個變異數相等。要用 **F 分配**。

---

## 4. F 分配

> **定義**（[▶ 23:06](https://youtu.be/VbnrF6d9m5w?t=1386)；課本 §3.6.2，p. 212）：隨機變數 $F$ 具有自由度 $(r_1,r_2)$ 的 **F 分配**，記為 $F\sim F(r_1,r_2)$，如果存在**獨立**的
> $$U\sim\chi^2(r_1),\qquad V\sim\chi^2(r_2),$$
> 使
> $$F=\frac{U/r_1}{V/r_2}.$$

- [▶ 23:36](https://youtu.be/VbnrF6d9m5w?t=1416) $t$、$\chi^2$ 有一個自由度；F 分配有**兩個**。
- [▶ 25:48](https://youtu.be/VbnrF6d9m5w?t=1548) 兩個隨機變數各除以自由度再相除，仍是隨機變數。
- $\chi^2>0$，自由度 $>0$ ⇒ $F>0$。
- [▶ 26:20](https://youtu.be/VbnrF6d9m5w?t=1580) 形狀：從 0 上去再下來，右尾可以到無窮（分子可以到無窮），但很遠的地方機率很小。

**記號**（[▶ 27:50](https://youtu.be/VbnrF6d9m5w?t=1670)）：$F_\alpha(r_1,r_2)$：$F(r_1,r_2)$ **左尾**（某一點以下）機率為 $\alpha$ 的點——老師說「我們是查某一點以下的機率是 $\alpha$」。注意這和 $z_\alpha$（右尾）的慣例不同。

[▶ 28:20](https://youtu.be/VbnrF6d9m5w?t=1700) 要會查表；表不是全部都有，有些要用技巧導出來——下次講。

---

## 5. 一頁速查表

**先想好最後用什麼**：

| 關心 | 另一參數 | 統計量（$H_0$ 下） |
|---|---|---|
| $\mu$ | $\sigma^2$ 已知 | $\frac{\bar X-\mu_0}{\sigma/\sqrt n}\sim N(0,1)$ |
| $\mu$ | $\sigma^2$ 未知 | $\frac{\bar X-\mu_0}{S/\sqrt n}\sim t(n-1)$ |
| $\sigma^2$ | $\mu$ 已知 | $\frac{\sum(X_i-\mu)^2}{\sigma_0^2}\sim\chi^2(n)$ |
| $\sigma^2$ | $\mu$ 未知 | $\frac{(n-1)S^2}{\sigma_0^2}\sim\chi^2(n-1)$ |

**LRT ⇒ t 檢定**（$H_0:\mu=0$，$\sigma^2$ 未知）：
$$\Lambda^{2/n}=\frac{\sum(x_i-\bar x)^2}{\sum(x_i-\bar x)^2+n\bar x^2}=\frac{1}{1+\frac{t^2}{n-1}},\qquad t=\frac{\bar x}{s/\sqrt n}.$$
$\Lambda$ 小 ⇔ $|t|$ 大：拒絕域 $|t|\ge t_{\alpha/2}(n-1)$。

（上式中的 $\frac{t^2}{n-1}$ 寫法不是逐字稿內容，是把步驟 2–4 合併推得的。）

**兩樣本比較平均數**：需 $\sigma_1^2=\sigma_2^2$，要先檢定 $\sigma_1^2/\sigma_2^2=1$。

**F 分配**：$F=\frac{U/r_1}{V/r_2}$，$U\sim\chi^2(r_1)$、$V\sim\chi^2(r_2)$ 獨立；$F>0$；$F_\alpha(r_1,r_2)$ 左尾（以下）機率 $\alpha$。

---

## 6. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| F 分配 | 下一集：查表技巧、$\sigma_1^2/\sigma_2^2$ 的檢定與信賴區間 |
| $t$ 檢定 | 兩樣本 $t$ 檢定 |

---

## 附：本集一句話總結

> **做檢定前心裡要先知道最後會用哪個熟悉的統計量；$N(\theta_1,\theta_2)$ 檢定 $\theta_1=0$ 的 LRT，用 $\sum x_i^2=\sum(x_i-\bar x)^2+n\bar x^2$ 一步步轉成 $|\bar x/(s/\sqrt n)|\ge t_{\alpha/2}(n-1)$，就是 $t$ 檢定；兩樣本比較平均數要先確認變異數相等，這需要 F 分配：兩個獨立 $\chi^2$ 各除以自由度再相除。**

---

*筆記依據「高等統計學」Lec20 錄影逐字稿（whisper large-v3-turbo）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
