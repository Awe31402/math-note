# 《Understanding Cryptography》習題解答總覽

> 規格見 `BRIEF.md`。每章一個檔案，每題格式：題目摘要 → 步驟 → 答案 → 出處（📖 課本章節 / 📝 筆記 lectureXX §）。
> ⚠️ **全部計算都是手算**：撰寫時的 session 無法執行程式。大部分題目都有交叉驗算，但仍建議用程式再驗一次（特別是下表標「建議驗算」的題目）。

| 章 | 檔案 | 題數 | 對應筆記 |
|---|---|---|---|
| 1 密碼學導論 | `chapter01_solutions.md` | 14 | L01、L02 |
| 2 串流密碼 | `chapter02_solutions.md` | 12 | L03、L04 |
| 3 DES 與替代方案 | `chapter03_solutions.md` | 13 | L05、L06 |
| 4 AES | `chapter04_solutions.md` | 17 | L07、L08 |
| 5 區塊密碼進階 | `chapter05_solutions.md` | 16 | L09、L10 |
| 6 公鑰密碼入門 | `chapter06_solutions.md` | 13 | L11、L12 |
| 7 RSA | `chapter07_solutions.md` | 16 | L12、L11 |
| 8 離散對數系統 | `chapter08_solutions.md` | 18 | L13、L14、L15、L27 |
| 9 橢圓曲線 | `chapter09_solutions.md` | 12 | L16、L17 |
| 10 數位簽章 | `chapter10_solutions.md` | 16 | L18、L19、L17 |
| 11 雜湊函數 | `chapter11_solutions.md` | 8 | L20、L21 |
| 12 MAC | `chapter12_solutions.md` | 5 | L25、L20 |
| 13 金鑰建立 | `chapter13_solutions.md` | 19 | L26、L27 |

## 沒有完成或需要注意的題目

| 題號 | 狀態 |
|---|---|
| 1.1 (1) | **待補**：密文字母的精確頻率（需要程式計數） |
| 8.12 | **待補**：$\log_{106} 12375$ in $\mathbb{Z}_{24691}$（需要執行程式） |
| 8.18 (3) | **待補 / 不確定**：數學推導確定，但解出的字母串讀不懂 |
| 7.16 | **待補**：課本圖 7.5 解析度不夠，S/SM 圖樣由 $p, q, e$ 反推 |
| 1.1、1.2、1.11、1.12、2.1 | 「作者／出處」類小題依記憶推論，**不確定** |
| 2.1 (2) | ⚠️ 推測課本打字錯誤（hausep → hauser） |
| 9.2 | ⚠️ 題目給的點不在曲線上 |
| 3.1、6.11、9.1 | ⚠️ PDF 轉文字把「≠」變成「=」 |
| 建議驗算 | 3.3–3.5、3.13（DES、PRESENT）、4.9、4.10（AES）、8.4（Z₄₉₆₉* 生成元）、7.13、13.12 |
