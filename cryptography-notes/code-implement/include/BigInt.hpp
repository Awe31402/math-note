#ifndef BIGINT_HPP
#define BIGINT_HPP

// =============================================================
// BigInt：非負大整數（任意長度）
// -------------------------------------------------------------
// RSA 的 n, e, d, x, y 動輒 1024~2048 bit（lecture12 §3.6
// 「沒有其他技術應用需要處理這麼長的數字」），C++ 內建型別
// 最多 64 bit，所以必須自己做多精度算術。
//
// 表示法：以 2^32 為底的「位數」（limb），little-endian 存放：
//     value = limbs[0] + limbs[1]·2^32 + limbs[2]·2^64 + ...
// 永遠保持正規化（最高 limb 不為 0；數值 0 = 空陣列）。
//
// 只支援非負整數 —— RSA 裡所有量都在 Z_n 或 Z_Φ(n) 中，
// 擴展歐幾里得演算法的負係數用「mod m 的代表元」處理
// （見 RSA.cpp 的 modInverse）。
// =============================================================

#include <cstdint>
#include <functional>
#include <string>
#include <vector>

namespace crypto {

// 亂數來源：每次呼叫回傳 32 個隨機 bit
using RandomSource = std::function<uint32_t()>;

class BigInt {
public:
    BigInt() = default;
    BigInt(uint64_t v);  // NOLINT(google-explicit-constructor)：讓 BigInt x = 65537 可以寫

    // ---- 轉換 ----
    static BigInt fromHex(const std::string& hex);
    static BigInt fromDec(const std::string& dec);
    static BigInt fromBytes(const std::vector<uint8_t>& bigEndian);
    std::string toHex() const;
    std::string toDec() const;
    std::string toBin() const;
    // 輸出固定 len bytes（big-endian，前面補 0）；len = 0 表示最短長度
    std::vector<uint8_t> toBytes(size_t len = 0) const;
    uint64_t toU64() const;  // 只取最低 64 bit

    // ---- 查詢 ----
    bool isZero() const { return limbs_.empty(); }
    bool isOdd() const { return !limbs_.empty() && (limbs_[0] & 1u); }
    size_t bitLength() const;
    bool testBit(size_t i) const;
    size_t popcount() const;  // Hamming weight（lecture12 §4.6）

    // ---- 比較 ----
    static int compare(const BigInt& a, const BigInt& b);
    friend bool operator==(const BigInt& a, const BigInt& b) { return compare(a, b) == 0; }
    friend bool operator!=(const BigInt& a, const BigInt& b) { return compare(a, b) != 0; }
    friend bool operator<(const BigInt& a, const BigInt& b) { return compare(a, b) < 0; }
    friend bool operator<=(const BigInt& a, const BigInt& b) { return compare(a, b) <= 0; }
    friend bool operator>(const BigInt& a, const BigInt& b) { return compare(a, b) > 0; }
    friend bool operator>=(const BigInt& a, const BigInt& b) { return compare(a, b) >= 0; }

    // ---- 算術 ----
    friend BigInt operator+(const BigInt& a, const BigInt& b);
    friend BigInt operator-(const BigInt& a, const BigInt& b);  // 要求 a >= b
    friend BigInt operator*(const BigInt& a, const BigInt& b);
    friend BigInt operator/(const BigInt& a, const BigInt& b);
    friend BigInt operator%(const BigInt& a, const BigInt& b);
    BigInt operator<<(size_t bits) const;
    BigInt operator>>(size_t bits) const;

    // 長除法（Knuth Algorithm D）：a = q·b + r，0 <= r < b
    static void divmod(const BigInt& a, const BigInt& b, BigInt& q, BigInt& r);
    // 除以單一 32-bit 數，回傳餘數（試除小質數、轉十進位時用）
    uint32_t divmodSmall(uint32_t d, BigInt* quotient = nullptr) const;

    // ---- 數論 ----
    static BigInt gcd(BigInt a, BigInt b);  // 歐幾里得演算法（lecture11 §1）

    // ---- 亂數 ----
    // 產生恰好 bits 個 bit 的隨機數（最高位 = 1）
    static BigInt random(size_t bits, const RandomSource& rng);
    // 產生 [0, bound) 的隨機數（拒絕取樣，沒有偏差）
    static BigInt randomBelow(const BigInt& bound, const RandomSource& rng);

private:
    std::vector<uint32_t> limbs_;
    void normalize();
};

}  // namespace crypto

#endif  // BIGINT_HPP
