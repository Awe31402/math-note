---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 1
lecture: Lec00 隨機過程課程介紹
date: 待補
video: https://youtu.be/IsQSWVbAKy0
notes: Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 目錄（Part II，第 9–13 章，pp. 371–628）
---

# 第 1 集 · Lec00：課程介紹 [▶ 影片](https://youtu.be/IsQSWVbAKy0)

← 上一集：（無） ｜ [總目錄](README.md) ｜ 下一集：[02](02-probability-space-random-variable-sigma-field.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 1 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（8:29，whisper large-v3-turbo）＋ Papoulis 目錄
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「Papoulis」聽成「Propolis」，「syllabus」聽成「syllabat」，「Fourier Series」聽成「Fully Series」，「ergodicity」聽成「Ergasticity」，「bandlimited process」聽成「bending process」，「sampling theorem」聽成「simpling theorem」，「馬里蘭大學」聽成「馬里亞大學」，「習題」聽成「習記」，「正交」聽成「證交」，「幾率」＝「機率」。以下一律用正確的字。

> 這一集沒有數學，只介紹為什麼要學、課本、考試、進度。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 為什麼要學隨機過程：設計手機的例子](#1-為什麼要學隨機過程設計手機的例子)
- [2. 課本和講義](#2-課本和講義)
- [3. 考試](#3-考試)
- [4. 進度：要上哪些章節](#4-進度要上哪些章節)
- [5. 一頁速查表](#5-一頁速查表)
- [6. 與後續集數的連結](#6-與後續集數的連結)

---

## 0. 這堂課要做什麼

第一次上課照慣例講 syllabus（課程大綱）：為什麼學、用什麼書、怎麼考、上哪些章。

---

## 1. 為什麼要學隨機過程：設計手機的例子

[▶ 00:33](https://youtu.be/IsQSWVbAKy0?t=33) 老師說他在美國馬里蘭大學讀研究所時，**第一門課**就是 random process。【口頭】

為什麼這麼重要？用「設計一支手機」來想【口頭】：

- **要傳的資料不知道**：設計手機的當下，不知道將來使用者要傳什麼。
  - 做法：把資料當成**隨機的**。不知道下一個是 0 還是 1，但可以**假設**它們的機率，例如各 1/2。在這個前提下設計系統。
- **雜訊不知道**：將來一定有雜訊 (noise)，但不知道長什麼樣子。
  - 做法：假設它是隨機的，例如**高斯雜訊** (Gaussian noise)，針對它設計。
- 在這些機率假設下，設計出**機率意義下**傳輸效能最好的系統。

[▶ 02:03](https://youtu.be/IsQSWVbAKy0?t=123) 結論：**不管設計什麼系統，裡面都有隨機的部分和確定的部分**。所以需要一個模型 (model) 來描述隨機的部分，那就是隨機過程。

課程內容：

- 前兩章（第 9、10 章）是非常基本 (fundamental) 的部分。
- 後面會教比較深入 (advanced) 的部分。老師說二十幾年前他在美國學的時候只教基本的，這次會把進階的也納進來。【口頭】

---

## 2. 課本和講義

[▶ 03:06](https://youtu.be/IsQSWVbAKy0?t=186)

- **課本**：Papoulis（＆ Pillai），《Probability, Random Variables and Stochastic Processes》，2002 年（第 4 版）。
  - 老師說這幾年雖然有新書，但沒有特別的新內容，所以沿用舊課本。
  - 優點：**例題特別多，習題也非常多**，是經典。
- **講義**：很多內容是老師自己補充的、課本沒有，所以**以老師的講義為主**，順序大致跟課本走。【口頭】

（講義沒有公開；本系列筆記的次要來源只用課本。）

---

## 3. 考試

[▶ 04:12](https://youtu.be/IsQSWVbAKy0?t=252)【口頭】

- **三次大考**（期中、期末等），每次大約考 **3 小時**。
- **三次小考**，讓老師了解大家的學習狀況。

---

## 4. 進度：要上哪些章節

[▶ 04:12](https://youtu.be/IsQSWVbAKy0?t=252) 從**第 9 章**開始。

| 章節 | 主題 | 老師的說明 |
|---|---|---|
| 第 9 章 | General Concepts（基本概念） | 花最多時間；非常基本，還有很多老師補充的內容 |
| §9-3 | Power Spectrum（功率頻譜） | 工程上**最關心**的：功率（能量）在頻率上怎麼分布；花一節討論 |
| §10-1、§10-2 | Random Walks、Poisson Points and Shot Noise | **跳過**。random walk 很簡單，自己讀 |
| §10-3 | Modulation（調變） | 從這裡開始講；電信所很重視調變 |
| §10-4 | Cyclostationary Processes（循環平穩過程） | 工程上碰到的隨機訊號源，**基本上都是 cyclostationary** |
| §10-5 | Bandlimited Processes and Sampling Theory（帶限過程與取樣定理） | |
| §10-6 | Deterministic Signals in Noise（雜訊中的確定訊號） | 討論雜訊 |
| 附錄 10A | Poisson Sum Formula（Poisson 求和公式） | 很重要的公式，會推一次 |
| 第 11 章 | Spectral Representation（頻譜表示） | 進階內容開始 |
| §11-1 | Factorization and Innovations（分解與創新過程） | 真實世界看得到的隨機過程，一般都**可以做分解** |
| §11-2 | Finite-Order Systems and State Variables | 簡單的狀態機 (state machine) 概念 |
| §11-3 | Fourier Series and Karhunen–Loève Expansions | 兩種分析工具：Fourier 級數從**頻率**看，KL 展開從**正交**看 |
| §11-4 | Spectral Representation of Random Processes | 隨機過程和頻譜的關係 |
| §12-1 | Ergodicity（遍歷性） | **保證你可以估計**；不 ergodic 的訊號源沒辦法估計。每本書講法不太一樣、有混淆，會講清楚 |
| §12-2 | Spectrum Estimation（頻譜估計） | |
| 第 13 章 | Mean Square Estimation（均方估計） | 非常重要的工程工具 |
| §13-2 | Prediction（預測） | |

### 為什麼分解很重要（預告）

[▶ 06:16](https://youtu.be/IsQSWVbAKy0?t=376) 老師先給理由【口頭】：線性系統的

$$\text{輸出的功率頻譜}=\text{輸入的功率頻譜}\times\left|\text{濾波器的頻率響應}\right|^{2},$$

而「絕對值平方」$|H|^2=H\cdot H^{*}$ 本身就是一種分解。

【課本補充】這個關係是 §9-3 的式子 $S_{yy}(\omega)=S_{xx}(\omega)\left|H(\omega)\right|^{2}$（之後的集數會推導）。

### 最後一段：lattice structure

[▶ 07:50](https://youtu.be/IsQSWVbAKy0?t=470) 老師說「12-3」會從實作的角度看頻譜估計，用 **lattice structure**（格狀結構）。

⚠️ 待確認：課本裡 lattice filter 出現在 p. 553「Lattice Filters and Levinson's Algorithm」，在 §12-2 和 §12-4 之間；老師說的「12-3」可能指這一段，也可能是口誤。另外，這個播放清單最後一部是 Lec 13-2，沒有 12-3 的錄影。

---

## 5. 一頁速查表

- **隨機過程 = 描述系統裡「隨機部分」的模型**：資料、雜訊、干擾都是隨機的；機率假設已知，在這個前提下設計系統。
- **課本**：Papoulis & Pillai 4th ed.（2002），例題、習題多。
- **進度**：第 9 章 → §10-3～10-6、附錄 10A → 第 11 章 → §12-1、12-2 → §13-1、13-2。
- **關鍵預告**：$S_{yy}(\omega)=S_{xx}(\omega)\left|H(\omega)\right|^{2}$，$|H|^2=HH^{*}$ 就是分解的原型。

---

## 6. 與後續集數的連結

| 本集提到的 | 在哪幾集 |
|---|---|
| 第 9 章 General Concepts | 第 2–15 集 |
| 調變、循環平穩、取樣、雜訊、Poisson 求和公式 | 第 16–21 集 |
| 分解與創新、狀態變數、KL 展開、頻譜表示 | 第 22–29 集 |
| 遍歷性、頻譜估計 | 第 30–36 集 |
| 均方估計、預測 | 第 37–40 集 |

---

## 附：本集一句話總結

> **設計任何系統都有不確定的部分（資料、雜訊），隨機過程就是用機率去描述它們的模型；這門課用 Papoulis 第 9–13 章，從基本概念一路講到頻譜估計和均方估計。**

---

## ⚠️ 待確認清單

1. [▶ 07:50](https://youtu.be/IsQSWVbAKy0?t=470) 老師說「12-3」講 lattice structure 的頻譜估計；課本 lattice filter 在 p. 553，節號待確認；播放清單沒有這一段。
2. 上課日期：OCW 頁面和逐字稿都沒寫（影片上傳日 2017-09-20）。

---

*筆記依據陳伯寧老師「隨機過程」Lec00 錄影逐字稿（whisper large-v3-turbo，8:29）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
