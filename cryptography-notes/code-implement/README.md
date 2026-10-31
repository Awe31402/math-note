# DES & AES C++ 實作指南與 Lecture Notes 理論對照文件

本專案於 `code-implement/` 中完整實作了**資料加密標準（Data Encryption Standard, DES）**與**進階加密標準（Advanced Encryption Standard, AES-128/192/256）**的加密與解密演算法，並提供 **ECB（電子密碼本）** 與 **CBC（密碼區塊鏈）** 兩種分組密碼操作模式及 **PKCS#7** 填補標準。

本實作深入參考並對照：
1. **參考教科書**：*Practical Cryptography Algorithms and Implementations Using C++*（Azad S., Khan P. Al-Sakib 編著，CRC Press），特別是 Chapter 4（Block Cipher）、Chapter 5（DES）與 Chapter 6（AES）。
2. **課程筆記**：Christof Paar 教授之 *Introduction to Cryptography* 系列講義筆記：
   - `lecture05_note.md`：資料加密標準 DES —— 加密
   - `lecture06_note.md`：DES —— 金鑰排程與解密
   - `lecture07_note.md`：AES 需要的伽羅瓦體（Galois Fields $\text{GF}(2^8)$）
   - `lecture08_note.md`：進階加密標準 AES
   - `lecture09_note.md`：區塊密碼的操作模式（Modes of Operation）

---

## 目錄

