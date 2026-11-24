---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 19
lecture: Lecture 7 (Part 4) – The fundamental and essential matrices
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/WQvJICS3Ecc
notes: MVG §12.2（線性三角化，書頁 312，PDF 頁 330）、§10.1–10.4（書頁 262–275，PDF 頁 280–293）
---

# 第 19 集 · Lecture 7 (Part 4)：線性三角化、重建的模糊、分層重建 [▶ 影片](https://youtu.be/WQvJICS3Ecc)

← 上一集：[18-fundamental-essential-part3](18-fundamental-essential-part3.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[20-absolute-pose-part1](20-absolute-pose-part1.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 19 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（25:52，Whisper `medium.en` 轉錄）＋ MVG §12.2、§10.1–10.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 線性三角化](#1-線性三角化)
- [2. 重建的模糊](#2-重建的模糊)
  - [2.1 已校正：相似模糊](#21-已校正相似模糊)
  - [2.2 未校正：射影模糊](#22-未校正射影模糊)
- [3. 分層重建](#3-分層重建)
  - [3.1 第一步：找無窮遠平面 → 仿射重建](#31-第一步找無窮遠平面--仿射重建)
  - [3.2 第二步：用 ω → 度量重建](#32-第二步用-ω--度量重建)
- [4. Lecture 7 總結](#4-lecture-7-總結)
- [5. 一頁速查表](#5-一頁速查表)
- [6. 與後續集數的連結](#6-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/WQvJICS3Ecc?t=0)

**回顧**：

- **未校正**：從對應點求 $F$，分解成 $P,P'$——但只確定到差一個 $4\times4$ 射影變換 $H$。
- **已校正**：已知 $K,K'$，從對應點求 $E$，分解出 $R,\mathbf{t}$，加上 $K,K'$ 就**唯一**得到 $P,P'$。

**今天的問題**：已知（或算出）$P,P'$ 和對應點 $\mathbf{x}\leftrightarrow\mathbf{x}'$，能不能恢復 3D 點？——可以，用**線性三角化**。然後看重建結果有什麼模糊、怎麼去掉。

| 主題 | MVG |
|---|---|
| 線性三角化 | §12.2 |
| 重建的模糊（相似、射影） | §10.2–10.3 |
| 分層重建：射影 → 仿射 → 度量 | §10.4 |

---

## 1. 線性三角化

[▶ 01:44](https://youtu.be/WQvJICS3Ecc?t=104)

**在解什麼**：已知兩個相機 $P$、$P'$ 和一對對應點 $\mathbf{x}\leftrightarrow\mathbf{x}'$，求 3D 點 $\mathbf{X}$。

**約束**：

$$
\mathbf{x}=P\mathbf{X},\qquad\mathbf{x}'=P'\mathbf{X}\qquad(\text{都只差縮放})
$$

**去掉縮放：取外積**（同第 08 集 DLT 的技巧）[▶ 02:30](https://youtu.be/WQvJICS3Ecc?t=150)：

$$
\mathbf{x}\times(P\mathbf{X})=\mathbf{0},\qquad\mathbf{x}'\times(P'\mathbf{X})=\mathbf{0}
$$

- 每個式子 3 條方程式，但只有 **2 條獨立**。
- 兩個視角各取兩條，疊成 $4\times4$：
$$
A\mathbf{X}=\mathbf{0},\qquad A=\begin{pmatrix}x\,\mathbf{p}^{3\mathsf{T}}-\mathbf{p}^{1\mathsf{T}}\\ y\,\mathbf{p}^{3\mathsf{T}}-\mathbf{p}^{2\mathsf{T}}\\ x'\,\mathbf{p}'^{3\mathsf{T}}-\mathbf{p}'^{1\mathsf{T}}\\ y'\,\mathbf{p}'^{3\mathsf{T}}-\mathbf{p}'^{2\mathsf{T}}\end{pmatrix}
$$
  $\mathbf{p}^{i\mathsf{T}}$ 是 $P$ 的第 $i$ 列。

（$A$ 的具體元素依 MVG §12.2 寫出；逐字稿只說「疊成 $4\times4$ 矩陣 $A$」。）

> 以下**不是逐字稿內容**，是第一列怎麼來的：$\mathbf{x}=(x,y,1)^\mathsf{T}$，$P\mathbf{X}=(\mathbf{p}^{1\mathsf{T}}\mathbf{X},\mathbf{p}^{2\mathsf{T}}\mathbf{X},\mathbf{p}^{3\mathsf{T}}\mathbf{X})^\mathsf{T}$。外積的第二個分量是 $1\cdot\mathbf{p}^{1\mathsf{T}}\mathbf{X}-x\cdot\mathbf{p}^{3\mathsf{T}}\mathbf{X}$，設為 0 就是 $(x\mathbf{p}^{3\mathsf{T}}-\mathbf{p}^{1\mathsf{T}})\mathbf{X}=0$。

**解** [▶ 04:07](https://youtu.be/WQvJICS3Ecc?t=247)：

- $\mathbf{X}$ 有 3 個未知數（齊次 4 維、差縮放），$A$ 有 4 條 → **超定**，足以唯一解。
- SVD：$A=U\Sigma V^\mathsf{T}$，$\mathbf{X}=\mathbf{v}_4$（最小奇異值的右奇異向量）。
- **換成非齊次** [▶ 04:51](https://youtu.be/WQvJICS3Ecc?t=291)：$\mathbf{v}_4=(v_x,v_y,v_z,v_w)^\mathsf{T}$，前三個除以 $v_w$，讓最後一個分量是 1。

**什麼時候會失敗**：

> 以下**不是逐字稿內容**，是依幾何推論的：(a) 點在**基線**上（兩條光線重合），無法三角化；(b) 兩條光線**幾乎平行**（基線太短或點太遠），解對雜訊非常敏感；(c) 線性三角化最小化的是代數誤差，有雜訊時可用 MVG §12.5 的最佳三角化（最小化重投影誤差）改善。

---

## 2. 重建的模糊

### 2.1 已校正：相似模糊

[▶ 05:26](https://youtu.be/WQvJICS3Ecc?t=326)

用 $E$ 和已知 $K,K'$ 得到 $P,P'$，三角化出來的 3D 結構**只確定到一個相似變換**。

**理由**：任取一個 $4\times4$ 相似變換

$$
H_S=\begin{pmatrix}R & \mathbf{t}\\\mathbf{0}^\mathsf{T} & \lambda\end{pmatrix}
$$

- 投影：$\mathbf{x}_i=P\mathbf{X}_i=(PH_S^{-1})(H_S\mathbf{X}_i)$。
- 把 3D 點變成 $H_S\mathbf{X}_i$、相機變成 $PH_S^{-1}$，像點完全一樣。
- 而且 $PH_S^{-1}$ **仍然是合法的已校正相機**：$K[R_P\mid\mathbf{t}_P]H_S^{-1}$ 還是 $K$ 乘一個「旋轉 + 平移」（只是旋轉、平移變了）——內參 $K$ 沒變。
- 所以光靠影像，**分不出**整體的旋轉、平移、縮放。

（$H_S$ 的寫法依講者口述「左上旋轉、右上平移、右下縮放 $\lambda$」。）

【課本補充】MVG §10.2：直觀地說，沒有外部資訊（例如場景中某段已知長度），永遠不知道重建的**絕對尺度**、也不知道它在世界中的**絕對位置和方向**。

### 2.2 未校正：射影模糊

[▶ 08:11](https://youtu.be/WQvJICS3Ecc?t=491)

用 8 點法求 $F$、分解出 $P,P'$——第 17 集說過，這只確定到差一個 $4\times4$ 射影變換。

- 重建出 $\mathbf{X}$；換成 $H\mathbf{X}$、相機換成 $PH^{-1}$、$P'H^{-1}$：
$$
(PH^{-1})(H\mathbf{X})=P\mathbf{X}=\mathbf{x}
$$
- $(PH^{-1},P'H^{-1})$ 給同一個 $F$，所以也是合法的分解。
- 結論：**重建結果有射影模糊**。

**例子** [▶ 10:44](https://youtu.be/WQvJICS3Ecc?t=644)：一對照片，取至少 8 對對應點求 $F$、分解、三角化。重建出來的 3D 結構：

- 平行線**不再平行**（在場景中平行的兩條線，在重建中交於一個有限點）；
- 無窮遠點被拉到有限位置。

【課本補充】MVG Theorem 10.1（射影重建定理）：若兩組重建都和同一組對應點吻合（且 $F$ 唯一），它們之間只差一個射影變換。

---

## 3. 分層重建

[▶ 11:46](https://youtu.be/WQvJICS3Ecc?t=706)

**分層法（stratified approach）**：和第 05–06 集 2D 影像校正一樣，分兩步去掉射影模糊：

1. **射影 → 仿射**：去掉射影模糊，剩仿射模糊。
2. **仿射 → 度量**：去掉仿射模糊，得到**度量重建（metric reconstruction）**（只差相似變換）。

兩步都需要**場景的額外資訊**。

### 3.1 第一步：找無窮遠平面 → 仿射重建

[▶ 12:33](https://youtu.be/WQvJICS3Ecc?t=753)

**想法**（第 07 集）：

- 射影變換會把 $\boldsymbol{\pi}_\infty$ 送到有限位置。
- 仿射變換保持 $\boldsymbol{\pi}_\infty$。
- 所以：在射影重建中找出（被扭到有限位置的）$\boldsymbol{\pi}_\infty$，用一個射影變換把它送回 $(0,0,0,1)^\mathsf{T}$ → 剩下的只是仿射模糊。

**變換** [▶ 13:50](https://youtu.be/WQvJICS3Ecc?t=830)：在射影重建中，$\boldsymbol{\pi}_\infty$ 的座標是 $\boldsymbol{\pi}$（4 維向量）。

$$
H=\begin{pmatrix}I\mid\mathbf{0}\\\boldsymbol{\pi}^\mathsf{T}\end{pmatrix}
$$

（前三列是 $[I\mid\mathbf{0}]$，最後一列是 $\boldsymbol{\pi}^\mathsf{T}$。）

- 驗證（講者留作練習）：平面的變換是 $\boldsymbol{\pi}'=H^{-\mathsf{T}}\boldsymbol{\pi}$。要 $H^{-\mathsf{T}}\boldsymbol{\pi}=(0,0,0,1)^\mathsf{T}$，等價於 $\boldsymbol{\pi}=H^\mathsf{T}(0,0,0,1)^\mathsf{T}$ = $H$ 的最後一列轉置 = $\boldsymbol{\pi}$ ✓。
- 把所有重建點 $\mathbf{X}$ 換成 $H\mathbf{X}$（相機換成 $PH^{-1}$），就得到**仿射重建**。

（$H$ 的矩陣依 MVG §10.4.1 寫出；逐字稿只說「這個 homography 由這個式子給出」。）

【課本補充】MVG §10.4.1：$\boldsymbol{\pi}$ 的最後一個分量為 0 時這個公式不能用（那時 $H$ 奇異），要改用別的形式。

**怎麼找到 $\boldsymbol{\pi}_\infty$** [▶ 15:13](https://youtu.be/WQvJICS3Ecc?t=913)：

- 知道場景中哪些線**平行** → 需要**三組不同方向的平行線**。
- 在射影重建中，每組平行線（例如屋頂的兩條邊）交於一點：$\mathbf{V}_1$、$\mathbf{V}_2$、$\mathbf{V}_3$。
- 它們本來是無窮遠點，應該在 $\boldsymbol{\pi}_\infty$ 上；現在被扭到有限位置，但仍然在（被扭過的）$\boldsymbol{\pi}$ 上。
- 三點決定一個平面 → 得到 $\boldsymbol{\pi}$。

講者用外積描述：$\mathbf{V}_1\times\mathbf{V}_2$、$\mathbf{V}_2\times\mathbf{V}_3$ 得兩條線，兩線再外積得平面法向 [▶ 16:56](https://youtu.be/WQvJICS3Ecc?t=1016)。

> 以下**不是逐字稿內容**：在 3D（4 維齊次座標）裡，外積不能直接用。三點決定平面的正確做法是第 04 集的零空間：
> $$\begin{pmatrix}\mathbf{V}_1^\mathsf{T}\\\mathbf{V}_2^\mathsf{T}\\\mathbf{V}_3^\mathsf{T}\end{pmatrix}\boldsymbol{\pi}=\mathbf{0}$$
> 3D 中兩條線的交點也要用第 04 集的方法（或在影像上求消失點再三角化）。講者的外積說法是 2D 的類比。

**結果** [▶ 17:33](https://youtu.be/WQvJICS3Ecc?t=1053)：平行線恢復平行（交在真正的無窮遠）。但**角度還是錯的**——仿射失真還在。

【課本補充】MVG Result 10.3：仿射重建中若相機是 $P=[I\mid\mathbf{0}]$、$P'=[M\mid\mathbf{e}']$，則**無窮遠 homography** $H_\infty=M$（第 17 集）。所以找到 $\boldsymbol{\pi}_\infty$ 等價於找到 $H_\infty$。MVG 也提到其他做法：純平移運動、或其中一台是仿射相機（它的主平面就是 $\boldsymbol{\pi}_\infty$）。

### 3.2 第二步：用 ω → 度量重建

[▶ 18:14](https://youtu.be/WQvJICS3Ecc?t=1094)

**關鍵**：找出**絕對二次曲線的像** $\omega$（第 14 集）。

**變換** [▶ 19:04](https://youtu.be/WQvJICS3Ecc?t=1144)：

$$
H=\begin{pmatrix}A^{-1} & \mathbf{0}\\\mathbf{0}^\mathsf{T} & 1\end{pmatrix},\qquad AA^\mathsf{T}=(M^\mathsf{T}\omega M)^{-1}
$$

- $M$：仿射重建中第二個相機 $P'=[M\mid\mathbf{m}]$ 的左邊 $3\times3$。
- $\omega$：第二張影像的絕對二次曲線的像。
- $A$：對 $(M^\mathsf{T}\omega M)^{-1}$ 做 **Cholesky 分解**得到。

**證明** [▶ 19:40](https://youtu.be/WQvJICS3Ecc?t=1180)：

1. 真正的（度量）第二個相機：$P'_M=K'[R\mid\mathbf{t}]$（只差相似變換）。
2. 仿射重建的第二個相機：$P'=[M\mid\mathbf{m}]$。
3. 兩者差一個仿射變換：$P'_M=P'H_A^{-1}$，取 $H_A^{-1}=\begin{pmatrix}A&\mathbf{0}\\\mathbf{0}^\mathsf{T}&1\end{pmatrix}$（就是上面 $H$ 的逆）。
4. 比較左邊 $3\times3$：
$$
MA=K'R
$$
5. 兩邊各乘自己的轉置 [▶ 21:31](https://youtu.be/WQvJICS3Ecc?t=1291)：
$$
(MA)(MA)^\mathsf{T}=(K'R)(K'R)^\mathsf{T}\quad\Longrightarrow\quad MAA^\mathsf{T}M^\mathsf{T}=K'RR^\mathsf{T}K'^\mathsf{T}=K'K'^\mathsf{T}
$$
   （$R$ 正交，$RR^\mathsf{T}=I$。）
6. $K'K'^\mathsf{T}=\omega^*=\omega^{-1}$（第 14 集）。把 $M$ 移到右邊：
$$
AA^\mathsf{T}=M^{-1}\omega^{-1}M^{-\mathsf{T}}=(M^\mathsf{T}\omega M)^{-1}\qquad\blacksquare
$$
7. Cholesky 分解 $AA^\mathsf{T}$ 得 $A$，組出 $H$。

- $\omega$ 可以用 Lecture 6 講的各種方法得到（垂直消失點、三個正方形、零斜切等）。

⚠️ 逐字稿缺字：Whisper 把 Cholesky 寫成 “Kolosky”、“Kolesky”；把 ambiguity 寫成 “MPUAT”；把 orthogonal 寫成 “octagonal”。

**結果** [▶ 23:55](https://youtu.be/WQvJICS3Ecc?t=1435)：把 $H$ 套到仿射重建上，得到**度量重建**——角度恢復、平行線平行，只剩相似變換（整體旋轉、平移、縮放）。

【課本補充】MVG Result 10.4 就是這個公式。MVG 也指出，若相機內參已知（$\omega$ 已知），可以直接一步從射影重建升到度量重建；分層法的好處是每一步需要的資訊比較少、可以分開取得。

---

## 4. Lecture 7 總結

[▶ 24:17](https://youtu.be/WQvJICS3Ecc?t=1457)

1. 極幾何的名詞，用來描述兩個視角的關係（第 16 集）。
2. 用 $F$ 求極線：$\mathbf{l}'=F\mathbf{x}$（第 16 集）。
3. 在未校正／已校正情況下，用 8 點對應求 $F$／$E$（第 18 集）。
4. 把 $F$ 分解成 $P,P'$；把 $E$ 分解成 $R,\mathbf{t}$（第 17–18 集）。
5. 線性三角化恢復 3D 結構（本集）。
6. 未校正情況下，用分層重建去除射影和仿射模糊（本集）。

---

## 5. 一頁速查表

### 線性三角化

| 公式 | 關鍵一步 |
|---|---|
| $A\mathbf{X}=0$，$A=\begin{pmatrix}x\mathbf{p}^{3\mathsf{T}}-\mathbf{p}^{1\mathsf{T}}\\y\mathbf{p}^{3\mathsf{T}}-\mathbf{p}^{2\mathsf{T}}\\x'\mathbf{p}'^{3\mathsf{T}}-\mathbf{p}'^{1\mathsf{T}}\\y'\mathbf{p}'^{3\mathsf{T}}-\mathbf{p}'^{2\mathsf{T}}\end{pmatrix}$ | $\mathbf{x}\times P\mathbf{X}=0$，每個視角取兩列 |
| $\mathbf{X}=\mathbf{v}_4$，再除以第四個分量 | SVD |

### 重建模糊

| 情況 | 模糊 | 理由 |
|---|---|---|
| 已校正（$E$ + $K$） | 相似（7 dof） | $(PH_S^{-1})(H_S\mathbf{X})$，$PH_S^{-1}$ 仍是 $K[R'\mid\mathbf{t}']$ |
| 未校正（$F$） | 射影（15 dof） | $(PH^{-1})(H\mathbf{X})$ 給同一個 $F$ |

### 分層重建

| 步驟 | 需要 | 變換 | 關鍵一步 |
|---|---|---|---|
| 射影 → 仿射 | $\boldsymbol{\pi}_\infty$ 在射影重建中的座標 $\boldsymbol{\pi}$（例：三組平行線的交點） | $H=\begin{pmatrix}I\mid\mathbf{0}\\\boldsymbol{\pi}^\mathsf{T}\end{pmatrix}$ | $H^\mathsf{T}(0,0,0,1)^\mathsf{T}=\boldsymbol{\pi}$ |
| 仿射 → 度量 | $\omega$（Lecture 6 的方法） | $H=\begin{pmatrix}A^{-1}&\mathbf{0}\\\mathbf{0}^\mathsf{T}&1\end{pmatrix}$，$AA^\mathsf{T}=(M^\mathsf{T}\omega M)^{-1}$ | $MA=K'R$ → $MAA^\mathsf{T}M^\mathsf{T}=K'K'^\mathsf{T}=\omega^{-1}$ |

---

## 6. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 線性三角化 | 第 27–30 集（SfM 中增量加點）；第 31–34 集（stereo 深度） |
| 相似模糊、尺度未知 | 第 20–22 集（PnP：用已知 3D 點固定尺度）；第 27–30 集 |
| 射影重建、分層升級 | 第 27–30 集（未校正 SfM）；Lecture 13 自校正（本播放清單沒有） |
| $H_\infty$ 與仿射重建 | 第 23–26 集（三視角中的 homography 關係） |

---

## 附：本集一句話總結

> **有了 $P,P'$ 和一對對應點，把 $\mathbf{x}\times P\mathbf{X}=0$ 兩個視角各取兩列疊成 $4\times4$ 的 $A$，SVD 就三角化出 3D 點；已校正時重建只差一個相似變換，未校正時差一個射影變換——這時用分層法：先找出被扭過的無窮遠平面 $\boldsymbol{\pi}$，用 $H=[I\mid\mathbf{0};\boldsymbol{\pi}^\mathsf{T}]$ 送回 $(0,0,0,1)$ 得仿射重建，再用 $\omega$ 解 $AA^\mathsf{T}=(M^\mathsf{T}\omega M)^{-1}$ 得度量重建。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 7 (Part 4) 錄影逐字稿（Whisper `medium.en`，25:52）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §12.2、§10.1–10.4 整理。*
