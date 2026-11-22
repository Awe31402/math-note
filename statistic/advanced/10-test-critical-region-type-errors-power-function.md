---
course: 高等統計學（數理統計續）
episode: 10
lecture: Lec10（第六週 1/2）
date: 待補
video: https://youtu.be/0bduTBX_Mvw
notes: Hogg 8th ed. §4.5 檢定、拒絕域（critical region）、型一／型二錯誤、檢定力函數（power function）（p. 267–270）
---

# 第 10 集 · 第六週 (1/2)：檢定與拒絕域；型一、型二錯誤；檢定力函數 [▶ 影片](https://youtu.be/0bduTBX_Mvw)

← 上一集：[09](09-hypothesis-testing-intro-null-alternative.md) ｜ [總目錄](../README.md) ｜ 下一集：[11](11-size-significance-level-most-powerful-test.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 10 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（1:01:52，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §4.5
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「critical region」照錄（中文「拒絕域」），「power function」→「Pow Function」，「Type I/II error」→「行醫錯誤／形1形2」，「observation」→「adervation／Attervation」，「past」→「Post」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習：H₀ 放「新的沒有比較好」](#1-複習h₀-放新的沒有比較好)
- [2. 檢定（test）是什麼](#2-檢定test是什麼)
- [3. 拒絕域 C](#3-拒絕域-c)
- [4. 型一錯誤、型二錯誤](#4-型一錯誤型二錯誤)
- [5. 檢定力函數](#5-檢定力函數)
- [6. 例：學生程度有沒有變好](#6-例學生程度有沒有變好)
  - [6.1 設定](#61-設定)
  - [6.2 拒絕域 C₁：x̄＞75](#62-拒絕域-c₁x75)
  - [6.3 拒絕域 C₂：x̄＞78](#63-拒絕域-c₂x78)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 檢定＝規則；拒絕域 $C$ | §4.5 |
| 型一錯誤、型二錯誤 | §4.5 |
| 檢定力函數 $\pi_C(\theta)$ | §4.5 |
| 例：$N(\mu,100)$，$H_0:\mu\le 75$ | §4.5 |

---

## 1. 複習：H₀ 放「新的沒有比較好」

[▶ 00:32](https://youtu.be/0bduTBX_Mvw?t=32) 兩個假設就是兩個選擇。統計討論的通常是**新的和舊的比**。

【口頭】

- 新藥向 FDA 申請：FDA 不會輕易核准，因為核准了你就大賺；而且萬一上市後發現副作用（例如心臟不好的人吃了出問題），就來不及了。要統計分析證明**好很多**才核准。
- [▶ 02:08](https://youtu.be/0bduTBX_Mvw?t=128) 工廠新生產線：整個生產要改、要買新設備、要訓練人員，花很多成本；舊的拆了、新的生產幾個月發現比較差，就來不及了。
- [▶ 03:42](https://youtu.be/0bduTBX_Mvw?t=222) 舊的用了很久（FDA 某個藥用了幾十年），雖然沒那麼好，但不會很差、沒有其他副作用。新的會不會有副作用不知道。

[▶ 04:15](https://youtu.be/0bduTBX_Mvw?t=255) 所以：

> $H_0$：新的**沒有比較好**（not better than the old）
> vs
> $H_1$：新的**比較好**。

拒絕 $H_0$ ⇒ 相信 $H_1$ ⇒ 採用新的（新藥上市）。採用新的是比較冒險的選擇，所以不輕易拒絕 $H_0$。

[▶ 08:23](https://youtu.be/0bduTBX_Mvw?t=503) 假設定好，就去做實驗（在新產品上），得到隨機樣本，用它來檢定。

---

## 2. 檢定（test）是什麼

[▶ 09:24](https://youtu.be/0bduTBX_Mvw?t=564)

> **定義（檢定，test）**：一個**規則**（rule），決定什麼時候**拒絕** $H_0$、什麼時候**不拒絕** $H_0$。

[▶ 11:26](https://youtu.be/0bduTBX_Mvw?t=686) 學理上的結論說法只有兩種：「拒絕 $H_0$」或「不拒絕 $H_0$」，都沒有講到 $H_1$。拒絕 $H_0$ 可以想成接受 $H_1$。

---

## 3. 拒絕域 C

[▶ 12:28](https://youtu.be/0bduTBX_Mvw?t=748) 規則怎麼表現：給一個**樣本空間的子集** $C$。

**樣本空間**（[▶ 12:59](https://youtu.be/0bduTBX_Mvw?t=779)）：隨機變數可能發生的值的集合。

| 分配 | $X$ 的樣本空間 |
|---|---|
| 常態 | $\mathbb{R}$ |
| Poisson | $\{0,1,2,\dots\}$ |
| 二項 $b(n,p)$ | $\{0,1,\dots,n\}$ |

$n$ 個樣本 → $n$ 維的樣本空間。

[▶ 14:01](https://youtu.be/0bduTBX_Mvw?t=841) 把 $(X_1,\dots,X_n)$ 的樣本空間切成兩半，一半叫 $C$：

> **檢定的規則**：觀察到 $(x_1,\dots,x_n)$，
> - 若 $(x_1,\dots,x_n)\in C$ → **拒絕** $H_0$；
> - 若 $(x_1,\dots,x_n)\notin C$ → **不拒絕** $H_0$。
>
> $C$ 叫**拒絕域**（rejection region），也叫 **critical region**。

- [▶ 17:39](https://youtu.be/0bduTBX_Mvw?t=1059) 檢定和 $C$ 是**一體兩面**：有一個檢定就有一個 $C$，有一個 $C$ 就是一個檢定。
- [▶ 18:09](https://youtu.be/0bduTBX_Mvw?t=1089) 【口頭】微積分裡微分等於 0 的點叫 critical point；這裡叫 critical region，比較熟悉的叫法是 rejection region。
- [▶ 19:43](https://youtu.be/0bduTBX_Mvw?t=1183) 找檢定方法＝找 $C$。隨便找很容易，問題是要找**好的** $C$。

---

## 4. 型一錯誤、型二錯誤

[▶ 20:13](https://youtu.be/0bduTBX_Mvw?t=1213)

| | 不拒絕 $H_0$ | 拒絕 $H_0$ |
|---|---|---|
| **$H_0$ 對** | 對 | **型一錯誤**（Type I error） |
| **$H_1$ 對** | **型二錯誤**（Type II error） | 對 |

- [▶ 22:52](https://youtu.be/0bduTBX_Mvw?t=1372) 希望兩種錯誤都不發生，不可能：$\hat\theta$ 通常不等於 $\theta$，根本不知道真正的 $\theta$。
- [▶ 23:22](https://youtu.be/0bduTBX_Mvw?t=1402) 希望兩種錯誤的機率都很低，**也不可能**（$n$ 有限時）。
- 所以選一種**比較嚴重**的，讓它的機率很低：**型一錯誤**（$H_0$ 對卻被拒絕）。這就是「除非資料強烈顯示 $H_0$ 不對，否則不拒絕」。
- [▶ 25:53](https://youtu.be/0bduTBX_Mvw?t=1553) 除非 $n\to\infty$（那時 $\hat\theta\to\theta$，就知道 $\theta$ 了）；但人的生命有限，不可能抽無窮多樣本。
- [▶ 26:24](https://youtu.be/0bduTBX_Mvw?t=1584) 原則：先控制一種（型一）很小，再讓另一種也小。

---

## 5. 檢定力函數

[▶ 26:55](https://youtu.be/0bduTBX_Mvw?t=1615)

> **定義（檢定力函數，power function）**：給定拒絕域 $C$，
> $$\pi_C(\theta)=P_\theta(\text{拒絕 }H_0)=P_\theta\left((X_1,\dots,X_n)\in C\right).$$
> 當真正的參數是 $\theta$ 時，拒絕 $H_0$ 的機率。是 $\theta$ 的函數。

**怎麼算**（[▶ 34:41](https://youtu.be/0bduTBX_Mvw?t=2081)）：拒絕 $H_0$ ⇔ $(X_1,\dots,X_n)$ 落在 $C$，兩個事件一樣，所以
$$\pi_C(\theta)=\int\!\cdots\!\int_Cf(x_1,\dots,x_n;\theta)\,dx_1\cdots dx_n.$$
$C$ 和 joint pdf 的形式固定，給一個 $\theta$ 就得一個積分值。

**希望的樣子**（[▶ 29:02](https://youtu.be/0bduTBX_Mvw?t=1742)）：

| $\theta$ 在哪裡 | $\pi_C(\theta)$ 的意義 | 希望 |
|---|---|---|
| $H_0$ 為真 | 型一錯誤的機率 | **小** |
| $H_1$ 為真 | 正確拒絕的機率 | **大** |

[▶ 30:35](https://youtu.be/0bduTBX_Mvw?t=1835) $H_1$ 為真時，$1-\pi_C(\theta)$＝沒拒絕 $H_0$ 的機率＝**型二錯誤**的機率。所以 $\pi_C$ 大 ⇔ 型二錯誤小。

---

## 6. 例：學生程度有沒有變好

【口頭】[▶ 37:18](https://youtu.be/0bduTBX_Mvw?t=2238) 這個例子要花時間自己推導、想它的意義；清楚了，就會了解型一、型二錯誤的機率大小，以及後面為什麼用那些方法找檢定。

### 6.1 設定

[▶ 37:48](https://youtu.be/0bduTBX_Mvw?t=2268) 【口頭】美國政府常研究教育改革、提升學生能力，通常著重數學、理科（比較難）。想知道現在學生有沒有變聰明；也研究都市小孩是否比鄉下小孩數學好——通常是對的，像交大學生來自台北的比例一定很高。確定的話，政府應該改善鄉下的師資、教育資源。美國有 SAT 這種大家都能考的測驗。

[▶ 40:20](https://youtu.be/0bduTBX_Mvw?t=2420) 過去的經驗：以前的學生平均 75 分。

[▶ 40:50](https://youtu.be/0bduTBX_Mvw?t=2450) $X$：隨便抽一個現在的學生考試的成績。

- [▶ 41:22](https://youtu.be/0bduTBX_Mvw?t=2482) 為什麼是隨機變數：抽之前每個學生都可能被抽到。讓每人被抽到機會一樣，抽 $n$ 個就是 $n$ 個 iid 隨機變數。
- [▶ 42:54](https://youtu.be/0bduTBX_Mvw?t=2574) 假設 $X\sim N(\mu,100)$：$\mu$ 是所有學生的平均程度；學生程度不會都一樣，有變異，$\sigma^2=100$ 假設已知。

**假設**（[▶ 43:54](https://youtu.be/0bduTBX_Mvw?t=2634)）：希望現在的學生比較好（$\mu>75$），但「沒有比較好」放 $H_0$：
$$H_0:\mu\le 75\quad\text{vs}\quad H_1:\mu>75.$$

[▶ 44:24](https://youtu.be/0bduTBX_Mvw?t=2664) 除非抽出來的學生成績普遍比 75 好很多，否則不拒絕 $H_0$。

**樣本**（[▶ 45:25](https://youtu.be/0bduTBX_Mvw?t=2725)）：抽 $n=25$ 個學生。

⚠️ 逐字稿缺字：[▶ 50:32](https://youtu.be/0bduTBX_Mvw?t=3032) 老師一開始說抽 20 個，算變異數時改口「這裡是 25，不然沒辦法除」。以下用 $n=25$。

$$\bar X\sim N\left(\mu,\frac{100}{25}\right)=N(\mu,4),\qquad\text{標準差}=2.$$

### 6.2 拒絕域 C₁：x̄＞75

[▶ 46:56](https://youtu.be/0bduTBX_Mvw?t=2816) 先給一個拒絕域（以後再講怎麼找）：
$$C_1=\{(x_1,\dots,x_{25}):\bar x>75\}.$$
它是 25 維空間的子集，把空間切成 $\bar x>75$ 和 $\bar x\le 75$ 兩半。

**檢定力函數**（[▶ 49:29](https://youtu.be/0bduTBX_Mvw?t=2969)）：
$$\pi_{C_1}(\mu)=P_\mu(\bar X>75)=P_\mu\left(\frac{\bar X-\mu}{2}>\frac{75-\mu}{2}\right)=1-\Phi\left(\frac{75-\mu}{2}\right).$$

[▶ 52:34](https://youtu.be/0bduTBX_Mvw?t=3154) 代幾個值：

| $\mu$ | $\frac{75-\mu}{2}$ | $\pi_{C_1}(\mu)$ |
|---|---|---|
| 75 | 0 | 0.5 |
| 77 | $-1$ | 0.841 |
| 79 | $-2$ | 0.977 |

[▶ 54:09](https://youtu.be/0bduTBX_Mvw?t=3249) 圖形：遞增曲線，$\mu\to\infty$ 時趨近 1（機率最多是 1）。

**評價**（[▶ 54:39](https://youtu.be/0bduTBX_Mvw?t=3279)）：

- 好的一面：$H_0$ 區（$\mu\le 75$）比較小、$H_1$ 區越來越大。$\mu=77$ 時拒絕 $H_0$ 的機率 0.84，很棒。
- [▶ 55:41](https://youtu.be/0bduTBX_Mvw?t=3341) 壞的一面：$\mu=75$ 屬於 $H_0$，卻有 **50%** 的機會拒絕 $H_0$——型一錯誤太大。所以 $C_1$ **不好**。

**理想**（[▶ 57:13](https://youtu.be/0bduTBX_Mvw?t=3433)）：$H_0$ 區通通很小、一過 75 就通通很大（像階梯）。**不存在**這種檢定。

### 6.3 拒絕域 C₂：x̄＞78

[▶ 58:15](https://youtu.be/0bduTBX_Mvw?t=3495) 原本超過 75 就拒絕；改大一點：
$$C_2=\{\bar x>78\},\qquad\pi_{C_2}(\mu)=1-\Phi\left(\frac{78-\mu}{2}\right).$$

- $\mu=75$：$\pi_{C_2}(75)=1-\Phi(1.5)=0.067$。型一錯誤小多了。
- [▶ 59:48](https://youtu.be/0bduTBX_Mvw?t=3588) 但曲線整個往右移，$\mu=77$ 時一定不高。

**結論**（[▶ 60:21](https://youtu.be/0bduTBX_Mvw?t=3621)）：

- 讓 $H_0$ 為真時拒絕的機率變小（型一小），$H_1$ 為真時拒絕的機率也不會很大 ⇒ 型二錯誤變大。
- **不可能同時讓兩種錯誤都很小**。
- 做法：先把型一錯誤控制得很小；在所有滿足這條件的 $C$ 裡，選 $H_1$ 為真時檢定力最大的那個。

---

## 7. 一頁速查表

**$H_0$ / $H_1$**：$H_0$＝新的沒比較好；$H_1$＝新的比較好。

**檢定**＝規則＝拒絕域 $C$（樣本空間的子集）：$\mathbf x\in C$ ⇒ 拒絕 $H_0$。

**兩種錯誤**

| | 定義 | 地位 |
|---|---|---|
| 型一 | $H_0$ 對但拒絕 | 比較嚴重，先控制 |
| 型二 | $H_1$ 對但不拒絕 | 再盡量小 |

**檢定力函數**：$\pi_C(\theta)=P_\theta(\mathbf X\in C)=\int_Cf(\mathbf x;\theta)\,d\mathbf x$。

- $\theta\in H_0$：$\pi_C(\theta)$＝型一錯誤機率，要小。
- $\theta\in H_1$：$1-\pi_C(\theta)$＝型二錯誤機率；$\pi_C$ 要大。

**例**（$X\sim N(\mu,100)$，$n=25$，$\bar X\sim N(\mu,4)$，$H_0:\mu\le 75$）

| $C$ | $\pi_C(\mu)$ | $\pi(75)$ | $\pi(77)$ |
|---|---|---|---|
| $\bar x>75$ | $1-\Phi\left(\frac{75-\mu}{2}\right)$ | 0.5 | 0.841 |
| $\bar x>78$ | $1-\Phi\left(\frac{78-\mu}{2}\right)$ | 0.067 | 較小 |

型一變小 ⇒ 型二變大。兩者不能同時很小。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 先控制型一錯誤 | 下一集：顯著水準 $\alpha$、檢定的大小（size） |
| 在型一受控下讓檢定力最大 | 最強力檢定、Neyman–Pearson 引理、UMP 檢定 |

---

## 附：本集一句話總結

> **檢定就是一個拒絕域 $C$：樣本落在 $C$ 就拒絕 $H_0$；會犯型一錯誤（$H_0$ 對卻拒絕）和型二錯誤（$H_1$ 對卻不拒絕），兩者無法同時很小，所以先控制比較嚴重的型一錯誤；檢定力函數 $\pi_C(\theta)=P_\theta(\mathbf X\in C)$ 在 $H_0$ 區代表型一錯誤、在 $H_1$ 區越大越好。**

---

*筆記依據「高等統計學」Lec10 錄影逐字稿（whisper large-v3-turbo，1:01:52）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
