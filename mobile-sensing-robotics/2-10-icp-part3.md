---
course: Mobile Sensing and Robotics 2（Uni Bonn, Summer 2021）
episode: 2-10
lecture: ICP & Point Cloud Registration – Part 3: Non-linear Least Squares
date: 待補（2021 夏季學期）
video: https://youtu.be/CJE59i8oxIE
notes: MVG 附錄 6 §A6.2（書頁 600–602，PDF 頁 618–620）；《視覺 SLAM 十四講》第 2 版 §7.9.2（書頁 198，PDF 頁 221）
---

# 第 2-10 集 · 點雲對齊（三）：非線性最小平方 [▶ 影片](https://youtu.be/CJE59i8oxIE)

← 上一集：[2-08-icp-part2](2-08-icp-part2.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[2-11-graph-slam-pose-graphs](2-11-graph-slam-pose-graphs.md) →

> **課程**：Mobile Sensing and Robotics 2，Uni Bonn，2021 夏季學期 — 第 2-10 集
> **講者**：Cyrill Stachniss
> **來源**：YouTube 錄影逐字稿（1:03:37，Whisper `medium.en` 轉錄；最後約 4 分鐘是附上的「5 分鐘 ICP」短片）＋ MVG §A6.2 ＋《視覺 SLAM 十四講》§7.9.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `【十四講補充】` 十四講有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 為什麼要用最小平方取代 SVD](#1-為什麼要用最小平方取代-svd)
- [2. 2D 點到點](#2-2d-點到點)
  - [2.1 誤差與參數](#21-誤差與參數)
  - [2.2 Jacobian](#22-jacobian)
  - [2.3 Gauss-Newton 迴圈](#23-gauss-newton-迴圈)
- [3. 2D 點到平面](#3-2d-點到平面)
  - [3.1 估計法向量](#31-估計法向量)
  - [3.2 誤差與 Jacobian](#32-誤差與-jacobian)
- [4. 對稱的點到平面度量](#4-對稱的點到平面度量)
- [5. 強健最小平方](#5-強健最小平方)
- [6. 實務建議](#6-實務建議)
- [7. 非剛體對齊](#7-非剛體對齊)
- [8. 資源與總結](#8-資源與總結)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

ICP 第三部分：不用 2-07 的 SVD，改用 2-05 的**一般非線性最小平方**（Gauss-Newton）來算每一輪的對齊。先用 2D 點到點示範（SVD 也做得到），再推廣到**點到平面**、**對稱點到平面**和**強健核**，最後談實務和非剛體對齊。

---

## 1. 為什麼要用最小平方取代 SVD

[▶ 08:10](https://youtu.be/CJE59i8oxIE?t=490)

- SVD 解假設**點到點**對應；想用其他誤差函數（例如點到平面）就放不進去。
- 有高斯不確定性時，最小平方是**統計上最佳**的解，可以考慮比單一權重更複雜的不確定性形狀（這種資訊通常很難取得，但有的話可以用）。
- 想做**非剛體**對齊（物體會變形）也需要最小平方。
- 【口頭】如果 SVD 夠用、和你的誤差函數相容，就沒有理由改用最小平方 [▶ 04:09](https://youtu.be/CJE59i8oxIE?t=249)。
- 做法：通常用 **Gauss-Newton** 或 **Levenberg-Marquardt** 迭代最小化；本集用 Gauss-Newton。

複習 2-08 的最佳做法 [▶ 06:57](https://youtu.be/CJE59i8oxIE?t=417)：投資在資料關聯上；有初始猜測（例如輪式里程計）一定要用；用法向量的度量通常比點到點好；動態環境要處理離群值。這些在本集仍然成立。

【課本補充】MVG §A6.2（書頁 600–602，PDF 頁 618–620）的 **Levenberg-Marquardt**（LM）：
- 把正規方程 $J^{\mathsf T}J\Delta = -J^{\mathsf T}\epsilon$ 換成**擴增正規方程** $(J^{\mathsf T}J + \lambda I)\Delta = -J^{\mathsf T}\epsilon$，$\lambda$ 每輪變動；典型初值是 $J^{\mathsf T}J$ 對角元素平均的 $10^{-3}$ 倍。
- 誤差下降 → 接受，$\lambda$ 除以某個因子（通常 10）；誤差上升 → $\lambda$ 乘以同一因子，重解，直到誤差下降。
- 理由：$\lambda$ 小時 ≈ Gauss-Newton（在解附近收斂快）；$\lambda$ 大時 ≈ $\lambda\Delta = -J^{\mathsf T}\epsilon$，也就是**梯度下降**方向（情況困難時保證代價下降，而且步長變短）。
- 對任何 $\lambda$，$\Delta$ 都是下坡方向：$-g_P^{\mathsf T}\Delta = (J^{\mathsf T}\epsilon)^{\mathsf T}(J^{\mathsf T}J + \lambda I)^{-1}J^{\mathsf T}\epsilon > 0$，因為 $J^{\mathsf T}J + \lambda I$ 正定（除非梯度為零）。

---

## 2. 2D 點到點

[▶ 09:45](https://youtu.be/CJE59i8oxIE?t=585)

（這個例子 SVD 也能完美解；只是當作練習。）

### 2.1 誤差與參數

- 2D 點集；剛體轉換 = 2D 平移 $t = (t_x, t_y)$ ＋ 1 個旋轉角 $\theta$。參數 $x = (t_x, t_y, \theta)^{\mathsf T}$。
- 誤差向量（對應 $n$）：轉換後的點和目標點的差：

$$
e_n(x) = R(\theta)\, x_n + t - y_n, \qquad
R(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}
$$

- 旋轉矩陣有 $\sin$、$\cos$ → **非線性** → 要線性化、迭代。

（誤差的正負號依講者算出的 Jacobian（$t$ 的偏導是 $+1$）整理；和 2-05 的 $z - f(x)$ 差一個負號，不影響最小值。）

### 2.2 Jacobian

[▶ 11:39](https://youtu.be/CJE59i8oxIE?t=699)

$e_n$ 是 2 維、參數 3 個 → $J_n$ 是 $2 \times 3$：

$$
J_n = \frac{\partial e_n}{\partial (t_x, t_y, \theta)} =
\begin{bmatrix}
\dfrac{\partial e_{n,x}}{\partial t_x} & \dfrac{\partial e_{n,x}}{\partial t_y} & \dfrac{\partial e_{n,x}}{\partial \theta} \\[2mm]
\dfrac{\partial e_{n,y}}{\partial t_x} & \dfrac{\partial e_{n,y}}{\partial t_y} & \dfrac{\partial e_{n,y}}{\partial \theta}
\end{bmatrix}
$$

- 對 $t_x$、$t_y$：平移是線性的 → 前兩欄是單位矩陣 [▶ 13:22](https://youtu.be/CJE59i8oxIE?t=802)。
- 對 $\theta$：唯一的非線性在旋轉矩陣 → 要旋轉矩陣對 $\theta$ 的導數（$\cos \to -\sin$、$\sin \to \cos$）[▶ 15:30](https://youtu.be/CJE59i8oxIE?t=930)：

$$
\frac{\partial R}{\partial \theta} = \begin{bmatrix} -\sin\theta & -\cos\theta \\ \cos\theta & -\sin\theta \end{bmatrix}
$$

所以，記 $x_n = (x_n, y_n)^{\mathsf T}$（點的原始座標）：

$$
\boxed{\;J_n = \Bigl[\; I_2 \;\Big|\; \frac{\partial R}{\partial \theta}\, x_n \;\Bigr] =
\begin{bmatrix}
1 & 0 & -\sin\theta\, x_n - \cos\theta\, y_n \\
0 & 1 & \cos\theta\, x_n - \sin\theta\, y_n
\end{bmatrix}\;}
$$

（這裡 $x_n$、$y_n$ 指來源點的兩個座標分量；講者口述「$x_n$ 和 $y_n$ 是向量 $x_n$ 的 $x$、$y$ 座標」。）

### 2.3 Gauss-Newton 迴圈

[▶ 16:51](https://youtu.be/CJE59i8oxIE?t=1011)

照 2-05（這裡資訊矩陣取單位矩陣）：

$$
H_n = J_n^{\mathsf T}J_n, \quad b_n = J_n^{\mathsf T}e_n, \qquad
H = \sum_n H_n, \quad b = \sum_n b_n, \qquad
\Delta x = -H^{-1}b
$$

- $H$ 只是 $3 \times 3$，直接求反就好。
- 更新 $(t_x, t_y, \theta)$，迭代到收斂。
- 和 SVD 相比：多了彈性（可以換誤差函數），代價是每換一種表示都要**自己手算 Jacobian**。

**例子** [▶ 19:11](https://youtu.be/CJE59i8oxIE?t=1151)：藍色和橘色點集；每輪用最近鄰找對應、做一次最小平方對齊、重新找對應……每輪有些對應會改變，慢慢前進直到完全重疊。誤差隨迭代下降，約 15、16 輪收斂。

---

## 3. 2D 點到平面

[▶ 20:50](https://youtu.be/CJE59i8oxIE?t=1250)

### 3.1 估計法向量

[▶ 22:07](https://youtu.be/CJE59i8oxIE?t=1327)

- 對每個點看它的鄰居，估計法向量。
- 比較進階的做法：取局部鄰域的點，算**特徵向量和特徵值**，**最小特徵值對應的特徵向量**就是表面法向量。
- 也可以直接用外積。有快的、有慢但比較準和穩健的；選一種就好。

### 3.2 誤差與 Jacobian

[▶ 23:05](https://youtu.be/CJE59i8oxIE?t=1385)

點到點的誤差向量和法向量做內積（投影到法向量上）：

$$
e_n(x) = \bigl( R(\theta)\, x_n + t - y_n \bigr)^{\mathsf T} n_n
$$

- 兩個 2 維向量的內積 → **純量** → Jacobian 是 $1 \times 3$ [▶ 24:03](https://youtu.be/CJE59i8oxIE?t=1443)。
- 就是把點到點的 Jacobian 左乘 $n_n^{\mathsf T}$：

$$
\boxed{\;J_n = n_n^{\mathsf T}\Bigl[\; I_2 \;\Big|\; \frac{\partial R}{\partial \theta}\, x_n \;\Bigr] = \Bigl[\; n_{n,x} \quad n_{n,y} \quad n_n^{\mathsf T}\frac{\partial R}{\partial \theta}x_n \;\Bigr]\;}
$$

- 之後照樣算 $H$、$b$、迭代。

**例子** [▶ 25:30](https://youtu.be/CJE59i8oxIE?t=1530)：誤差降得比較快，約 10、11 輪收斂（點到點約 16 輪）。講者提醒：兩張圖的軸尺度不同，不能直接比。

---

## 4. 對稱的點到平面度量

[▶ 26:33](https://youtu.be/CJE59i8oxIE?t=1593)

- 點到平面的問題：**不對稱**。用哪一邊的法向量，結果就不同（兩邊表面的法向量一般不一樣）。
- 很簡單的解法（講者說是不久前才提出的）：**把兩個法向量加起來**（平均），用這個新向量代替單一法向量 [▶ 28:04](https://youtu.be/CJE59i8oxIE?t=1684)：

$$
e_n(x) = \bigl( R(\theta)\, x_n + t - y_n \bigr)^{\mathsf T} (n_{y_n} + n_{x_n})
$$

- 唯一多的工作：**另一個點雲也要算法向量**。

（式子依講者口述「和點到平面一樣，只是單一法向量換成兩個法向量的和」整理；原始方法在 3D 中如何處理來源點法向量隨旋轉改變，講者沒有細講。）

**效果** [▶ 29:21](https://youtu.be/CJE59i8oxIE?t=1761)：圖上把 ICP 前的誤差映到 ICP 後的誤差：**對稱 < 點到平面 < 點到點**。

- 收斂更快（誤差降得快 → 資料關聯更好 → 更快收斂到正解）。
- **收斂域更大**：初始誤差比較大時仍能找到好的對應、正確對齊。
- 【口頭】自己做 ICP 時，對稱度量大概是最好的起點 [▶ 30:43](https://youtu.be/CJE59i8oxIE?t=1843)。

---

## 5. 強健最小平方

[▶ 30:50](https://youtu.be/CJE59i8oxIE?t=1850)

- 一般最小平方：誤差是**二次**的，越遠誤差平方成長。這對應高斯分布：殘差很大的點機率極小，超過三、四、五、六個 $\sigma$ 幾乎是零。
- 現實不是這樣：總有一定機率出現嚴重離群值（通常是場景裡發生了模型沒考慮到的事）。
- **強健核**（robust kernel，又叫 **M 估計子**，M-estimator）：用別的函數代替二次函數：
  - 絕對值（線性成長）；
  - **Huber**：誤差小時保持二次（假設高斯），超過某點後改成線性（降低遠點的影響）；
  - 有些核到後來幾乎是常數：誤差是 2 還是 10 差不多。
- 核的選擇反映你對**離群值分布**的假設；有一大類核，要找最符合資料的。
- 怎麼放進最小平方 [▶ 33:52](https://youtu.be/CJE59i8oxIE?t=2032)：誤差經過強健核後，Jacobian 會改變；可以轉換成每個誤差項的**權重**，在最小化中降低大誤差的權重。權重 1 對應二次核。
- **自適應核** [▶ 35:01](https://youtu.be/CJE59i8oxIE?t=2101)：一族由參數 $\alpha$ 控制的核：$\alpha = 2$ 是二次；$\alpha$ 變小，離群值的影響越來越小。解最小平方的同時**也最佳化 $\alpha$**，讓核自動適應目前的離群值情況。
- KITTI 高速公路例子（同 2-08）：固定的 Huber 核會讓車子「黏」到超車的車上，對齊失敗；自適應核在那時 $\alpha$ 降到很低，強烈剔除離群值，沒有黏上去。
- `⚠️ 逐字稿缺字`：Whisper 寫 “Hooper”、“Hoover”，應為 **Huber**；“kitty” 應為 **KITTI**。

詳細推導在 2-15。

**兩種處理離群值的方式** [▶ 37:28](https://youtu.be/CJE59i8oxIE?t=2248)：

| | 啟發式（用問題知識） | 一般方法（強健核） |
|---|---|---|
| 優點 | 用了背景知識，結果更好 | 可推廣到其他情況 |
| 缺點 | 針對特定問題，難推廣 | — |

最好兩者結合：有環境資訊就明確用（至少在初始對齊時不用可疑的點），再加上強健核（最簡單是 Huber，自適應的通常更好）。也可以問：哪些部分確定是靜態的、比較可信？對自運動知道什麼（車子不會橫移）？

**多個里程計提案** [▶ 39:19](https://youtu.be/CJE59i8oxIE?t=2359)：

- 同時跑多種對齊方法（點到點、點到平面、對稱、用顏色、用語意、用強健核……），得到多個**感測器里程計**提案。
- 用對車輛的了解做合理性檢查，挑出可能錯的、選出最可能對的。
- 結果：**沒有最好的單一方法**。不同情況下被選中的方法不同（例如 Generalized ICP（點到點和點到平面的結合）和點到點最常被選中，有時用顏色資訊）。

---

## 6. 實務建議

[▶ 41:22](https://youtu.be/CJE59i8oxIE?t=2482)

1. **一定要用初始猜測**：會帶來更好的資料關聯。沒有其他里程計來源時，用**等速模型**：增量估計時重複上一次估計的運動（車子通常不會一直變速）。
2. **用法向量的度量**通常比點到點好；講者會先從**對稱度量**開始（它比長期標準的點到平面更好）。
3. **有資訊的離群值剔除**：知道離群值或可信區域時，明確使用（但會限制演算法的通用性）。
4. **自適應核**很好用：不用事先決定核。
5. 多個感測器時一起用：例如雷射和相機各自估計轉換。即使只有單眼相機，也能得到 6 個自由度中的 5 個，而且相機通常給出很好的**朝向**估計。可以融合、聯合使用，或互相做合理性檢查（都同意才採用）。
6. **速度限制**等動力學限制：車子不會一秒從 0 加速到 100 km/h，可以用來發現失敗。
7. 增量對齊只給**增量修正**（對前 5、10 次掃描對齊，等於建一個局部地圖）。長期要不漂移，最終要用 **SLAM**：做全域最佳化（全域最小平方），修改過去的軌跡、正確閉合迴圈（2-11）。
8. 【口頭】**不要太相信 ICP 給的不確定性** [▶ 45:23](https://youtu.be/CJE59i8oxIE?t=2723)：通常會高估對齊的精度。可以部分使用，但要打折扣（最近也有針對這點的新方法）。

**例子：光達 SLAM** [▶ 46:10](https://youtu.be/CJE59i8oxIE?t=2770)：主要由 Jens Behley 開發的系統：投影式資料關聯的 ICP，把目前的雷射掃描對到 **surfel**（表面元素）地圖上，用法向量和強健核；在 KITTI 資料集各序列上建圖、修正迴圈閉合，同時得到軌跡和地圖。

- `⚠️ 逐字稿缺字`：Whisper 寫 “Jens Bielle”、“circle based map”，推測為 **Jens Behley**（`⚠️ 待確認`，同 1-20）、**surfel-based map**。

---

## 7. 非剛體對齊

[▶ 47:06](https://youtu.be/CJE59i8oxIE?t=2826)

- 到目前都是**剛體**對齊：一個剛體轉換把整個點雲轉過去。
- 自主系統常面對**會變形**的物體（人的手臂會動）。
- 非剛體對齊的研究已有約 20 年：很多針對人（利用骨架結構，知道手臂只能怎麼動）。
- 需要最小平方：代價函數更複雜；有時甚至最小平方也不是最好的選擇，也有用有限元素法等方法處理變形（本課不講）。
- 通常會加**額外的代價項**，例如不要大幅改變拓撲。

**例子：植物生長** [▶ 49:11](https://youtu.be/CJE59i8oxIE?t=2951)：

- 番茄植株在第 1、6、10 天的點雲，要對齊才能估計莖長了多少、葉子變多大。
- 資料關聯很難（例如隔一天就多長出一片葉子，從兩片變三片），需要投入大量腦力。
- 做法：
  1. 在莖和葉子上擬合**骨架**，利用植物生長的方式，只在骨架點上做資料關聯（允許新分枝長出來）。
  2. 每個骨架點有自己的轉換：不只是剛體，而是**仿射**轉換（因為會長大）。
  3. 加**正則化**：沿著骨架，相鄰點的仿射轉換不要劇烈變化。
  4. 對齊骨架後，把資訊轉回整個點雲。
- 用途：**表型分析**（phenotyping，推出植物性狀）；在各時刻之間追蹤植物發展，甚至在沒有量測的時刻內插出植物的樣子。
- 很多非剛體文獻也在處理人和衣服。

---

## 8. 資源與總結

### 資源

[▶ 53:24](https://youtu.be/CJE59i8oxIE?t=3204)

- **Jupyter notebook**（Igor Bogoslavskyi）：Python，從最簡單的 SVD 點到點、到最小平方、到簡單強健核，全部在 2D。本集一些例子出自這裡。講者強烈推薦當學習和專案的起點。
- **Open3D**：現成的點到點、點到平面對齊，想直接用可以看看。
- 論文：從早期的 Arun 等人、Besl & McKay（提出 ICP），到效率變體、度量比較、離群值處理、全域 ICP 等。
- **simple ICP**：有 Python、Julia、C++、MATLAB、Octave 等版本（`⚠️ 待確認`：作者 Whisper 寫 “Philip Iglera”）。
- `⚠️ 待確認`：notebook 作者 Whisper 寫 “Igor Bogoslavsky／Boguslavsky”，拼法待確認。

### 總結

[▶ 55:57](https://youtu.be/CJE59i8oxIE?t=3357)

- 點雲對齊是機器人感知和建圖的重要任務：移動感測器位置讓點雲對齊，有時甚至最佳化點雲裡的點本身。
- **ICP** 是標準選擇，新系統都要和 ICP 及其變體比較。
- 已知資料關聯很簡單；未知時很難。**真正的難處是決定正確的資料關聯**：哪些點可信、哪些是離群值、哪些屬於移動物體。
- 實務上反覆「資料關聯 → 對齊」；最一般的形式是非線性最小平方。
- 初始猜測永遠有幫助；用最小平方時沒有初始猜測就很難得到好結果（除非能對場景做很強的假設，這等於初始猜測）。
- 成熟演算法的標準成分：最小平方、點到平面（或基於平面）的度量、資料關聯的啟發式、相容性、離群值剔除。

**附錄：5 分鐘 ICP**（[▶ 58:47](https://youtu.be/CJE59i8oxIE?t=3527) 之後）：影片最後附上的短片，重述 ICP 兩步（最近鄰資料關聯 → 重心對齊＋SVD 旋轉），點到平面需要改用最小平方（Gauss-Newton），以及投影式 ICP 和強健核。內容和前三集重複，不另外整理。

---

## 9. 一頁速查表

### 9.1 2D 誤差與 Jacobian（參數 $t_x, t_y, \theta$）

$$
\frac{\partial R}{\partial\theta} = \begin{bmatrix} -\sin\theta & -\cos\theta \\ \cos\theta & -\sin\theta \end{bmatrix}
$$

| 度量 | 誤差 $e_n$ | Jacobian $J_n$ | 大小 |
|---|---|---|---|
| 點到點 | $Rx_n + t - y_n$ | $[\,I_2 \mid \partial_\theta R\, x_n\,]$ | $2 \times 3$ |
| 點到平面 | $(Rx_n + t - y_n)^{\mathsf T}n_n$ | $n_n^{\mathsf T}[\,I_2 \mid \partial_\theta R\, x_n\,]$ | $1 \times 3$ |
| 對稱 | $(Rx_n + t - y_n)^{\mathsf T}(n_{y_n} + n_{x_n})$ | 同上，法向量換成和 | $1 \times 3$ |

### 9.2 求解

| 方法 | 更新方程 |
|---|---|
| Gauss-Newton | $\bigl(\sum J_n^{\mathsf T}J_n\bigr)\Delta x = -\sum J_n^{\mathsf T}e_n$ |
| LM（MVG） | $(J^{\mathsf T}J + \lambda I)\Delta = -J^{\mathsf T}\epsilon$；誤差降 → $\lambda/10$，升 → $\lambda \times 10$ |
| 強健 | 每項乘上核給的權重 $w_n$：$\sum w_nJ_n^{\mathsf T}J_n$，$\sum w_nJ_n^{\mathsf T}e_n$ |

### 9.3 法向量

| 方法 | 說明 |
|---|---|
| PCA | 鄰域點的共變異數，最小特徵值的特徵向量 |
| 外積 | 快，但對雜訊敏感 |

### 9.4 實務

| 建議 | 說明 |
|---|---|
| 初始猜測 | 里程計，或等速模型 |
| 度量 | 對稱 > 點到平面 > 點到點 |
| 離群值 | 有資訊的剔除 ＋ 自適應核 |
| 長期 | 增量對齊會漂移 → SLAM 全域最佳化 |
| 不確定性 | ICP 給的共變異數通常過度自信 |

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 增量 ICP 的相對轉換、閉合迴圈 | 2-11 位姿圖 SLAM |
| ICP 共變異數不可全信 | 2-11（邊的資訊矩陣怎麼給） |
| 強健核、自適應核 | 2-15 強健最小平方 |
| Gauss-Newton、Jacobian 推導 | 2-11、2-12（位姿圖、地標的 Jacobian） |
| 相機可給 5 自由度、朝向準 | 2-33、2-37（本質矩陣、相對定向） |

---

## 附：本集一句話總結

> **用最小平方取代 SVD，ICP 就能用任何誤差函數：2D 點到點的 Jacobian 是 $[I \mid \partial_\theta R\,x_n]$，點到平面再左乘法向量 $n^{\mathsf T}$，對稱度量用兩個法向量的和，收斂最快、收斂域最大。再加強健（自適應）核處理離群值；長期要靠 SLAM 消除漂移。**

---

## ⚠️ 待確認清單

1. [▶ 46:17](https://youtu.be/CJE59i8oxIE?t=2777) 光達 SLAM 系統的主要開發者，Whisper 寫 “Jens Bielle”，推測為 Jens Behley，待確認。
2. [▶ 53:31](https://youtu.be/CJE59i8oxIE?t=3211) ICP Jupyter notebook 的作者，Whisper 寫 “Igor Bogoslavsky／Boguslavsky”，拼法待確認。
3. [▶ 55:38](https://youtu.be/CJE59i8oxIE?t=3338) simple ICP 的作者，Whisper 寫 “Philip Iglera”，姓名待確認。

---

*筆記依據 Cyrill Stachniss「Mobile Sensing and Robotics 2」ICP Part 3 錄影逐字稿（Whisper `medium.en`，1:03:37）、MVG §A6.2 與《視覺 SLAM 十四講》§7.9.2 整理。*
