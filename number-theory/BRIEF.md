# 任務說明：Number Theory 隨堂筆記

> 確認日期：2026-11-19（取代 2026-11-17 的舊版，舊版在 `_old/BRIEF.md`）

## 範圍

- 播放清單：<https://www.youtube.com/playlist?list=PLBY4G2o7DhF0cSwKCx9YBFTK4mDeNx_xU>（47 部影片，全部是課程內容，不跳過）
- 講者：**James S. Cook（Liberty University）**。2026-11-19 確認：第 27 集講者說「我正在寫講義第 4 章〈Introduction to Rings and Fields〉」「這是講義的 Example 4.1.8」，跟 `../abstract-algebra/AlgebraInotes_2018.pdf`（封面署名 James S. Cook, Liberty University）的第 4 章標題、Example 4.1.8 完全一致。學期：2021 秋（每部標題有日期，8-16-21 到 12-1-21）。
- 切法：**一部影片 = 一份筆記**，共 **47 份**。集數 = 播放清單順序 01–47。檔名用**英文**（小寫、連字號），例如 `01-history-of-numbers.md`。
- 很多堂課分 part 1 / part 2：**part 2 是接著前一部講**，筆記開頭要用一兩句接上前一份。
- 標題的日期或 part 有怪的地方（見下表 ⚠️），以影片內容為準，在筆記標 ⚠️ 待確認。

