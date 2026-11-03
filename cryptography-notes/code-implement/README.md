# DES、AES & RSA C++ 實作指南與 Lecture Notes 理論對照文件

本專案於 `code-implement/` 中完整實作了**資料加密標準（Data Encryption Standard, DES）**與**進階加密標準（Advanced Encryption Standard, AES-128/192/256）**的加密與解密演算法，並提供 **ECB（電子密碼本）** 與 **CBC（密碼區塊鏈）** 兩種分組密碼操作模式及 **PKCS#7** 填補標準；另外實作了公鑰密碼 **RSA**（含自製大整數運算、Miller–Rabin 質數產生、CRT 加速解密與 PKCS#1 v1.5 padding）。

本實作深入參考並對照：
1. **參考教科書**：*Practical Cryptography Algorithms and Implementations Using C++*（Azad S., Khan P. Al-Sakib 編著，CRC Press），特別是 Chapter 4（Block Cipher）、Chapter 5（DES）、Chapter 6（AES）與 Chapter 8（RSA）。
2. **課程筆記**：Christof Paar 教授之 *Introduction to Cryptography* 系列講義筆記：
   - `lecture05_note.md`：資料加密標準 DES —— 加密
   - `lecture06_note.md`：DES —— 金鑰排程與解密
   - `lecture07_note.md`：AES 需要的伽羅瓦體（Galois Fields $\text{GF}(2^8)$）
   - `lecture08_note.md`：進階加密標準 AES
   - `lecture09_note.md`：區塊密碼的操作模式（Modes of Operation）
   - `lecture11_note.md`：公鑰密碼的數論基礎（歐幾里得演算法、EEA、Euler phi、Euler 定理）
   - `lecture12_note.md`：RSA 密碼系統與快速指數運算

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
  - [6.3 RSA 實作之對照與缺陷改進](#63-rsa-實作之對照與缺陷改進)
- [7. 標準測試向量（KAT）與實驗驗證數據](#7-標準測試向量kat與實驗驗證數據)
  - [7.1 NIST FIPS 測試向量 Known Answer Tests](#71-nist-fips-測試向量-known-answer-tests)
  - [7.2 雪崩效應（Avalanche Effect）實測分析](#72-雪崩效應avalanche-effect實測分析)
- [8. RSA 演算法實作與 Lecture Notes 對照](#8-rsa-演算法實作與-lecture-notes-對照)
  - [8.1 為什麼要自己寫大整數（BigInt）](#81-為什麼要自己寫大整數bigint)
  - [8.2 擴展歐幾里得演算法與反元素（對照 Lecture 11）](#82-擴展歐幾里得演算法與反元素對照-lecture-11)
  - [8.3 RSA 金鑰產生五步驟（對照 Lecture 12 §2）](#83-rsa-金鑰產生五步驟對照-lecture-12-2)
  - [8.4 加密與解密：紅框公式（對照 Lecture 12 §3）](#84-加密與解密紅框公式對照-lecture-12-3)
  - [8.5 Square-and-Multiply（對照 Lecture 12 §4）](#85-square-and-multiply對照-lecture-12-4)
  - [8.6 產生大質數：Miller–Rabin（對照 Lecture 12 §6）](#86-產生大質數millerrabin對照-lecture-12-6)
  - [8.7 用 CRT 加速解密（對照 Lecture 12 §5.2）](#87-用-crt-加速解密對照-lecture-12-52)
  - [8.8 Schoolbook RSA 的弱點與 Padding（對照 Lecture 12 §7、§8.1）](#88-schoolbook-rsa-的弱點與-padding對照-lecture-12-781)
  - [8.9 旁通道攻擊：從 SQ/MUL 順序讀出私鑰（對照 Lecture 12 §8.3）](#89-旁通道攻擊從-sqmul-順序讀出私鑰對照-lecture-12-83)
  - [8.10 RSA 測試總表](#810-rsa-測試總表)

---

## 1. 專案架構與檔案清單

```
code-implement/
├── include/
│   ├── BlockCipher.hpp   // 通用密碼常數、十六進制轉碼、PKCS#7 填補、ECB/CBC 模式介面
│   ├── GF256.hpp         // GF(2^8) 有限體算術模組（xtime、多項式乘法、Log/Alog 生成表、S-Box 數學求值）
│   ├── DES.hpp           // DES 密碼類別定義（NIST FIPS 46-3，支援 64-bit 區塊、字串加解密、單輪追蹤）
│   ├── AES.hpp           // AES 密碼類別定義（NIST FIPS 197，支援 128/192/256-bit 金鑰、單輪追蹤）
│   ├── BigInt.hpp        // 非負大整數（2^32 進位 limb）：加減乘、Knuth 長除法、gcd、亂數
│   └── RSA.hpp           // RSA 類別、EEA、modInverse、Square-and-Multiply、Miller–Rabin
├── src/
│   ├── BlockCipher.cpp   // 十六進制處理、PKCS#7 填補/移除、矩陣除錯輸出實作
│   ├── GF256.cpp         // GF(2^8) 核心運算、仿射轉換（Affine Transform）、教科書 Log/Alog 表
│   ├── DES.cpp           // DES IP/FP、16 輪 Feistel 函數、S-box 查表、金鑰排程、ECB/CBC
│   ├── AES.cpp           // AES SubBytes、ShiftRows、MixColumns、KeyExpansion、InvCipher、ECB/CBC
│   ├── BigInt.cpp        // 大整數算術實作（Knuth Algorithm D 除法）
│   ├── RSA.cpp           // RSA 金鑰產生、加解密、CRT 解密、PKCS#1 v1.5、質數產生
│   ├── RSADemo.cpp       // RSA 展示：筆記中的每個例子、RSA-1024 測試向量、弱點與旁通道示範
│   └── main.cpp          // 完整展示與驗證程式（NIST KAT 測試、雪崩效應驗證、模式比對、RSA、單步追蹤）
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

### 執行全自動測試（KAT 測試、雪崩效應、ECB/CBC 對比、有限體驗證、RSA）
```bash
make test
# 或直接執行
./crypto_demo
```

### 執行單輪逐步追蹤（查看 Feistel 與 SPN 各輪中間狀態、RSA square-and-multiply 每一步）
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

### 6.3 RSA 實作之對照與缺陷改進

教科書 Chapter 8「The RSA Algorithm」（Saad Andaleeb & Saiful Azad）§8.4 的程式碼有以下問題：

1. **只能用 `long int`，乘法會溢位**：
   - **書中程式碼（p. 143, `Encrypt_Decrypt()`）**：`x = (x * t) % n;`、`t = (t * t) % n;`。只要 $n > 2^{32}$，`x * t` 就超過 64 bit 溢位，結果錯誤。所以書中只能跑 $n = 221$ 這種數字，**離 RSA-1024 差了 1000 bit**。
   - **本專案修正**：自己寫 `BigInt`（§8.1），可以跑真正的 RSA-1024 / 2048。
2. **`FindD()` 遞迴結果被丟掉**：
   - **書中程式碼（p. 143）**：當 `y < 1` 時呼叫 `e = FindE(phi_n); FindD(phi_n, e);` 但**沒有接回傳值**，最後 `return y;` 回傳的仍是舊的、錯誤的 $y$；而且新的 `e` 只改到區域變數，呼叫端拿到的 $e$ 和 $d$ 不成對。
   - 另外，書中虛擬碼 Algorithm 8.2 寫的是 `if y < 1 then y ← phi_n + y`（這才是對的：負的 $t$ 加上 $\Phi(n)$），但 C++ 程式碼卻改成「叫使用者重選 $e$」，兩者不一致。
   - **本專案修正**：`modInverse()` 全程以 mod $m$ 計算 $t$（§8.2），不會出現負數，也不需要重選。
3. **質數與互質檢查是暴力法**：
   - **書中程式碼（p. 141–142）**：`CheckIsPrime()` 從 2 試除到 $n/2$；`CheckCoPrime()` 從 2 試到較小的數。對 512-bit 的數要試 $2^{511}$ 次，**宇宙毀滅都跑不完**（筆記 §6.3：「不能用分解來判斷」）。
   - **本專案修正**：互質用歐幾里得演算法（`lecture11_note.md` §1，對數複雜度）；質數用 Miller–Rabin（§8.6）。
4. **質數由使用者手動輸入**：
   - **書中程式碼（p. 144, `generate_key()`）**：`cin >> p; cin >> q;`。
   - **本專案修正**：`generatePrime()` 用作業系統的亂數產生（筆記 §6.1：「$p, q$ 必須是**隨機**的」）。
5. **字串加密把 `long` 塞進 `char`**：
   - **書中程式碼（p. 144, `EncDecStr()`）**：`str1[i] = Encrypt_Decrypt(str[i], e, n);` 密文最大到 $n-1 = 220$，但存進 `char`（有號 −128～127）會被截斷，**解不回來**；`str1` 沒有結尾 `'\0'` 就直接 `cout`；兩個 `new char[1000]` 都沒有 `delete`。而且這是**逐字元加密**，等於一個替代密碼（`lecture01_note.md`），用字母頻率就能破。
   - **本專案修正**：整段訊息轉成一個大數 $x < n$ 一次加密；並提供 PKCS#1 v1.5 padding（§8.8）。
6. **Square-and-multiply 的方向不同**（不是錯誤，只是對照）：
   - 書中 `Encrypt_Decrypt()` 是**由右到左**（從 LSB 開始，`rem = e % 2; e = e / 2;`）。
   - 本專案依照筆記 §4.5 寫成**由左到右**（從 MSB 開始），這樣才能印出「指數左移、補 1」的追蹤表。兩者運算次數相同。

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
| **RSA（玩具）** | `lecture12_note.md` §3.3 | $p=3, q=11, e=3$ | $x = 4$ | $y = 31$（$d = 7$） | **MATCH (通過)** |
| **RSA（教科書）** | Azad & Pathan §8.2.3 | $p=17, q=13, e=131$ | $M = 8$ | $C = 70$（$d = 107$） | **MATCH (通過)** |
| **RSA-1024** | Python `pow()` 獨立計算 | 見 `RSADemo.cpp` TEST 5.4 | `"Introduction to ... RSA"` | `94B3EF56...9919061D` | **MATCH (通過)** |

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

---

## 8. RSA 演算法實作與 Lecture Notes 對照

RSA 跟 DES / AES 最大的不同：**它不是「攪亂 bit」，而是一個數學公式**。所以程式分成兩層：

| 層 | 檔案 | 做什麼 | 對照筆記 |
|---|---|---|---|
| 大整數算術 | `BigInt.hpp/.cpp` | 1024~2048 bit 的加減乘除、比較、亂數 | `lecture12_note.md` §3.6「沒有其他技術應用需要處理這麼長的數字」 |
| 數論工具 | `RSA.hpp/.cpp` | EEA、反元素、Square-and-Multiply、Miller–Rabin | `lecture11_note.md` §1–§3、`lecture12_note.md` §4、§6 |
| RSA 本體 | `RSA.hpp/.cpp` | 金鑰產生、加解密、CRT 解密、PKCS#1 padding | `lecture12_note.md` §2、§3、§5、§7 |
| 展示與驗證 | `RSADemo.cpp` | 筆記裡的每個例子都跑一次 | 見 §8.10 |

### 8.1 為什麼要自己寫大整數（BigInt）

對照 **`lecture12_note.md` §3.6**：真實 RSA 的 $n, d$ 約 1024 bit 以上，C++ 的 `uint64_t` 只有 64 bit。

`BigInt` 把一個大數拆成很多個 32-bit「位數」（limb），以 $2^{32}$ 為底：

$$\text{value} = \text{limbs}[0] + \text{limbs}[1]\cdot 2^{32} + \text{limbs}[2]\cdot 2^{64} + \cdots$$

- **加、減、乘**：就是小學的直式運算，只是「一位數」變成 32 bit，進位用 64-bit 暫存。
- **除法 / 取餘數**：Knuth *TAOCP* Vol.2 §4.3.1 的 **Algorithm D**（直式長除法：每次估一位商，估太大就加回來）。RSA 每一步都要 `mod n`，所以除法的速度決定整體速度。
- 只存**非負數**。RSA 裡的量都在 $\mathbb{Z}_n$ 或 $\mathbb{Z}_{\Phi(n)}$ 中；EEA 的負係數改用「mod $m$ 的代表元」處理（§8.2）。
- 正確性：用 Python 內建大整數獨立產生 20000 組隨機測資（含全 1、最高位為 1 等邊界），比對 `divmod` 與 `modPow`，**0 錯**。

### 8.2 擴展歐幾里得演算法與反元素（對照 Lecture 11）

對照 **`lecture11_note.md` §2.5「遞迴公式」**：

$$s_i = s_{i-2} - q_{i-1} \cdot s_{i-1}, \qquad t_i = t_{i-2} - q_{i-1} \cdot t_{i-1}$$

初始值 $s_0 = 1, s_1 = 0, t_0 = 0, t_1 = 1$。程式有兩個版本：

1. **教學版** `extendedEuclidTrace(int64_t r0, int64_t r1)`：完整保留 $q, r, s, t$ 四欄，印出來就是筆記 §2.5 的驗算表：
   ```
      i | q_{i-1} |   s_i |   t_i |  r_i
      0 |         |     1 |     0 |  973
      1 |         |     0 |     1 |  301
      2 |       3 |     1 |    -3 |   70
      3 |       4 |    -4 |    13 |   21
      4 |       3 |    13 |   -42 |    7
   ```
   → $7 = 13 \cdot 973 - 42 \cdot 301$，和筆記一模一樣。

2. **大數版** `modInverse(a, m)`：對照 **`lecture11_note.md` §3** 與 **`lecture12_note.md` §2.2**：
   $\gcd(\Phi(n), e) = s\cdot\Phi(n) + t\cdot e = 1 \Rightarrow d = t \bmod \Phi(n)$，**$s$ 用不到**。
   因為 BigInt 沒有負數，$t$ 每一步都存成 mod $m$ 的值：
   ```cpp
   BigInt qt = (q * t1) % m;
   BigInt t2 = (t0 + m - qt) % m;   // t_i = t_{i-2} - q·t_{i-1}  (mod m)
   ```
   最後餘數不是 1 → 反元素不存在 → 丟出例外（對應筆記 §2.1 步驟 4：「$e$ 和 $\Phi(n)$ 要互質」）。

### 8.3 RSA 金鑰產生五步驟（對照 Lecture 12 §2）

對照 **`lecture12_note.md` §2.1**，`RSA::fromPrimes()` 一行對一步：

```cpp
k.n_   = p * q;                                 // 步驟 2：n = p·q
k.phi_ = (p - BigInt(1)) * (q - BigInt(1));     // 步驟 3：Φ(n) = (p-1)(q-1)
if (BigInt::gcd(e, k.phi_) != BigInt(1))        // 步驟 4：gcd(e, Φ(n)) = 1
    throw std::invalid_argument(...);
k.d_   = modInverse(e, k.phi_);                 // 步驟 5：d = e^{-1} mod Φ(n)
```

`RSA::generate(bits, rng)` 負責步驟 1（產生 $p, q$，見 §8.6），另外做了筆記提到的檢查：

| 檢查 | 筆記出處 |
|---|---|
| $p \ne q$ | 教科書 §8.2.1 步驟 1 |
| $\gcd(e, p-1) = \gcd(e, q-1) = 1$ | §2.3 Q&A「$p-1$ 剛好有 17 這個質因數的機率很低，當然要檢查」 |
| $n$ 恰好 `bits` 位（$p, q$ 最高兩位都設為 1） | §2.3 Q&A「RSA-1024 永遠是指 $n$ 的長度」 |
| $d$ 至少 $0.3t$ bit | §5.1「$d$ 不能也選短的」 |
| 預設 $e = 2^{16}+1 = 65537$ | §5.1 短的公開指數 |

⚠️ 筆記 §2.1 的提醒在程式裡看得很清楚：**只有 `modInverse(e, phi_)` 是 mod $\Phi(n)$**，其他所有運算都是 mod $n$。

### 8.4 加密與解密：紅框公式（對照 Lecture 12 §3）

對照 **`lecture12_note.md` §3.1**：

$$y = x^e \bmod n \qquad x = y^d \bmod n$$

```cpp
BigInt RSA::encrypt(const BigInt& x) const {
    if (x >= n_) throw ...;          // x 必須在 Z_n 裡（§3.1 要求 (2)）
    return modPow(x, e_, n_);
}
BigInt RSA::decrypt(const BigInt& y) const { return modPow(y, d_, n_); }
```

**玩具例子**（§3.3）：$p=3, q=11, e=3 \Rightarrow d=7$；$4^3 \bmod 33 = 31$，$31^7 \bmod 33 = 4$ ✔。程式輸出完全相同。

**正確性**（§3.5）：程式用固定的 RSA-1024 向量驗證 `decrypt(encrypt(x)) == x`，並且把 $n, d, y$ 跟 Python 的 `pow()` 獨立算出的結果逐位比對。

### 8.5 Square-and-Multiply（對照 Lecture 12 §4）

對照 **`lecture12_note.md` §4.5 偽碼**，`modPow()` 是**由左到右**的版本：

```cpp
BigInt r = base;                              // 最高位 h_t = 1，由初始值處理
for (size_t i = H.bitLength() - 1; i-- > 0;) {
    r = (r * r) % n;                          // 每個 bit 都平方（指數左移一位）
    if (H.testBit(i)) r = (r * base) % n;     // bit 是 1 才乘（最右邊的 0 變 1）
}
```

每步之後都 `% n`，中間值不會超過 $n^2$（筆記 §4.5【課本補充】）。

`modPow` 可以傳入 `trace`，記錄每一步的「操作」和「目前指數的二進位」，印出來就是 §4.4 的追蹤表：

```
  x = 2, H = 26 = 11010₂
  step | op  | exponent (binary) | value
     1 | SQ  |                10 | 4
     2 | MUL |                11 | 8
     3 | SQ  |               110 | 64
     4 | SQ  |              1100 | 4096
     5 | MUL |              1101 | 8192
     6 | SQ  |             11010 | 67108864
```

→ **平方、乘、平方、平方、乘、平方**，6 次（天真法 25 次）。

也驗證了 §5.1 的表：$e = 3, 17, 2^{16}+1$ 分別要 **2、5、17** 次運算。

### 8.6 產生大質數：Miller–Rabin（對照 Lecture 12 §6）

對照 **`lecture12_note.md` §6.1** 的流程「隨機數 → 質數測試 → 不是就重來」：

```cpp
BigInt generatePrime(size_t bits, const RandomSource& rng) {
    while (true) {
        BigInt cand = BigInt::random(bits, rng);
        // 只測奇數（§6.2「只測奇數的話機率加倍」），最高兩位設為 1
        ...
        if (isProbablePrime(cand, 40, rng)) return cand;
    }
}
```

`isProbablePrime()` 做兩件事：

1. **先試除前 300 個小質數**：大部分合數在這裡就被擋掉，比做一次指數運算便宜很多。
2. **Miller–Rabin**（§6.3 提到的機率性測試）：把 $n-1 = 2^u \cdot r$。若 $n$ 是質數，對任何 $a$：$a^r \equiv 1$，或某個 $a^{r \cdot 2^j} \equiv -1 \pmod n$。找到不符合的 $a$ 就**一定是合數**；跑 40 輪都通過，是合數的機率 $\le 4^{-40}$。

實測（固定亂數種子）：找 5 個 512-bit 質數共試了約 1000 個奇數，**平均約 200 個**，跟筆記 §6.2 估的 **177 個**同一個量級。

亂數來源：`systemRandom()` 用 `std::random_device`（Linux 上讀 `getrandom` / `/dev/urandom`）。§6.1：「$p, q$ 必須是**隨機**的」。展示程式中標為 `fixedRandom` 的 xorshift 只用在需要可重現輸出的地方，**不能**拿來產生真的金鑰。

### 8.7 用 CRT 加速解密（對照 Lecture 12 §5.2）

對照 **`lecture12_note.md` §5.2** 的三個步驟，`decryptCRT()`：

```cpp
BigInt yp = y % p_;                     // 1. 轉到 CRT 領域
BigInt yq = y % q_;
BigInt xp = modPow(yp, dp_, p_);        // 2. 在 CRT 領域做指數（數字只有一半長）
BigInt xq = modPow(yq, dq_, q_);
BigInt x  = (q·c_p·xp + p·c_q·xq) % n;  // 3. 轉回來
```

其中 $d_p = d \bmod (p-1)$、$d_q = d \bmod (q-1)$、$c_p = q^{-1} \bmod p$、$c_q = p^{-1} \bmod q$ 都在 `computeCRTParams()` **預先算好**（筆記：「係數可以預先算好」）。

為什麼 $d_p = d \bmod (p-1)$ 可以用？Fermat 小定理（`lecture11_note.md` §5.1）：$y^{p-1} \equiv 1 \pmod p$，所以指數只需要 mod $(p-1)$。

實測 RSA-1024：一般解密約 3.6 ms，CRT 約 1.1 ms，**快約 3 倍**（筆記估 4 倍；差距來自我們的乘法和除法不是純粹的 $O(t^2)$，還有固定開銷）。

### 8.8 Schoolbook RSA 的弱點與 Padding（對照 Lecture 12 §7、§8.1）

`RSADemo.cpp` 把筆記 §7 表格裡的弱點逐一跑出來：

| 弱點 | 程式示範 | 輸出 |
|---|---|---|
| **確定性** | `encrypt("YES")` 兩次 | 兩次密文相同 |
| **小明文** | `encrypt(0)`、`encrypt(1)`、`encrypt(n-1)` | 0、1、$n-1$（原封不動） |
| **可塑性** | Oscar 只用公鑰把 $y$ 乘上 $3^e$ | Bob 解出 $3 \times 1000 = 3000$ |

**解法：Padding**。`encryptPKCS1()` 實作 **PKCS#1 v1.5**（RFC 8017 §7.2）：

$$\text{EM} = \texttt{00} \,\|\, \texttt{02} \,\|\, \underbrace{\text{PS}}_{\ge 8 \text{ 個非零隨機 byte}} \,\|\, \texttt{00} \,\|\, M$$

- 同一個 `"YES"` 加密兩次 → **兩個不同的密文**，都解得回 `"YES"`。
- 解密端 `decryptPKCS1()` **檢查結構**（筆記：「解密端要檢查解密後訊息的結構是否正確」）。被乘上 $2^e$ 竄改過的密文，結構檢查失敗，丟出例外。

⚠️ 為什麼不是 OAEP？筆記 §7 說標準做法是 **OAEP**，但 OAEP 需要**雜湊函數**（第 20 講）。這裡先用 v1.5 示範「加入隨機結構」的核心想法。v1.5 本身有 **Bleichenbacher 攻擊**（1998，利用「padding 對不對」的錯誤訊息當成解密神諭），新系統應該用 OAEP。

### 8.9 旁通道攻擊：從 SQ/MUL 順序讀出私鑰（對照 Lecture 12 §8.3）

對照 **`lecture12_note.md` §8.3**：「bit 是 0 → 只做平方（短）；bit 是 1 → 平方 + 乘法（長）。**看曲線就能直接讀出私鑰**。」

`demoSideChannel()` 用 `modPow(..., d, n, &trace)` 記下解密時的操作順序，模擬耗電曲線：

```
  power trace : S SM SM S SM SM SM S SM S S SM SM ...
  recovered d : 101101110100111101110101110111000010...
  real d      : 101101110100111101110101110111000010...
```

攻擊者的規則就一行：**每個 S 開一個新 bit，後面跟著 M 就是 1，不然是 0**。64-bit 的 $d$ 被**完整讀出**。

這也說明本實作的 `modPow` **不是常數時間**，只能拿來學習。實務對策（課本未展開）：Montgomery ladder、每個 bit 都做相同運算、blinding（解密前先乘上隨機數 $r^e$）。

### 8.10 RSA 測試總表

`./crypto_demo` 第 5 節會跑以下測試，全部 `PASSED`：

| 測試 | 內容 | 對照 |
|---|---|---|
| 5.1 | EEA 表格 gcd(973, 301)；$3^{-1} \bmod 20 = 7$ | `lecture11_note.md` §2.3–2.5、§3 |
| 5.2 | 玩具例子 $n=33$；教科書例子 $n=221$；$e=4$ 被拒絕 | `lecture12_note.md` §3.3、§2.1 步驟 4 |
| 5.3 | $x^{26}$ 追蹤表；$e = 3, 17, 65537$ 的運算次數 | `lecture12_note.md` §4.4、§5.1 |
| 5.4 | 固定 RSA-1024 向量（$n, d, y$ 跟 Python 逐位比對） | `lecture12_note.md` §3 |
| 5.5 | 隨機產生 RSA-1024、$d\cdot e \equiv 1$、CRT 速度、質數密度 | `lecture12_note.md` §2、§5.2、§6 |
| 5.6 | 確定性、小明文、可塑性；PKCS#1 v1.5 | `lecture12_note.md` §7、§8.1 |
| 5.7 | 從 SQ/MUL 順序還原私鑰 | `lecture12_note.md` §8.3 |

`./crypto_demo --trace` 還會多印出 $31^7 \bmod 33$（玩具例子的解密）每一步的 square-and-multiply 追蹤。
