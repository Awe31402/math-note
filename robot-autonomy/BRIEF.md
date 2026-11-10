# 任務說明：AA274A 機器人自主原理 隨堂筆記

> 草稿日期：2026-11-10（待使用者確認）

## 範圍

- 播放清單：<https://www.youtube.com/playlist?list=PLR9iNyexfIkk>（21 部影片，含 1 部 Extra Session）
- 課程：Stanford **AA274A Principles of Robotic Autonomy**（2019 秋）。講者每集開頭從逐字稿確認。
- 切法：**一部影片 = 一份筆記**，檔名用**英文**（小寫、連字號），例如 `03-trajectory-optimization.md`
- 順序：先做**第 1 集**當樣品 → OK 才批次做，每批 4–5 集

## 1. Purpose（用途）

給自己自學、複習用。看完筆記就懂這一集，不用重看影片。

- 老師口頭多講、課本沒有的內容，標 `【口頭】`。
- 速查表放**公式＋推導的關鍵一步**。
- 遇到演算法（A*、RRT、EKF、粒子濾波……），寫清楚：**在解什麼問題、步驟、什麼時候會失敗**。

## 2. Situation（背景）

- 英文授課，筆記用**繁體中文**，術語第一次出現附英文。每集約 1 小時 15 分。
- 逐字稿：**一律用 Whisper**（`medium.en`，GPU）從音檔轉。YouTube 沒有人工字幕，自動字幕又常被擋（HTTP 429），所以不用。音檔和 Whisper 輸出（`.vtt`）放 `_work/audio/`，轉成帶時間點的純文字放 `_work/txt/NN.txt`。Whisper 聽錯的字用 `⚠️ 逐字稿缺字` 標。
- 課本：《Principles of Robot Autonomy》，檔案在 `../optimal-control/optimal-control.pdf`（不複製）。**PDF 頁碼 = 書頁 + 2**。課本是新版，課程是 2019 年，內容可能有出入 → 兩邊都寫。

  | 集 | 主題 | 課本 |
  |---|---|---|
  | 1 | Overview, Mobile Robot Kinematics | 前言、§1.2–1.3 |
  | 2 | ROS | Robot Autonomy Software 章 |
  | 3 | Trajectory Optimization | 第 2 章 |
  | 4 | Trajectory Tracking | 第 3 章 |
  | 5 | Advanced Trajectory Optimization | 第 2–3 章（§2.4 微分平坦？做到時查） |
  | 6 | Motion Planning: Graph Search | §4.2–4.3 |
  | 7 | Motion Planning: Sampling-Based | §4.4–4.5 |
  | 8 | Sensors & Intro to CV | 第 5 章 |
  | 9 | Camera Models & Calibration | 第 6 章 |
  | 10 | Stereo Vision | 第 7 章 |
  | 11 | Image Processing | 第 8 章 |
  | 12 | Classic Visual Recognition | 第 8 章 |
  | 13 | Localization & Filters | 第 11 章 |
  | 14 | Parametric Filtering | 第 12 章 |
  | 15 | EKF Localization | 第 13 章 |
  | 16 | EKF SLAM | 第 14 章 |
  | 17 | Multi-Sensor Fusion | 第 15 章 |
  | 18 | Modern Computer Vision | 第 9–10 章 |
  | 19 | State Machines | 第 16 章 |
  | 20 | Decision Making Under Uncertainty | 第 17 章 |
  | 21 | Extra: Particle Filter SLAM | 第 14 章 |

- 讀者**會線性代數、微積分、基本機率；沒學過控制、機器人、電腦視覺** → 遇到專業名詞要停下來解釋。
- 與 `../optimal-control/` 重疊的主題（軌跡最佳化、LQR、DP）：可連結過去，但本課內容照本課逐字稿寫。

## 3. Inputs（資料）

1. **主要**：該集逐字稿。骨架照影片順序。
2. **次要**：課本，標 `【課本補充】`，註明章節。
3. **不用**：網路上其他筆記、別年 AA274A 講義、影片截圖。
4. 黑板／投影片公式字幕抓不到 → 從口述和課本重建；重建不出來寫「待補」。
5. 逐字稿與課本不一致 → 兩邊都寫，標明出處。

## 4. Limits（不能做）

- 只寫該集講到的；老師跳過的課本內容**不補**，只寫一行「課本 §x.y 還有 ○○，本集沒講」。
- 不整段抄課本。
- **不寫程式碼**；演算法用步驟或虛擬碼。ROS 那集只寫概念（節點、topic 等），指令列可以列但不寫程式。
- 作業、考試題目不做解答。
- 不編 `【Q&A】`。
- ⚠️ 待確認項沒查清楚不能刪。
- 數學語法照 `lecture-notes` skill 的 Typst 相容規則。
- 沒問過不 commit、不 push。

## 5. Done-when（完成條件）

- 每集先交目錄大綱 → 確認 OK 才寫全文。樣品確認後，每批 4–5 集交一次。
- 結構照 `lecture-notes` 的 `TEMPLATE.md`，演算法加「在解什麼／步驟／什麼時候會失敗」。
- 進度檔：`PROGRESS.md` 與 `README.md`；每集做完更新狀態與待確認數。
- 21 集都完成 = 任務完成。