- [1. 專案架構與檔案清單](#1-專案架構與檔案清單)
- [2. 編譯與執行方法](#2-編譯與執行方法)
- [3. DES 演算法實作與 Lecture Notes 對照](#3-des-演算法實作與-lecture-notes-對照)
  - [3.1 最外層參數與結構](#31-最外層參數與結構)
  - [3.2 Feistel 網路與可逆性原理（對照 Lecture 05 & 06）](#32-feistel-網路與可逆性原理對照-lecture-05--06)
  - [3.3 輪函數 $f$ 內部四部曲（對照 Lecture 05）](#33-輪函數-f-內部四部曲對照-lecture-05)
  - [3.4 金鑰排程 Key Schedule（對照 Lecture 06）](#34-金鑰排程-key-schedule對照-lecture-06)
  - [3.5 DES 解密原理與逆向金鑰（對照 Lecture 06）](#35-des-解密原理與逆向金鑰對照-lecture-06)
- [4. AES 演算法實作與 Lecture Notes 對照](#4-aes-演算法實作與-lecture-notes-對照)
  - [4.1 有限體 $\text{GF}(2^8)$ 算術（對照 Lecture 07）](#41-有限體-textgf28-算術對照-lecture-07)
  - [4.2 SPN 結構 vs Feistel 結構（對照 Lecture 08）](#42-spn-結構-vs-feistel-結構對照-lecture-08)
  - [4.3 AES 四大輪運算層（對照 Lecture 08）](#43-aes-四大輪運算層對照-lecture-08)
  - [4.4 AES S-Box 數學建構與動態驗證（對照 Lecture 07 & 08）](#44-aes-s-box-數學建構與動態驗證對照-lecture-07--08)
  - [4.5 金鑰擴展 Key Expansion（對照 Lecture 08）](#45-金鑰擴展-key-expansion對照-lecture-08)
  - [4.6 AES 嚴格逆向解密流程（對照 Lecture 08）](#46-aes-嚴格逆向解密流程對照-lecture-08)
- [5. 操作模式與填補機制（對照 Lecture 09）](#5-操作模式與填補機制對照-lecture-09)
  - [5.1 ECB 模式的局限與資訊洩漏](#51-ecb-模式的局限與資訊洩漏)
  - [5.2 CBC 模式與初始化向量 IV](#52-cbc-模式與初始化向量-iv)
  - [5.3 PKCS#7 填補標準](#53-pkcs7-填補標準)
- [6. 與教科書《Practical Cryptography》之實作對照與錯誤修正](#6-與教科書practical-cryptography之實作對照與錯誤修正)
  - [6.1 DES 實作之對照與缺陷改進](#61-des-實作之對照與缺陷改進)
  - [6.2 AES 實作之對照與缺陷改進](#62-aes-實作之對照與缺陷改進)
- [7. 標準測試向量（KAT）與實驗驗證數據](#7-標準測試向量kat與實驗驗證數據)
  - [7.1 NIST FIPS 測試向量 Known Answer Tests](#71-nist-fips-測試向量-known-answer-tests)
  - [7.2 雪崩效應（Avalanche Effect）實測分析](#72-雪崩效應avalanche-effect實測分析)

---

## 1. 專案架構與檔案清單

```
code-implement/
├── include/
│   ├── BlockCipher.hpp   // 通用密碼常數、十六進制轉碼、PKCS#7 填補、ECB/CBC 模式介面
│   ├── GF256.hpp         // GF(2^8) 有限體算術模組（xtime、多項式乘法、Log/Alog 生成表、S-Box 數學求值）
│   ├── DES.hpp           // DES 密碼類別定義（NIST FIPS 46-3，支援 64-bit 區塊、字串加解密、單輪追蹤）
│   └── AES.hpp           // AES 密碼類別定義（NIST FIPS 197，支援 128/192/256-bit 金鑰、單輪追蹤）
├── src/
│   ├── BlockCipher.cpp   // 十六進制處理、PKCS#7 填補/移除、矩陣除錯輸出實作
│   ├── GF256.cpp         // GF(2^8) 核心運算、仿射轉換（Affine Transform）、教科書 Log/Alog 表
│   ├── DES.cpp           // DES IP/FP、16 輪 Feistel 函數、S-box 查表、金鑰排程、ECB/CBC
│   ├── AES.cpp           // AES SubBytes、ShiftRows、MixColumns、KeyExpansion、InvCipher、ECB/CBC
│   └── main.cpp          // 完整展示與驗證程式（NIST KAT 測試、雪崩效應驗證、模式比對、單步追蹤）
├── Makefile              // 自動化建置腳本（支援 make, make test, make trace, make clean）
└── README.md             // 本詳細實作手冊與理論對照說明文件
```

---

## 2. 編譯與執行方法

本專案使用標準 C++17 語法，依賴 GCC 或 Clang，無外部第三方密碼學函式庫相依性。

### 編譯專案
```bash
cd code-implement
make
```
這將編譯出可執行檔 `crypto_demo`。

### 執行全自動測試（KAT 測試、雪崩效應、ECB/CBC 對比、有限體驗證）
```bash
make test
# 或直接執行
./crypto_demo
```

### 執行單輪逐步追蹤（查看 Feistel 與 SPN 各輪中間狀態）
```bash
make trace
# 或直接執行
./crypto_demo --trace
```

### 清理編譯產物
```bash
make clean
```

---

## 3. DES 演算法實作與 Lecture Notes 對照

### 3.1 最外層參數與結構

對照 **`lecture05_note.md` §2「DES 從最外層看」**：
- **區塊大小（Block Size）**：64 bits（8 bytes）。
- **金鑰長度（Key Length）**：64 bits 輸入，但其中每第 8 位元為奇偶校驗位（Parity Bits），有效金鑰長度為 **56 bits**。
- **輪數（Rounds）**：16 輪 Feistel 迭代。

在 C++ 類別中，我們定義：
```cpp
class DES {
public:
    static constexpr size_t BLOCK_SIZE = 8;
    static constexpr size_t KEY_SIZE   = 8;
    static constexpr size_t NUM_ROUNDS = 16;
...
```

---

### 3.2 Feistel 網路與可逆性原理（對照 Lecture 05 & 06）

對照 **`lecture05_note.md` §4「Feistel 網路」** 與 **`lecture06_note.md` §2「DES 解密」**：
1. **半塊加密**：在每一輪中，64-bit 資料被切分為左半部 $L_i$（32 bit）與右半部 $R_i$（32 bit）。
2. **狀態轉移方程式**：
   $$L_i = R_{i-1}$$
   $$R_i = L_{i-1} \oplus f(R_{i-1}, K_i)$$
3. **為什麼 $f$ 函數不需要可逆？**
   在解密時，給定 $(L_i, R_i)$：
   - 由於 $L_i = R_{i-1}$，解密方直接獲得了上一輪的右半邊 $R_{i-1}$。
   - 接著解密方可以直接計算 $f(R_{i-1}, K_i) = f(L_i, K_i)$。
   - 透過 XOR 的自我抵消性質（$A \oplus B \oplus B = A$）：
     $$L_{i-1} = R_i \oplus f(R_{i-1}, K_i) = R_i \oplus f(L_i, K_i)$$
   - 因此，**不論輪函數 $f$ 多麼不可逆（包含單向雜湊或非線性壓損），整個密碼結構依然 100% 可逆！**

在 `src/DES.cpp` 中的實作代碼完全呼應此數學原理：
```cpp
// 16 輪 Feistel 網路迭代
for (size_t i = 0; i < NUM_ROUNDS; ++i) {
    uint32_t f_res = roundFunctionF(r, subkeys_[i]);
    uint32_t next_l = r;
    uint32_t next_r = l ^ f_res;
    l = next_l;
    r = next_r;
}
// 第 16 輪結束後進行 Pre-output 左右互換 (R16, L16)，再送入逆初始置換 FP
uint64_t rl = (static_cast<uint64_t>(r) << 32) | l;
uint64_t cipher = finalPermutation(rl);
```

---

### 3.3 輪函數 $f$ 內部四部曲（對照 Lecture 05）

對照 **`lecture05_note.md` §5「DES 的內部」**，輪函數 $f(R_{i-1}, K_i)$ 包含四個核心步驟：
1. **擴展置換 $E$（Expansion Permutation, §5.3）**：
   - 將 32 bits 的 $R_{i-1}$ 依據擴展表擴展為 48 bits。
   - 32 位元被切為 8 個 4 位元塊，每個塊的左右邊界位元與相鄰塊重疊，擴展為 6 位元。
2. **XOR 子金鑰（§5.4）**：
   - 48 bits 的擴展結果與該輪的 48-bit 子金鑰 $K_i$ 進行位元 XOR：$E(R_{i-1}) \oplus K_i$。
3. **S-Box 代換（§5.5，Shannon 的混淆 Confusion）**：
   - 這是 DES **唯一的非線性核心**！
   - 48 位元被分為 8 組，每組 6 位元，分別輸入 8 個相異的 S-Box（$S_1 \sim S_8$）。
   - 尋址規則：設 6 位元為 $b_1 b_2 b_3 b_4 b_5 b_6$：
     - **列（Row）**：由外側兩位決定 $\text{Row} = (b_1 \ll 1) \mid b_6 \in \{0, 1, 2, 3\}$。
     - **行（Column）**：由中間四位決定 $\text{Col} = (b_2 \ll 3) \mid (b_3 \ll 2) \mid (b_4 \ll 1) \mid b_5 \in \{0, \dots, 15\}$。
     - 每個 S-Box 輸出 4 bits，8 個 S-Box 共產生 32 bits。
4. **置換 $P$（§5.6，Shannon 的擴散 Diffusion）**：
   - 將 S-Box 輸出的 32 bits 重新排列，打散輸出到位元組的不同位置，確保下一輪擴展時能迅速影響到不同的 S-Box。

在 `src/DES.cpp` 中的實作：
```cpp
uint32_t DES::roundFunctionF(uint32_t r32, uint64_t subkey) {
    uint64_t expanded = expansion(r32);          // 1. 擴展 E: 32 -> 48 bits
    uint64_t xorKey = expanded ^ subkey;         // 2. XOR 子金鑰: 48 bits
    uint32_t substituted = substitution(xorKey); // 3. 8 個 S-Box 代換: 48 -> 32 bits
    return permutationP(substituted);            // 4. 置換 P: 32 -> 32 bits
}
```

---

### 3.4 金鑰排程 Key Schedule（對照 Lecture 06）

對照 **`lecture06_note.md` §1「金鑰排程」**：
1. **$PC\text{-}1$ 置換（§1.2）**：
   - 64-bit 原始金鑰中，捨棄第 8, 16, 24, 32, 40, 48, 56, 64 位（Parity Bits），剩餘 56 bits。
   - 將其拆分為 $C_0$（高 28 bits）與 $D_0$（低 28 bits）。
2. **左旋移位 $LS_i$（§1.3）**：
   - 每一輪對 $C$ 與 $D$ 分別進行獨立的循環左移：
   - **第 1, 2, 9, 16 輪**：左移 1 bit。
   - **其餘輪次**：左移 2 bits。
   - 總移位數：$4 \times 1 + 12 \times 2 = 28$ 位元！剛好轉一整圈，使得 $C_{16} = C_0, D_{16} = D_0$。
3. **$PC\text{-}2$ 壓縮置換（§1.5）**：
   - 每輪移位後的 56 bits $(C_i, D_i)$，透過 $PC\text{-}2$ 表選出 48 bits，作為該輪子金鑰 $K_i$。

在 `src/DES.cpp` 中的實作：
```cpp
void DES::keygen(uint64_t key64) {
    uint64_t pc1 = permute(key64, PC1_TABLE, 64, 56);
    uint32_t c = (pc1 >> 28) & 0x0FFFFFFF;
    uint32_t d = pc1 & 0x0FFFFFFF;

    for (size_t r = 0; r < NUM_ROUNDS; ++r) {
        int shift = SHIFT_SCHEDULE[r];
        // 28-bit 循環左移
        c = ((c << shift) | (c >> (28 - shift))) & 0x0FFFFFFF;
        d = ((d << shift) | (d >> (28 - shift))) & 0x0FFFFFFF;
        uint64_t cd = (static_cast<uint64_t>(c) << 28) | d;
        subkeys_[r] = permute(cd, PC2_TABLE, 56, 48);
    }
}
```

---

### 3.5 DES 解密原理與逆向金鑰（對照 Lecture 06）

對照 **`lecture06_note.md` §2.2「解密 = 加密，只是金鑰順序反過來」**：
- 解密時的流程與加密完全一致，唯一差別是子金鑰的使用次序為 $K_{16}, K_{15}, \dots, K_1$。
- 程式碼中：
```cpp
// 解密輪次使用逆序子金鑰：subkeys_[15] down to subkeys_[0]
for (int i = static_cast<int>(NUM_ROUNDS) - 1; i >= 0; --i) {
    uint32_t f_res = roundFunctionF(r, subkeys_[i]);
    uint32_t next_l = r;
    uint32_t next_r = l ^ f_res;
    l = next_l;
    r = next_r;
}
```

---

## 4. AES 演算法實作與 Lecture Notes 對照

### 4.1 有限體 $\text{GF}(2^8)$ 算術（對照 Lecture 07）

對照 **`lecture07_note.md`**：
1. **多項式表示法**：AES 中的每個 byte 均被視為係數在 $\text{GF}(2) = \{0, 1\}$ 上的 7 次多項式：
   $$b_7 x^7 + b_6 x^6 + \dots + b_1 x + b_0$$
2. **不可約多項式**：AES 選定之質多項式為：
   $$P(x) = x^8 + x^4 + x^3 + x + 1 \quad (\text{0x11B})$$
3. **加法**：多項式係數相加模 2，等價於**位元 XOR**。
4. **乘法與 `xtime` 運算（§4.3）**：
   - 乘以 $x$（二進制 `0x02`）：左移 1 位元。若最高位（$b_7$）為 1，則減去 $P(x)$（即 XOR `0x1B`）。
   ```cpp
   uint8_t GF256::xtime(uint8_t a) {
       return (a & 0x80) ? static_cast<uint8_t>((a << 1) ^ 0x1B) : static_cast<uint8_t>(a << 1);
   }
   ```
   - 任意多項式乘法：透過條件位移與 XOR 相加。
   - 生成元乘法（Log/Alog Table）：利用 $\text{GF}(2^8)^\times$ 的生成元 $g = x + 1$（`0x03`）建立對數表，透過指數加法模 255 計算乘積。本專案在 `GF256.cpp` 中完整實作這兩種演算法，並於單元測試中證明兩者精確相等！

---

### 4.2 SPN 結構 vs Feistel 結構（對照 Lecture 08）

對照 **`lecture08_note.md` §2.1「不是 Feistel 網路」**：

| 特性 | DES | AES |
|---|---|---|
| **基本架構** | Feistel 網路 | 代換-置換網路（SPN, Substitution-Permutation Network） |
| **每輪處理資料** | 僅加密一半（32 bits） | **全狀態同時加密（128 bits）** |
| **資料路徑狀態** | 64-bit 向量 | $4 \times 4$ Byte 狀態矩陣（Column-Major） |
| **輪函數可逆性** | $f$ 函數不需要可逆 | **每一層運算都必須有嚴格的數學逆運算** |
| **加解密對稱性** | 同一套電路，金鑰反序 | **解密必須使用各層的逆運算（InvSubBytes、InvMixColumns 等）** |

本實作的狀態矩陣映射方式符合 FIPS 197 標準（行主序/Column-major）：
```cpp
// 16-byte 輸入陣列映射為 4x4 State: state[row][col] = in[row + 4 * col]
for (int c = 0; c < 4; ++c) {
    for (int r = 0; r < 4; ++r) {
        state[r][c] = in[r + 4 * c];
    }
}
```

---

### 4.3 AES 四大輪運算層（對照 Lecture 08）

對照 **`lecture08_note.md` §2.2～§7**，AES 每輪包含四個步驟：

1. **`SubBytes`（位元組代換層，§4，Shannon 的混淆）**：
   - 狀態矩陣中每個 byte 獨立透過 Rijndael S-Box 進行非線性替換。
2. **`ShiftRows`（行移位層，§5，Shannon 的擴散）**：
   - Row 0：不移位。
   - Row 1：循環左移 1 byte。
   - Row 2：循環左移 2 bytes。
   - Row 3：循環左移 3 bytes。
3. **`MixColumns`（列混合層，§6，Shannon 的擴散）**：
   - 狀態矩陣的每一 column 與固定 MDS 矩陣在 $\text{GF}(2^8)$ 上相乘：
     $$
     \begin{bmatrix} s'_{0,c} \\ s'_{1,c} \\ s'_{2,c} \\ s'_{3,c} \end{bmatrix} =
     \begin{bmatrix} 02 & 03 & 01 & 01 \\ 01 & 02 & 03 & 01 \\ 01 & 01 & 02 & 03 \\ 03 & 01 & 01 & 02 \end{bmatrix}
     \begin{bmatrix} s_{0,c} \\ s_{1,c} \\ s_{2,c} \\ s_{3,c} \end{bmatrix}
     $$
   - 關鍵特性：只要輸入 column 中有 1 個 byte 改變，輸出 column 的 4 個 bytes 全部都會改變（Branch Number = 5）。
4. **`AddRoundKey`（金鑰加法層，§7）**：
   - 狀態矩陣與輪金鑰進行位元 XOR。
5. **最後一輪不規則點（§2.2）**：
   - 第 $N_r$ 輪**省略 `MixColumns`**，這使得加密與解密結構具備對稱性。

---

### 4.4 AES S-Box 數學建構與動態驗證（對照 Lecture 07 & 08）

對照 **`lecture08_note.md` §4.3「S-box 是怎麼造出來的」**：
AES S-Box 是由兩個數學步驟複合而成：
1. **$\text{GF}(2^8)$ 上的乘法求逆**：
   $a \mapsto a^{-1} \pmod{P(x)}$，其中特別定義 $0^{-1} = 0$。
2. **$\text{GF}(2)$ 上的仿射轉換（Affine Transformation）**：
   $$s'_i = s_i \oplus s_{(i+4)\%8} \oplus s_{(i+5)\%8} \oplus s_{(i+6)\%8} \oplus s_{(i+7)\%8} \oplus c_i$$
   其中常數向量 $c = \text{0x63} = (11000110_2)$。

本專案在 `GF256::computeSBox` 中完全依據此數學公式動態計算，並在 `main.cpp` 的測試中逐一比對全域靜態 `AES::S_BOX` 查表：
```cpp
uint8_t GF256::computeSBox(uint8_t b) {
    uint8_t inv = inverse(b);
    return affineTransform(inv);
}
```
**測試結果證實：動態數學計算產生的 256 個 bytes 與標準 S-Box 100% 完全相符！**

---

### 4.5 金鑰擴展 Key Expansion（對照 Lecture 08）

對照 **`lecture08_note.md` §8「金鑰排程」**：
- AES 將原始金鑰擴展為 $N_b \times (N_r + 1)$ 個 32-bit Words（即 $W[i]$）。
- 關鍵函數：
  - `RotWord`：字組循環左移 1 byte。
  - `SubWord`：字組中的 4 個 bytes 分別查 S-Box。
  - `Rcon[i]`：輪常數（最高位為 $x^{i-1}$ 在 $\text{GF}(2^8)$ 中的值）。
- **AES-256 特殊規則**：
  若金鑰長度 $N_k > 6$（如 AES-256，$N_k = 8$），當 $i \pmod{N_k} == 4$ 時，必須額外執行一次 `temp = SubWord(temp)`。本專案於 `src/AES.cpp` 中完整支援此規格。

---

### 4.6 AES 嚴格逆向解密流程（對照 Lecture 08）

對照 **`lecture08_note.md` §9「解密」**：
AES 解密採用 FIPS 197 標準的逆密碼流程（InvCipher）：
1. 先執行 `AddRoundKey(Nr)`（消除加密最後一輪的金鑰加法）。
2. 對每一輪 $r = N_r - 1$ 遞減至 1：
   - `InvShiftRows`（各列右移）
   - `InvSubBytes`（反向 S-Box 查表）
   - `AddRoundKey(r)`
   - `InvMixColumns`（乘上反向矩陣，元素為 `0x0E, 0x0B, 0x0D, 0x09`）
3. 第 0 輪（最後）：
   - `InvShiftRows`
   - `InvSubBytes`
   - `AddRoundKey(0)`（消除加密初始的金鑰白化）

---

## 5. 操作模式與填補機制（對照 Lecture 09）

### 5.1 ECB 模式的局限與資訊洩漏

對照 **`lecture09_note.md` §1「ECB 模式」**：
- **原理**：各個明文區塊各自獨立加密，互不相干：$C_i = E_K(P_i)$。
- **缺陷**：相同明文區塊必然產生完全相同的密文區塊。攻擊者不需破解金鑰即可進行模式分析與重送攻擊。
- **實測數據**（詳見 `crypto_demo` 執行結果）：
  明文為連續三個相同區塊 `"AAAAAAAAAAAAAAAA"` 時：
  - Block 0 密文：`6C2A3FD93AA7B417C5438D26A4619519`
  - Block 1 密文：`6C2A3FD93AA7B417C5438D26A4619519`
  - Block 2 密文：`6C2A3FD93AA7B417C5438D26A4619519`
  密文完全重複，洩漏明文結構。

---

### 5.2 CBC 模式與初始化向量 IV

對照 **`lecture09_note.md` §2「CBC 模式」**：
- **加密公式**：$C_i = E_K(P_i \oplus C_{i-1})$，其中 $C_0 = IV$。
- **解密公式**：$P_i = D_K(C_i) \oplus C_{i-1}$，其中 $C_0 = IV$。
- **優點**：即使明文區塊相同，因前一區塊的密文鏈接與隨機 IV 的引入，產生完全隨機、無規律的密文區塊。
- **實測數據**：
  同一明文在 CBC 模式下各區塊密文：
  - Block 0：`AB74350F2F19B4EA4DE050762E12DBC1`
  - Block 1：`8D2F731D5AE2FA0858814A0E6DF219CA`
  - Block 2：`DBE383CB7C0DC7188F754EE6F65A3F7F`
  三個區塊完全相異，成功消除統計特徵。

---

### 5.3 PKCS#7 填補標準

區塊密碼要求輸入資料長度為區塊大小（DES 為 8 bytes，AES 為 16 bytes）的整數倍。
- 設不足區塊之位元組數為 $P$（$1 \le P \le \text{BlockSize}$），則在結尾附加 $P$ 個值為 $P$ 的 byte。
- 若明文剛好是區塊整數倍，則附加一整塊填補區塊（值皆為 $\text{BlockSize}$），保證解密時必定能無歧義地還原真實資料。

---

## 6. 與教科書《Practical Cryptography》之實作對照與錯誤修正

教科書 *Practical Cryptography Algorithms and Implementations Using C++*（Azad & Pathan 編著）在 Chapter 5 與 Chapter 6 中提供了初學者的教學程式碼。我們在研究該書程式碼時發現若干實務限制與嚴重錯誤，並於本專案中給予徹底修正：

### 6.1 DES 實作之對照與缺陷改進

1. **陣列越界存取錯誤（Array Out-of-Bounds Bug）**：
   - **書中程式碼（p. 75, `split_key()`）**：
     ```cpp
     for(i = 28; i < 56; i++) {
         cout << dk[i] << "\t"; // dk 大小僅宣告為 28 (int dk[28])，存取 dk[28..55] 造成記憶體越界未定義行為！
     }
     ```
   - **本專案修正**：採用 64-bit 純位元遮罩與平移運算（`uint32_t c = (pc1 >> 28) & 0x0FFFFFFF; uint32_t d = pc1 & 0x0FFFFFFF;`），完全杜絕陣列越界與記憶體風險。
2. **低效率的 48 行硬編碼（Hardcoded assignments）**：
   - **書中程式碼（p. 76, `PermChoice2()`）**：書中手動撰寫了 48 行 `z[0] = per[13]; z[1] = per[16]; ... z[47] = per[31];`。
   - **本專案修正**：統整為標準 FIPS 46-3 置換表與通用迴圈置換函式 `permute()`，代碼簡潔優雅且易於維護。
3. **記憶體洩漏與危險字串指標**：
   - **書中程式碼（p. 77 & 88）**：多次呼叫 `new char[1000]` 且從未 `delete`，造成記憶體持續洩漏；且採用空白字元補齊（Space Padding），會破壞原本結尾帶有空白的明文。
   - **本專案修正**：全面採用現代 C++ RAII（`std::vector<uint8_t>`、`std::string`），並採用工業級 **PKCS#7** 填補標準。

---

### 6.2 AES 實作之對照與缺陷改進

1. **解密演算法金鑰順序筆誤（Algorithm 6.3 Bug）**：
   - **書中 Algorithm 6.3 虛擬碼（p. 106）**：
     第一步寫成 `AddRoundKey(State, ExpandedKey[0])`，最後一步寫成 `AddRoundKey(State, ExpandedKey[Nr])`。這在數學上完全相反！
   - **本專案修正**：嚴格依循 FIPS 197 標準逆密碼結構，解密先與第 $N_r$ 輪金鑰 XOR，最後才與第 0 輪金鑰 XOR。
2. **S-Box 表負數表示與符號混淆**：
   - **書中程式碼（p. 122–123）**：
     書中的 `Si_Box` 出現了大量的負數數值（例如 `82, 9, 106, -43, 48, ...`），這是將 Java signed byte 直接轉存所致，在 C++ `unsigned char` 環境下極易產生編譯警訊與隱含轉型錯誤。
   - **本專案修正**：全面回歸標準十六進制表示法（`0x00 ~ 0xFF`），並提供有限體多項式求逆的動態推導機制。
3. **擴展支援金鑰長度**：
   - 書中主要僅展示 AES-128；本專案完整支援 AES-128（10 輪）、AES-192（12 輪）與 AES-256（14 輪），涵蓋 AES-256 特有的第 4 輪額外 `SubWord` 處理。

---

## 7. 標準測試向量（KAT）與實驗驗證數據

執行 `./crypto_demo` 即可重現以下完整實測數據：

### 7.1 NIST FIPS 測試向量 Known Answer Tests

| 演算法 | NIST 規範來源 | 測試金鑰（Hex） | 明文（Hex） | 預期密文（Hex） | 實測結果 |
|---|---|---|---|---|---|
| **DES** | FIPS 46-3 | `133457799BBCDFF1` | `0123456789ABCDEF` | `85E813540F0AB405` | **MATCH (通過)** |
| **AES-128** | FIPS 197 App. B | `000102030405060708090A0B0C0D0E0F` | `00112233445566778899AABBCCDDEEFF` | `69C4E0D86A7B0430D8CDB78070B4C55A` | **MATCH (通過)** |
| **AES-192** | FIPS 197 App. C.2 | `00010203...14151617` | `00112233445566778899AABBCCDDEEFF` | `DDA97CA4864CDFE06EAF70A0EC0D7191` | **MATCH (通過)** |
| **AES-256** | FIPS 197 App. C.3 | `00010203...1E1F` | `00112233445566778899AABBCCDDEEFF` | `8EA2B7CA516745BFEAFC49904B496089` | **MATCH (通過)** |

---

### 7.2 雪崩效應（Avalanche Effect）實測分析

對照 **`lecture05_note.md` §3.4** 與 **`lecture08_note.md` §3.3**：
在密碼學中，理想的擴散特性要求：**明文改變 1 個 bit，密文應有約 50% 的 bits 發生改變**。

實測數據：
- **DES**（64 bits 區塊）：
  - 翻轉明文最後 1 個 bit（`0x...DEF` $\to$ `0x...DEE`）。
  - 密文翻轉位元數：**37 / 64 bits（57.8%）**。
- **AES**（128 bits 區塊）：
  - 翻轉明文最後 1 個 bit（`0x...FF` $\to$ `0x...FE`）。
  - 密文翻轉位元數：**62 / 128 bits（48.4%）**。

兩者皆極為接近統計上的 50% 完美雪崩效應，證實 S-Box（混淆）與 P-Box / ShiftRows / MixColumns（擴散）的設計完全發揮功效！
