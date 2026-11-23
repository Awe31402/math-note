# 任務說明：Mobile Sensing and Robotics 1 & 2 隨堂筆記

> 建立：2026-11-23

## 範圍

- 播放清單：
  - **MSR1**（Winter 2021/22, Uni Bonn）：<https://www.youtube.com/playlist?list=PLgnQpQtFTOGQEn33QDVGJpiZLi-SlL7vA>（21 部）
  - **MSR2**（Summer 2021, Uni Bonn）：<https://www.youtube.com/playlist?list=PLgnQpQtFTOGQh_J16IMwDlji18SWQ2PZ6>（37 部）
- 講者：主要是 Cyrill Stachniss；另有 Nived Chebrolu、Lasse Peters（照影片標題，每集開頭再從逐字稿確認）。
- **跳過**「5 Minutes with Cyrill」短片（共 21 部，內容是長片的濃縮）。其餘 37 部長片都做。
- 切法：**一部影片 = 一份筆記**。檔名 `<課>-<播放清單序號>-<英文主題>.md`，小寫、連字號，例如 `1-03-bayes-filter.md`、`2-11-graph-slam-pose-graphs.md`。序號照播放清單，跳過的短片號碼空著。
- 順序：先做 **MSR1 第 1 集**當樣品 → OK 才批次做，每批 4–5 集。

## 1. Purpose（用途）

給自己自學、複習用。看完筆記就懂這一集，不用重看影片。

- 老師口頭多講、課本沒有的內容，標 `【口頭】`。
- 速查表放**公式＋推導的關鍵一步**。
- 遇到演算法（Bayes filter、EKF、MCL、A*、ICP、RANSAC……），寫清楚：**在解什麼問題、步驟、什麼時候會失敗**。

## 2. Situation（背景）

- 英文授課，筆記用**繁體中文**，術語第一次出現附英文。
- 逐字稿：**一律用 Whisper**（`medium.en`，GPU）從音檔轉（同 `../robot-autonomy/` 的做法）。音檔和 `.vtt` 放 `_work/audio/`，帶時間點的純文字放 `_work/txt/<課>-<序號>.txt`。Whisper 聽錯的字用 `⚠️ 逐字稿缺字` 標。
- **MSR1 課本**：Thrun, Burgard, Fox《Probabilistic Robotics》**1999–2000 早期草稿版**，`ProbabilisticRobotics.pdf`。**PDF 頁碼 = 書頁 + 12**。草稿版章節和 2005 正式版不同，筆記一律寫草稿版的章節號。
- **MSR2 課本**：Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版，`Richard_Hartley_Andrew_Zisserman-Multiple_View_Geometry_in_Computer_Vision-EN.pdf`（簡稱 **MVG**）。**PDF 頁碼 = 書頁 + 18**。MVG 只管相機與多視角幾何；SLAM、ICP、特徵點書上沒有 → 那幾集只靠逐字稿（SLAM 那幾集可參考《Probabilistic Robotics》草稿版）。
- **MSR2 第二參考**：高翔、張濤《視覺 SLAM 十四講：從理論到實踐》第 2 版，`视觉SLAM十四讲从理论到实践 第2版 (高翔,张涛) (z-library.sk, 1lib.sk, z-lib.sk).pdf`（簡稱 **十四講**，簡體中文，完整 14 講＋附錄）。**PDF 頁碼 = 書頁 + 23**。這是**掃描檔、沒有文字層**，只能用 Read 看圖，不能 grep。標 `【十四講補充】`。
- **2-14 專用論文**：Grisetti, Kümmerle, Stachniss, Frese, Hertzberg〈Hierarchical Optimization on Manifolds for Online 2D and 3D Mapping〉（HOG-Man；簡稱 **HOG-Man 論文**），`grisetti2010-hogman.pdf`，6 頁。下載自 Stachniss 在 Freiburg 的個人網頁。標 `【論文補充】`。篇名和五位作者已經對過。PDF 上沒寫會議和年份，「ICRA 2010」是憑記憶寫的。
- 表中「PR」= 《Probabilistic Robotics》草稿版，「MVG」= Hartley & Zisserman，「十四講」= 高翔。

  | 集 | 主題 | 課本 |
  |---|---|---|
  | 1-01 | Course Intro | 第 1 章 |
  | 1-02 | Probability Primer | §2.2 |
  | 1-03 | Bayes Filter | §2.3–2.4 |
  | 1-05 | Occupancy Grid Maps | 第 9 章、§4.1.4 |
  | 1-06 | Robot Locomotion | §5.2（大多書上沒有） |
  | 1-07 | Motion Models | 第 5 章 |
  | 1-08 | Observation Models | 第 6 章 |
  | 1-10 | Kalman Filter & EKF | §3.2–3.3 |
  | 1-12 | EKF Localization | §7.5 |
  | 1-14 | Particle Filter & MCL | §4.2、§8.3 |
  | 1-15 | Robot Control | 無 |
  | 1-16 | MPC Part 1 | 無 |
  | 1-17 | MPC Part 2 | 無 |
  | 1-18 | Motion Planning using A* | 無 |
  | 1-19 | MDP | 第 15 章 |
  | 1-20 | Outlook（其他課程介紹） | 無 |
  | 1-21 | Robot Localization Overview | 第 7–8 章 |
  | 2-01 | Course Intro | 十四講 第 2 講（做到時查） |
  | 2-03 | Introduction to SLAM | PR 第 10 章；十四講 §2.2–2.3 |
  | 2-05 | Least Squares | MVG 附錄 5–6；十四講 第 6 講 |
  | 2-07 | ICP Part 1 | 十四講 §7.9.1（SVD 法）；MVG 附錄 4 |
  | 2-08 | ICP Part 2 | 十四講 §7.9（做到時查） |
  | 2-10 | ICP Part 3 | 十四講 §6.2、§7.9.2；MVG 附錄 6 |
  | 2-11 | Graph-based SLAM (Pose Graphs) | 十四講 §10.2；PR 第 14 章？（做到時查） |
  | 2-12 | Graph-based SLAM with Landmarks | 十四講 §9.2（BA 與圖優化、稀疏性）；MVG §18.1、附錄 6 |
  | 2-14 | Hierarchical Pose Graphs | HOG-Man 論文；十四講 §10.2（位姿圖基礎） |
  | 2-15 | Robust Least Squares | 十四講 §9.2.4（魯棒核函數）；MVG 附錄 6 §A6.8（強健代價函數；§4.7 其實是 RANSAC，留給 2-22） |
  | 2-17 | Visual Features Part 1 | 十四講 §7.1 |
  | 2-20 | Visual Features Part 2 | 十四講 §7.1.2–7.1.3（ORB、BRIEF） |
  | 2-22 | RANSAC | MVG §4.7；十四講 §7.4 末（只提一句） |
  | 2-24 | Camera Parameters | MVG 第 6 章；十四講 §5.1 |
  | 2-27 | Direct Linear Transform | MVG §4.1、第 7 章；十四講 §7.7.1 |
  | 2-29 | Zhang's Method | MVG §8.5（IAC = 本集的 B）；§8.8 是消失點法，未用 |
  | 2-31 | P3P (Grunert) | 十四講 §7.7.2 |
  | 2-33 | Relative Orientation, F & E Matrix | MVG 第 9 章；十四講 §7.3 |
  | 2-35 | Epipolar Geometry Basics | MVG §9.1；十四講 §7.3.1 |
  | 2-37 | Direct Solution for F & E | MVG 第 11 章、§9.6；十四講 §7.3.2 |

