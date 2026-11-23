---
course: Mobile Sensing and Robotics 2（Uni Bonn, Summer 2021）
episode: 2-31
lecture: Projective 3-Point Algorithm using Grunert's Method
date: 待補（2021 夏季學期）
video: https://youtu.be/N1aCvzFll6Q
notes: 《視覺 SLAM 十四講》第 2 版 §7.7.2（書頁 182–184，PDF 頁 205–207）
---

# 第 2-31 集 · 投影三點演算法（P3P）：Grunert 法 [▶ 影片](https://youtu.be/N1aCvzFll6Q)

← 上一集：[2-29-zhang-calibration](2-29-zhang-calibration.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[2-33-relative-orientation](2-33-relative-orientation.md) →

> **課程**：Mobile Sensing and Robotics 2，Uni Bonn，2021 夏季學期 — 第 2-31 集
> **講者**：Cyrill Stachniss
> **來源**：YouTube 錄影逐字稿（45:48，Whisper `medium.en` 轉錄）＋《視覺 SLAM 十四講》§7.7.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【十四講補充】` 十四講有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 問題設定：已校正相機](#1-問題設定已校正相機)
- [2. 兩步驟](#2-兩步驟)
- [3. 射線方向與夾角](#3-射線方向與夾角)
- [4. 餘弦定理：三個方程](#4-餘弦定理三個方程)
- [5. 化成四次多項式](#5-化成四次多項式)
- [6. 四個解的幾何意義](#6-四個解的幾何意義)
- [7. 第二步：剛體轉換](#7-第二步剛體轉換)
- [8. 臨界圓柱、RANSAC、迭代解](#8-臨界圓柱ransac迭代解)
- [9. 總結](#9-總結)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

**空間後方交會**（spatial resection）：相機看到一個**已知**的場景（幾個點的完整 3D 座標已知），估計相機在哪拍的——投影中心在哪、朝哪個方向。方法：**投影三點演算法**（P3P），用 Grunert 的原始解法。

- 例：羅馬廣場上標了 3、4 個已知 3D 座標的點，要定位拍照的人（相機）。
- `⚠️ 逐字稿缺字`：Whisper 寫 “Gounod”，應為 **Grunert**（見影片標題）。

---

## 1. 問題設定：已校正相機

[▶ 01:20](https://youtu.be/N1aCvzFll6Q?t=80)

$$
\mathbf x_i = K\,R\,[\,I_3 \mid -\boldsymbol X_O\,]\,\mathbf X_i
$$

| 給定 | 要求 |
|---|---|
| 物體點 3D 座標 $\boldsymbol X_i$ | 外參：旋轉 $R$、投影中心 $\boldsymbol X_O$（6 個） |
| 它們的影像座標 $\mathbf x_i$ | |
| 資料關聯（沒有歧義） | |
| **校正矩陣 $K$**（內參、內方位） | |

**和 DLT 比較** [▶ 04:14](https://youtu.be/N1aCvzFll6Q?t=254)：

| | DLT（2-27） | P3P |
|---|---|---|
| 相機 | 未校正 | **已校正** |
| 未知數 | 11（$K, R, \boldsymbol X_O$） | 6（$R, \boldsymbol X_O$） |
| 最少點數 | 6 | **3**（沒有初始猜測時要 4，因為有歧義） |

- 本集給的是**直接解**：不需初始猜測；但**不是統計最佳**：不考慮任何不確定性（假設像素座標完美、控制點 3D 座標完美）。可以當作之後最小平方的初始猜測。
- 這問題研究很久了，約 160 年前就有解法；這裡講 Grunert 的原始解法 [▶ 07:14](https://youtu.be/N1aCvzFll6Q?t=434)。

---

## 2. 兩步驟

[▶ 07:36](https://youtu.be/N1aCvzFll6Q?t=456)

1. 求投影中心到三個點的**射線長度** $s_1, s_2, s_3$ → 得到三個點在**相機座標系**中的位置。
2. 現在三個點在兩個座標系都知道 → 算**剛體轉換**（相似轉換）→ $R$、$\boldsymbol X_O$。

**記號** [▶ 08:26](https://youtu.be/N1aCvzFll6Q?t=506)：

| 符號 | 意義 | 已知？ |
|---|---|---|
| $\boldsymbol X_1, \boldsymbol X_2, \boldsymbol X_3$ | 控制點 | 已知 |
| $\boldsymbol X_O$ | 投影中心 | 未知 |
| ${}^k\boldsymbol x_i$ | 相機座標系中的射線方向 | 已知（因為 $K$ 已知） |
| $s_1, s_2, s_3$ | $\boldsymbol X_O$ 到 $\boldsymbol X_i$ 的距離 | 未知（深度；但因為知道 3D 點，可以算出來） |
| $a, b, c$ | 三個控制點構成的三角形的邊長 | 已知 |
| $\alpha, \beta, \gamma$ | 射線之間的夾角 | 可算 |

（邊和角的對應：$a = \lVert\boldsymbol X_2 - \boldsymbol X_3\rVert$、$\alpha$ 是射線 2、3 的夾角；$b = \lVert\boldsymbol X_1 - \boldsymbol X_3\rVert$、$\beta$ 是射線 1、3 的夾角；$c = \lVert\boldsymbol X_1 - \boldsymbol X_2\rVert$、$\gamma$ 是射線 1、2 的夾角。依講者寫出的三個方程整理。）

---

## 3. 射線方向與夾角

[▶ 10:19](https://youtu.be/N1aCvzFll6Q?t=619)

相機座標系中的點 = 長度 × 單位方向：

$$
{}^{k}\boldsymbol X_i = R\,(\boldsymbol X_i - \boldsymbol X_O) = s_i\ {}^{k}\boldsymbol n_i, \qquad
{}^{k}\boldsymbol n_i = \pm\,\frac{K^{-1}\mathbf x_i}{\lVert K^{-1}\mathbf x_i \rVert}
$$

- $K^{-1}\mathbf x_i$ 是射線方向（2-24）；正規化成單位向量，$s_i$ 才是真正的距離。
- 正負號要依相機常數的符號，確保射線指向場景；本課相機常數為負，所以講者這裡寫負號 [▶ 11:29](https://youtu.be/N1aCvzFll6Q?t=689)。

**夾角** [▶ 13:07](https://youtu.be/N1aCvzFll6Q?t=787)：兩條射線的夾角 = 單位方向的內積：

$$
\cos\gamma = \frac{(\boldsymbol X_1 - \boldsymbol X_O)^{\mathsf T}(\boldsymbol X_2 - \boldsymbol X_O)}{\lVert\boldsymbol X_1 - \boldsymbol X_O\rVert\,\lVert\boldsymbol X_2 - \boldsymbol X_O\rVert} = {}^{k}\boldsymbol n_1^{\mathsf T}\,{}^{k}\boldsymbol n_2
$$

$\alpha, \beta, \gamma$ 都用反餘弦算出。

- 【口頭】這就是相機**一定要校正**的原因：不知道 $K$，就不知道射線方向，也算不出夾角 [▶ 14:52](https://youtu.be/N1aCvzFll6Q?t=892)。

---

## 4. 餘弦定理：三個方程

[▶ 15:35](https://youtu.be/N1aCvzFll6Q?t=935)

- $a, b, c$：已知 3D 點的歐氏距離，直接算。
- 三個三角形：$(\boldsymbol X_O, \boldsymbol X_1, \boldsymbol X_2)$、$(\boldsymbol X_O, \boldsymbol X_2, \boldsymbol X_3)$、$(\boldsymbol X_O, \boldsymbol X_3, \boldsymbol X_1)$：每個都知道一個角和對邊，要求另兩邊。

三角形 $(\boldsymbol X_O, \boldsymbol X_1, \boldsymbol X_2)$：已知 $\gamma$、$c$，未知 $s_1, s_2$ → **餘弦定理** [▶ 17:06](https://youtu.be/N1aCvzFll6Q?t=1026)：

$$
c^2 = s_1^2 + s_2^2 - 2 s_1 s_2 \cos\gamma
$$

（若 $\gamma = 90°$，最後一項消失，就是畢氏定理。）

另外兩個三角形同理：

$$
\boxed{\;
\begin{aligned}
a^2 &= s_2^2 + s_3^2 - 2 s_2 s_3 \cos\alpha \\
b^2 &= s_1^2 + s_3^2 - 2 s_1 s_3 \cos\beta \\
c^2 &= s_1^2 + s_2^2 - 2 s_1 s_2 \cos\gamma
\end{aligned}
\;}
$$

三個方程、三個未知數 $s_1, s_2, s_3$，含平方項和交叉項 → 整理後會得到一個**四次多項式**。

【十四講補充】§7.7.2（書頁 182–183）的出發點相同：三角形對應 $\Delta Oab - \Delta OAB$ 等（式 7.29），餘弦定理 $OA^2 + OB^2 - 2OA \cdot OB\cos\langle a, b\rangle = AB^2$（式 7.30–7.31），其中 $\cos\langle a, b\rangle$ 由 2D 像點算出——和講者的三個方程一樣（$OA = s_1$ 等）。

---

## 5. 化成四次多項式

[▶ 19:37](https://youtu.be/N1aCvzFll6Q?t=1177)

**代換**：$u = s_2 / s_1$，$v = s_3 / s_1$，即 $s_2 = u s_1$、$s_3 = v s_1$。

第一式：$a^2 = s_1^2 u^2 + s_1^2 v^2 - 2 s_1^2 uv\cos\alpha$，解出 $s_1^2$ [▶ 21:21](https://youtu.be/N1aCvzFll6Q?t=1281)；另兩式同理：

$$
s_1^2 = \frac{a^2}{u^2 + v^2 - 2uv\cos\alpha} = \frac{b^2}{1 + v^2 - 2v\cos\beta} = \frac{c^2}{1 + u^2 - 2u\cos\gamma}
$$

（後兩個分母是把 $s_2 = us_1$、$s_3 = vs_1$ 代入 $b^2$、$c^2$ 式得到的；講者只說「同樣的代換」。）

- 三個式子都等於 $s_1^2$。從其中一個等式解出 $u$，代入另一個 → 消去 $u$ 和 $s_1$，只剩 $v$ [▶ 23:08](https://youtu.be/N1aCvzFll6Q?t=1388)：

$$
A_4 v^4 + A_3 v^3 + A_2 v^2 + A_1 v + A_0 = 0
$$

- 係數 $A_0, \dots, A_4$ 只依賴已知的 $a, b, c, \alpha, \beta, \gamma$。講者說推導約要兩頁、沒有複雜的轉換，投影片上列出了係數但沒有念出來 → **待補**（`⚠️ 待確認`）[▶ 24:30](https://youtu.be/N1aCvzFll6Q?t=1470)。

**回代** [▶ 26:14](https://youtu.be/N1aCvzFll6Q?t=1574)：

1. 解四次多項式得 $v$。
2. 由 $s_1^2 = b^2 / (1 + v^2 - 2v\cos\beta)$ 得 $s_1$。
3. $s_3 = v\,s_1$。
4. 把 $s_1, s_3$ 代回含 $s_2$ 的方程（例如 $c^2$ 式或 $a^2$ 式），解出 $s_2$。

（用哪個式子算 $s_1$、用哪個解 $s_2$，講者口述不完全清楚，這裡依代換關係補成一種可行的順序。）

**最多四組解**：四次多項式 → 最多 **4 組** $(s_1, s_2, s_3)$ 都滿足方程 → 無法唯一定位相機 [▶ 27:20](https://youtu.be/N1aCvzFll6Q?t=1640)。

【十四講補充】§7.7.2（書頁 183–184）的整理方式不同：三式除以 $OC^2$，令 $x = OA/OC$、$y = OB/OC$（式 7.32），$v = AB^2/OC^2$、$uv = BC^2/OC^2$、$wv = AC^2/OC^2$（式 7.33），消去 $v$ 得兩個方程

$$
\begin{aligned}
(1 - u)y^2 - ux^2 - \cos\langle b, c\rangle y + 2uxy\cos\langle a, b\rangle + 1 &= 0 \\
(1 - w)x^2 - wy^2 - \cos\langle a, c\rangle x + 2wxy\cos\langle a, b\rangle + 1 &= 0
\end{aligned} \qquad (7.34)
$$

已知：三個餘弦（由 2D 像點）、$u = BC^2/AB^2$、$w = AC^2/AB^2$（由世界座標算，換到相機座標比值不變）；未知 $x, y$ → 二元二次方程，用吳消元法求解析解；**最多 4 個解**，用驗證點選最可能的。（注意十四講的 $u, v$ 和講者的 $u, v$ 意思不同。）

---

## 6. 四個解的幾何意義

[▶ 28:23](https://youtu.be/N1aCvzFll6Q?t=1703)

- 用到的資訊只有 $a, b, c$ 和 $\alpha, \beta, \gamma$。能不能找到另一個幾何組態，這六個量都不變？
- 可以：固定 $\boldsymbol X_O$，把三角形 $\boldsymbol X_1\boldsymbol X_2\boldsymbol X_3$ 沿某一邊**翻轉**（以 $a$、$b$ 或 $c$ 為旋轉軸），讓被轉的那個頂點再次落在它的射線上（等價於移動 $\boldsymbol X_O$，但固定 $\boldsymbol X_O$ 比較好畫）。
- 例：以某邊為軸把 $\boldsymbol X_1$ 往上轉，和原射線再次相交 → 邊長、夾角都相同，但空間組態不同。
- 三個旋轉軸 → 另外 **3 個**錯誤的解 ＋ 1 個正確的解 = 4 個。只靠這六個量，只能說「在這四個之一」。

**怎麼選出正確的解** [▶ 31:34](https://youtu.be/N1aCvzFll6Q?t=1894)：

1. **好的初始猜測**：例如相機上的 GPS，知道大概在哪 → 接近其中一個解、離其他解很遠。（或任何其他位姿先驗。）
2. **第四個點**：看哪個解和第四個點相容；或用 $(s_1, s_2, s_4)$ 再解一次，看哪個解重疊。

→ 三個點只能解到最多四個解的歧義；要**唯一**定位，需要**四個點**。

---

## 7. 第二步：剛體轉換

[▶ 33:22](https://youtu.be/N1aCvzFll6Q?t=2002)

- 有了 $s_i$ 和方向 ${}^k\boldsymbol n_i$ → 三個點在相機座標系中的座標 ${}^k\boldsymbol X_i = s_i\,{}^k\boldsymbol n_i$。
- 同三個點在世界座標系的座標已知，對應也已知 → 算剛體轉換，把兩組點疊在一起 → $R$、$\boldsymbol X_O$。（相對簡單的一步。）

**一種做法（複習）** [▶ 35:07](https://youtu.be/N1aCvzFll6Q?t=2107)：

1. 兩組點都以 $\boldsymbol X_1$ 為新的參考原點（平移讓兩組在 $\boldsymbol X_1$ 重合）。
2. 各有兩個方向向量：$\boldsymbol X_1 \to \boldsymbol X_2$、$\boldsymbol X_1 \to \boldsymbol X_3$。
3. 求讓這兩對向量重合的旋轉矩陣 → $R$；再直接算出平移。

（也可以用 2-07 的 SVD 法。）

【十四講補充】§7.7.2（書頁 184）：得到 $A, B, C$ 在相機座標系的 3D 座標後，就變成 3D-3D 的位姿估計（§7.9，即 ICP），帶匹配資訊的 3D-3D 很容易解。EPnP 也採用這種思路。

---

## 8. 臨界圓柱、RANSAC、迭代解

### 8.1 臨界圓柱

[▶ 37:34](https://youtu.be/N1aCvzFll6Q?t=2254)

- 三個控制點在一個圓柱底面的圓上，投影中心在這個圓柱的**側面**上 → **臨界圓柱**（critical cylinder）。
- 角度的小變化造成座標的大變化 → 數值不穩定，無法好好定位。要避免落入這種退化情況。

### 8.2 錯誤的資料關聯 → RANSAC

[▶ 38:30](https://youtu.be/N1aCvzFll6Q?t=2310)

- 現實中資料關聯常不完美（把控制點搞混）→ 一個錯的關聯就會得到完全錯的解。
- 試錯法（其實就是 RANSAC，2-22）：假設有夠多點的關聯是對的、少數是錯的。
  1. 例如有 6、7 個點，隨機選 3 個，跑 P3P。
  2. 用解出的相機位姿把其他點投影到影像，數有幾個和觀測一致。
  3. 重複，取最多點同意的解。
- 有一個離群值時，其他點仍會同意正確的解；離群值越多需要越多點。實務上很好用，控制點夠多時甚至能處理大量錯誤關聯。
- 【口頭】實務上一定要有 RANSAC 步驟，因為永遠無法確定沒有離群值 [▶ 41:02](https://youtu.be/N1aCvzFll6Q?t=2462)。

### 8.3 迭代解（多於三點）

[▶ 41:23](https://youtu.be/N1aCvzFll6Q?t=2483)

- 想考慮不確定性（例如影像點或 3D 點的共變異數）→ **非線性最小平方**；雜訊為高斯時是**統計最佳**。
- 步驟：觀測方程（觀測 = 像素座標）→ 初始解（用 P3P）→ 線性化 → 解線性系統更新外參 → 直到收斂（例如兩次迭代的參數差接近零）。
- 初始解要夠好：講者說朝向誤差約 5° 以內還可以；偏離初始解太多時非線性會出問題 [▶ 43:38](https://youtu.be/N1aCvzFll6Q?t=2618)。

【十四講補充】§7.7.2–7.7.3（書頁 184）：P3P 的問題：(1) 只用 3 個點，點多時難以利用更多資訊；(2) 3D 或 2D 點有雜訊或誤匹配時演算法失效。所以有 EPnP、UPnP 等用更多資訊、迭代最佳化的方法。SLAM 中通常先用 P3P/EPnP 估相機位姿，再建最小平方問題調整（**BA**）；運動夠連續時，也可以假設相機不動或等速，用推測值當初值。

---

## 9. 總結

[▶ 44:03](https://youtu.be/N1aCvzFll6Q?t=2643)

- 估計**已校正**相機的位姿（位置＋朝向），至少 3 個控制點（最好 4 個以上）。
- P3P 直接解：算得快（不需迭代）→ 很適合和 **RANSAC** 結合處理離群值。
- 要統計最佳：用迭代非線性最小平方，用上所有點和不確定性；但它假設沒有離群值 → 流程：RANSAC（內含 P3P）剔除離群值 → P3P 解當初始猜測 → 最小平方。還能得到精度資訊（對各參數知道多少）。

**流程** [▶ 36:21](https://youtu.be/N1aCvzFll6Q?t=2181)：

```
輸入：4 個點的 3D 座標、像素座標、K
1. 射線方向 K⁻¹ x_i → 反餘弦得 α, β, γ
2. 解四次多項式 → s1, s2, s3（最多 4 組）
3. 用第 4 個點選出正確的一組
4. 剛體轉換 → R, X_O
```

---

## 10. 一頁速查表

### 10.1 已知與未知

已知：$\boldsymbol X_i$、$\mathbf x_i$、$K$；未知：$R$、$\boldsymbol X_O$（6）；最少 3 點（唯一解要 4 點）。

### 10.2 第一步：距離

$$
\cos\gamma = {}^k\boldsymbol n_1^{\mathsf T}\,{}^k\boldsymbol n_2, \qquad {}^k\boldsymbol n_i \propto K^{-1}\mathbf x_i
$$

$$
a^2 = s_2^2 + s_3^2 - 2s_2s_3\cos\alpha, \quad
b^2 = s_1^2 + s_3^2 - 2s_1s_3\cos\beta, \quad
c^2 = s_1^2 + s_2^2 - 2s_1s_2\cos\gamma
$$

關鍵一步：$u = s_2/s_1$、$v = s_3/s_1$ →

$$
s_1^2 = \frac{a^2}{u^2 + v^2 - 2uv\cos\alpha} = \frac{b^2}{1 + v^2 - 2v\cos\beta} = \frac{c^2}{1 + u^2 - 2u\cos\gamma}
$$

→ 消去 $u$ → $v$ 的四次多項式（係數待補）→ 最多 4 組解。

### 10.3 四個解

三角形沿 $a$、$b$、$c$ 任一邊翻轉，邊長和夾角不變 → 1 個正確 + 3 個錯誤；用第四點或 GPS 先驗選。

### 10.4 第二步與實務

| 項 | 做法 |
|---|---|
| 剛體轉換 | ${}^k\boldsymbol X_i = s_i\,{}^k\boldsymbol n_i$ ↔ $\boldsymbol X_i$ → $R$、$\boldsymbol X_O$ |
| 退化 | 臨界圓柱 |
| 離群值 | RANSAC（每次 3 點） |
| 精化 | 非線性最小平方，P3P 當初值（朝向誤差約 5° 內） |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 已知 3D 點定位相機（3D-2D） | 視覺 SLAM 的追蹤 |
| 兩張影像、沒有已知 3D 點（2D-2D） | 2-33～2-37 相對定向、基本／本質矩陣 |
| 剛體轉換 | 2-07 ICP 的 SVD 解 |
| RANSAC + 最小子集 | 2-22 |

---

## 附：本集一句話總結

> **P3P（Grunert）：已校正相機看到 3 個已知 3D 點，先由 $K^{-1}\mathbf x_i$ 算射線夾角，再用三個餘弦定理方程（代換 $u = s_2/s_1$、$v = s_3/s_1$）化成 $v$ 的四次多項式求出距離 $s_1, s_2, s_3$（最多 4 組解，用第 4 點選），最後用剛體轉換得 $R$ 和 $\boldsymbol X_O$。算得快，適合放進 RANSAC，再用最小平方精化。**

---

## ⚠️ 待確認清單

1. [▶ 24:39](https://youtu.be/N1aCvzFll6Q?t=1479) 四次多項式的係數 $A_0, \dots, A_4$（以 $a, b, c, \alpha, \beta, \gamma$ 表示）：講者只展示投影片、沒有念出；BRIEF 列的十四講用不同的代換，沒有這組係數。待補。

---

*筆記依據 Cyrill Stachniss「Mobile Sensing and Robotics 2」Projective 3-Point Algorithm using Grunert's Method 錄影逐字稿（Whisper `medium.en`，45:48）與《視覺 SLAM 十四講》§7.7.2 整理。*
