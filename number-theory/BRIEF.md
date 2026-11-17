# 任務說明：Number Theory 隨堂筆記

> 確認日期：2026-11-17

## 範圍

- 播放清單：<https://www.youtube.com/playlist?list=PLBY4G2o7DhF2JDh2UrckBJ6MBBUJw-YVa>（26 部影片）
- **跳過** 2 部非課程影片：播放清單第 5 部「Lecture 4 the secret word is...」（15 秒）、第 26 部「HAPPY BIRTHDAY JAMES!」。實際做 **24 集**。
- 講者：播放清單頻道與內容推斷為 James Cook（Liberty University），⚠️ 待確認。學期：2021 秋（第 18 部標題有 10-13-21）。
- 切法：**一部影片 = 一份筆記**。集數 = 去掉 2 部後的順序 01–24（影片標題裡的 Lecture 編號另寫在 frontmatter 的 `lecture`）。檔名用**英文**（小寫、連字號），例如 `01-numbers-and-algebra.md`。
- 順序：先做**第 1 集**當樣品 → OK 後剩下 23 集**一次做完**再交。

| 集 | 播放清單 # | 影片 ID | 標題 |
|---|---|---|---|
| 01 | 1 | b-Irzbkw8Ok | Lecture 1: Numbers and Algebra |
| 02 | 2 | VidWfDkc2kU | Lecture 2: Induction |
| 03 | 3 | Wl3coW1Sl8Y | Lecture 3: Binomial Theorem |
| 04 | 4 | cQABm2t4Paw | Lecture 4: Divisibility and The Euclidean Algorithm |
| 05 | 6 | BDf4V_l8e3E | Lecture 5: Vector Euclidean Algorithm, Bezout, gcd, lcm, Linear Diophantine Eq. |
| 06 | 7 | 5NCjLzWh7gQ | Lecture 6: Euclid / Bezout for polynomials, rationalization tricks |
| 07 | 8 | jBbFBFjwocQ | Lecture 7: Fundamental Theorem of Arithmetic |
| 08 | 9 | QA0sz79U22s | Lecture 8: Structure of Primes |
| 09 | 10 | Y4lLt7Pchpc | Lecture 9: Irrationality of √2 |
| 10 | 11 | 743PRycdLDg | Lecture 10: Modular Arithmetic |
| 11 | 12 | neymBRqoTZ8 | Lecture 11: Modular Calculations and Integer Roots of Polynomials |
| 12 | 13 | uaqHImi8i3Y | Lecture 12: Chinese Remainder Theorem |
| 13 | 14 | TyTUi2pe2sA | Lecture 13: Fermat's Little Theorem and Polynomial Congruences |
| 14 | 15 | ouAlEMkHuyI | Lecture 14: Group of Units and Euler's Function |
| 15 | 16 | 3oq1C2sOXdU | Lecture 15: Euler's Theorem and the Structure of the Unit Group |
| 16 | 17 | NbIUZZTJq1A | Lecture 16: RSA Encryption |
| 17 | 18 | 5gAKNbqAIMM | Quadratic Reciprocity, 10-13-21 part 1 |
| 18 | 19 | 2pqaUWxNgbQ | Quadratic Reciprocity, 10-13-21 part 2 |
| 19 | 20 | 4KLw_qaQMk8 | Complex Numbers and Roots of Unity |
| 20 | 21 | Bw7o1pAhoq4 | Lecture 19: On the Solution of the Cubic Equation |
| 21 | 22 | xjNSJ8G3dug | Lecture 20: Sums of Squares and Gaussian Integers |
| 22 | 23 | JkiyK4harX0 | Lecture 21: Primes and Gaussian Integers |
| 23 | 24 | pH5yhI17fCw | Lecture 22: Quaternions |
| 24 | 25 | n1E-LOmXY-0 | Lecture 23: Fermat's Last Theorem |

## 1. Purpose（用途）

給自己自學、複習用。看完筆記就懂這一集，不用重看影片。

- 老師口頭多講、課本沒有的內容，標 `【口頭】`。
- 速查表放**定理＋證明的關鍵一步**，不只列名詞。
- 遇到演算法（輾轉相除法、擴展歐幾里得、中國剩餘定理的解法、RSA……），寫清楚：**它在解什麼、步驟、一個算到底的例子**。

## 2. Situation（背景）

- **英文授課**，線上錄影（講者對著螢幕講，有時提到作業題號）。筆記用**繁體中文**，術語第一次出現附英文。
- 逐字稿：YouTube 自動字幕，放 `_work/subs/`（檔名用播放清單編號）；轉成帶時間點的純文字放 `_work/txt/NN.txt`（NN = 播放清單編號）。
  - 播放清單第 13、21、23 部的字幕一直被 YouTube 擋（HTTP 429），改下載音訊（`_work/audio/`）用 whisper large-v3-turbo 轉錄（`_work/subs/*.whisper.vtt`）。這三集的「來源」註明 whisper。
- 課本：Gareth A. Jones & J. Mary Jones《Elementary Number Theory》（Springer, 1998），`Elementary number theory -- Gareth Jones.pdf`。**掃描檔，沒有文字層**，要用 Read 看圖。**PDF 頁碼 = 書頁 + 15**。講者在課堂上會說「我照 Jones and Jones 第幾頁」，以逐字稿說的為準。
- 讀者**會基本證明，沒學過數論** → 證明一步一步寫，不跳步；群、環、體等代數名詞第一次出現要停下來解釋。

## 3. Inputs（資料）

1. **主要**：該集逐字稿。筆記骨架照影片順序。
2. **次要**：課本 Jones & Jones，補定義、定理、證明、例子。標 `【課本補充】`，註明章節與頁碼（例如 §1.2，p. 7）。
3. **不用**：網路上其他筆記或文章、講者的 PDF 講義（沒有提供）、影片截圖。
4. 板書／螢幕上的公式字幕沒唸出 → 從口述和課本重建；重建不出來寫「待補」。
5. 抓不到、查不到 → 寫「待補」，**不亂編**。
6. 逐字稿與課本不一致 → 兩邊都寫，標明出處。

## 4. Limits（不能做）

- 只寫該集講到的內容；最後一節可列「後面哪一集會用到」。
- 老師跳過的課本內容：**重要的**（定義、主要定理、與本集主題直接相關的例子）標 `【課本補充】` 補進來；次要的只寫一行「課本 §x.y 還有 ○○，本集沒講」。
- 不整段抄課本，用自己的話重寫；定義、公式可照用。
- 作業題目**不做解答**（老師在課堂上示範的除外）。
- 不編 `【Q&A】`：逐字稿裡真的有學生提問才寫。
- ⚠️ 待確認項：沒查清楚前不能刪。
- 數學語法照 `lecture-notes` skill 的 Typst 相容規則；**不用 `\underset`、`\overset`**。
- 沒問過不 commit、不 push。

## 5. Done-when（完成條件）

- **檢查點**：第 1 集先交目錄大綱 → 確認 OK 才寫全文 → 樣品確認後，剩下 23 集一次做完再交。
- **每份筆記結構**：照 `lecture-notes` skill 的 `TEMPLATE.md`。
- **進度檔**：`PROGRESS.md` 與 `README.md`（總目錄）；每集做完更新狀態與待確認數。
- 24 集都完成 = 任務完成。
