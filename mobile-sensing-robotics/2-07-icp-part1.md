---
course: Mobile Sensing and Robotics 2（Uni Bonn, Summer 2021）
episode: 2-07
lecture: ICP & Point Cloud Registration – Part 1: Known Data Association & SVD
date: 待補（2021 夏季學期）
video: https://youtu.be/dhzLQfDBx2Q
notes: 《視覺 SLAM 十四講》第 2 版 §7.9–7.9.1（書頁 196–198，PDF 頁 219–221）
---

# 第 2-07 集 · 點雲對齊（一）：已知對應與 SVD 解法 [▶ 影片](https://youtu.be/dhzLQfDBx2Q)

← 上一集：[2-05-least-squares](2-05-least-squares.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[2-08-icp-part2](2-08-icp-part2.md) →

> **課程**：Mobile Sensing and Robotics 2，Uni Bonn，2021 夏季學期 — 第 2-07 集
> **講者**：Cyrill Stachniss
> **來源**：YouTube 錄影逐字稿（52:37，Whisper `medium.en` 轉錄）＋《視覺 SLAM 十四講》§7.9
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【十四講補充】` 十四講有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 為什麼需要點雲對齊](#1-為什麼需要點雲對齊)
- [2. 問題定義](#2-問題定義)
- [3. 先看答案：SVD 解法](#3-先看答案svd-解法)
- [4. 推導](#4-推導)
  - [4.1 換座標、改寫平移](#41-換座標改寫平移)
  - [4.2 展開目標函數](#42-展開目標函數)
  - [4.3 求最佳的 x₀](#43-求最佳的-x)
  - [4.4 求最佳的 R：化成 trace](#44-求最佳的-r化成-trace)
  - [4.5 用 SVD 構造 R 並證明最佳](#45-用-svd-構造-r-並證明最佳)
  - [4.6 唯一性與平移](#46-唯一性與平移)
- [5. 總結與預告：未知對應](#5-總結與預告未知對應)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

ICP（iterative closest point，迭代最近點）系列的第一部分：**已知**對應點時，怎麼一次算出讓兩組點雲對齊得最好的旋轉 $R$ 和平移 $t$。答案用 **SVD**（奇異值分解），而且是**直接解**（不需初始猜測）、**最佳解**。後半段完整推導為什麼。

---

## 1. 為什麼需要點雲對齊

[▶ 01:05](https://youtu.be/dhzLQfDBx2Q?t=65)

- 平台移動時，感測器（雷射、深度相機、雙眼相機）產生 3D 點。要把不同時刻的讀數放進**同一個參考座標系**。
- 例：小機器人每走幾公尺拍一次掃描，要把掃描對齊才能建出準確的模型。
- 例：車上的 3D 光達每秒產生 10 個點雲，對齊它們就能估計車的軌跡，把點雲接起來就是地圖。
- 掃描匹配（scan matching）是建圖的第一步；也就是 1-21 講的**光達里程計**。

---

## 2. 問題定義

[▶ 03:37](https://youtu.be/dhzLQfDBx2Q?t=217)

- 兩組點雲，在不同位置拍的。找一個**剛體轉換**（旋轉矩陣 $R$＋平移向量 $t$），讓兩組點雲裡**同一個 3D 位置**對齊。
- 假設點雲是剛體（不會變形）。
- 兩種基本做法：**SVD 法**（本集，ICP 的基礎）和之後的最小平方法（2-10）。

**已知對應** [▶ 06:32](https://youtu.be/dhzLQfDBx2Q?t=392)：

- 點雲 $Y = \{y_j\}$、$X = \{x_i\}$，點數可以不同。
- 對應集合 $C = \{(i, j)\}$：例如 $Y$ 的第 1 點對應 $X$ 的第 10 點。不是每個點都要有對應，但要夠多。
- **簡化記號** [▶ 08:55](https://youtu.be/dhzLQfDBx2Q?t=535)：只留有對應的點，重新排序，讓 $x_n$ 和 $y_n$ 是一對（不改變問題）。

**目標**（加權版本）[▶ 11:43](https://youtu.be/dhzLQfDBx2Q?t=703)：

$$
\{R^*, t^*\} = \arg\min_{R,\, t} \sum_{n} \bigl\| y_n - (R\, x_n + t) \bigr\|^2\, p_n
$$

- $p_n$：每對的權重（例如對這個對應有多確定）。完美對應時全部設為 1。
- 沒雜訊、量到完全相同的點時，總和可以是 0；實際上不是 0，但要盡量小。

**和絕對定向的關係** [▶ 10:42](https://youtu.be/dhzLQfDBx2Q?t=642)：這是大地測量和電腦視覺常用的**絕對定向**（absolute orientation）問題的特例。絕對定向找的是**相似轉換**（多一個尺度參數，例如單眼 3D 重建沒有尺度時）。點雲對齊已知尺度，尺度 = 1，只剩剛體轉換。

---

## 3. 先看答案：SVD 解法

[▶ 12:41](https://youtu.be/dhzLQfDBx2Q?t=761)

**性質**：存在**直接解**：不用迭代、不用初始猜測，而且是**最佳**的（假設對應正確）。

**直覺** [▶ 13:20](https://youtu.be/dhzLQfDBx2Q?t=800)：先**平移**讓兩組點的重心重合，再繞重心**旋轉**到誤差最小。重心好算；旋轉要用 SVD。

**步驟**：

1. 加權重心：

$$
y_0 = \frac{\sum_n p_n\, y_n}{\sum_n p_n}, \qquad x_0 = \frac{\sum_n p_n\, x_n}{\sum_n p_n}
$$

2. 去重心座標：$a_n = y_n - y_0$，$b_n = x_n - x_0$。

3. **交叉共變異數矩陣**（cross-covariance）：

$$
H = \sum_n p_n\, b_n\, a_n^{\mathsf T} = \sum_n p_n\, (x_n - x_0)(y_n - y_0)^{\mathsf T}
$$

4. SVD：$H = U D V^{\mathsf T}$。

5. 旋轉和平移：

$$
\boxed{\;R = V U^{\mathsf T}, \qquad t = y_0 - R\, x_0\;}
$$

6. 轉換：$\bar x_n = R x_n + t$，這時 $\sum_n \|y_n - \bar x_n\|^2 p_n$ 最小。

（$H$ 的乘法順序：講者口述「$Y$ 去重心、$X$ 去重心，算外積」，沒說哪個在前。以下**不是逐字稿內容**：要讓 $R = VU^{\mathsf T}$ 成立，$H$ 必須是「$X$ 去重心 × $Y$ 去重心的轉置」，見第 4.4 節的推導。如果把 $H$ 定義成轉置 $\sum p_n a_n b_n^{\mathsf T}$，$U$、$V$ 對調，答案變成 $R = UV^{\mathsf T}$，十四講就是這樣寫的。）

【口頭】「如果你不在乎為什麼，只想算 $R$ 和 $t$，看到這裡就可以停了。」[▶ 16:53](https://youtu.be/dhzLQfDBx2Q?t=1013) 已知對應時，這樣做就對了，不需要其他步驟。

【十四講補充】十四講 §7.9.1（書頁 196–198，PDF 頁 219–221）同樣的方法：
- 誤差 $e_i = p_i - (Rp_i' + t)$，目標 $\min \tfrac12\sum\|p_i - (Rp_i' + t)\|^2$。
- 去質心：$q_i = p_i - p$，$q_i' = p_i' - p'$。展開後交叉項求和為零，目標拆成「只和 $R$ 有關」和「只和質心有關」兩項：$\tfrac12\sum\|q_i - Rq_i'\|^2 + \|p - Rp' - t\|^2$。先求 $R$，再令第二項為零得 $t = p - Rp'$。
- $W = \sum q_i q_i'^{\mathsf T}$（目標 × 來源的轉置），SVD $W = U\Sigma V^{\mathsf T}$，$R = UV^{\mathsf T}$。
- 十四講說「若 $R$ 行列式為負，取 $-R$」。以下**不是逐字稿內容**，是筆記依線性代數推論的提醒：$\det R = -1$ 代表解出來的是**鏡射**而不是旋轉；直接取 $-R$ 在 3D 雖然讓行列式變正，但不保證最佳。常見的修正是 $R = V\,\mathrm{diag}(1, 1, \det(VU^{\mathsf T}))\,U^{\mathsf T}$（只翻轉最小奇異值對應的方向）。講者沒有談鏡射的情況。

---

## 4. 推導

[▶ 19:21](https://youtu.be/dhzLQfDBx2Q?t=1161)

為什麼這是最佳解、為什麼不需要初始猜測？從頭推。

### 4.1 換座標、改寫平移

**以 $Y$ 的加權重心為原點** [▶ 20:04](https://youtu.be/dhzLQfDBx2Q?t=1204)：

$$
y_0 = \frac{\sum_n p_n y_n}{\sum_n p_n}
$$

目標裡同時減掉、加回 $y_0$，問題不變：

$$
\sum_n \bigl\| (y_n - y_0) - (R x_n + t - y_0) \bigr\|^2 p_n
$$

**改寫平移** [▶ 21:32](https://youtu.be/dhzLQfDBx2Q?t=1292)：利用 $RR^{\mathsf T} = I$，

$$
R x_n + t - y_0 = R x_n - R R^{\mathsf T}(y_0 - t) = R\bigl(x_n - \underbrace{R^{\mathsf T}(y_0 - t)}_{=:\, x_0}\bigr)
$$

- 定義 $x_0 = R^{\mathsf T}(y_0 - t)$。知道 $R$、$t$ 就知道 $x_0$，**沒有增加未知數**。
- 這時**還不知道** $x_0$ 是 $X$ 的重心；那是之後算出來的結果。
- 平移被搬進括號：先從 $x_n$ 減掉 $x_0$，再旋轉。

新的問題：對 $R$ 和 $x_0$ 最小化

$$
\Phi(R, x_0) = \sum_n \bigl[ (y_n - y_0) - R(x_n - x_0) \bigr]^{\mathsf T} \bigl[ (y_n - y_0) - R(x_n - x_0) \bigr]\, p_n
$$

### 4.2 展開目標函數

[▶ 25:17](https://youtu.be/dhzLQfDBx2Q?t=1517)

求最小值：一階導數設為零、解方程（和學校學的一樣）。先把內積展開：

$$
\begin{aligned}
\Phi &= \sum_n (y_n - y_0)^{\mathsf T}(y_n - y_0)\, p_n && \text{（第 1 行：不含 } x_0, R\text{）} \\
&\quad + \sum_n (x_n - x_0)^{\mathsf T}(x_n - x_0)\, p_n && \text{（第 2 行：只含 } x_0\text{）} \\
&\quad - 2\sum_n (y_n - y_0)^{\mathsf T} R\, (x_n - x_0)\, p_n && \text{（第 3 行：兩者都有）}
\end{aligned}
$$

（第 2 行原本是 $(x_n - x_0)^{\mathsf T}R^{\mathsf T}R(x_n - x_0)$，用 $R^{\mathsf T}R = I$ 化簡，所以不含 $R$。第 3 行的兩個交叉項是純量、互為轉置，合併成 $-2$ 倍。這兩點說明是筆記補的。）

### 4.3 求最佳的 x₀

[▶ 27:35](https://youtu.be/dhzLQfDBx2Q?t=1655)

對 $x_0$ 微分：

- 第 1 行：常數 → 0。
- 第 2 行：$x_0$ 的二次式 → $-2\sum_n (x_n - x_0)\, p_n$。
- 第 3 行：$x_0$ 的一次式，負號和 $-x_0$ 的負號抵消 → $+2\sum_n R^{\mathsf T}(y_n - y_0)\, p_n$。

$$
\frac{\partial \Phi}{\partial x_0} = -2\sum_n (x_n - x_0)\, p_n + 2 R^{\mathsf T}\sum_n (y_n - y_0)\, p_n
$$

設為零、除以 2、移項：

$$
\sum_n (x_n - x_0)\, p_n = R^{\mathsf T}\sum_n (y_n - y_0)\, p_n
$$

**右邊是零** [▶ 29:54](https://youtu.be/dhzLQfDBx2Q?t=1794)：$y_0$ 是 $y_n$ 的加權平均，所以「每個點減掉平均、再加權加總」= 0：

$$
\sum_n (y_n - y_0)\, p_n = \sum_n p_n y_n - y_0 \sum_n p_n = y_0\sum_n p_n - y_0\sum_n p_n = 0
$$

旋轉矩陣乘零向量還是零，所以

$$
\sum_n (x_n - x_0)\, p_n = 0 \quad\Rightarrow\quad \sum_n p_n x_n = x_0 \sum_n p_n \quad\Rightarrow\quad \boxed{\;x_0 = \frac{\sum_n p_n x_n}{\sum_n p_n}\;}
$$

**$x_0$ 就是 $X$ 的加權重心**。這是**最小化的結果**，不是我們事先設定的 [▶ 32:03](https://youtu.be/dhzLQfDBx2Q?t=1923)；這也是為什麼取名 $x_0$。

### 4.4 求最佳的 R：化成 trace

[▶ 33:13](https://youtu.be/dhzLQfDBx2Q?t=1993)

只有第 3 行含 $R$，第 1、2 行和 $R$ 無關。所以

$$
\min_R \Phi \quad\Longleftrightarrow\quad \max_R \sum_n (y_n - y_0)^{\mathsf T} R\,(x_n - x_0)\, p_n \qquad \text{s.t.}\quad R^{\mathsf T}R = I
$$

（最小化負的那一項 = 最大化正的那一項。）

用去重心座標 $a_n = y_n - y_0$、$b_n = x_n - x_0$（兩組點的重心都移到原點）[▶ 34:39](https://youtu.be/dhzLQfDBx2Q?t=2079)：

$$
\max_R \sum_n a_n^{\mathsf T} R\, b_n\, p_n
$$

**改寫成 trace** [▶ 35:58](https://youtu.be/dhzLQfDBx2Q?t=2158)（為了之後用一個關於 trace 的不等式）：

$$
\sum_n a_n^{\mathsf T} R\, b_n\, p_n = \operatorname{tr}\!\Bigl( R \underbrace{\sum_n p_n\, b_n a_n^{\mathsf T}}_{=:\, H} \Bigr) = \operatorname{tr}(R H)
$$

（以下說明不是逐字稿內容：$a^{\mathsf T}Rb$ 是純量，等於自己的 trace；再用 $\operatorname{tr}(AB) = \operatorname{tr}(BA)$：$\operatorname{tr}(a^{\mathsf T}Rb) = \operatorname{tr}(R\,b\,a^{\mathsf T})$。這就決定了 $H = \sum p_n b_n a_n^{\mathsf T}$ 的乘法順序。）

**任務**：找讓 $\operatorname{tr}(RH)$ 最大的旋轉矩陣 $R$。

### 4.5 用 SVD 構造 R 並證明最佳

[▶ 37:15](https://youtu.be/dhzLQfDBx2Q?t=2235)

**策略**：用 SVD 分解 $H$，定義一個 $R$，再證明它是最佳的。

**SVD**：

$$
H = U D V^{\mathsf T}, \qquad U^{\mathsf T}U = I, \quad V^{\mathsf T}V = I, \quad D = \operatorname{diag}(d_1, d_2, d_3),\ d_i \ge 0
$$

**定義** $R = VU^{\mathsf T}$ [▶ 38:35](https://youtu.be/dhzLQfDBx2Q?t=2315)：

$$
\operatorname{tr}(RH) = \operatorname{tr}(V U^{\mathsf T} U D V^{\mathsf T}) = \operatorname{tr}(V D V^{\mathsf T})
$$

（中間 $U^{\mathsf T}U = I$。）

**把 $D$ 拆成兩半** [▶ 39:22](https://youtu.be/dhzLQfDBx2Q?t=2362)：$D$ 是對角、元素非負，令 $\sqrt D = \operatorname{diag}(\sqrt{d_1}, \sqrt{d_2}, \sqrt{d_3})$，$D = \sqrt D\sqrt D$；對角矩陣的轉置是自己：

$$
\operatorname{tr}(V D V^{\mathsf T}) = \operatorname{tr}\bigl(V\sqrt D\,(V\sqrt D)^{\mathsf T}\bigr)
$$

定義 $A = V\sqrt D$：

$$
\operatorname{tr}(RH) = \operatorname{tr}(A A^{\mathsf T})
$$

到這裡只用了 SVD 的性質。$AA^{\mathsf T}$ 是正定（至少半正定）矩陣。

**不等式** [▶ 41:42](https://youtu.be/dhzLQfDBx2Q?t=2502)：對正定的 $AA^{\mathsf T}$ 和**任何**旋轉矩陣 $R'$，

$$
\operatorname{tr}(A A^{\mathsf T}) \ge \operatorname{tr}(R' A A^{\mathsf T})
$$

講者說這來自 **Schwarz 不等式**。以下**不是逐字稿內容**，是筆記依 Cauchy-Schwarz 補的證明：設 $a_i$ 是 $A$ 的第 $i$ 欄，則

$$
\operatorname{tr}(R' A A^{\mathsf T}) = \operatorname{tr}(A^{\mathsf T} R' A) = \sum_i a_i^{\mathsf T}(R' a_i) \le \sum_i \|a_i\|\,\|R' a_i\| = \sum_i \|a_i\|^2 = \operatorname{tr}(A^{\mathsf T}A) = \operatorname{tr}(AA^{\mathsf T})
$$

（不等號是 Cauchy-Schwarz；$\|R'a_i\| = \|a_i\|$ 因為旋轉保持長度。）

**結論** [▶ 42:47](https://youtu.be/dhzLQfDBx2Q?t=2567)：把 $AA^{\mathsf T} = RH$ 代回：

$$
\operatorname{tr}(RH) = \operatorname{tr}(AA^{\mathsf T}) \ge \operatorname{tr}(R' A A^{\mathsf T}) = \operatorname{tr}(R' R H)
$$

$R'R$ 是另一個任意的旋轉矩陣。所以**換成任何其他旋轉矩陣，trace 都不會更大** → $R = VU^{\mathsf T}$ 讓 $\operatorname{tr}(RH)$ 最大 → 讓 $\Phi$ 最小。

（講者在這裡說了幾次「最大化目標函數」，隨即更正：目標函數是要**最小化**；被最大化的是 trace 那一項。）

不等式的出處：講者說是 Arun 等人的論文（`⚠️ 待確認`：Whisper 寫 “1978 paper of Aaron et al”，年份和作者拼法待確認）。

### 4.6 唯一性與平移

**唯一性** [▶ 45:06](https://youtu.be/dhzLQfDBx2Q?t=2706)：3D 時 $H$、$U$、$V$、$D$ 都是 $3 \times 3$。只有當 $H$ **滿秩**（$D$ 的三個奇異值都大於零）時解才唯一；有一個奇異值為零時，有多個可能的 $R$。

**平移** [▶ 45:56](https://youtu.be/dhzLQfDBx2Q?t=2756)：從 $x_0$ 的定義 $x_0 = R^{\mathsf T}(y_0 - t)$，兩邊左乘 $R$：$Rx_0 = y_0 - t$，

$$
t = y_0 - R\, x_0
$$

**小結** [▶ 46:41](https://youtu.be/dhzLQfDBx2Q?t=2801)：只需要算交叉共變異數矩陣（簡單）、加權重心（簡單）、一個 SVD（數學工具箱）。得到的解：**最佳**、**不需初始猜測**（直接解）、而且很快（只有 $3 \times 3$ 矩陣的 SVD）。

---

## 5. 總結與預告：未知對應

[▶ 48:02](https://youtu.be/dhzLQfDBx2Q?t=2882)

- 已知對應時對齊兩組點雲的方法：剛體轉換，是絕對定向問題的特例（有尺度歧義時加一個參數也能做，目標函數會複雜一點），直接又最佳，很有效也很常用。
- 標準 ICP 就是建立在這個 SVD 解上。

**預告：未知對應**（2-08）[▶ 49:04](https://youtu.be/dhzLQfDBx2Q?t=2944)：

- 不知道對應時，**沒有直接解**。
- 可以猜一組對應（不是最佳的）→ 對齊結果不完美 → **重複**：重新猜對應、重新對齊。這就是 ICP。
- 前提：對應不完美，但大致知道（有初始猜測，例如依點的位置找最近鄰）。完全沒有初始猜測時，可以先把重心對齊，但通常比較麻煩。
- ICP 已經有將近 30 年歷史，是點雲對齊和很多 SLAM 演算法的標準：每個點找最近鄰 → 算剛體轉換 → 執行對齊 → 重複直到不再改變。

---

## 6. 一頁速查表

### 6.1 演算法

| 步驟 | 公式 |
|---|---|
| 目標 | $\min_{R,t}\sum_n \|y_n - (Rx_n + t)\|^2 p_n$ |
| 加權重心 | $y_0 = \frac{\sum p_n y_n}{\sum p_n}$，$x_0 = \frac{\sum p_n x_n}{\sum p_n}$ |
| 交叉共變異數 | $H = \sum_n p_n (x_n - x_0)(y_n - y_0)^{\mathsf T}$ |
| SVD | $H = UDV^{\mathsf T}$ |
| 旋轉 | $R = VU^{\mathsf T}$ |
| 平移 | $t = y_0 - Rx_0$ |
| 唯一 | $H$ 滿秩 |
| 性質 | 直接解、最佳、不需初始猜測（假設對應正確） |

### 6.2 推導關鍵步驟

| 步驟 | 關鍵 |
|---|---|
| 改寫平移 | $Rx + t - y_0 = R(x - x_0)$，$x_0 := R^{\mathsf T}(y_0 - t)$ |
| 求 $x_0$ | 導數設零，$\sum(y_n - y_0)p_n = 0$ ⇒ $x_0$ 是 $X$ 的加權重心 |
| 化成 trace | $\max\sum a_n^{\mathsf T}Rb_np_n = \max\operatorname{tr}(RH)$，$H = \sum p_n b_n a_n^{\mathsf T}$ |
| 代入 SVD | $\operatorname{tr}(VU^{\mathsf T}UDV^{\mathsf T}) = \operatorname{tr}(AA^{\mathsf T})$，$A = V\sqrt D$ |
| 最佳性 | $\operatorname{tr}(AA^{\mathsf T}) \ge \operatorname{tr}(R'AA^{\mathsf T})$（Cauchy-Schwarz：$a^{\mathsf T}R'a \le \|a\|^2$） |

### 6.3 注意

| 項 | 說明 |
|---|---|
| $H$ 的順序 | $\sum b a^{\mathsf T}$（來源 × 目標$^{\mathsf T}$）→ $R = VU^{\mathsf T}$；轉置定義（十四講）→ $R = UV^{\mathsf T}$ |
| 鏡射（推論） | $\det(VU^{\mathsf T}) = -1$ 時用 $R = V\operatorname{diag}(1, 1, -1)U^{\mathsf T}$ |
| 絕對定向 | 多一個尺度參數的一般化問題 |

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 已知對應的 SVD 解 | 2-08 ICP：每輪猜對應後用它算轉換 |
| 對應的權重 $p_n$ | 2-08（剔除壞對應）、2-15（強健核） |
| 最小平方解法（另一種做法） | 2-10 ICP 的非線性最小平方（point-to-plane 等） |
| 對齊得到的相對轉換 | 2-11 位姿圖的邊（虛擬觀測） |
| 絕對定向、相似轉換 | MSR2 相機部分（單眼重建沒有尺度） |

---

## 附：本集一句話總結

> **已知對應時，點雲對齊有直接、最佳的閉式解：先算兩組點的加權重心並去重心，交叉共變異數 $H = \sum p_n(x_n - x_0)(y_n - y_0)^{\mathsf T}$ 做 SVD $H = UDV^{\mathsf T}$，則 $R = VU^{\mathsf T}$、$t = y_0 - Rx_0$。推導關鍵：$x_0$ 是最小化的結果；旋轉部分化成最大化 $\operatorname{tr}(RH)$，再用 Cauchy-Schwarz 證明 SVD 給出的 $R$ 最佳。**

---

## ⚠️ 待確認清單

1. [▶ 43:55](https://youtu.be/dhzLQfDBx2Q?t=2635) trace 不等式的出處：Whisper 寫 “1978 paper of Aaron et al”，作者拼法（推測 Arun）與年份待確認。

---

*筆記依據 Cyrill Stachniss「Mobile Sensing and Robotics 2」ICP Part 1 錄影逐字稿（Whisper `medium.en`，52:37）與《視覺 SLAM 十四講》§7.9 整理。*