- 讀者**會線性代數、微積分、基本機率；沒學過機器人、電腦視覺、攝影測量** → 遇到專業名詞要停下來解釋。
- 與 `../robot-autonomy/`（EKF、粒子濾波、A*、相機模型）和 `../optimal-control/`（MPC）重疊：可連結過去，但本課內容照本課逐字稿寫。

## 3. Inputs（資料）

1. **主要**：該集逐字稿。骨架照影片順序。
2. **次要**：課本，標 `【課本補充】`（PR、MVG）或 `【十四講補充】`、`【論文補充】`（只限 2-14 的 HOG-Man 論文），註明章節（MSR1 用草稿版章節號）。十四講是簡體，引用時轉繁體。
3. **不用**：網路上其他筆記、Stachniss 的投影片、影片截圖。
4. 投影片公式逐字稿抓不到 → 從口述和課本重建；重建不出來寫「待補」。
5. 逐字稿與課本不一致 → 兩邊都寫，標明出處。

## 4. Limits（不能做）

- 只寫該集講到的；老師跳過的課本內容**不補**，只寫一行「課本 §x.y 還有 ○○，本集沒講」。
- 不整段抄課本。
- **不寫程式碼**；演算法用步驟或虛擬碼。
- 作業、考試題目不做解答。
- 不編 `【Q&A】`（這是錄製課，多半沒有學生提問）。
- ⚠️ 待確認項沒查清楚不能刪。
- 數學語法照 `lecture-notes` skill 的 Typst 相容規則。
- 沒問過不 commit、不 push。

## 5. Done-when（完成條件）

- 每集先交目錄大綱 → 確認 OK 才寫全文。樣品確認後，每批 4–5 集交一次。
- 結構照 `lecture-notes` 的 `TEMPLATE.md`，演算法加「在解什麼／步驟／什麼時候會失敗」。
- 進度檔：`PROGRESS.md`；每集做完更新狀態與待確認數。
- 37 部長片都完成 = 任務完成。
