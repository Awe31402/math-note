# 任務說明：EE274 資料壓縮 隨堂筆記

> 確認日期：2026-11-24

## 範圍

- 播放清單：<https://www.youtube.com/playlist?list=PLoROMvodv4rPj4uhbgUAaEKwNNak8xgkz>（18 部影片）
- 課程：Stanford **EE274 Data Compression: Theory and Applications**（2023 秋）。
- 講者不只一位：Tsachy Weissman、Shubham Chandak、Pulkit Tandon（全名見第 1 集投影片），第 18 集客座 Kedar Tatwawadi。**每集開頭從逐字稿確認誰在講**。
- 切法：**一部影片 = 一份筆記**，檔名用**英文**（小寫、連字號），例如 `01-course-intro-lossless-basics.md`。
- 順序：先做**第 1 集**當樣品 → OK 後剩下 17 集**一次做完**再交。

| 集 | 日期 | 影片 ID | 長度 | 主題 | 投影片 |
|---|---|---|---|---|---|
| 01 | 2023-09-27 | FF7DRogZZdY | 1:02:40 | Course Intro, Lossless Data Compression Basics | L1_part1, L1_part2(_ann) |
| 02 | 2023-10-02 | EKdlz3vae04 | 1:16:36 | Prefix Free Codes | L2_ann |
| 03 | 2023-10-04 | kbAif7XhlTI | 1:17:02 | Kraft Inequality, Entropy, Introduction to SCL | L3_ann |
| 04 | 2023-10-09 | 975qcAxZCG0 | 1:15:09 | Huffman Codes | L4_ann |
| 05 | 2023-10-11 | yeKngztLcBs | 1:20:03 | Asymptotic Equipartition Property | （無；L4_extended） |
| 06 | 2023-10-16 | L4n2u1TTkO4 | 1:17:34 | Arithmetic Coding | L6_ann |
| 07 | 2023-10-18 | 5Hp4bnvSjng | 1:20:03 | ANS | L7(_ann) |
| 08 | 2023-10-23 | tGPF2nw5Exc | 1:16:25 | Beyond IID distributions: Conditional entropy | L8 |
| 09 | 2023-10-25 | B8ucNShRwjQ | 1:19:52 | Context-based AC & LLM Compression | L9_ann |
| 10 | 2023-10-30 | amv9LiGyY5s | 1:24:38 | LZ and Universal Compression | L10(_ann) |
| 11 | 2023-11-01 | YEF0iCiQlOg | 1:24:27 | Lossy Compression Basics; Quantization | slide_11_2023(_ann) |
| 12 | 2023-11-06 | 9Fv8PlpPUCI | 1:24:50 | Mutual Information; Rate-Distortion Function | slide_12_2023 |
| 13 | 2023-11-08 | 9ZcYlFYqAhU | 1:21:23 | Gaussian RD, Water-Filling Intuition; Transform Coding | slide_13_2023(_ann) |
| 14 | 2023-11-13 | eaMrplHvxlg | 1:28:03 | Transform Coding in real-life: image, audio, etc. | L14(_ann) |
| 15 | 2023-11-15 | pMNVQIZa-G8 | 1:24:15 | Image Compression: JPEG, BPG | L15(_ann) |
| 16 | 2023-11-27 | H7dvh35xNuE | 1:21:18 | Learnt Image Compression | slide_16_2023 |
| 17 | 2023-11-29 | LE6GLWv63wc | 1:18:39 | Humans and Compression | slide_17_2023 |
| 18 | 2023-12-04 | uKnEZKpZKVA | 1:08:39 | Video Compression | L18, L18_conclusion |

## 1. Purpose（用途）

給自己自學、複習用。看完筆記就懂這一集，不用重看影片。

- 老師口頭多講、課本沒有的，標 `【口頭】`。
- 速查表放**定理、公式＋證明或推導的關鍵一步**。
- 遇到編碼法或演算法（Huffman、算術編碼、ANS、LZ77、量化、轉換編碼、JPEG…），要寫清楚：**它在解什麼問題、步驟是什麼、手算一個小例子、什麼時候不好用**。

