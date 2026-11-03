#include "RSA.hpp"

#include <memory>
#include <random>
#include <stdexcept>

namespace crypto {

// =============================================================
// lecture11 §2.5：擴展歐幾里得演算法（教學版，int64）
//   s_i = s_{i-2} - q_{i-1}·s_{i-1}
//   t_i = t_{i-2} - q_{i-1}·t_{i-1}
//   初始值 s0 = 1, s1 = 0, t0 = 0, t1 = 1
// =============================================================
std::vector<EEARow> extendedEuclidTrace(int64_t r0, int64_t r1) {
    std::vector<EEARow> rows;
    rows.push_back({0, r0, 1, 0});
    rows.push_back({0, r1, 0, 1});
    while (rows.back().r != 0) {
        const EEARow& a = rows[rows.size() - 2];  // 上上一行
        const EEARow& b = rows[rows.size() - 1];  // 上一行
        int64_t q = a.r / b.r;
        rows.push_back({q, a.r - q * b.r, a.s - q * b.s, a.t - q * b.t});
    }
    rows.pop_back();  // 最後那列餘數為 0，不算；gcd 是倒數第二列的 r
    return rows;
}

// =============================================================
// lecture11 §3 / lecture12 §2.2：用 EEA 求反元素
//   gcd(m, a) = s·m + t·a = 1  ⇒  t·a ≡ 1 (mod m)，所以 a^{-1} = t mod m
//
// BigInt 只存非負數，所以 t 一律存成「mod m 的代表元」：
//   t_i = t_{i-2} - q·t_{i-1}  改寫成  (t_{i-2} + m - (q·t_{i-1} mod m)) mod m
// s 用不到（筆記：「s 用不到」），所以不算。
// =============================================================
BigInt modInverse(const BigInt& a, const BigInt& m) {
    BigInt r0 = m, r1 = a % m;
    BigInt t0 = BigInt(0), t1 = BigInt(1);
    while (!r1.isZero()) {
        BigInt q, r2;
        BigInt::divmod(r0, r1, q, r2);
        BigInt qt = (q * t1) % m;
        BigInt t2 = (t0 + m - qt) % m;
        r0 = r1;
        r1 = r2;
        t0 = t1;
        t1 = t2;
    }
    if (r0 != BigInt(1)) throw std::domain_error("modInverse: gcd(a, m) != 1, inverse does not exist");
    return t0;
}

// =============================================================
// lecture12 §4.5：Square-and-Multiply（由左到右）
//
//   r = x
//   FOR i = t-1 DOWNTO 0:
//       r = r² mod n          ← 每個 bit 都平方（指數左移一位）
//       IF h_i = 1:
//           r = r·x mod n     ← bit 是 1 才乘（最右邊的 0 變成 1）
//   RETURN r
//
// 最高位 h_t 一定是 1，由初始值 r = x 處理掉了。
// 每一步之後都 mod n，讓中間值不會超過 n²。
// =============================================================
BigInt modPow(const BigInt& x, const BigInt& H, const BigInt& n, std::vector<ExpStep>* trace) {
    if (n.isZero()) throw std::domain_error("modPow: modulus is zero");
    if (n == BigInt(1)) return BigInt(0);
    if (H.isZero()) return BigInt(1);

    BigInt base = x % n;
    BigInt r = base;
    std::string bits = "1";
    for (size_t i = H.bitLength() - 1; i-- > 0;) {
        r = (r * r) % n;
        bits.push_back('0');
        if (trace) trace->push_back({'S', bits, r});
        if (H.testBit(i)) {
            r = (r * base) % n;
            bits.back() = '1';
            if (trace) trace->push_back({'M', bits, r});
        }
    }
    return r;
}

// =============================================================
// lecture12 §6：質數產生 = 隨機奇數 + 質數測試，失敗就重來
// =============================================================
namespace {
// 先用小質數試除，擋掉大部分合數（比做一次 Miller–Rabin 便宜很多）
const std::vector<uint32_t>& smallPrimes() {
    static std::vector<uint32_t> primes = [] {
        std::vector<uint32_t> ps;
        for (uint32_t c = 3; ps.size() < 300; c += 2) {
            bool isP = true;
            for (uint32_t p : ps) {
                if (p * p > c) break;
                if (c % p == 0) { isP = false; break; }
            }
            if (isP) ps.push_back(c);
        }
        return ps;
    }();
    return primes;
}
}  // namespace

// Miller–Rabin：把 n-1 寫成 2^u · r（r 為奇數）。
// 如果 n 是質數，對任何 a：a^r ≡ 1，或某個 a^{r·2^j} ≡ -1 (mod n)。
// 找到不符合的 a（"witness"）就證明 n 是合數。
bool isProbablePrime(const BigInt& n, int rounds, const RandomSource& rng) {
    if (n < BigInt(2)) return false;
    if (n < BigInt(4)) return true;  // 2, 3
    if (!n.isOdd()) return false;
    for (uint32_t p : smallPrimes()) {
        if (n == BigInt(p)) return true;
        if (n.divmodSmall(p) == 0) return false;
    }

    const BigInt one(1), two(2);
    const BigInt nMinus1 = n - one;
    BigInt r = nMinus1;
    size_t u = 0;
    while (!r.isOdd()) {
        r = r >> 1;
        ++u;
    }

    for (int k = 0; k < rounds; ++k) {
        BigInt a = BigInt::randomBelow(n - BigInt(3), rng) + two;  // a ∈ [2, n-2]
        BigInt z = modPow(a, r, n);
        if (z == one || z == nMinus1) continue;
        bool maybePrime = false;
        for (size_t j = 1; j < u; ++j) {
            z = (z * z) % n;
            if (z == nMinus1) { maybePrime = true; break; }
            if (z == one) break;  // 出現 1 的非平凡平方根 → 合數
        }
        if (!maybePrime) return false;
    }
    return true;
}

BigInt generatePrime(size_t bits, const RandomSource& rng) {
    if (bits < 8) throw std::invalid_argument("generatePrime: need at least 8 bits");
    while (true) {
        BigInt cand = BigInt::random(bits, rng);
        cand = cand + BigInt(cand.isOdd() ? 0 : 1);           // 只測奇數，機率加倍（§6.2）
        if (!cand.testBit(bits - 2)) cand = cand + (BigInt(1) << (bits - 2));  // 最高兩位 = 11
        if (cand.bitLength() != bits) continue;
        if (isProbablePrime(cand, 40, rng)) return cand;
    }
}

RandomSource systemRandom() {
    // shared_ptr 讓 std::function 可以被複製
    auto dev = std::make_shared<std::random_device>();
    return [dev]() { return static_cast<uint32_t>((*dev)()); };
}

// =============================================================
// lecture12 §2.1：RSA 金鑰產生
//   1. 選兩個大質數 p, q
//   2. n = p·q
//   3. Φ(n) = (p-1)(q-1)
//   4. 選 e，gcd(e, Φ(n)) = 1
//   5. d = e^{-1} mod Φ(n)      ← 只有這一步是 mod Φ(n)！
// =============================================================
RSA RSA::fromPrimes(const BigInt& p, const BigInt& q, const BigInt& e) {
    if (p == q) throw std::invalid_argument("RSA: p must differ from q");
    RSA k;
    k.p_ = p;
    k.q_ = q;
    k.n_ = p * q;                                 // 步驟 2
    k.phi_ = (p - BigInt(1)) * (q - BigInt(1));   // 步驟 3
    if (e <= BigInt(1) || e >= k.phi_) throw std::invalid_argument("RSA: e must be in [2, phi(n)-1]");
    if (BigInt::gcd(e, k.phi_) != BigInt(1))      // 步驟 4
        throw std::invalid_argument("RSA: gcd(e, phi(n)) != 1, choose another e");
    k.e_ = e;
    k.d_ = modInverse(e, k.phi_);                 // 步驟 5：EEA
    k.computeCRTParams();
    return k;
}

RSA RSA::generate(size_t bits, const RandomSource& rng, const BigInt& e) {
    if (bits < 32 || bits % 2) throw std::invalid_argument("RSA::generate: bits must be even and >= 32");
    while (true) {
        BigInt p = generatePrime(bits / 2, rng);  // 步驟 1
        BigInt q = generatePrime(bits / 2, rng);
        if (p == q) continue;
        // 筆記 §2.3 Q&A：「p-1 或 q-1 剛好有 e 這個質因數的機率很低，當然要檢查」
        if (BigInt::gcd(e, p - BigInt(1)) != BigInt(1) || BigInt::gcd(e, q - BigInt(1)) != BigInt(1)) continue;
        RSA k = fromPrimes(p, q, e);
        if (k.n_.bitLength() != bits) continue;
        // §5.1：d 不能太短，至少 0.3t bit
        if (k.d_.bitLength() * 10 < bits * 3) continue;
        return k;
    }
}

void RSA::computeCRTParams() {
    dp_ = d_ % (p_ - BigInt(1));
    dq_ = d_ % (q_ - BigInt(1));
    cp_ = modInverse(q_ % p_, p_);
    cq_ = modInverse(p_ % q_, q_);
}

// =============================================================
// lecture12 §3.1：紅框公式
// =============================================================
BigInt RSA::encrypt(const BigInt& x) const {
    if (x >= n_) throw std::invalid_argument("RSA::encrypt: plaintext must be < n");
    return modPow(x, e_, n_);
}

BigInt RSA::decrypt(const BigInt& y) const {
    if (y >= n_) throw std::invalid_argument("RSA::decrypt: ciphertext must be < n");
    return modPow(y, d_, n_);
}

// =============================================================
// lecture12 §5.2：用 CRT 加速解密（只有私鑰持有者知道 p, q）
//   1. 轉到 CRT 領域：y_p = y mod p，y_q = y mod q
//   2. 在 CRT 領域做指數：x_p = y_p^{d_p} mod p，x_q = y_q^{d_q} mod q
//   3. 轉回來：x = [q·c_p]·x_p + [p·c_q]·x_q mod n
//      其中 c_p = q^{-1} mod p，c_q = p^{-1} mod q（預先算好）
// d_p = d mod (p-1) 可以用，因為由 Fermat 小定理 y^{p-1} ≡ 1 (mod p)。
// =============================================================
BigInt RSA::decryptCRT(const BigInt& y) const {
    if (y >= n_) throw std::invalid_argument("RSA::decryptCRT: ciphertext must be < n");
    BigInt yp = y % p_;
    BigInt yq = y % q_;
    BigInt xp = modPow(yp, dp_, p_);
    BigInt xq = modPow(yq, dq_, q_);
    BigInt x = ((q_ * cp_) % n_ * xp + (p_ * cq_) % n_ * xq) % n_;
    if (verbose_) {
        std::cout << "    [CRT] y_p = " << yp.toHex() << "\n"
                  << "    [CRT] y_q = " << yq.toHex() << "\n"
                  << "    [CRT] x_p = y_p^d_p mod p = " << xp.toHex() << "\n"
                  << "    [CRT] x_q = y_q^d_q mod q = " << xq.toHex() << "\n";
    }
    return x;
}

// =============================================================
// lecture12 §7：Padding。這裡實作 PKCS#1 v1.5（RFC 8017 §7.2）：
//     EM = 0x00 || 0x02 || PS || 0x00 || M
// PS 是至少 8 個「非零」隨機 byte → 同一個明文每次加密結果都不同。
//
// ⚠️ v1.5 有 Bleichenbacher 攻擊（1998），新系統應該用 OAEP。
//    OAEP 需要雜湊函數（lecture20），這裡先用 v1.5 示範「加入隨機結構」的想法。
// =============================================================
std::vector<uint8_t> RSA::encryptPKCS1(const std::vector<uint8_t>& msg, const RandomSource& rng) const {
    const size_t k = modulusBytes();
    if (msg.size() + 11 > k) throw std::length_error("RSA::encryptPKCS1: message too long");
    std::vector<uint8_t> em(k);
    em[0] = 0x00;
    em[1] = 0x02;
    size_t psLen = k - msg.size() - 3;
    for (size_t i = 0; i < psLen; ++i) {
        uint8_t b;
        do { b = static_cast<uint8_t>(rng()); } while (b == 0);
        em[2 + i] = b;
    }
    em[2 + psLen] = 0x00;
    std::copy(msg.begin(), msg.end(), em.begin() + 3 + static_cast<long>(psLen));
    BigInt y = encrypt(BigInt::fromBytes(em));
    return y.toBytes(k);
}

std::vector<uint8_t> RSA::decryptPKCS1(const std::vector<uint8_t>& ct) const {
    const size_t k = modulusBytes();
    if (ct.size() != k) throw std::invalid_argument("RSA::decryptPKCS1: wrong ciphertext length");
    std::vector<uint8_t> em = decryptCRT(BigInt::fromBytes(ct)).toBytes(k);
    // 解密端要檢查結構（筆記：「解密端要檢查解密後訊息的結構是否正確」）
    if (em[0] != 0x00 || em[1] != 0x02) throw std::runtime_error("RSA::decryptPKCS1: bad padding");
    size_t sep = 2;
    while (sep < k && em[sep] != 0x00) ++sep;
    if (sep == k || sep < 10) throw std::runtime_error("RSA::decryptPKCS1: bad padding");
    return std::vector<uint8_t>(em.begin() + static_cast<long>(sep) + 1, em.end());
}

}  // namespace crypto
