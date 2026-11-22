---
course: 高等統計學（數理統計續）
episode: 26
lecture: Lec26（第十四週 1/2）
date: 待補
video: https://youtu.be/WURM1Rq-5Cg
notes: Hogg 8th ed. §4.7 卡方檢定（p. 283 起）；習題 4.7.5 孟德爾豌豆（p. 290）
---

# 第 26 集 · 第十四週 (1/2)：Pearson 卡方適合度檢定——Q_k 趨近 χ²(k−1)（k=2 的證明）；例：孟德爾遺傳理論 [▶ 影片](https://youtu.be/WURM1Rq-5Cg)

← 上一集：[25](25-bivariate-normal-marginal-conditional-chi-square-intro.md) ｜ [總目錄](../README.md) ｜ 下一集：[27](27-chi-square-test-estimated-parameters-normality.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 26 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（約 32 分鐘，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §4.7
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚的地方

> ⚠️ 逐字稿缺字（整集通用）：「Mendelian theory」→「Mandaling Theory／mandarin theory」，「pea」→「P／堕類」，「yellow」→「arrow／Error」，「二項」→「歐向／偶向」，「theoretical」→「Cheretka」，「$\chi^2$」→「卡方／High square」。[▶ 00:00](https://youtu.be/WURM1Rq-5Cg?t=0) 開頭重複的「字幕提供 李宗盛」是幻聽。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 設定：實際次數 vs 理論次數](#1-設定實際次數-vs-理論次數)
- [2. Q_k 與它的極限分配](#2-q_k-與它的極限分配)
- [3. 證明 k=2](#3-證明-k2)
- [4. 檢定](#4-檢定)
- [5. 統計為什麼到處都要用](#5-統計為什麼到處都要用)
- [6. 例：孟德爾遺傳理論](#6-例孟德爾遺傳理論)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)
- [⚠️ 待確認清單](#️-待確認清單)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| $Q_k=\sum\frac{(N_j-np_j)^2}{np_j}\xrightarrow{D}\chi^2(k-1)$ | §4.7 |
| $k=2$ 的證明（CLT） | §4.7 |
| 孟德爾豌豆例 | 習題 4.7.5（p. 290，數字不同） |

---

## 1. 設定：實際次數 vs 理論次數

[▶ 00:00](https://youtu.be/WURM1Rq-5Cg?t=0) $X_1,\dots,X_n$ iid 來自未知分配 $F$。
$$H_0:F=F_0\quad(F_0\text{ 是我們給的，例如常態、}\chi^2\text{、Gamma}).$$

[▶ 01:34](https://youtu.be/WURM1Rq-5Cg?t=94) 把空間切成 $A_1,\dots,A_k$。$H_0$ 下分配已知，每塊的機率可以算：
$$p_j=\int_{A_j}f_0(x)\,dx,\qquad j=1,\dots,k.$$

- **理論次數**（theoretical number）：$np_j$——做了 $n$ 次實驗，$H_0$ 下理論上落在 $A_j$ 的次數。
- [▶ 03:44](https://youtu.be/WURM1Rq-5Cg?t=224) **實際次數**（樣本次數）：$N_j$＝$X_1,\dots,X_n$ 真正落在 $A_j$ 的個數。樣本可以觀察，所以算得出來。$\sum_{j=1}^kN_j=n$。

---

## 2. Q_k 與它的極限分配

> **定義**（[▶ 05:18](https://youtu.be/WURM1Rq-5Cg?t=318)）：
> $$Q_k=\sum_{j=1}^k\frac{(N_j-np_j)^2}{np_j}=\sum\frac{(\text{實際}-\text{理論})^2}{\text{理論}}.$$
>
> **定理**：$H_0$ 為真時，$Q_k\xrightarrow{D}\chi^2(k-1)$。

---

## 3. 證明 k=2

[▶ 05:49](https://youtu.be/WURM1Rq-5Cg?t=349) 只證 $k=2$（分成 $A_1$、$A_2$ 兩塊），比較簡單。

$$Q_2=\frac{(N_1-np_1)^2}{np_1}+\frac{(N_2-np_2)^2}{np_2}.$$

**化簡**（[▶ 07:29](https://youtu.be/WURM1Rq-5Cg?t=449)）：

- 只有兩塊：沒落在 $A_1$ 就落在 $A_2$ ⇒ $N_2=n-N_1$，$p_2=1-p_1$。
- 第二項分子：$N_2-np_2=(n-N_1)-n(1-p_1)=-(N_1-np_1)$，平方後一樣。

[▶ 08:32](https://youtu.be/WURM1Rq-5Cg?t=512)
$$Q_2=(N_1-np_1)^2\left[\frac{1}{np_1}+\frac{1}{n(1-p_1)}\right]=\frac{(N_1-np_1)^2}{np_1(1-p_1)}=\left(\frac{N_1-np_1}{\sqrt{np_1(1-p_1)}}\right)^2.$$

**$N_1$ 的分配**（[▶ 11:09](https://youtu.be/WURM1Rq-5Cg?t=669)）：把「落在 $A_1$」當成功、「落在 $A_2$」當失敗。做 $n$ 次，成功機率 $p_1$ ⇒
$$N_1\sim b(n,p_1).$$
（知道成功幾次就知道失敗幾次，所以 $N_2=n-N_1$。）

**CLT**（[▶ 09:35](https://youtu.be/WURM1Rq-5Cg?t=575)）：以前證過 $Y\sim b(n,p)$ 時
$$\frac{\hat p-p}{\sqrt{p(1-p)/n}}\xrightarrow{D}N(0,1);$$
上下乘以 $n$：
$$\frac{Y-np}{\sqrt{np(1-p)}}\xrightarrow{D}N(0,1).$$

[▶ 14:16](https://youtu.be/WURM1Rq-5Cg?t=856) 所以 $\frac{N_1-np_1}{\sqrt{np_1(1-p_1)}}\xrightarrow{D}N(0,1)$；$N(0,1)$ 的平方是 $\chi^2(1)$：
$$Q_2\xrightarrow{D}\chi^2(1)=\chi^2(k-1).$$
∎

（這一步用到：$Z_n\xrightarrow{D}Z$ ⇒ $Z_n^2\xrightarrow{D}Z^2$，連續函數保持依分配收斂。這句不是逐字稿內容，是補上的依據。）

[▶ 14:47](https://youtu.be/WURM1Rq-5Cg?t=887) 一般 $k$ 的證明比較困難，但道理一樣。

---

## 4. 檢定

[▶ 16:50](https://youtu.be/WURM1Rq-5Cg?t=1010) **直覺**：$H_0$ 對的話，實際次數應該很接近理論次數，$(N_j-np_j)^2$ 都小（不管大一點或小一點）。所以 $Q_k$ 小就接受 $H_0$，大就拒絕。

> **Pearson 卡方檢定**（[▶ 17:50](https://youtu.be/WURM1Rq-5Cg?t=1070)）：拒絕 $H_0$ 若
> $$Q_k\ge\chi^2_\alpha(k-1),$$
> $\chi^2_\alpha(k-1)$ 是 $\chi^2(k-1)$ **右尾**機率 $\alpha$ 的點。$Q_k$ 是**檢定統計量**。

⚠️ 記號提醒：這裡老師的 $\chi^2_\alpha$ 是**右尾**（「超過這一點的機率是 $\alpha$」），和第 15、19 集用的左尾記法不同。

**size**（[▶ 18:51](https://youtu.be/WURM1Rq-5Cg?t=1131)）：$H_0$ 下 $Q_k\ \dot\sim\ \chi^2(k-1)$，
$$P_{H_0}\left(Q_k\ge\chi^2_\alpha(k-1)\right)\approx\alpha.$$

[▶ 19:51](https://youtu.be/WURM1Rq-5Cg?t=1191) 要分幾塊：看樣本數，樣本數大就分多塊、小就分少塊。現在只學理論，實際做時要自己再看。

【課本補充】§4.7 的經驗法則是每塊的理論次數 $np_j$ 不要太小（常見建議至少 5），$\chi^2$ 近似才好。

---

## 5. 統計為什麼到處都要用

【口頭】[▶ 20:22](https://youtu.be/WURM1Rq-5Cg?t=1222)

- 每一個領域都要用統計。交大電機學院（電子、電機、資工）都要修統計：去電子公司上班，生產過程中有很多不確定因素沒辦法控制，只能用統計。問題是電子的，解決要用統計；不懂統計就沒辦法跟統計的人合作。
- [▶ 21:24](https://youtu.be/WURM1Rq-5Cg?t=1284) 管理有管理統計，經濟有計量經濟，生物有生物統計，流行病學很多都是統計。
- [▶ 21:55](https://youtu.be/WURM1Rq-5Cg?t=1315) 早期經濟學家可以看社會現象憑空想理論；現在太複雜，要收集大量資料、用統計方法分析，再回頭想理論應該長什麼樣子。所以現在的經濟學家必然是統計學家。
- 統計方法可以配合各種科學，驗證那些理論對不對。

---

## 6. 例：孟德爾遺傳理論

[▶ 22:57](https://youtu.be/WURM1Rq-5Cg?t=1377) **孟德爾理論**（Mendelian theory）：某種豌豆，形狀有兩種（round 圓、angular），顏色有兩種（yellow 黃、green 綠），共四類，理論機率：

| 類別 | 理論機率 |
|---|---|
| $A_1$：round, yellow | $\frac{9}{16}$ |
| $A_2$：round, green | $\frac{3}{16}$ |
| $A_3$：angular, yellow | $\frac{3}{16}$ |
| $A_4$：angular, green | $\frac{1}{16}$ |

⚠️ 待確認：[▶ 23:27](https://youtu.be/WURM1Rq-5Cg?t=1407) 老師說「應該是講它的葉子」有兩種顏色。依課本習題 4.7.5，分類的是豌豆（種子）的形狀（round／wrinkled）和顏色，不是葉子。另外課本的第二類是 wrinkled and yellow、第三類是 round and green，和課堂的排序不同，但 $\frac{3}{16}$ 兩類對稱，不影響結果。

**假設**（[▶ 25:02](https://youtu.be/WURM1Rq-5Cg?t=1502)）：
$$H_0:p_1=\frac{9}{16},\ p_2=\frac{3}{16},\ p_3=\frac{3}{16},\ p_4=\frac{1}{16}.$$
$H_0$ 對 ⇒ 理論對；不對 ⇒ 理論不對。

**資料**（[▶ 25:34](https://youtu.be/WURM1Rq-5Cg?t=1534)）：$n=556$，

| | $A_1$ | $A_2$ | $A_3$ | $A_4$ |
|---|---|---|---|---|
| 實際 $N_j$ | 315 | 108 | 101 | 32 |
| 理論 $np_j$ | 312.75 | 104.25 | 104.25 | 34.75 |
| $\frac{(N_j-np_j)^2}{np_j}$ | 0.016 | 0.135 | 0.101 | 0.218 |

（理論次數與各項數值不是逐字稿內容，是依 $556\times p_j$ 算出來的，用來核對老師的 0.47。）

$$Q_4=\frac{(315-556\cdot\frac9{16})^2}{556\cdot\frac9{16}}+\frac{(108-556\cdot\frac3{16})^2}{556\cdot\frac3{16}}+\frac{(101-556\cdot\frac3{16})^2}{556\cdot\frac3{16}}+\frac{(32-556\cdot\frac1{16})^2}{556\cdot\frac1{16}}\approx 0.47.$$

⚠️ 逐字稿缺字：[▶ 28:40](https://youtu.be/WURM1Rq-5Cg?t=1720) 老師最後一項分母念成「556 乘以 16 分之 9」，應是 $\frac1{16}$（算出 0.47 用的是 $\frac1{16}$）。

**比較**（[▶ 29:10](https://youtu.be/WURM1Rq-5Cg?t=1750)）：$\alpha=0.05$，自由度 $k-1=3$，查表 $\chi^2_{0.05}(3)=7.81$。
$$Q_4=0.47<7.81.$$

> **結論**（[▶ 30:13](https://youtu.be/WURM1Rq-5Cg?t=1813)）：接受 $H_0$，接受孟德爾理論。

[▶ 30:56](https://youtu.be/WURM1Rq-5Cg?t=1856) 理論次數和實際次數真的很接近，$Q_4$ 才那麼小。$H_0$ 對時，超過 7.81 的機率只有 0.05；實際的點 0.47 比它小太多。差得很遠才不相信 $H_0$。有時候驗證一個理論就是這樣驗證的。

---

## 7. 一頁速查表

**Pearson 卡方適合度檢定**（$H_0:F=F_0$）：

1. 切成 $A_1,\dots,A_k$，算 $p_j=P_{H_0}(X\in A_j)$。
2. 理論次數 $np_j$；實際次數 $N_j$。
3. $Q_k=\sum_{j=1}^k\frac{(N_j-np_j)^2}{np_j}\ \dot\sim\ \chi^2(k-1)$（$H_0$ 下）。
4. 拒絕 $H_0$ 若 $Q_k\ge\chi^2_\alpha(k-1)$（右尾）。

**$k=2$ 證明關鍵**：$N_2=n-N_1$、$p_2=1-p_1$ ⇒
$$Q_2=\left(\frac{N_1-np_1}{\sqrt{np_1(1-p_1)}}\right)^2,\quad N_1\sim b(n,p_1)\ \xrightarrow{\text{CLT}}\ N(0,1)^2=\chi^2(1).$$

**孟德爾例**：$n=556$，$(315,108,101,32)$ vs $(9,3,3,1)/16$：$Q_4\approx 0.47<\chi^2_{0.05}(3)=7.81$ ⇒ 接受。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 卡方檢定 | 下一集（最後一集）：卡方檢定的其他用法（獨立性、參數需估計時） |

---

## 附：本集一句話總結

> **Pearson 卡方檢定把空間切成 $k$ 塊，比較實際次數 $N_j$ 和 $H_0$ 下的理論次數 $np_j$，統計量 $Q_k=\sum(N_j-np_j)^2/(np_j)$ 在 $H_0$ 下趨近 $\chi^2(k-1)$（$k=2$ 時就是二項的 CLT 再平方），太大就拒絕；孟德爾豌豆資料算出 $Q_4\approx 0.47$ 遠小於 7.81，所以接受孟德爾理論。**

---

## ⚠️ 待確認清單

1. [▶ 23:27](https://youtu.be/WURM1Rq-5Cg?t=1407) 孟德爾例分類的是葉子還是豌豆（種子）？課本習題 4.7.5 是豌豆的形狀與顏色。

---

*筆記依據「高等統計學」Lec26 錄影逐字稿（whisper large-v3-turbo）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