## 2. Situation（背景）

- **英文授課**。筆記用**繁體中文**，術語第一次出現附英文。
- 每集約 1 小時–1 小時 28 分。
- 逐字稿：YouTube 人工字幕（`en-US`），原檔在 `_work/subs/`；轉成每段約 30 秒、帶時間點的純文字在 `_work/txt/NN.txt`。
- 課本：Cover & Thomas《Elements of Information Theory》2nd ed.（2006），`Wiley.Interscience.Elements.of.Information.Theory.Jul.2006.eBook-DDU.pdf`。**PDF 頁碼 = 書頁 + 26**。
- 課本大概只蓋到第 1–13 集（熵、AEP、Huffman、算術編碼、LZ、率失真）。**第 7 集 ANS、第 9 集 LLM 壓縮、第 14–18 集（JPEG、學習式壓縮、人類感知、影片）課本幾乎沒有** → 靠逐字稿＋投影片。
- 投影片：課程網站 <https://stanforddatacompressionclass.github.io/Fall23/lectures/> 下載，放在 `_work/slides/`（有 `_ann` 的是上課手寫註記版，優先看）。第 5 集沒有自己的投影片（網站只列 `L4_extended.pdf`）。第 14 集網站上兩個檔名的標籤疑似對調。上課日期也來自這一頁。
- 課堂會用 SCL（Stanford Compression Library，Python）示範。
- 讀者**會微積分、基本機率；沒學過資訊理論和壓縮**。名詞（熵、前綴碼、典型集合、互資訊…）第一次出現要停下來解釋。
- 同 repo 的 `information-theory/` 是另一門課（陳伯寧），不互相引用。

## 3. Inputs（資料）

1. **主要**：該集逐字稿。筆記骨架照影片順序。
2. **次要**：
   - 投影片 `_work/slides/`：補投影片上有、口頭沒唸的公式、表格、數字、手寫註記。標 `【投影片補充】`，註明頁碼（例如 `L1_part2_ann.pdf` p.17）。
   - 課本：補定義、定理、證明、例子。標 `【課本補充】`，註明章節（例如 §5.6）。
3. **不用**：網路上其他筆記或文章、影片截圖、EE274 課程網站的文字講義（notes）、Colab、SCL 原始碼。
4. 投影片公式字幕沒唸出 → 先查投影片，再從口述和課本重建；都查不到寫「待補」。
5. 抓不到、查不到 → 寫「待補」，**不亂編**。
6. 逐字稿、投影片、課本不一致（例如符號、定義方式、數字）→ 都寫，標明出處。

## 4. Limits（不能做）

- 只寫該集講到的內容；最後一節可列「後面哪一集會用到」。
- 老師跳過的課本內容：**重要的**標 `【課本補充】` 補進來；次要的只寫一行「課本 §x.y 還有 ○○，本集沒講」。
- 不整段抄課本，用自己的話重寫；定義、公式可照用。
- **不寫程式碼**（SCL 只描述用法）；演算法用步驟或虛擬碼說明。
- 作業、考試題目**不做解答**。
- 不編 `【Q&A】`：逐字稿裡真的有學生提問才寫。
- ⚠️ 待確認項：沒查清楚前不能刪。
- 數學語法照 `lecture-notes` skill 的 Typst 相容規則；**不用 `\underset`、`\overset`**。
- 沒問過不 commit、不 push。

## 5. Done-when（完成條件）

- **檢查點**：第 1 集先交目錄大綱 → 確認 OK 才寫全文 → 樣品確認後，剩下 17 集一次做完再交。
- **每份筆記結構**：照 `lecture-notes` skill 的 `TEMPLATE.md`；每個編碼法／演算法都有「在解什麼／步驟／小例子／什麼時候不好用」。
- **進度檔**：`PROGRESS.md` 與 `README.md`（總目錄）；每集做完更新狀態與待確認數。
- 18 集都完成 = 任務完成。
