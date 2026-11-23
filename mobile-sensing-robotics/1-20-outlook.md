---
course: Mobile Sensing and Robotics 1（Uni Bonn, Winter 2021/22）
episode: 1-20
lecture: Outlook – Further M.Sc. Courses from the Photogrammetry & Robotics Lab
date: 待補（2021/22 冬季學期末）
video: https://youtu.be/0AFiT7TZ_U8
notes: 沒有對應章節（課程介紹）
---

# 第 1-20 集 · 展望：實驗室的其他碩士課程（Outlook） [▶ 影片](https://youtu.be/0AFiT7TZ_U8)

← 上一集：[1-19-mdp](1-19-mdp.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[1-21-localization-overview](1-21-localization-overview.md) →

> **課程**：Mobile Sensing and Robotics 1，Uni Bonn，2021/22 冬季學期 — 第 1-20 集
> **講者**：Cyrill Stachniss
> **來源**：YouTube 錄影逐字稿（10:39，Whisper `medium.en` 轉錄）。沒有次要來源。
> **標記說明**：
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 課程總覽](#1-課程總覽)
- [2. Mobile Sensing and Robotics 2](#2-mobile-sensing-and-robotics-2)
- [3. 機器學習](#3-機器學習)
- [4. 自駕車](#4-自駕車)
- [5. 現代 C++](#5-現代-c)
- [6. 碩士專題](#6-碩士專題)
- [7. 碩士論文](#7-碩士論文)
- [8. 與本系列的連結](#8-與本系列的連結)

---

## 0. 這堂課要做什麼

MSR1 結束時的 10 分鐘介紹：Bonn 大學攝影測量與機器人實驗室（Photogrammetry and Robotics Lab）從碩士第二學期起開的其他課。沒有技術內容。

---

## 1. 課程總覽

[▶ 00:41](https://youtu.be/0AFiT7TZ_U8?t=41)

- 所有課程的資訊在實驗室網站的 teaching 頁面。大部分課程有完整的影片，可以先看去年的內容（每年可能稍有變動，但整體概念通常不變）。
- 四門講課＋一個實作專題：

| 課程 | 學期 | 對象 |
|---|---|---|
| Mobile Sensing and Robotics 2 | 第 2 學期（夏季） | 大地工程（英文碩士）學生 |
| 機器學習（針對機器人、電腦視覺、攝影測量） | 第 2 學期（夏季） | 英文、德文碩士都可 |
| 自駕車（講課＋小型研討） | 第 3 學期（冬季） | 英文、德文碩士都可 |
| 現代 C++ | 第 3 學期（冬季） | 英文、德文碩士都可 |
| 碩士專題 Mobile Sensing and Robotics | 第 2–3 學期（一年） | 所有學生 |

---

## 2. Mobile Sensing and Robotics 2

[▶ 03:07](https://youtu.be/0AFiT7TZ_U8?t=187)

- MSR1 的續集。
- **至少一半**在講 **SLAM**（同時定位與建圖）：圖式 SLAM、點雲對齊、強健最佳化、地標、位姿圖，用來解最小平方問題，建地圖並在地圖中定位。
- 第二部分：**相機資料的解讀**，例如計算影像對的**相對定向**、建立視覺幾何系統。這部分和講者在學士班、德文碩士班的攝影測量課重疊，所以德文碩士生可以上，但不算學分。
- 夏季學期，選了 mobile sensing and robotics 方向的大地工程學生必修。

（本系列的 2-xx 集就是這門課。）

---

## 3. 機器學習

[▶ 04:25](https://youtu.be/0AFiT7TZ_U8?t=265)

- 由實驗室的 Jens Behley 博士主講（`⚠️ 待確認`：Whisper 寫 “Dr. Jens Belay”）。
- 先介紹機器學習的基本技術，再進入**深度學習**：用網路解讀感測資料。
- 監督式：分類、語意分割；也講非監督式方法和最近提出的網路架構。
- 講者強烈推薦：只要想做和學習系統有關的事都該修。處理感測資料、想理解世界發生什麼時的基本能力。

---

## 4. 自駕車

[▶ 05:23](https://youtu.be/0AFiT7TZ_U8?t=323)

- 2020 年第一次開，第三學期（冬季）。
- 建立在 MSR1 之上：定位；控制部分有大量重疊，但針對汽車。
- 內容：車輛的基本控制、高層規劃、感知（理解場景）、決策、執行決策。
- 研討部分：準備並報告一兩篇最新論文（每年換新論文）。
- 程式部分：模擬系統，要自己實作自駕車的各個元件，累積實作經驗。

---

## 5. 現代 C++

[▶ 06:37](https://youtu.be/0AFiT7TZ_U8?t=397)

- 特別講 C++ 的現代發展。
- 不假設學過 C/C++，只假設有本課用的基本 Python 能力。
- 大部分由實驗室裡程式能力很強、常在業界工作過的學生教。
- 理由：真的要做線上執行、所有軟體元件整合在機器人上的系統，Python 通常不太夠。
- 講者強烈推薦給之後想做真實系統（碩士論文或畢業後）的人。
- 主要是 C++ 本身；有一個小專題，例如用**詞袋模型**（bag of words）做地點辨識，會用到一些影像函式庫。

---

## 6. 碩士專題

[▶ 08:06](https://youtu.be/0AFiT7TZ_U8?t=486)

- 第二、三學期，為期一年，開放所有學生。
- 實作一個真實世界的系統，通常兩人一組（每年可能不同）。
- 題目部分已知怎麼做、部分是探索性的研究問題。
- 約 **25%** 的學生把專題寫成論文，發表在 ICRA 等重要機器人會議。講者大力支持，讓學生在學期間就累積紮實的發表紀錄。
- 和 Heiner Kuhlmann 的團隊（通常是 Lasse Klingbeil）合作，Chris McCool 通常也參與（`⚠️ 待確認`：Whisper 寫 “Hannah Kuhlmann”）。

---

## 7. 碩士論文

[▶ 09:45](https://youtu.be/0AFiT7TZ_U8?t=585)

- 第四學期通常是碩士論文。
- 想在這個實驗室寫論文的話，講者期望你修過上面這些課：論文要建立在學過的東西上，做新的研究，目標是寫成科學論文發表。

---

## 8. 與本系列的連結

| 本集提到 | 本系列 |
|---|---|
| MSR2：SLAM、點雲對齊、強健最佳化、位姿圖 | 2-03 SLAM 入門、2-05 最小平方、2-07～2-10 ICP、2-11/12 Graph SLAM、2-14 階層式位姿圖、2-15 強健最小平方 |
| MSR2：相機、相對定向 | 2-17～2-37（特徵、RANSAC、相機參數、DLT、Zhang、P3P、對極幾何） |
| 自駕車的控制、規劃 | 1-15～1-18 |

---

## 附：本集一句話總結

> **MSR1 結束後，實驗室還開 MSR2（SLAM＋相機幾何）、機器學習、自駕車、現代 C++ 和一年的碩士專題；想在這裡寫碩士論文，最好都修過。**

---

## ⚠️ 待確認清單

1. [▶ 04:30](https://youtu.be/0AFiT7TZ_U8?t=270) 機器學習課的講者，Whisper 寫 “Dr. Jens Belay”，推測為 Jens Behley，待確認。
2. [▶ 09:22](https://youtu.be/0AFiT7TZ_U8?t=562) 碩士專題合作團隊，Whisper 寫 “Hannah Kuhlmann”，推測為 Heiner Kuhlmann，待確認。

---

*筆記依據 Cyrill Stachniss「Mobile Sensing and Robotics 1」Outlook 錄影逐字稿（Whisper `medium.en`，10:39）整理。*