| 集 | 影片 ID | 長度 | 標題（去掉開頭的 "Number Theory:"） | 檔名 |
|---|---|---|---|---|
| 01 | 16uu-IIgKT0 | 59:51 | an unfair and incomplete history of numbers, 8-16-21 | `01-history-of-numbers` |
| 02 | guJluWw1ArE | 18:52 | number systems and their properties vs. construction, 8-16-21 part 2 | `02-number-systems-properties-vs-construction` |
| 03 | qBrYneqX_vE | 59:51 | divisibility, division algorithm, Euclid's algorithm, 8-18-21 part 1 | `03-divisibility-euclid-algorithm-1` |
| 04 | T1AY0qP9Ncw | 17:13 | divisibility, division algorithm, Euclid's algorithm, 8-18-21 part 2 | `04-divisibility-euclid-algorithm-2` |
| 05 | MaqUqwpkPBM | 59:51 | vector Euclidean Algorithm, survey of prime integers, 8-23-21 part 1 | `05-vector-euclid-survey-of-primes` |
| 06 | QccYwX6LAnk | 27:54 | more prime results, Fermat Numbers, Mersenne primes, Sieve of E., 8-23-21 part 2 | `06-fermat-numbers-mersenne-primes-sieve` |
| 07 | _F8TN0rLjuc | 59:51 | modular arithmetic, 8-25-21 part 1 | `07-modular-arithmetic-1` |
| 08 | dWjxtmqki2Y | 14:37 | modular arithmetic, 8-25-21 part 2 | `08-modular-arithmetic-2` |
| 09 | gjOBOOhFo9o | 59:51 | review of groups with focus on cyclic groups, 8-31-21 part 1 | `09-review-of-groups-cyclic-groups` |
| 10 | qdbZCjSL4UM | 24:23 | order of elements, unique cyclic subgroups of Z20, 8-31-21 part 2 | `10-order-of-elements-subgroups-of-z20` |
| 11 | NMBZuUuHnVg | 48:16 | short course in cyclic groups part 2, 9-18-21 part 1 ⚠️ 8-31 到 9-18 中間沒有影片 | `11-cyclic-groups-short-course-2` |
| 12 | VFnFvZFWkSY | 55:27 | structure of U(n) and story of cyclic groups, 9-18-21 part 2 | `12-structure-of-un` |
| 13 | A3pI7AlRl0E | 59:51 | RSA encryption, quadratic diophantine, Pell's equation, 9-20-21 part 1 | `13-rsa-quadratic-diophantine-pell-1` |
| 14 | oYTGNI8GT5I | 20:19 | RSA encryption, quadratic diophantine, Pell's equation, 9-20-21 part 2 | `14-rsa-quadratic-diophantine-pell-2` |
| 15 | GUXX7Q4qpJI | 59:51 | Gaussian Integers up through division algorithm, 9-29-21 part 1 | `15-gaussian-integers-division-algorithm-1` |
| 16 | w47fBFeDmyw | 22:07 | proof of division algorithm in Gaussian Integers continued, 9-29-21 part 2 | `16-gaussian-integers-division-algorithm-2` |
| 17 | Gd9xAj5FrjA | 59:51 | Euclidean Algorithm, factoring Gaussian integers, composite vs. prime, 10-4-21 part 1 | `17-gaussian-euclid-factoring-1` |
| 18 | tQJiKBEiUpM | 19:35 | Euclidean Algorithm, factoring Gaussian integers, composite vs. prime, 10-4-21 part 2 | `18-gaussian-euclid-factoring-2` |
| 19 | TCiZSJDcOhs | 59:51 | Gaussian Integers, primes, and some applications, 10-6-21 part 1 | `19-gaussian-primes-applications-1` |
| 20 | jH9tcr7oqZc | 10:29 | Gaussian Integers, primes, and some applications, 10-6-21 part 2 | `20-gaussian-primes-applications-2` |
| 21 | Y3Y5rMriYE0 | 35:54 | this is the end … (of Gaussian Integers), 10-7-21 p1 ⚠️ 和 22 都寫 10-7 part 1 | `21-end-of-gaussian-integers` |
| 22 | AA4HgRiI-TE | 59:51 | Algebraic Integers, unique factorization fails, Eisenstein integers, 10-7-21 part 1 ⚠️ | `22-algebraic-integers-eisenstein-integers` |
| 23 | d-NiXk_5Lrw | 4:21 | on proving Fermat's Last Theorem, 10-7-21 part 3 | `23-proving-fermats-last-theorem` |
| 24 | PUh12RiezXc | 59:12 | Quaternions and their application to Number Theory, 10-11-21 | `24-quaternions` |
| 25 | 5gAKNbqAIMM | 59:51 | Quadratic Reciprocity, 10-13-21 part 1 | `25-quadratic-reciprocity-1` |
| 26 | 2pqaUWxNgbQ | 11:45 | Quadratic Reciprocity, 10-13-21 part 2 | `26-quadratic-reciprocity-2` |
| 27 | M5mrDvWtSF0 | 59:51 | rings, rngs, subrings and subrngs, basic examples, 10-18-21 part 1 | `27-rings-and-subrings-1` |
| 28 | uaPdoM88DgY | 22:06 | rings, rngs, subrings and subrngs, basic examples, 10-18-21 part 2 | `28-rings-and-subrings-2` |
| 29 | J2_uWsESIcE | 59:51 | ideals, principal ideals, factor ring, examples, 10-20-21 part 1 | `29-ideals-factor-rings` |
| 30 | Ihh0LA4rpwg | 17:13 | prime and maximal ideals introduced, 10-20-21 part 2 | `30-prime-maximal-ideals-intro` |
| 31 | dcfaKtJTPUo | 59:51 | prime and maximal ideal theorems, ring isomorphism, 10-25-21 part 1 | `31-prime-maximal-ideal-theorems-1` |
| 32 | MpcuKv4yme8 | 14:22 | prime and maximal ideal theorems, ring isomorphism, 10-25-21 part 2 | `32-prime-maximal-ideal-theorems-2` |
| 33 | zqSMBhwWN4c | 59:51 | prime subfields, field of fractions construction, 10-27-21 part 1 | `33-prime-subfields-field-of-fractions-1` |
| 34 | 1uoSyglHXTM | 12:00 | prime subfields, field of fractions construction, 10-27-21 part 2 | `34-prime-subfields-field-of-fractions-2` |
| 35 | UvyX3w-swSk | 1:17:28 | polynomial construction, evaluation homomorphism, factor theorem, 11-1-21 | `35-polynomial-rings-factor-theorem` |
| 36 | M9GwrboiER0 | 59:51 | PIDs, factorization, Eisenstein, 11-3-21 part 1 | `36-pids-factorization-eisenstein-1` |
| 37 | RO9oZWQILrY | 17:40 | PIDs, factorization, Eisenstein, 11-3-21 part 2 | `37-pids-factorization-eisenstein-2` |
| 38 | NtLY8zphbb4 | 59:51 | PIDs, Euclidean Domains, and UFDs, quick overview, 11-8-21 part 1 | `38-pids-euclidean-domains-ufds-1` |
| 39 | uqJKPJkNJks | 32:37 | PIDs, Euclidean Domains, and UFDs, quick overview, 11-8-21 part 2 | `39-pids-euclidean-domains-ufds-2` |
| 40 | edCfHBhMyz4 | 59:51 | extension fields, fundamental theorem of field extensions, 11-10-21 part 2 ⚠️ 應是 part 1 | `40-extension-fields-1` |
| 41 | Rh0Q54CQNxg | 17:35 | extension fields, fundamental theorem of field extensions, 11-10-21 part 2 | `41-extension-fields-2` |
| 42 | kNYaxKcq8YY | 59:51 | the irreducible polynomial and degree of a number, simple extensions, 11-15-21 part 1 | `42-irreducible-polynomial-simple-extensions-1` |
| 43 | Yj0aLQVsROk | 23:44 | the irreducible polynomial and degree of a number, simple extensions, 11-15-21 part 2 | `43-irreducible-polynomial-simple-extensions-2` |
| 44 | nOfJamAwAn0 | 59:51 | algebraic extensions and degree considerations, 11-17-21 part 1 | `44-algebraic-extensions-degree-1` |
| 45 | y7Pv0GBJor0 | 20:08 | algebraic extensions and degree considerations, 11-17-21 part 2 | `45-algebraic-extensions-degree-2` |
| 46 | JbU-Ulsjcp8 | 59:51 | ideals fix numbers, 12-1-21 part 1 | `46-ideals-fix-numbers-1` |
| 47 | b8ygAt9n4nY | 16:41 | ideals fix numbers, 12-1-21 part 2 | `47-ideals-fix-numbers-2` |

