#ifndef RSA_HPP
#define RSA_HPP

// =============================================================
// RSA 公鑰密碼系統
// -------------------------------------------------------------
// 對照：lecture11_note.md（EEA、Euler phi、Euler 定理）
//       lecture12_note.md（RSA 金鑰產生、加解密、Square-and-Multiply、
//                          CRT 加速、質數產生、Padding、攻擊）
// =============================================================

#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

#include "BigInt.hpp"

namespace crypto {

// ---------- 數論工具（lecture11） ----------

// 擴展歐幾里得演算法的一列：r_i = s_i·r0 + t_i·r1
// （教學用，int64 版本，可以印出跟筆記 §2.5 一樣的表格）
struct EEARow {
    int64_t q;  // q_{i-1}（第 0、1 列沒有商，記為 0）
    int64_t r, s, t;
};
std::vector<EEARow> extendedEuclidTrace(int64_t r0, int64_t r1);

// a^{-1} mod m（大數版本）。gcd(a, m) != 1 時丟出例外。
BigInt modInverse(const BigInt& a, const BigInt& m);

// ---------- 快速指數運算（lecture12 §4） ----------

// 一次 square-and-multiply 執行中，每個步驟的紀錄
struct ExpStep {
    char op;              // 'S' = 平方, 'M' = 乘以 x
    std::string expBits;  // 做完這步之後「目前的指數」（二進位）
    BigInt value;         // 做完這步之後的 r
};

// 由左到右（MSB → LSB）的 Square-and-Multiply：回傳 x^H mod n。
// trace 不為 nullptr 時，記錄每一步（用來印表或模擬旁通道攻擊）。
BigInt modPow(const BigInt& x, const BigInt& H, const BigInt& n,
              std::vector<ExpStep>* trace = nullptr);

// ---------- 質數（lecture12 §6） ----------

// Miller–Rabin 機率性質數測試：回傳 false 一定是合數；
// 回傳 true 時，是合數的機率 <= 4^{-rounds}
bool isProbablePrime(const BigInt& n, int rounds, const RandomSource& rng);

// 產生 bits 位的隨機質數（最高兩位設為 1，讓 p·q 恰好 2·bits 位）
BigInt generatePrime(size_t bits, const RandomSource& rng);

// 作業系統提供的亂數（Linux 上 std::random_device 讀 getrandom/urandom）
RandomSource systemRandom();

// ---------- RSA ----------

class RSA {
public:
    // lecture12 §2.1 五個步驟：隨機產生 bits 位的 n
    static RSA generate(size_t bits, const RandomSource& rng, const BigInt& e = BigInt(65537));
    // 直接給 p、q、e（玩具例子用）。gcd(e, Φ(n)) != 1 時丟出例外。
    static RSA fromPrimes(const BigInt& p, const BigInt& q, const BigInt& e);

    // ---- Schoolbook RSA（lecture12 §3.1 紅框公式） ----
    BigInt encrypt(const BigInt& x) const;     // y = x^e mod n
    BigInt decrypt(const BigInt& y) const;     // x = y^d mod n
    BigInt decryptCRT(const BigInt& y) const;  // 同上，但用 CRT 加速（§5.2）

    // ---- 加上 PKCS#1 v1.5 padding 的 RSA（§7） ----
    std::vector<uint8_t> encryptPKCS1(const std::vector<uint8_t>& msg, const RandomSource& rng) const;
    std::vector<uint8_t> decryptPKCS1(const std::vector<uint8_t>& ct) const;

    // ---- 金鑰 ----
    const BigInt& n() const { return n_; }
    const BigInt& e() const { return e_; }
    const BigInt& d() const { return d_; }
    const BigInt& p() const { return p_; }
    const BigInt& q() const { return q_; }
    const BigInt& phi() const { return phi_; }
    size_t modulusBytes() const { return (n_.bitLength() + 7) / 8; }

    void setVerbose(bool v) { verbose_ = v; }

private:
    BigInt p_, q_, n_, phi_, e_, d_;
    // CRT 預先計算（§5.2）
    BigInt dp_, dq_;    // d mod (p-1), d mod (q-1)
    BigInt cp_, cq_;    // q^{-1} mod p, p^{-1} mod q
    bool verbose_ = false;

    void computeCRTParams();
};

}  // namespace crypto

#endif  // RSA_HPP
