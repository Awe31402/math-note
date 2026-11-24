---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 14
lecture: Lecture 6 (Part 2) – Single view metrology
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/XSflleJr4qM
notes: MVG §8.4.3（書頁 205–207，PDF 頁 223–225）、§8.5（書頁 208–211，PDF 頁 226–229）
---

# 第 14 集 · Lecture 6 (Part 2)：合成視角、全景拼接、已知 K 能做什麼、絕對二次曲線的像 ω [▶ 影片](https://youtu.be/XSflleJr4qM)

← 上一集：[13-single-view-metrology-part1](13-single-view-metrology-part1.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[15-single-view-metrology-part3](15-single-view-metrology-part3.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 14 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（39:32，Whisper `medium.en` 轉錄）＋ MVG §8.4.3、§8.5
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 純旋轉的應用一：合成視角](#1-純旋轉的應用一合成視角)
- [2. 純旋轉的應用二：平面全景拼接](#2-純旋轉的應用二平面全景拼接)
- [3. 已知內參 K 能做什麼](#3-已知內參-k-能做什麼)
  - [3.1 像點 → 光線方向 d = K⁻¹x](#31-像點--光線方向-d--kx)
  - [3.2 量兩條光線的夾角](#32-量兩條光線的夾角)
  - [3.3 影像線反投影平面的法向 n = Kᵀl](#33-影像線反投影平面的法向-n--kᵀl)
- [4. 絕對二次曲線的像 ω](#4-絕對二次曲線的像-ω)
  - [4.1 無窮遠平面到影像：H = KR](#41-無窮遠平面到影像h--kr)
  - [4.2 ω = (KKᵀ)⁻¹](#42-ω--kkᵀ)
  - [4.3 四點說明](#43-四點說明)
  - [4.4 circular points 的像在 ω 上](#44-circular-points-的像在-ω-上)
- [5. 簡單校正裝置：三個正方形](#5-簡單校正裝置三個正方形)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | MVG |
|---|---|
| 純旋轉的兩個應用：合成視角、全景拼接 | §8.4.3 |
| 已知 $K$：光線方向、光線夾角、平面法向 | §8.5 |
| 絕對二次曲線的像 $\omega$ 和它的對偶 $\omega^*$ | §8.5.1 |
| 三個正方形做校正（開頭） | §8.5 Example 8.18 |

---

## 1. 純旋轉的應用一：合成視角

[▶ 00:00](https://youtu.be/XSflleJr4qM?t=0)

**目標**：給一張走廊的照片（**來源影像**），走廊裡有好幾個平面（例如地板、牆）。產生一張**目標影像**，讓某個平面（例如地板）**正對（fronto-parallel）**目標影像平面。

- 場景平面投影到影像是 homography（第 13 集），所以這種扭轉可以用一個平面 homography 完成——等同於讓相機純旋轉到正對那個平面。
- 換另一個平面（例如牆）也可以，用另一個 homography（另一個純旋轉）。

**演算法** [▶ 01:25](https://youtu.be/XSflleJr4qM?t=85)：

1. 在來源影像上找出那個平面的**四邊形**，取四個頂點。
2. 定好目標**矩形的長寬比（aspect ratio）**，四個頂點對應矩形的四個角 → 4 對對應點 $\mathbf{x}\leftrightarrow\mathbf{x}'$。
3. 用 4 對點求 $H$（$\mathbf{x}'=H\mathbf{x}$，第 08 集的線性方法）。
4. **反向映射建查表**：對目標影像每個像素 $\mathbf{x}'$，算 $\mathbf{x}=H^{-1}\mathbf{x}'$，到來源影像取 RGB 值填進來（第 05 集）。

⚠️ 逐字稿缺字：講者說「lecture three」講過 homography 估計，依本播放清單應為 Lecture 4（第 08 集）。Whisper 把 aspect ratio 寫成 “expect ratio”。

---

## 2. 純旋轉的應用二：平面全景拼接

[▶ 04:19](https://youtu.be/XSflleJr4qM?t=259)

**設定**：相機**純旋轉**拍了好幾張照片。任兩張照片的對應點都由 homography 連起來（相機中心固定）。目標：把它們拼成一張**全景圖（panoramic mosaic）**。

**做法** [▶ 06:01](https://youtu.be/XSflleJr4qM?t=361)：例如 5 張 $I_1,\dots,I_5$。

1. 選一張當**參考影像**，例如 $I_3$。
2. 對 $I_2$：找和 $I_3$ 的 4 對對應點，求 $H_{23}$（$I_2\to I_3$）。
3. 開一張比較大的畫布，以 $I_3$ 的座標系為準。對畫布上的每個像素 $\mathbf{x}'$，用 $H_{23}^{-1}$ 找回 $I_2$ 上的位置 $\mathbf{x}$，查 RGB 填進來。（$I_2$ 的內容大多在 $I_3$ 視野之外，所以畫布要比較大。）
4. 對 $I_4$、$I_1$ 同樣做。
5. **離參考影像太遠、沒有重疊視野的影像**（例如 $I_5$ 和 $I_3$ 完全不重疊）：不能直接求 $H_{53}$。改成串接 [▶ 09:23](https://youtu.be/XSflleJr4qM?t=563)：
$$
H_{53}=H_{43}\,H_{54}
$$
   先用 $I_5$、$I_4$ 的對應點求 $H_{54}$，再乘上已知的 $H_{43}$。homography 是線性映射，所以可以這樣串。
6. 所有影像都有了到參考影像的 homography，就能建查表、拼出全景圖。

> 以下**不是逐字稿內容**，是串接順序的檢查：$\mathbf{x}_4=H_{54}\mathbf{x}_5$、$\mathbf{x}_3=H_{43}\mathbf{x}_4$ → $\mathbf{x}_3=H_{43}H_{54}\mathbf{x}_5$。和第 03 集 $g_{ik}=g_{ij}g_{jk}$ 一樣，中間的下標「消掉」。

---

## 3. 已知內參 K 能做什麼

[▶ 11:13](https://youtu.be/XSflleJr4qM?t=673)

假設已知 $K$（$3\times3$），只看單張影像上的點，能推出什麼？

### 3.1 像點 → 光線方向 d = K⁻¹x

[▶ 11:42](https://youtu.be/XSflleJr4qM?t=702)

- 把相機放在標準位置：$P=K[I\mid\mathbf{0}]$（相機座標系 = 世界座標系）。
- 光線上的點：$\tilde{\mathbf{X}}=\lambda\mathbf{d}$，齊次 $(\lambda\mathbf{d}^\mathsf{T},1)^\mathsf{T}$。$\mathbf{d}$ 是方向。
- 投影：
$$
\mathbf{x}=K[I\mid\mathbf{0}]\begin{pmatrix}\lambda\mathbf{d}\\1\end{pmatrix}=\lambda K\mathbf{d}\ \sim\ K\mathbf{d}
$$
  光線上所有點都投影到同一個像點。
- $K$ 是**可逆的上三角**矩陣（不像 $P$ 不可逆），所以反過來：
$$
\mathbf{d}=K^{-1}\mathbf{x}
$$
- 已知 $K$ 時：給一個像點，就能寫出它的**光線方程式**；反之給一個方向，就能找出它投影到哪個像點。

### 3.2 量兩條光線的夾角

[▶ 15:05](https://youtu.be/XSflleJr4qM?t=905)

場景中兩點 $\mathbf{X}_1$、$\mathbf{X}_2$，它們和相機中心連成的兩條光線夾角 $\theta$。

1. 方向：$\mathbf{d}_1=K^{-1}\mathbf{x}_1$、$\mathbf{d}_2=K^{-1}\mathbf{x}_2$。
2. 內積：$\mathbf{d}_1^\mathsf{T}\mathbf{d}_2=\|\mathbf{d}_1\|\|\mathbf{d}_2\|\cos\theta$。
3. 代入：
$$
\cos\theta=\frac{\mathbf{d}_1^\mathsf{T}\mathbf{d}_2}{\sqrt{(\mathbf{d}_1^\mathsf{T}\mathbf{d}_1)(\mathbf{d}_2^\mathsf{T}\mathbf{d}_2)}}=\frac{\mathbf{x}_1^\mathsf{T}(K^{-\mathsf{T}}K^{-1})\mathbf{x}_2}{\sqrt{\left(\mathbf{x}_1^\mathsf{T}(K^{-\mathsf{T}}K^{-1})\mathbf{x}_1\right)\left(\mathbf{x}_2^\mathsf{T}(K^{-\mathsf{T}}K^{-1})\mathbf{x}_2\right)}}
$$

（中間代入的步驟依 MVG 式 (8.9) 寫出；逐字稿只說「代進去得到這個式子，再化簡成這個」。）

- 意義：**校正過的相機是一個方向感測器**，像一個 2D **量角器（protractor）**——量兩個像點的夾角，就等於量兩個 3D 點相對相機中心的夾角。

### 3.3 影像線反投影平面的法向 n = Kᵀl

[▶ 17:59](https://youtu.be/XSflleJr4qM?t=1079)

影像上的線 $\mathbf{l}$ 反投影成一個平面，它的**法向量**是

$$
\mathbf{n}=K^\mathsf{T}\mathbf{l}
$$

**證明** [▶ 18:21](https://youtu.be/XSflleJr4qM?t=1101)：

1. $\mathbf{l}$ 上的點 $\mathbf{x}$ 反投影成光線，方向 $\mathbf{d}=K^{-1}\mathbf{x}$。
2. 這條光線在反投影平面裡 → 垂直於法向量：$\mathbf{d}^\mathsf{T}\mathbf{n}=0$。
3. 代入：$\mathbf{x}^\mathsf{T}K^{-\mathsf{T}}\mathbf{n}=0$。
4. 這對 $\mathbf{l}$ 上**所有**點成立 → $\mathbf{x}$ 在線 $K^{-\mathsf{T}}\mathbf{n}$ 上 → $\mathbf{l}=K^{-\mathsf{T}}\mathbf{n}$（差縮放）。
5. 兩邊左乘 $K^\mathsf{T}$：$\mathbf{n}=K^\mathsf{T}\mathbf{l}$。∎

⚠️ 逐字稿缺字：Whisper 把 orthogonal 寫成 “octagonal”；講者說「unknown camera matrix」應為 “known”。

> 以下**不是逐字稿內容**，是和第 13 集的關係：第 13 集說 $\boldsymbol{\pi}=P^\mathsf{T}\mathbf{l}$。$P=K[I\mid\mathbf{0}]$ 時 $\boldsymbol{\pi}=\begin{pmatrix}K^\mathsf{T}\mathbf{l}\\0\end{pmatrix}$——前三個分量（法向）正是 $K^\mathsf{T}\mathbf{l}$，第四個是 0（平面通過原點，也就是相機中心）。

---

## 4. 絕對二次曲線的像 ω

[▶ 20:11](https://youtu.be/XSflleJr4qM?t=1211)

第 07 集：無窮遠平面上有一條**絕對二次曲線** $\Omega_\infty$。已知 $K$ 就能寫出它在影像上的投影——**絕對二次曲線的像（image of the absolute conic, IAC）** $\omega$。

### 4.1 無窮遠平面到影像：H = KR

[▶ 20:47](https://youtu.be/XSflleJr4qM?t=1247)

- $\boldsymbol{\pi}_\infty$ 上的點都是理想點 $\mathbf{X}_\infty=(\mathbf{d}^\mathsf{T},0)^\mathsf{T}$（$\mathbf{d}$ 是方向）。
- 一般相機 $P=KR[I\mid-\tilde{\mathbf{C}}]$（外參不再是單位矩陣）：
$$
\mathbf{x}=P\mathbf{X}_\infty=KR[I\mid-\tilde{\mathbf{C}}]\begin{pmatrix}\mathbf{d}\\0\end{pmatrix}=KR\mathbf{d}
$$
- **和相機中心（平移）無關**，只和 $K$、$R$、方向 $\mathbf{d}$ 有關。
- $\mathbf{d}$ 和 $\mathbf{x}$ 都是 3 維 → 這是平面到平面的映射，$\boldsymbol{\pi}_\infty$ 到影像是一個 homography：
$$
H=KR
$$
- 不意外：兩個平面（$\boldsymbol{\pi}_\infty$ 和影像平面）之間本來就是 homography。

### 4.2 ω = (KKᵀ)⁻¹

[▶ 23:57](https://youtu.be/XSflleJr4qM?t=1437)

$$
\boxed{\ \omega=(KK^\mathsf{T})^{-1}=K^{-\mathsf{T}}K^{-1}\ }
$$

**證明** [▶ 25:44](https://youtu.be/XSflleJr4qM?t=1544)：

1. 第 02 集：點變換 $\mathbf{x}'=H\mathbf{x}$ 下，二次曲線變成 $C'=H^{-\mathsf{T}}CH^{-1}$。
2. $\Omega_\infty$ 在 $\boldsymbol{\pi}_\infty$ 上的矩陣是 $I$（第 07 集）。
3. $\boldsymbol{\pi}_\infty$ 到影像的 homography 是 $H=KR$。
4. 代入：
$$
\omega=(KR)^{-\mathsf{T}}\,I\,(KR)^{-1}=K^{-\mathsf{T}}R^{-\mathsf{T}}R^{-1}K^{-1}=K^{-\mathsf{T}}(RR^\mathsf{T})^{-1}K^{-1}=K^{-\mathsf{T}}K^{-1}
$$
   （$R$ 正交，$RR^\mathsf{T}=I$。）∎

- $\omega$ 只有**虛點**，沒有實點——在任何照片上都看不到。
- 但它**只由 $K$ 決定** → 如果能想辦法求出 $\omega$，就能求出 $K$ → **$\omega$ 可以用來校正相機**。

⚠️ 逐字稿缺字 [▶ 24:42](https://youtu.be/XSflleJr4qM?t=1482)：Whisper 寫「k transpose k multiplied by k transpose inverse ... k inverse transpose multiplied by k」，依證明應為 $\omega=(KK^\mathsf{T})^{-1}=K^{-\mathsf{T}}K^{-1}$。

### 4.3 四點說明

[▶ 28:29](https://youtu.be/XSflleJr4qM?t=1709)

**說明 1**：$\omega$ **只依賴內參 $K$**，不依賴相機的方向或位置。之後用它來校正。

**說明 2：用 $\omega$ 量光線夾角** [▶ 29:01](https://youtu.be/XSflleJr4qM?t=1741)：第 3.2 節的公式直接寫成

$$
\cos\theta=\frac{\mathbf{x}_1^\mathsf{T}\omega\mathbf{x}_2}{\sqrt{(\mathbf{x}_1^\mathsf{T}\omega\mathbf{x}_1)(\mathbf{x}_2^\mathsf{T}\omega\mathbf{x}_2)}}
$$

- 這個式子在**影像的射影變換**下不變。

**證明（分子）** [▶ 30:45](https://youtu.be/XSflleJr4qM?t=1845)：影像做射影變換 $\mathbf{x}'=H\mathbf{x}$，$\omega$ 跟著變成 $\omega'=H^{-\mathsf{T}}\omega H^{-1}$：

$$
\mathbf{x}_1'^\mathsf{T}\omega'\mathbf{x}_2'=\mathbf{x}_1^\mathsf{T}H^\mathsf{T}\cdot H^{-\mathsf{T}}\omega H^{-1}\cdot H\mathbf{x}_2=\mathbf{x}_1^\mathsf{T}\omega\mathbf{x}_2
$$

所有 $H$ 都消掉。分母同理。

**說明 3：垂直** [▶ 32:28](https://youtu.be/XSflleJr4qM?t=1948)：兩條光線垂直（$\cos90^\circ=0$）⟺

$$
\mathbf{x}_1^\mathsf{T}\omega\mathbf{x}_2=0
$$

**說明 4：對偶** [▶ 33:01](https://youtu.be/XSflleJr4qM?t=1981)：

- 第 02 集：非退化二次曲線的對偶 $C^*=C^{-1}$。
- $\omega$ 由 $K$ 決定，$K$ 永遠滿秩 → $\omega$ 永遠滿秩 → 對偶一定存在。
- **絕對二次曲線的對偶像（dual image of the absolute conic, DIAC）**：
$$
\omega^*=\omega^{-1}=KK^\mathsf{T}
$$
- $\omega$ 是點二次曲線（由點定義）；$\omega^*$ 由包絡它的線定義。同樣看不到。
- $\omega^*$ 也等於**絕對對偶二次曲面 $Q_\infty^*$ 的像**（第 07 集），用第 13 集的 $C^*=PQ^*P^\mathsf{T}$。

> 以下**不是逐字稿內容**，是驗證 $\omega^*$ 是 $Q_\infty^*$ 的像：$PQ_\infty^*P^\mathsf{T}=KR[I\mid-\tilde{\mathbf{C}}]\begin{pmatrix}I&\mathbf{0}\\\mathbf{0}^\mathsf{T}&0\end{pmatrix}[I\mid-\tilde{\mathbf{C}}]^\mathsf{T}R^\mathsf{T}K^\mathsf{T}=KR\,I\,R^\mathsf{T}K^\mathsf{T}=KK^\mathsf{T}$。

**從 $\omega$ 求 $K$** [▶ 34:57](https://youtu.be/XSflleJr4qM?t=2097)：一旦在影像上找出 $\omega$（或 $\omega^*$），因為 $\omega^*=KK^\mathsf{T}$，用 **Cholesky 分解**就能唯一求出上三角的 $K$（和第 12 集一樣）。

⚠️ 逐字稿缺字：Whisper 把 Cholesky 寫成 “kolinsky”。

### 4.4 circular points 的像在 ω 上

[▶ 35:24](https://youtu.be/XSflleJr4qM?t=2124)

- 場景平面 $\boldsymbol{\pi}$ 和 $\boldsymbol{\pi}_\infty$ 交於一條線（$\boldsymbol{\pi}$ 的無窮遠線 $\mathbf{l}_\infty$）。
- 這條線和 $\Omega_\infty$ 交於兩點——$\boldsymbol{\pi}$ 的 **circular points**（第 07 集）。
- 投影到影像：
  - $\Omega_\infty$ → $\omega$；
  - $\boldsymbol{\pi}$ 的 $\mathbf{l}_\infty$ → 影像上有限的**消失線**；
  - circular points → **circular points 的像**。
- 所以：**平面的 circular points 的像，落在 $\omega$ 和這個平面消失線的交點上**。
- 注意：消失線看得到；但 $\omega$ 和 circular points 的像是複數，看不到（數學上存在）。

⚠️ 逐字稿缺字 [▶ 37:10](https://youtu.be/XSflleJr4qM?t=2230)：講者說「the intersection of this vanishing point with this omega ... omega star」，依上下文應為「消失**線**和 $\omega$ 的交點」。

---

## 5. 簡單校正裝置：三個正方形

[▶ 38:01](https://youtu.be/XSflleJr4qM?t=2281)

- 用 $\omega$ 的知識可以設計一個很簡單的校正裝置：**三個平面，各印一個黑色正方形**（白邊），要能在影像上看到四個角點。
- 三個平面**不需要互相垂直**，也不需要任何特定配置——**但不能互相平行**。
  - 平行的話等於一個大平面，就沒有三個獨立平面提供足夠的約束。

（本集到 39:25 結束，下一集接著講這個裝置怎麼算 $K$。）

【課本補充】MVG Example 8.18（下一集會講）的步驟：每個正方形 4 角 → homography $H=[\mathbf{h}_1\ \mathbf{h}_2\ \mathbf{h}_3]$ → circular points 的像 $\mathbf{h}_1\pm i\mathbf{h}_2$ → 兩條約束 $\mathbf{h}_1^\mathsf{T}\omega\mathbf{h}_2=0$、$\mathbf{h}_1^\mathsf{T}\omega\mathbf{h}_1=\mathbf{h}_2^\mathsf{T}\omega\mathbf{h}_2$；三個正方形共 6 條 → 解 $\omega$ → Cholesky 得 $K$。這和第 12 集的 Zhang 方法本質相同。

---

## 6. 一頁速查表

### 純旋轉應用

| 應用 | 做法 |
|---|---|
| 合成視角 | 平面四邊形 4 角 → 指定長寬比的矩形 → $H$ → 反向映射 |
| 全景拼接 | 選參考影像；$H_{i\to\text{ref}}$；不重疊就串接 $H_{53}=H_{43}H_{54}$ |

### 已知 K

| 公式 | 關鍵一步 |
|---|---|
| 光線方向 $\mathbf{d}=K^{-1}\mathbf{x}$ | $\mathbf{x}=K[I\mid\mathbf{0}](\lambda\mathbf{d},1)^\mathsf{T}=\lambda K\mathbf{d}$ |
| 光線夾角 $\cos\theta=\dfrac{\mathbf{x}_1^\mathsf{T}\omega\mathbf{x}_2}{\sqrt{(\mathbf{x}_1^\mathsf{T}\omega\mathbf{x}_1)(\mathbf{x}_2^\mathsf{T}\omega\mathbf{x}_2)}}$ | 代 $\mathbf{d}_i=K^{-1}\mathbf{x}_i$ |
| 垂直 $\mathbf{x}_1^\mathsf{T}\omega\mathbf{x}_2=0$ | $\cos90^\circ=0$ |
| 影像線反投影平面的法向 $\mathbf{n}=K^\mathsf{T}\mathbf{l}$ | $\mathbf{d}^\mathsf{T}\mathbf{n}=0$ 對線上所有點成立 |

### 絕對二次曲線的像

| 公式 | 關鍵一步 |
|---|---|
| $\boldsymbol{\pi}_\infty\to$ 影像：$H=KR$ | $P(\mathbf{d},0)^\mathsf{T}=KR\mathbf{d}$，和 $\tilde{\mathbf{C}}$ 無關 |
| $\omega=(KK^\mathsf{T})^{-1}=K^{-\mathsf{T}}K^{-1}$ | $(KR)^{-\mathsf{T}}I(KR)^{-1}$，$RR^\mathsf{T}=I$ |
| $\omega^*=KK^\mathsf{T}$ = $Q_\infty^*$ 的像 | $PQ_\infty^*P^\mathsf{T}$ |
| 從 $\omega$ 求 $K$ | Cholesky($\omega^*$) |
| circular points 的像 = 消失線 ∩ $\omega$ | 平面的 $\mathbf{l}_\infty$ ∩ $\Omega_\infty$ |

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 三個正方形校正 | 第 15 集（細節） |
| $\omega$、正交約束 $\mathbf{x}_1^\mathsf{T}\omega\mathbf{x}_2=0$ | 第 15 集（三個互相垂直的消失點求 $K$） |
| $\mathbf{n}=K^\mathsf{T}\mathbf{l}$ | 第 15 集（從消失線求平面方向） |
| $\mathbf{d}=K^{-1}\mathbf{x}$（正規化座標） | 第 16–19 集（本質矩陣 $E$ 用正規化座標）；第 20–22 集（PnP 的方向向量） |
| 全景拼接、串接 homography | 第 27–30 集（多視角時串接位姿） |

---

## 附：本集一句話總結

> **相機中心不動時，用 homography 就能做合成視角和全景拼接；知道 $K$ 就能把像點變成光線方向 $K^{-1}\mathbf{x}$、量光線夾角、求影像線反投影平面的法向 $K^\mathsf{T}\mathbf{l}$——這一切都濃縮在絕對二次曲線的像 $\omega=(KK^\mathsf{T})^{-1}$ 裡：它只依賴 $K$，所以只要能在影像上找出 $\omega$，Cholesky 一下就校正好了。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 6 (Part 2) 錄影逐字稿（Whisper `medium.en`，39:32）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §8.4.3、§8.5 整理。*