## 1. Purpose（用途）

給自己自學、複習用。看完筆記就懂這一集，不用重看影片。

- 老師口頭多講、課本沒有的內容，標 `【口頭】`。
- 速查表放**定理＋證明的關鍵一步**，不只列名詞。
- 遇到演算法（輾轉相除法、擴展歐幾里得、中國剩餘定理的解法、RSA……），寫清楚：**它在解什麼、步驟、一個算到底的例子**。
- 抽象代數名詞（群、環、理想、商環、體擴張……）第一次出現時，**停下來用例子講清楚**。

## 2. Situation（背景）

- **英文授課**，線上錄影（講者對著螢幕講）。筆記用**繁體中文**，術語第一次出現附英文。
- 逐字稿：YouTube 自動字幕，放 `_work/subs/`（檔名 `NN-影片ID`，NN = 播放清單編號）；轉成帶時間點的純文字放 `_work/txt/NN.txt`。
  - 字幕被 YouTube 擋（HTTP 429）的 → 下載音訊到 `_work/audio/`，用 whisper large-v3-turbo 轉錄（`_work/subs/*.whisper.vtt`），筆記的「來源」註明 whisper。
- 課本：Gareth A. Jones & J. Mary Jones《Elementary Number Theory》（Springer, 1998），`Elementary number theory -- Gareth Jones.pdf`。**掃描檔，沒有文字層**，要用 Read 看圖。**PDF 頁碼 = 書頁 + 15**。
- 讀者**會基本證明，沒學過數論，也沒學過抽象代數** → 證明一步一步寫，不跳步。
- 舊版筆記（另一套錄影，24 集）在 `_old/`。新的第 25、26 部 = 舊的第 17、18 集（同一支影片）。

## 3. Inputs（資料）

