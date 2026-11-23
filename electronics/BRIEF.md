# 任務說明：電子學（一）～（四） 隨堂筆記

> 建立日期：2026-11-23

## 範圍

- 課：**電子學（一）～（四）**（Electronics I–IV），陽明交大 電子物理系 **陳振芳** 老師，NYCU OCW，112 學年度。
- 共 **81** 部影片，一部影片 = 一份筆記。完整清單（課、集數、影片 ID、長度、標題）在 `_work/videos.txt`。

| 資料夾 | 課 | 集數 | 老師的章 | 播放清單 |
|---|---|---|---|---|
| `E1/` | 電子學（一） | 21 | 1 基本概念、2 運算放大器 | <https://www.youtube.com/playlist?list=PLj6E8qlqmkFtaNMQgkZxZujfU8rfPx9uW> |
| `E2/` | 電子學（二） | 26 | 3 P-N 介面、4 MOSFET | <https://www.youtube.com/playlist?list=PLj6E8qlqmkFtT9IGAVdFEjI9Qf5Zg5rQN> |
| `E3/` | 電子學（三） | 22 | 5 BJT、6 信號產生與處理、7 差動放大器、8 負回授 | <https://www.youtube.com/playlist?list=PLj6E8qlqmkFv_1J7CbRzNCnFYdzuKWiMJ> |
| `E4/` | 電子學（四） | 12 | 9 放大器頻率響應、10 高功率輸出級 | 沒有完整清單，從頻道撈（見 `_work/videos.txt`） |

- **E3 的 01–10 集**是「電子學（三）─ 前導課程 113 學年度」（第 5、6 章），官方放在同一個播放清單裡，補上第 5、6 章，所以一起做。11–22 集是 112 學年度 Lec01–12。
- 集數 = 播放清單順序（E4 照 Lec 編號）。
- 檔名：`E<k>/NN-<英文主題>.md`（小寫、連字號），主題看完逐字稿再定。
- 老師的章號**不等於**課本章號。筆記標題用老師的節號（例如 1.1、2.3），課本章節另外註明。

### 老師的章 ↔ 課本（Sedra/Smith 7th ed.）

初步對照，做每集時再確認：

| 老師 | 課本 |
|---|---|
| 1 基本概念 | Ch 1 Signals and Amplifiers |
| 2 運算放大器 | Ch 2 Operational Amplifiers（部分用到 Ch 4、Ch 12） |
| 3 P-N 介面 | Ch 3 Semiconductors、Ch 4 Diodes |
| 4 MOSFET | Ch 5 MOSFETs、Ch 7 Transistor Amplifiers |
| 5 BJT | Ch 6 BJTs、Ch 7 |
| 6 信號產生與處理 | Ch 18 Signal Generators、Ch 17 Filters |
| 7 差動放大器 | Ch 9 Differential and Multistage Amplifiers、Ch 8 |
| 8 負回授 | Ch 11 Feedback |
| 9 頻率響應 | Ch 10 Frequency Response |
| 10 輸出級 | Ch 12 Output Stages and Power Amplifiers |

## 1. Purpose（用途）

給自己自學、複習用。看完筆記就懂這一集，不用重看影片。

- 老師口頭多講、課本沒有的（應用例子、經驗談），標 `【口頭】`。
- 每個重要電路：**電路圖＋它在做什麼＋怎麼推出增益或特性＋一個帶數字算到底的例子**。
- 速查表放公式＋推導的關鍵一步。

## 2. Situation（背景）

- **中文授課**，夾英文術語。筆記用繁體中文，術語第一次出現附英文。
- 逐字稿：**E1** YouTube 有**人工 zh-TW 字幕** → `_work/scripts/fetch_subs.sh` 下載到 `_work/subs/`，`_work/scripts/vtt2txt.py` 轉成帶時間點的純文字 `_work/txt/<E k>-<NN>.txt`。筆記「來源」寫「人工字幕」。**E2–E4 沒有字幕** → `fetch_audio.sh` 下載音訊到 `_work/audio/`，`whisper_loop.sh` 用 whisper large-v3-turbo 轉成 `_work/subs/*.vtt`，筆記「來源」寫「whisper」。
- 字幕（尤其 whisper）偶爾聽錯術語、符號 → 依課本修正，標 `⚠️ 逐字稿缺字`。
- 老師邊講邊畫投影片或白板，**電路圖不會被唸出來** → 從口述＋課本重建；重建不出來寫「待補」。
- 課本：Sedra & Smith《Microelectronic Circuits》7th ed.（Oxford, 2015），本資料夾的 PDF，全文抽到 `_work/book.txt`。引用一律寫**書頁**，用文字搜尋定位。
- 讀者：會微積分、基本物理（電壓、電流、電阻）；沒學過電子學。電路分析（KVL、KCL、戴維寧等效）第一次用到時講清楚。數學步驟一步一步寫。

### 電路圖

- 用 **schemdraw**（Python）畫，輸出 SVG。
- 程式：`_work/figs/<E k>-<NN>-<名稱>.py`；圖：`figures/<E k>-<NN>-<名稱>.svg`。
- 筆記裡寫 `![說明](../figures/<檔名>.svg)`。
- schemdraw 標籤**只放符號**（$R_1$、10 V…），不放中文（中文寬度算不準，會被裁掉）；中文說明寫在圖說。
- 元件方向（試過的）：BjtPnp 不要 flip（射極在上）；NFet 接在線後要 `.anchor('gate').reverse()`；JFetN 要 `.right().anchor('gate').reverse()`（閘極在左、汲極在上）；Opamp 接在 up/down 之後要加 `.right()`。
- 共用設定：`_work/figs/common.py`；預覽：`_work/figs/preview.sh <E k>-<NN>` 會把該集的圖拼成一張 PNG。
- 每張圖畫完都轉成 PNG 打開看過，確認接線和標示對了才放進筆記。
- 波形圖、波特圖用 matplotlib，一樣輸出 SVG 放 `figures/`。

## 3. Inputs（資料）

1. **主要**：該部影片逐字稿。骨架照影片順序。
2. **次要**：課本，標 `【課本補充】`，註明章節、式號或圖號與書頁（例如 §2.2.1，Eq. 2.5，p. 66）。
3. 不用網路上的其他筆記、文章。

## 4. Limits（不能做）

- 只寫該部影片講到的內容；最後一節可列「後面哪一集會用到」。
- 老師跳過的課本內容：重要的標 `【課本補充】` 補；次要的寫一行帶過。
- 不整段抄課本。
- 作業題目不做解答（課堂示範的除外）。
- 不編 `【Q&A】`。
- 數學語法照 `lecture-notes` skill 的 Typst 相容規則；不用 `\underset`、`\overset`。
- 沒問過不 commit、不 push。

## 5. Done-when（完成條件）

- 檢查點：
  1. 準備：字幕、課本文字、BRIEF、PROGRESS。
  2. 樣品：**E1 第 01 集**（1.1 電壓、電流、電阻、基本電路）先交目錄 → OK 才寫全文 → 給使用者看。
  3. 其餘批次做完，順序 E1 → E2 → E3 → E4。
- 每份筆記結構照 `lecture-notes` skill 的 `TEMPLATE.md`。
- 進度檔：`PROGRESS.md`、`README.md`（總目錄）。
- 81 份都完成 = 任務完成。
