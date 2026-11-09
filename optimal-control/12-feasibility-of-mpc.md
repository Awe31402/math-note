---
course: Stanford AA203 Optimal and Learning-Based Control（2026 春）
episode: 12
lecture: Lecture 12
date: 待補（第 6 週週三）
video: https://youtu.be/8Elrw30y0tg
notes: 可行性、穩定性定理課本沒有（§3.4.2 只點出問題，轉介 Borrelli 等人）；δu 追蹤表述見《Principles of Robot Autonomy》§3.4.3（書頁 116–117，PDF 頁 118–119）
---

# 第 12 集 · Lecture 12：MPC 的可行性與穩定性（Feasibility of MPC） [▶ 影片](https://youtu.be/8Elrw30y0tg)

← 上一集：[11-intro-to-mpc](11-intro-to-mpc.md) ｜ [總目錄](README.md) ｜ 下一集：[13-intro-to-learning](13-intro-to-learning.md) →

> **課程**：Stanford AA203 Optimal and Learning-Based Control，2026 春 — 第 12 集
> **講者**：Marco Pavone（本集沒有自我介紹；提到自己的小孩、接續上一集，依此推斷）
> **來源**：YouTube 錄影逐字稿（1:15:26，上傳者提供的人工字幕）＋《Principles of Robot Autonomy》§3.4.3
> **標記說明**：
> - `【口頭】` 老師口頭補充，課本沒有
> - `【Q&A】` 學生提問與回答
> - `【課堂討論】` 老師問、學生答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 證明持續可行引理](#1-證明持續可行引理)
- [2. 主定理一：$\mathcal X_f$ 控制不變 ⟹ 持續可行](#2-主定理一mathcal-x_f-控制不變--持續可行)
  - [2.1 敘述與直覺](#21-敘述與直覺)
  - [2.2 證明](#22-證明)
- [3. Lyapunov 穩定性（速成）](#3-lyapunov-穩定性速成)
- [4. 主定理二：MPC 穩定性](#4-主定理二mpc-穩定性)
  - [4.1 敘述](#41-敘述)
  - [4.2 證明：最佳成本是 Lyapunov 函數](#42-證明最佳成本是-lyapunov-函數)
- [5. 怎麼實際選 $\mathcal X_f$ 和 $P$](#5-怎麼實際選-mathcal-x_f-和-p)
- [6. 顯式（離線）MPC](#6-顯式離線mpc)
- [7. MPC 設計流程](#7-mpc-設計流程)
- [8. 用 MPC 追蹤：δu 表述](#8-用-mpc-追蹤δu-表述)
- [9. 演算法整理](#9-演算法整理)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:05](https://youtu.be/8Elrw30y0tg?t=5)

1. 收尾**持續可行**。
2. **穩定性**：不只每刻都有可行解，還要做有用的事——這裡是讓系統**收斂到 0**。
3. 實務議題：
   - 部分最佳化**離線**做。【口頭】十年前這很重要：硬體和解法器都不夠強，把一部分最佳化移到離線能減少線上延遲。
   - MPC 用在**軌跡追蹤**要怎麼改。【口頭】「業界有時會搞錯，我要確保你不是那種人。」

| 主題 | 課本 |
|---|---|
| 持續可行引理證明、主定理一 | 課本沒有 |
| Lyapunov 穩定、主定理二與證明 | 課本沒有 |
| 選 $\mathcal X_f$、$P$ 的實際做法 | 課本沒有 |
| 顯式 MPC | 課本沒有 |
| δu 追蹤表述 | §3.4.3 |

**回顧** [▶ 01:37](https://youtu.be/8Elrw30y0tg?t=97)：線性系統 + 多面體約束；一步可控集、控制不變集、正不變集、可行集；**引理**：截斷可行集 $\mathcal X_1$ 控制不變 ⟹ MPC 持續可行。$\mathcal X_1$ 不是旋鈕，但它是通往「連結到旋鈕 $\mathcal X_f$ 的定理」的墊腳石。

---

## 1. 證明持續可行引理

[▶ 03:14](https://youtu.be/8Elrw30y0tg?t=194)

> **引理**：$\mathcal X_1$ 是控制不變集 ⟹ MPC 持續可行。

【口頭】證明不太有趣，但能測試你懂不懂這些概念。「大部分是在比對定義，沒什麼巧思。」

**Step 1：$\mathcal X_1\subseteq\mathcal X\cap\mathrm{Pre}(\mathcal X_1)$** [▶ 03:45](https://youtu.be/8Elrw30y0tg?t=225)

- 定義：$\mathrm{Pre}(\mathcal X_1)=\{x\in\mathbb R^n:\exists u\in\mathcal U,\ Ax+Bu\in\mathcal X_1\}$。
- $\mathcal X_1$ 控制不變：$\forall x\in\mathcal X_1,\ \exists u\in\mathcal U,\ Ax+Bu\in\mathcal X_1$。
- 比較兩個定義 → $\mathcal X_1$ 裡的點也在 $\mathrm{Pre}(\mathcal X_1)$ 裡。
- $\mathcal X_1$ 的點本來就在 $\mathcal X$ 裡（定義）。所以 $\mathcal X_1\subseteq\mathcal X\cap\mathrm{Pre}(\mathcal X_1)$。

【Q&A】[▶ 08:05](https://youtu.be/8Elrw30y0tg?t=485) 學生問 $\mathrm{Pre}$ 集不一定在 $\mathcal X$ 裡？答：對，照這裡的定義，$\mathrm{Pre}$ 只要求一步後落進 $\mathcal X_1$，起點本身可以不屬於 $\mathcal X$。

**Step 2：$\mathcal X_0=\mathcal X\cap\mathrm{Pre}(\mathcal X_1)$** [▶ 05:55](https://youtu.be/8Elrw30y0tg?t=355)

$\mathcal X_0$ 的定義（存在可行控制序列，狀態都可行且滿足終端條件）可以改寫成：**狀態可行**，而且**存在一個可行控制讓下一步落在 $\mathcal X_1$**（因為 $\mathcal X_1$ 正好包含了「剩下的截斷序列可行」這件事）。這就是 $\mathcal X\cap\mathrm{Pre}(\mathcal X_1)$。

**Step 3**：合起來 → $\mathcal X_1\subseteq\mathcal X_0$。

**Step 4：MPC 走一步之後** [▶ 08:36](https://youtu.be/8Elrw30y0tg?t=516)

- 取 $x_0\in\mathcal X_0$，$U_0^*$ 是 MPC 解，用第一個控制 $u_0^*$ 走到 $x_1$。
- $u_0^*$ 是可行 MPC 軌跡的一部分 → $x_1$ 滿足所有截斷約束 → $x_1\in\mathcal X_1$。
- 由 Step 3，$x_1\in\mathcal X_0$ → 新的 MPC 問題**可行**。
- 遞迴套用 → 永遠可行。∎

【口頭】[▶ 10:45](https://youtu.be/8Elrw30y0tg?t=645) 期末考會有一題問例如「什麼是控制不變集」。

**時域 $N=1$ 時** [▶ 10:45](https://youtu.be/8Elrw30y0tg?t=645)：$\mathcal X_1=\mathcal X_f$，所以選 $\mathcal X_f$ 控制不變就行。一般 $N>1$ 怎麼辦？→ 下一節。

---

## 2. 主定理一：$\mathcal X_f$ 控制不變 ⟹ 持續可行

### 2.1 敘述與直覺

[▶ 11:51](https://youtu.be/8Elrw30y0tg?t=711)

> **定理（持續可行）**：如果終端集 $\mathcal X_f$ 是系統的**控制不變集**，那麼 MPC 律是**持續可行**的。

$\mathcal X_f$ 是**我們自己選**的——這是可以調的旋鈕。

**最簡單的控制不變集** 【課堂討論】[▶ 12:21](https://youtu.be/8Elrw30y0tg?t=741)：老師問有什麼明顯的控制不變集？「數學問題沒把握時，永遠猜 0。」——**原點** $\{0\}$。在 0、用 $u=0$（「什麼都不做」通常是允許的），線性動態下下一步還是 0。

**直覺** [▶ 13:22](https://youtu.be/8Elrw30y0tg?t=802)：如果要求 $N$ 步到原點，下一刻時域往後移一步，總有可行序列：沿用上一次的序列，最後一步用 $u=0$ 待在原點就好。

**但原點不一定是好選擇** 【課堂討論】[▶ 14:25](https://youtu.be/8Elrw30y0tg?t=865)：

- 保證持續可行，很好。
- 但你通常也想**省控制力氣**。要求 $N$ 步內到原點，只能在「$N$ 步到原點」的序列中最佳化——通常都很耗力氣 → 控制很次佳。
- 所以終端約束（為了保證可行而人為加的）應該**越寬鬆越好**，不要過度限制系統。

【口頭】「這是大家真的在做的事」，怎麼設 $\mathcal X_f$ 一直是設計上的取捨。

### 2.2 證明

[▶ 15:58](https://youtu.be/8Elrw30y0tg?t=958) **思路**：證明 $\mathcal X_f$ 控制不變 ⟹ $\mathcal X_{N-1}$ 控制不變 ⟹ $\mathcal X_{N-2}$ 控制不變 ⟹ … ⟹ $\mathcal X_1$ 控制不變，再套用引理。

**第一步** [▶ 16:29](https://youtu.be/8Elrw30y0tg?t=989)：

$$\mathcal X_{N-1}=\left\{x\in\mathcal X:\ \exists u\in\mathcal U,\ Ax+Bu\in\mathcal X_f\right\}$$

（一步時域的截斷可行集。）要證：對 $x\in\mathcal X_{N-1}$，存在控制讓下一步回到 $\mathcal X_{N-1}$。

1. 由 $\mathcal X_{N-1}$ 的定義，存在 $u$ 使 $x_N:=Ax+Bu\in\mathcal X_f$。
2. 問：$x_N$ 也在 $\mathcal X_{N-1}$ 裡嗎？如果是，$\mathcal X_{N-1}$ 就控制不變了。
3. 由假設，$\mathcal X_f$ 控制不變：存在 $u'$ 使 $Ax_N+Bu'\in\mathcal X_f$。
4. 這**正好**是「$x_N\in\mathcal X_{N-1}$」的定義（另外 $x_N\in\mathcal X_f\subseteq\mathcal X$）。∎

【口頭】[▶ 19:11](https://youtu.be/8Elrw30y0tg?t=1151) 不要被下標搞混：$\mathcal X_{N-1}$ 只是一個集合的名字（一步可行集），「$x_N\in\mathcal X_{N-1}$」跟時間下標的先後無關。

遞迴套用到 $\mathcal X_1$，再用引理。∎

【口頭】[▶ 21:14](https://youtu.be/8Elrw30y0tg?t=1274) 作業 3 會用工具箱算控制不變集。

【口頭】[▶ 21:44](https://youtu.be/8Elrw30y0tg?t=1304) 老師咳嗽：「我兒子從托兒所帶回來的。小孩是生化武器。這是我第四還是第五次……我在錄影，就說到這。」

---

## 3. Lyapunov 穩定性（速成）

[▶ 22:45](https://youtu.be/8Elrw30y0tg?t=1365) 已經知道怎麼保證可行（旋鈕：$\mathcal X_f$）。剩下兩個旋鈕：終端成本 $P$ 和時域 $N$。能不能調它們保證**穩定**？工具：**Lyapunov 穩定性**。

**直覺** [▶ 23:46](https://youtu.be/8Elrw30y0tg?t=1426)：系統 $x_{k+1}=f(x_k)$（或 $\dot x=f(x)$）。從平衡點附近出發，會不會回到平衡點、不會失控？

- 碗底的球：被推開後會晃，有摩擦就耗散能量，回到碗底 → **穩定**平衡點。
- 倒扣的碗頂上的球：放著不動會待住，但稍微偏一點就滾下去 → **不穩定**平衡點。

**難處** [▶ 25:22](https://youtu.be/8Elrw30y0tg?t=1522)：原則上要對附近所有初始條件解（非線性）方程看會怎樣——很難。

**Lyapunov 的想法** [▶ 25:53](https://youtu.be/8Elrw30y0tg?t=1553)：不直接看狀態怎麼演化。如果能找到某個類似**能量**的函數，沿著系統軌跡一直**下降**——系統在耗散能量——那它應該會收斂到能量最低點。

> **Lyapunov 定理**（離散時間）[▶ 26:54](https://youtu.be/8Elrw30y0tg?t=1614)
>
> 考慮 $x_{k+1}=f(x_k)$，原點是平衡點（$f(0)=0$）。$\Omega$ 是包含原點的有界閉正不變集。如果存在函數 $V$ 使得
> 1. $V(0)=0$
> 2. $V(x)>0$，$\forall x\in\Omega\setminus\{0\}$
> 3. $V(f(x))-V(x)<0$，$\forall x\in\Omega\setminus\{0\}$（沿軌跡下降）
>
> 那麼原點是**漸近穩定**的（吸引域 $\Omega$）。

> ⚠️ 逐字稿缺字 [▶ 29:41](https://youtu.be/8Elrw30y0tg?t=1781)：老師口誤說「non-decreasing property」，依定理內容應為**遞減**（non-increasing／decreasing）。

**重點** [▶ 28:35](https://youtu.be/8Elrw30y0tg?t=1715)：不用顯式解狀態轉移方程，就能主張穩定。

**難的部分** [▶ 29:08](https://youtu.be/8Elrw30y0tg?t=1748)：找 $V$。有時有物理論證（能量）；MPC 用的是另一種論證。

【課堂討論】[▶ 30:13](https://youtu.be/8Elrw30y0tg?t=1813) 老師問多少人聽過 Lyapunov 穩定性——很少人舉手。「那就去讀一讀。」很有用、物理意義很豐富。

---

## 4. 主定理二：MPC 穩定性

### 4.1 敘述

[▶ 31:47](https://youtu.be/8Elrw30y0tg?t=1907)

【口頭】MPC 被用了 20 年沒有理論，90 年代才補上。「現在有什麼也是沒理論就在用的？深度學習。」大家不知道它為什麼有效，但一直在用；也許十年後也會有類似的理論。

> **定理（MPC 穩定性）**：考慮線性系統的 MPC，成本是二次的：$q(x,u)=x^\top Qx+u^\top Ru$，$p(x)=x^\top Px$。假設
>
> - **(A0)** $R\succ 0$，$Q\succ 0$，$P\succ 0$。
> - **(A1)** $\mathcal X$、$\mathcal X_f$、$\mathcal U$ 是包含原點的閉集。
> - **(A2)** $\mathcal X_f$ 是**控制不變集**。
> - **(A3)** 對所有 $x\in\mathcal X_f$：
> $$\min_{\substack{u\in\mathcal U\\Ax+Bu\in\mathcal X_f}}\left[-p(x)+q(x,u)+p(Ax+Bu)\right]\le 0$$
>
> 那麼閉迴路系統的原點是**漸近穩定**的，吸引域為 $\mathcal X_0$。

**為什麼要 (A2)** 【課堂討論】[▶ 33:49](https://youtu.be/8Elrw30y0tg?t=2029)：學生答「讓 MPC 可行」。老師：對。

**(A3) 的直覺** [▶ 34:20](https://youtu.be/8Elrw30y0tg?t=2060)：存在 $u$ 讓下一步留在 $\mathcal X_f$，且
$$p(\text{下一狀態})-p(\text{現在})\le -q(x,u)$$
$q$ 是正的 → 有點像 Lyapunov 條件：$p$ 在 $\mathcal X_f$ 裡沿某個控制會下降。

【口頭】「我學生時代第一次看到這個條件，心想：這是哪個數學家的惡夢？」

**意思**：從 $\mathcal X_0$ 出發，MPC 會漸近收斂到原點。

### 4.2 證明：最佳成本是 Lyapunov 函數

[▶ 35:53](https://youtu.be/8Elrw30y0tg?t=2153) 老師說這個證明「蠻可愛的」，比可行性證明有趣。

**思路**：證明 **MPC 的最佳成本** $J_0^*(x)$ 就是閉迴路系統的 Lyapunov 函數，然後用 Lyapunov 定理。

**準備**：由 (A2)，MPC 持續可行（主定理一）。閉迴路 $x_{t+1}=f_{cl}(x_t)=Ax_t+B\pi(x_t)$ [▶ 38:09](https://youtu.be/8Elrw30y0tg?t=2289)：$u$ 寫成 $x$ 的函數後，系統只剩 $x$。

**Step 0：原點是平衡點** 【課堂討論】[▶ 39:14](https://youtu.be/8Elrw30y0tg?t=2354)：

- 從 0 出發，MPC 會算出什麼？學生：待在 0。
- 成本是二次項的和 → $\ge 0$；從 0 出發用 $u\equiv 0$，成本恰好 = 0 → 達到下界 → 最佳。
- 下一狀態 $A\cdot 0+B\cdot 0=0$ → 原點是閉迴路的平衡點。

**Step 1：$J_0^*(0)=0$** [▶ 41:22](https://youtu.be/8Elrw30y0tg?t=2482)：剛才已證。

**Step 2：$x\ne 0\Rightarrow J_0^*(x)>0$**：成本至少含 $x_0^\top Qx_0$，$Q\succ 0$、$x_0\ne 0$ → 正。

**Step 3：沿軌跡下降**（難的部分）[▶ 42:26](https://youtu.be/8Elrw30y0tg?t=2546)

設在 $x_0$ 解出最佳序列 $U_0^{(0)}=\left(u_0^{(0)},\dots,u_{N-1}^{(0)}\right)$，對應狀態 $\left(x_0,x_1^{(0)},\dots,x_N^{(0)}\right)$。走一步到 $x_1=Ax_0+Bu_0^{(0)}$。

**構造一個候選序列** [▶ 43:56](https://youtu.be/8Elrw30y0tg?t=2636)：把上次的序列**去頭**，尾巴**接一個** $v$：

$$\tilde U_1=\left(u_1^{(0)},\dots,u_{N-1}^{(0)},\ v\right)$$

從 $x_1$ 出發，它會沿著上次預測的狀態走：$x_2^{(0)},\dots,x_N^{(0)}$，最後一步到 $Ax_N^{(0)}+Bv$。

**選 $v$ 讓它可行** [▶ 47:39](https://youtu.be/8Elrw30y0tg?t=2859)：$x_N^{(0)}\in\mathcal X_f$（上次的終端約束），$\mathcal X_f$ 控制不變 → 存在可行 $v$ 使 $Ax_N^{(0)}+Bv\in\mathcal X_f$。這樣 $\tilde U_1$ 對時刻 1 的 MPC 問題**可行**：$v$ 滿足控制約束；中間狀態本來就可行（上次軌跡）；終端約束也滿足。

**上界** [▶ 49:49](https://youtu.be/8Elrw30y0tg?t=2989)：$\tilde U_1$ 可行但不一定最佳，所以

$$J_0^*(x_1)\le J(\tilde U_1)=\sum_{k=1}^{N-1}q\left(x_k^{(0)},u_k^{(0)}\right)+q\left(x_N^{(0)},v\right)+p\left(Ax_N^{(0)}+Bv\right)$$

**加減項** [▶ 50:49](https://youtu.be/8Elrw30y0tg?t=3049)：加減 $p(x_N^{(0)})$ 和 $q(x_0,u_0^{(0)})$：

$$J_0^*(x_1)\le\underbrace{\sum_{k=0}^{N-1}q\left(x_k^{(0)},u_k^{(0)}\right)+p\left(x_N^{(0)}\right)}_{=J_0^*(x_0)}-q\left(x_0,u_0^{(0)}\right)+\underbrace{\left[-p\left(x_N^{(0)}\right)+q\left(x_N^{(0)},v\right)+p\left(Ax_N^{(0)}+Bv\right)\right]}_{\le 0\ \text{選 }v=\bar v\text{（由 A3）}}$$

【課堂討論】[▶ 51:28](https://youtu.be/8Elrw30y0tg?t=3088) 老師問紅色三項加起來是什麼？學生：從 $x_0$ 出發的最佳成本。老師：「對，你的成績加 1 分。」

**用 (A3)** [▶ 52:32](https://youtu.be/8Elrw30y0tg?t=3152)：在所有讓 $Ax+Bu\in\mathcal X_f$ 的 $u$ 中，取讓方括號最小的 $\bar v$；(A3) 保證那個最小值 $\le 0$。

> ⚠️ 逐字稿缺字 [▶ 54:15](https://youtu.be/8Elrw30y0tg?t=3255)：字幕寫「all of that stuff is **greater than or equal to 0**」，依 (A3) 應為 **$\le 0$**。

**結論** [▶ 54:47](https://youtu.be/8Elrw30y0tg?t=3287)：

$$J_0^*(x_1)\le J_0^*(x_0)-q\left(x_0,u_0^{(0)}\right)$$

$x_0\ne 0$ 時 $q(x_0,u_0^{(0)})\ge x_0^\top Qx_0>0$ → $J_0^*(x_1)<J_0^*(x_0)$。**沿軌跡嚴格下降**。

套用 Lyapunov 定理 → 原點漸近穩定，吸引域 $\mathcal X_0$。∎

【口頭】[▶ 56:57](https://youtu.be/8Elrw30y0tg?t=3417) 「很有趣的證明吧？而且很強大。多看幾次內化它，這是非常重要的證明。」

---

## 5. 怎麼實際選 $\mathcal X_f$ 和 $P$

[▶ 57:27](https://youtu.be/8Elrw30y0tg?t=3447) 兩個定理怎麼變成可操作的？（終端成本是二次的，所以要決定矩陣 $P$。）

**把 (A3) 寫成二次形式** [▶ 59:04](https://youtu.be/8Elrw30y0tg?t=3544)：

$$-x^\top Px+x^\top Qx+u^\top Ru+(Ax+Bu)^\top P(Ax+Bu)\le 0,\quad\forall x\in\mathcal X_f$$

**情況 1：$A$ 漸近穩定**（所有特徵值在單位圓內）[▶ 57:57](https://youtu.be/8Elrw30y0tg?t=3477)

- $\mathcal X_f$ ＝ 系統 $x_{t+1}=Ax_t$ 的**最大正不變集** $\mathcal O_\infty$（用工具箱算）。
- 它是控制不變的：在裡面用 $u=0$，$Ax$ 還在裡面 → (A2) 滿足。
- (A3)：取 $u=0$ [▶ 60:13](https://youtu.be/8Elrw30y0tg?t=3613)，含 $u$ 的項消失，剩
$$x^\top\left(-P+Q+A^\top PA\right)x\le 0$$
這不是隨便的矩陣式子，而是著名的 **Lyapunov 方程** [▶ 60:45](https://youtu.be/8Elrw30y0tg?t=3645)：
$$A^\top PA-P+Q=0$$
$Q\succ 0$ 且 $A$ 漸近穩定時，存在**正定**解 $P$ → 等號成立 → (A3) 滿足。

**直覺** [▶ 61:50](https://youtu.be/8Elrw30y0tg?t=3710)：MPC 最佳化讓 $N$ 步後進入 $\mathcal O_\infty$；之後就算什麼都不做，自然的穩定動態也會帶你到原點。實際上你不會什麼都不做（一直重新最佳化會找到別的序列），但那個集合像**錨**，讓你保持在好的行為上。

**機械步驟**：用工具算 $\mathcal O_\infty$，再用一行 MATLAB 解 Lyapunov 方程得 $P$，代進 MPC → 保證持續可行和穩定。

**情況 2：$A$ 不穩定** [▶ 62:56](https://youtu.be/8Elrw30y0tg?t=3776)

自然動態不會幫你，要**主動控制**。用 **LQR** 當「錨」：

- $F_\infty$ ＝ 無限時域 LQR 的最佳增益。
- $\mathcal X_f$ ＝ **LQR 閉迴路動態** $x_{t+1}=(A+BF_\infty)x_t$ 的最大正不變集（而且在裡面 LQR 控制滿足控制約束）。
- $P$ ＝ 離散 **Riccati 方程**的解（無限時域 LQR 的成本矩陣）。
- 推導類似：把 $u=F_\infty x$ 代進 (A3)，選 $P$ 為 Riccati 方程的解會讓等號成立。代數比較繁，老師不展示。

**直覺** [▶ 65:40](https://youtu.be/8Elrw30y0tg?t=3940)：劃出一塊區域 $\mathcal X_f$，在裡面**無約束最佳控制器**（LQR）保證可行；並用它的值函數當終端成本，保證穩定。

| $A$ | $\mathcal X_f$ | $P$ |
|---|---|---|
| 穩定 | $x^+=Ax$ 的最大正不變集 | Lyapunov 方程 $A^\top PA-P+Q=0$ 的解 |
| 不穩定 | $x^+=(A+BF_\infty)x$ 的最大正不變集 | 離散 Riccati 方程的解（$F_\infty$ 為 LQR 增益） |

【口頭】這些不一定是最好的選擇，但很程序化。作業會有幾題。

---

## 6. 顯式（離線）MPC

[▶ 66:13](https://youtu.be/8Elrw30y0tg?t=3973) 到目前都是**線上**：量測 → 在裝置上解最佳化 → 用第一步 → 重解。也有**顯式**（explicit）、**離線**版本，**線上完全不用最佳化**。

（MPC 也能推廣到非線性系統，但本課只講線性。）

**結果** [▶ 67:16](https://youtu.be/8Elrw30y0tg?t=4036)：線性動態 + 二次成本 + 多面體約束（**有約束的 LQR**）的解是：

$$u^*(x)=F_jx+g_j,\qquad x\in\mathcal R_j$$

一個**連續的分段仿射**函數，定義在狀態空間的**多面體分割** $\{\mathcal R_j\}$ 上。

**用法**：量測狀態 → 查它落在哪個區域 → 取出那區的增益 $F_j,g_j$ → 得到最佳控制。分割和增益都離線算好（老師沒講怎麼算）。

**優缺點** [▶ 68:52](https://youtu.be/8Elrw30y0tg?t=4132)：

| 優點 | 缺點 |
|---|---|
| 線上不用解最佳化 | 分割常常形狀很怪、**區域非常多** |
| 不用信任線上解法器沒有 bug（例：讓火箭降落地球這種安全關鍵場合）；開發成本低：不用專人挑選、客製、移植到嵌入式、驗證解法器 | 現在凸最佳化解法器很強，**直接解常常比查一個超大表還快** |
| 一切都是顯式的 → **驗證**容易很多 | |

結論：是個值得知道的概念，但現在通常就用線上最佳化。

---

## 7. MPC 設計流程

[▶ 70:25](https://youtu.be/8Elrw30y0tg?t=4225)

1. 選 $\mathcal X_f$ 為**控制不變集** → 持續可行。（本課主要用 $\mathcal X_f$ 當可行性的旋鈕；也可以調時域長度。）
2. **自由**選 $Q$、$R$ 來調控制表現。
3. 依穩定性定理調整 $P$。
4. 計算控制不變集等工具：**MPT3**（作業 3 會用）。

---

## 8. 用 MPC 追蹤：δu 表述

[▶ 70:56](https://youtu.be/8Elrw30y0tg?t=4256) 最後四分鐘。到目前 MPC 是為了穩定（狀態到 0），但常常要拿來**追蹤**參考軌跡（例如直接法算出來的），當成外殼抵抗擾動。

**天真的寫法（不行）** [▶ 71:27](https://youtu.be/8Elrw30y0tg?t=4287)：

$$\sum_k\left(y_k-r_k\right)^\top Q\left(y_k-r_k\right)+u_k^\top Ru_k$$

**為什麼不行** [▶ 71:58](https://youtu.be/8Elrw30y0tg?t=4318)：追蹤常常需要**非零**控制。例：飛機要維持固定高度，不能關引擎，需要固定推力。

- 追蹤誤差趨近 0 時，成本被**控制力氣**主導 → MPC 想減少控制 → 推力降低 → 追蹤誤差上升 → 又加推力……
- 在控制力氣和追蹤誤差之間**來回震盪**。

**解法：改用控制的變化量** [▶ 72:29](https://youtu.be/8Elrw30y0tg?t=4349)：

$$\min_{\delta u_0,\dots,\delta u_{N-1}}\ \sum_k\left(y_k-r_k\right)^\top Q\left(y_k-r_k\right)+\delta u_k^\top R\,\delta u_k,\qquad \delta u_k=u_k-u_{k-1}$$

- $y_k=Cx_k$（$C$ 可以是單位矩陣，那就是 $x_k-r_k$）。
- 完美追蹤時：誤差 0、控制**固定**（固定推力）→ $\delta u=0$ → 成本 0。這正好是 MPC 在這個表述下想做的事。
- 實作 [▶ 73:33](https://youtu.be/8Elrw30y0tg?t=4413)：最佳化變數是 $\delta u$；給定 $u_{t-1}$，遞迴得到 $u_k=u_{k-1}+\delta u_k$。

【課本補充】課本 §3.4.3（MPC for Tracking: Delta Input Formulation）是同一個想法：動態寫成 $x_{t+1}=Ax_t+Bu_t$、$u_t=u_{t-1}+\delta u_t$、$y_t=Cx_t$，假設 $(A,B)$ 可控；到穩態時控制不變（$\delta u_t=0$）。課本說這對「在非零操作點附近」的追蹤和調節特別有利。出處 Borrelli、Bemporad、Morari。

**課程分水嶺** [▶ 74:03](https://youtu.be/8Elrw30y0tg?t=4443)：這堂結束了課程第一部分（**模型已知**）。下週起進入新設定：模型可能**不完全已知**——要嘛**適應**未知部分，要嘛**學習**你不知道的東西，仍然最佳（或接近最佳）地行動。

---

## 9. 演算法整理

### 有保證的 MPC 設計（線性、二次、多面體約束）

**在解什麼**：讓 MPC 持續可行且漸近穩定。

```
1. 選 Q ≻ 0、R ≻ 0（調表現）
2. 若 A 穩定：
       X_f ← x⁺ = A x 的最大正不變集（MPT3）
       P   ← 解 Lyapunov 方程 AᵀPA − P + Q = 0
   若 A 不穩定：
       F_∞, P ← 無限時域 LQR（離散 Riccati）
       X_f ← x⁺ = (A + B F_∞) x 的最大正不變集（且 F_∞x ∈ U）
3. 選 N 夠大，使關心的初始狀態落在可行集 X₀ 裡
4. 線上：每步解 MPC（終端約束 x_N ∈ X_f、終端成本 x_NᵀP x_N），用第一步
```

**什麼時候會失敗**：初始狀態不在 $\mathcal X_0$ → 沒有保證（一開始就不可行）；$\mathcal X_f$ 選太小（例如原點）→ 可行但控制很耗力、表現差；模型有誤差或擾動 → 這裡的保證是針對標稱模型的；非線性系統 → 要另外的理論。

### 顯式 MPC

**在解什麼**：線上沒時間或不想跑解法器（安全關鍵、要驗證）。

```
離線：算出多面體分割 {R_j} 和每區增益 (F_j, g_j)
線上：找出 x ∈ R_j → u = F_j x + g_j
```

**什麼時候會失敗**：區域數爆炸 → 表太大，查表比直接解還慢。

### 追蹤 MPC（δu 表述）

**在解什麼**：追蹤需要非零穩態控制的參考軌跡。

```
變數：δu₀…δu_{N−1}；u_k = u_{k−1} + δu_k（u_{−1} = 上一刻用的控制）
成本：Σ (y_k − r_k)ᵀQ(y_k − r_k) + δu_kᵀ R δu_k
```

**什麼時候會失敗**：用天真寫法（懲罰 $u$ 而非 $\delta u$）→ 控制力氣和追蹤誤差互相拉扯、震盪。

---

## 10. 一頁速查表

### 持續可行

| 結果 | 關鍵一步 |
|---|---|
| 引理：$\mathcal X_1$ 控制不變 ⟹ 持續可行 | $\mathcal X_1\subseteq\mathcal X\cap\mathrm{Pre}(\mathcal X_1)=\mathcal X_0$；MPC 走一步後 $x_1\in\mathcal X_1\subseteq\mathcal X_0$ |
| 定理：$\mathcal X_f$ 控制不變 ⟹ 持續可行 | $\mathcal X_f$ 控制不變 ⟹ $\mathcal X_{N-1}$ 控制不變 ⟹ … ⟹ $\mathcal X_1$，再用引理 |
| 最簡單的 $\mathcal X_f$ | $\{0\}$：可行但太嚴、耗力 |

### Lyapunov

$V(0)=0$、$V>0$（其他）、$V(f(x))<V(x)$ ⟹ 漸近穩定。

### 穩定性定理

假設：$Q,R,P\succ 0$；$\mathcal X_f$ 控制不變；
$$\min_{u\in\mathcal U,\ Ax+Bu\in\mathcal X_f}\left[-p(x)+q(x,u)+p(Ax+Bu)\right]\le 0\quad\forall x\in\mathcal X_f$$
⟹ 原點漸近穩定，吸引域 $\mathcal X_0$。

**證明關鍵**：Lyapunov 函數 = $J_0^*(x)$；候選序列「去頭 + 接 $\bar v$」可行 →
$$J_0^*(x_1)\le J_0^*(x_0)-q(x_0,u_0^*)+\underbrace{[\cdots]}_{\le 0}<J_0^*(x_0)$$

### 選 $\mathcal X_f$、$P$

| $A$ | $\mathcal X_f$ | $P$ |
|---|---|---|
| 穩定 | $\mathcal O_\infty$ of $x^+=Ax$ | $A^\top PA-P+Q=0$ |
| 不穩定 | $\mathcal O_\infty$ of $x^+=(A+BF_\infty)x$ | DARE |

### 其他

- 顯式 MPC：$u^*=F_jx+g_j$，$x\in\mathcal R_j$（分段仿射、多面體分割）。
- 追蹤：懲罰 $\delta u_k=u_k-u_{k-1}$，不是 $u_k$。
- 工具：MPT3。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 模型已知的部分結束 | 第 13 集起：模型未知、學習型控制 |
| 「適應或學習未知部分」 | 第 13 集學習入門（適應控制、系統辨識，待確認） |
| MPC + 學到的模型 | 第 19 集基於模型的 RL（待確認） |
| Lyapunov 穩定性 | 學習型控制的安全保證（待確認） |
| 作業 3 | MPC、MPT3 工具箱 |

---

## 附：本集一句話總結

> **只要終端集 $\mathcal X_f$ 是控制不變集，MPC 就持續可行（證明：一路推到 $\mathcal X_1$ 控制不變）；再讓終端成本 $p$ 在 $\mathcal X_f$ 裡滿足「Lyapunov 型」條件，MPC 的最佳成本 $J_0^*$ 本身就是 Lyapunov 函數（證明：上次的解去頭接一步是可行候選，成本至少降 $q(x_0,u_0)$），所以閉迴路漸近穩定。實務上：$A$ 穩定就用 $Ax$ 的最大正不變集 + Lyapunov 方程；不穩定就用 LQR 閉迴路的最大正不變集 + Riccati 方程。追蹤時要懲罰控制的變化量 $\delta u$，不是控制本身。**

---

## ⚠️ 待確認清單

1. 上課日期待補（第 6 週週三）。

---

*筆記依據 Marco Pavone「Stanford AA203 Optimal and Learning-Based Control（2026 春）」Lecture 12 錄影逐字稿（人工字幕，1:15:26）與《Principles of Robot Autonomy》§3.4.3 整理。*