1. **主要**：該部影片逐字稿。筆記骨架照影片順序。
2. **次要**：課本 Jones & Jones，補定義、定理、證明、例子。標 `【課本補充】`，註明章節與頁碼（例如 §1.2，p. 7）。
3. **可以重用**：`_old/17-quadratic-reciprocity-1.md`、`_old/18-quadratic-reciprocity-2.md`（同一支影片），改成新編號、新格式。
4. **不用**：其他舊筆記（影片不同，不能混）、網路上其他筆記或文章、影片截圖。
5. 講者實際用的書（2026-11-19 從逐字稿查到）：
   - 前半主要用 **Stillwell《Elements of Number Theory》**（第 01 集說的），二次互反律部分參考 Jones & Jones（第 25 集）。
   - 第 27–47 部用講者**自己的講義**，講義照 **Gallian《Contemporary Abstract Algebra》** 寫，也參考 Fraleigh。
   - **決定（2026-11-19）**：Stillwell 不另外找，**次要來源照用 Jones & Jones**。講者說「Stillwell 第幾章」時照寫進筆記（標 `【口頭】`），但不去查、不從記憶補 Stillwell 的內容。
   - Jones & Jones **沒有**環、理想、體擴張。**決定（2026-11-19）**，第 27–47 部的資料順序：
     1. 主要：逐字稿。
     2. 次要：**講者自己的講義** `../abstract-algebra/AlgebraInotes_2018.pdf` 第 4 章（Lecture 21–30：環、理想、商環、質理想與極大理想、環同態、分式體、多項式、分解、整環的整除、體擴張、代數擴張）。PDF 頁碼 = 講義頁碼。標 `【講義補充】`，註明編號與頁碼（例如 Example 4.1.8，p. 123）。講者 2021 年說「正在寫」，2018 版可能跟他課堂上的版本有出入，不一致時兩邊都寫。
     3. 再次要：Gallian《Contemporary Abstract Algebra》`../abstract-algebra/Contemporary Abstract Algebra (Joseph A. Gallian) (z-library.sk, 1lib.sk, z-lib.sk).pdf`，補例子。標 `【Gallian 補充】`。
     - 不用 `../abstract-algebra/` 裡的其他筆記（別門課的筆記）。
6. 板書／螢幕上的公式沒唸出 → 從口述和課本重建；重建不出來寫「待補」。
7. 抓不到、查不到 → 寫「待補」，**不亂編**。逐字稿與課本不一致 → 兩邊都寫，標明出處。

## 4. Limits（不能做）

- 只寫該部影片講到的內容；最後一節可列「後面哪一集會用到」。
- 老師跳過的課本內容：**重要的**（定義、主要定理、與本集主題直接相關的例子）標 `【課本補充】` 補進來；次要的只寫一行「課本 §x.y 還有 ○○，本集沒講」。
- 不整段抄課本，用自己的話重寫；定義、公式可照用。
- 作業題目**不做解答**（老師在課堂上示範的除外）。
- 不編 `【Q&A】`：逐字稿裡真的有學生提問才寫。
- ⚠️ 待確認項：沒查清楚前不能刪。
- 數學語法照 `lecture-notes` skill 的 Typst 相容規則；**不用 `\underset`、`\overset`**。
- `_old/` 裡的東西不刪。
- 沒問過不 commit、不 push。

## 5. Done-when（完成條件）

- **檢查點**：
  1. 準備：舊檔搬到 `_old/`、47 部逐字稿抓好、新 BRIEF / README / PROGRESS → 給使用者看，回報第 27–47 部講者用的書。
  2. 樣品：第 1 集先交目錄大綱 → 確認 OK 才寫全文 → 給使用者看。
  3. 前半 02–26 一次做完 → 給使用者看。
  4. 後半 27–47：等使用者決定要不要提供那本書，再一次做完。
- **每份筆記結構**：照 `lecture-notes` skill 的 `TEMPLATE.md`。
- **進度檔**：`PROGRESS.md` 與 `README.md`（總目錄）；每集做完更新狀態與待確認數。
- 47 集都完成 = 任務完成。
