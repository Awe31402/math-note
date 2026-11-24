# 任務說明：3D Computer Vision（NUS CS4277/CS5477）隨堂筆記

> 建立：2026-11-24

## 範圍

- 播放清單：<https://www.youtube.com/playlist?list=PLxg0CGqViygP47ERvqHw_v7FVnUovJeaz>（39 部）
- 講者：Gim Hee Lee（National University of Singapore）。COVID-19 期間錄的線上課。
- **39 部全做**。01–37 是 Lecture 1–12（每講切 2–4 段）。38（3D Point Cloud Processing）、39（Neural Field Representations）放最後做。
- 切法：**一部影片 = 一份筆記**。檔名 `<播放清單序號>-<英文主題>.md`，小寫、連字號，例如 `01-projective-geometry-2d-part1.md`。序號兩位數，照播放清單。
- 順序：先做**第 01 集**當樣品 → OK 才批次做，每批 4–5 集。

## 1. Purpose（用途）

給自己自學、複習用。看完筆記就懂這一集，不用重看影片。

- 老師口頭多講、課本沒有的內容，標 `【口頭】`。
- 速查表放**公式＋推導的關鍵一步**。
- 遇到演算法（DLT、RANSAC、8 點法、bundle adjustment……），寫清楚：**在解什麼問題、步驟、什麼時候會失敗**。
- 遇到抽象幾何概念（無窮遠點、circular points、absolute conic……），多寫一句「直覺上是什麼」。

## 2. Situation（背景）

- 英文授課，筆記用**繁體中文**，術語第一次出現附英文。
- 逐字稿：**一律用 Whisper**（`medium.en`，GPU）從音檔轉（同 `../mobile-sensing-robotics/` 的做法）。音檔和 `.vtt` 放 `_work/audio/`，帶時間點的純文字放 `_work/txt/<序號>.txt`。Whisper 聽錯的字（講者口音）用 `⚠️ 逐字稿缺字` 標。
- **課本**：Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版，`Richard_Hartley_Andrew_Zisserman-Multiple_View_Geometry_in_Computer_Vision-EN.pdf`（簡稱 **MVG**）。**PDF 頁碼 = 書頁 + 18**（已驗：書 p.25 = PDF p.43）。有文字層，可以 `pdftotext` 搜尋。
- 對照表（章節是大概的，細節做到時查）：

  | 集 | 主題 | MVG |
  |---|---|---|
  | 01–02 | 2D and 1D projective geometry | 第 2 章 |
  | 03–04 | Rigid body motion and 3D projective geometry | 第 3 章（剛體運動書上不多） |
  | 05–07 | Circular points and Absolute conic | §2.7、§3.6、§8.5 |
  | 08–09 | Robust homography estimation | 第 4 章（DLT、RANSAC） |
  | 10–12 | Camera models and calibration | 第 6、7 章 |
  | 13–15 | Single view metrology | 第 8 章 |
  | 16–19 | The fundamental and essential matrices | 第 9、11 章 |
  | 20–22 | Absolute pose estimation from points or lines | 第 7 章；大多書上沒有 |
  | 23–26 | Three-view geometry from points and/or lines | 第 15、16 章 |
  | 27–30 | Structure-from-Motion and bundle adjustment | 第 10、12、18 章、附錄 6 |
  | 31–34 | Two-view and multi-view stereo | 大多書上沒有 |
  | 35–37 | Generalized cameras | 無 |
  | 38 | 3D Point Cloud Processing | 無 |
  | 39 | Neural Field Representations | 無 |

- 讀者**會線性代數、微積分；沒學過電腦視覺** → 遇到專業名詞要停下來解釋。
- 與 `../mobile-sensing-robotics/` MSR2（DLT、RANSAC、Zhang's method、P3P、F/E 矩陣）重疊：可連結過去，但本課內容照本課逐字稿寫。

## 3. Inputs（資料）

1. **主要**：該集逐字稿。骨架照影片順序。
2. **次要**：MVG，標 `【課本補充】`，註明章節。
3. **可連結、不當事實來源**：`../mobile-sensing-robotics/` 的筆記。
4. **不用**：網路上其他筆記、講者投影片、影片截圖。
5. 投影片公式逐字稿抓不到 → 從口述和課本重建；重建不出來寫「待補」。
6. 逐字稿與課本不一致 → 兩邊都寫，標明出處。
7. 書上沒有的集數（31–39 大部分）→ 只靠逐字稿。

## 4. Limits（不能做）

- 只寫該集講到的；老師跳過的課本內容**不補**，只寫一行「課本 §x.y 還有 ○○，本集沒講」。
- 不整段抄課本。
- **不寫程式碼**；演算法用步驟或虛擬碼。
- 作業、考試題目不做解答。
- 不編 `【Q&A】`（錄製課，多半沒有學生提問）。
- ⚠️ 待確認項沒查清楚不能刪。
- 數學語法照 `lecture-notes` skill 的 Typst 相容規則。
- 沒問過不 commit、不 push。

## 5. Done-when（完成條件）

- 每集先交目錄大綱 → 確認 OK 才寫全文。樣品確認後，每批 4–5 集交一次。
- 結構照 `lecture-notes` 的 `TEMPLATE.md`，演算法加「在解什麼／步驟／什麼時候會失敗」。
- 進度檔：`PROGRESS.md`；每集做完更新狀態與待確認數。
- 39 部都完成 = 任務完成。
