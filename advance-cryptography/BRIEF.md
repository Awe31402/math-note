# 任務說明：Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）隨堂筆記

> 建立：2026-11-24

## 範圍

- 播放清單：<https://www.youtube.com/playlist?list=PLUl4u3cNGP61EZllk7zwgvPbI4kbnKhWz>（17 部）
- 課程網站：<https://ocw.mit.edu/courses/6-5630-advanced-topics-in-cryptography-fall-2023/>
- 講者：Yael Tauman Kalai（MIT）。真人上課錄影，有學生提問。
- 主題：證明系統的演進：IP → 雙重有效 IP（GKR）→ PCP → 簡短論證（Kilian–Micali）→ Fiat–Shamir → BARG → SNARG。
- **17 部全做**。Lecture 1–9，大多一講切 2 段。
- 切法：**一部影片 = 一份筆記**。檔名 `<播放清單序號>-<英文主題>.md`，小寫、連字號，例如 `01-interactive-proofs-sumcheck-part1.md`。
- 順序：先做**第 01 集**當樣品 → OK 才批次做，每批 3–4 集。

| 集 | Lecture | 主題 | 次要來源 |
|---|---|---|---|
| 01–02 | L1 | Interactive Proofs and the Sum-Check Protocol | Thaler §3.1、§4.1、§4.2 |
| 03–04 | L2 | Doubly Efficient Interactive Proofs | Thaler §3.5、§4.3、§4.6；GKR「Muggles」論文 |
| 05 | L3 | GKR 續、IP = PSPACE | 無指定 |
| 06–07 | L4 | PCP via GKR、Interactive Arguments | 無指定 |
| 08–09 | L5 | Kilian–Micali Protocol | Micali「Computationally Sound Proofs」 |
| 10–11 | L6 | Fiat–Shamir、Zero-Knowledge | 無指定 |
| 12–13 | L7 | Fiat–Shamir 在標準模型的 soundness | Canetti–Lombardi–Wichs (ePrint 2018/1248) |
| 14–15 | L8 | BARGs from LWE | 無指定 |
| 16–17 | L9 | BARG ⇒ SNARG、non-signaling PCP | Choudhuri–Jain–Jin (ePrint 2021/808)；Kalai–Vaikuntanathan–Zhang (ePrint 2021/788) |

## 1. Purpose（用途）

給自己自學、複習用。看完筆記就懂這一集，不用重看影片。

- 講者口頭多講、書和論文沒有的，標 `【口頭】`。
- 遇到協定（protocol），寫清楚：**在證明什麼、每一輪誰送什麼、驗證者檢查什麼、completeness／soundness 怎麼證**。
- 速查表放**公式＋證明的關鍵一步**。

## 2. Situation（背景）

- 英文授課，筆記用**繁體中文**，術語第一次出現附英文。
- 逐字稿：**YouTube 真人字幕**（MIT 上傳的 CC，語言碼 `en-j3PyPqV-e1s`），用 `yt-dlp` 抓。`.vtt` 在 `_work/subs/`，帶時間點的純文字在 `_work/txt/<序號>.txt`。字幕把數學唸錯或寫 `[INAUDIBLE]` 的地方用 `⚠️ 逐字稿缺字` 標。
- **黑板內容看不到**：板書公式要從口述重建，重建不出來寫「待補」。
- **課本**：J. Thaler《Proofs, Arguments, and Zero-Knowledge》（2023-07 版），`_work/refs/thaler-proofs-args-zk.pdf`，簡稱 **Thaler**。**PDF 頁碼 = 書頁 + 1**（已驗：書 p.33 = PDF p.34）。有文字層。標 `【課本補充】`。
- **論文**：見上表，放 `_work/refs/`，標 `【論文補充】`並寫出是哪篇。ePrint（2018/1248、2021/808、2021/788）自動下載被擋，做到 L7、L9 時再手動下載；GKR ECCC 論文也還沒抓到。
- 讀者**會基本數學（線性代數、機率、有限體的基本概念）；沒學過複雜度理論和這門課** → NP、BPP、PSPACE 這類名詞第一次出現要解釋。先修課是 6.5620 Foundations of Cryptography，但筆記不假設讀過。
- 與 `../cryptography-notes/`（Paar 的入門密碼學）可互相連結，不當事實來源。

## 3. Inputs（資料）

1. **主要**：該集逐字稿。骨架照影片順序。
2. **次要**：Thaler 書、OCW 指定論文（照上表）。
3. **不用**：網路上其他筆記、scribe notes、講者投影片。
4. 沒有指定讀物的集數（L3、L4、L6、L8）→ 只靠逐字稿；若 Thaler 書剛好有對應章節可以用，標 `【課本補充】`並註明章節。
5. 逐字稿與書不一致 → 兩邊都寫，標明出處。

## 4. Limits（不能做）

- 只寫該集講到的；講者跳過的書上內容**不補**，只寫一行「Thaler §x.y 還有 ○○，本集沒講」。
- 不整段抄書或論文。
- **不寫程式碼**；協定用步驟寫。
- 習題（pset）不做解答。
- `【Q&A】`只寫逐字稿裡真的有的學生提問。
- ⚠️ 待確認項沒查清楚不能刪。
- 數學語法照 `lecture-notes` skill 的 Typst 相容規則。
- 沒問過不 commit、不 push。

## 5. Done-when（完成條件）

- 每集先交目錄大綱 → 確認 OK 才寫全文。樣品確認後，每批 3–4 集交一次。
- 結構照 `lecture-notes` 的 `TEMPLATE.md`。
- 進度檔：`PROGRESS.md`；每集做完更新狀態與待確認數。
- 17 部都完成 = 任務完成。
