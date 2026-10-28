# 任務說明：Matrix Lie Groups 隨堂筆記

> 確認日期：2026-10-28

## 範圍

- 播放清單：<https://www.youtube.com/playlist?list=PLBY4G2o7DhF3FS2CaX62eiQWGP9_xdLYs>（25 部影片）
- 切法：**一部影片 = 一份筆記**，檔名例如 `01-L1a-複數與四元數.md`（`a` = part 1，`b` = part 2）
- 順序：先做第 1 部（Lecture 1 part 1）當樣品 → OK 才批次做

## 1. Purpose（用途）

給自己自學、複習用。看完筆記就懂這一集，不用重看影片。
老師口頭多講、課本沒有的內容，要特別標出來（`【口頭】`）。
速查表放**定理＋證明的關鍵一步**，不只是名詞。

## 2. Situation（背景）

- 講者 James Cook（James Cook Math 頻道），**英文授課**，2016 年 1–5 月錄影。筆記用**繁體中文**，術語首次出現附英文。
- 25 部影片，大多是同一堂課切成 part 1、part 2。標題寫日期不寫章節，要自己對到 Stillwell 的章節。
- 第 13 部（March 21）只有一部，沒有 part 2。
- 逐字稿用 `yt-dlp` 抓 YouTube 自動字幕，放 `_work/subs/`。
- 沒有習題課，全部是講課。
- 讀者**會線性代數＋基本群論，沒學過拓樸、微分幾何** → 遇到路徑連通、緊緻（compact）等拓樸名詞要停下來解釋。

## 3. Inputs（資料）

1. **主要**：該集逐字稿 `_work/subs/*.vtt`（YouTube 自動字幕）。字幕太爛的集數改用 Whisper 重轉，放 `_work/audio/`。筆記骨架照影片順序。
2. **次要**：課本，補定義、定理、證明、例子。標記叫 `【課本補充】`，註明是哪本。
   - 第 1–8 集：Stillwell《Naive Lie Theory》`lie-group.pdf`（PDF 頁碼 = 書頁 + 12）
   - 第 9 集起：老師改用 Brian C. Hall《Lie Groups, Lie Algebras, and Representations》第 1 版（GTM 222）`brian-hall.pdf`（PDF 頁碼 = 書頁 + 14）為主，Stillwell 為輔
3. **不用**：網路上其他筆記或文章。
4. 抓不到、查不到 → 寫「待補」，**不亂編**。
5. 逐字稿與課本不一致 → 兩邊都寫，標明出處。

## 4. Limits（不能做）

- 只寫該集講到的內容；最後一節可列「後面哪一集會用到」。
- 老師跳過的課本內容**不補**，只在該節寫一行「課本 §x.y 還有 ○○，本集沒講」。
- 不整段抄課本，用自己的話重寫；定義、公式可照用。
- 不編 `【Q&A】`：逐字稿裡真的有學生提問才寫。
- ⚠️ 待確認項：沒查清楚前不能刪。
- 數學語法照 `lecture-notes` skill 的 Typst 相容規則。
- 沒問過不 commit、不 push。

## 5. Done-when（完成條件）

- **檢查點**：先交目錄大綱（每節一行）→ 確認 OK 才寫全文。
- **每份筆記結構**：照 `lecture-notes` skill 的 `TEMPLATE.md`（frontmatter、標題＋影片連結＋上下集、開頭資訊、目錄、各節內容、速查表、與後續集數的連結、一句話總結、⚠️ 待確認清單）。
- **進度檔**：`進度.md` 與 `README.md`（總目錄）；每集做完更新狀態與待確認數。
