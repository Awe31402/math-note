#include "BigInt.hpp"

#include <algorithm>
#include <stdexcept>

namespace crypto {

namespace {
constexpr uint64_t BASE = 1ULL << 32;

int hexValue(char c) {
    if (c >= '0' && c <= '9') return c - '0';
    if (c >= 'a' && c <= 'f') return c - 'a' + 10;
    if (c >= 'A' && c <= 'F') return c - 'A' + 10;
    return -1;
}

int countLeadingZeros32(uint32_t x) {
    int n = 0;
    while (n < 32 && !(x & 0x80000000u)) {
        x <<= 1;
        ++n;
    }
    return n;
}
}  // namespace

BigInt::BigInt(uint64_t v) {
    if (v) limbs_.push_back(static_cast<uint32_t>(v));
    if (v >> 32) limbs_.push_back(static_cast<uint32_t>(v >> 32));
}

void BigInt::normalize() {
    while (!limbs_.empty() && limbs_.back() == 0) limbs_.pop_back();
}

// -------------------------------------------------------------
// 轉換
// -------------------------------------------------------------
BigInt BigInt::fromHex(const std::string& hex) {
    BigInt r;
    for (char c : hex) {
        int v = hexValue(c);
        if (v < 0) {
            if (c == ' ' || c == '_' || c == ':') continue;
            throw std::invalid_argument("BigInt::fromHex: invalid hex character");
        }
        r = (r << 4) + BigInt(static_cast<uint64_t>(v));
    }
    return r;
}

BigInt BigInt::fromDec(const std::string& dec) {
    BigInt r;
    for (char c : dec) {
        if (c < '0' || c > '9') throw std::invalid_argument("BigInt::fromDec: invalid digit");
        r = r * BigInt(10) + BigInt(static_cast<uint64_t>(c - '0'));
    }
    return r;
}

BigInt BigInt::fromBytes(const std::vector<uint8_t>& be) {
    BigInt r;
    size_t n = be.size();
    r.limbs_.assign((n + 3) / 4, 0);
    for (size_t i = 0; i < n; ++i) {
        size_t pos = n - 1 - i;  // 從最低位 byte 算起的位置
        r.limbs_[pos / 4] |= static_cast<uint32_t>(be[i]) << (8 * (pos % 4));
    }
    r.normalize();
    return r;
}

std::vector<uint8_t> BigInt::toBytes(size_t len) const {
    size_t need = (bitLength() + 7) / 8;
    if (len == 0) len = std::max<size_t>(need, 1);
    if (need > len) throw std::length_error("BigInt::toBytes: value does not fit");
    std::vector<uint8_t> out(len, 0);
    for (size_t pos = 0; pos < need; ++pos) {
        out[len - 1 - pos] = static_cast<uint8_t>(limbs_[pos / 4] >> (8 * (pos % 4)));
    }
    return out;
}

std::string BigInt::toHex() const {
    if (isZero()) return "0";
    static const char* digits = "0123456789ABCDEF";
    std::string s;
    for (size_t i = limbs_.size(); i-- > 0;) {
        for (int sh = 28; sh >= 0; sh -= 4) s.push_back(digits[(limbs_[i] >> sh) & 0xF]);
    }
    size_t first = s.find_first_not_of('0');
    return s.substr(first);
}

std::string BigInt::toDec() const {
    if (isZero()) return "0";
    std::string s;
    BigInt cur = *this;
    while (!cur.isZero()) {
        BigInt q;
        uint32_t rem = cur.divmodSmall(1000000000u, &q);  // 一次取 9 位十進位
        for (int k = 0; k < 9; ++k) {
            s.push_back(static_cast<char>('0' + rem % 10));
            rem /= 10;
        }
        cur = q;
    }
    while (s.size() > 1 && s.back() == '0') s.pop_back();
    std::reverse(s.begin(), s.end());
    return s;
}

std::string BigInt::toBin() const {
    if (isZero()) return "0";
    std::string s;
    for (size_t i = bitLength(); i-- > 0;) s.push_back(testBit(i) ? '1' : '0');
    return s;
}

uint64_t BigInt::toU64() const {
    uint64_t v = 0;
    if (limbs_.size() > 0) v |= limbs_[0];
    if (limbs_.size() > 1) v |= static_cast<uint64_t>(limbs_[1]) << 32;
    return v;
}

// -------------------------------------------------------------
// 查詢
// -------------------------------------------------------------
size_t BigInt::bitLength() const {
    if (isZero()) return 0;
    return limbs_.size() * 32 - countLeadingZeros32(limbs_.back());
}

bool BigInt::testBit(size_t i) const {
    size_t w = i / 32;
    if (w >= limbs_.size()) return false;
    return (limbs_[w] >> (i % 32)) & 1u;
}

size_t BigInt::popcount() const {
    size_t c = 0;
    for (uint32_t w : limbs_) c += static_cast<size_t>(__builtin_popcount(w));
    return c;
}

int BigInt::compare(const BigInt& a, const BigInt& b) {
    if (a.limbs_.size() != b.limbs_.size()) return a.limbs_.size() < b.limbs_.size() ? -1 : 1;
    for (size_t i = a.limbs_.size(); i-- > 0;) {
        if (a.limbs_[i] != b.limbs_[i]) return a.limbs_[i] < b.limbs_[i] ? -1 : 1;
    }
    return 0;
}

// -------------------------------------------------------------
// 加、減、乘：直式運算（小學的直式，只是「一位數」是 32 bit）
// -------------------------------------------------------------
BigInt operator+(const BigInt& a, const BigInt& b) {
    const BigInt& lo = a.limbs_.size() < b.limbs_.size() ? a : b;
    const BigInt& hi = a.limbs_.size() < b.limbs_.size() ? b : a;
    BigInt r;
    r.limbs_.resize(hi.limbs_.size() + 1);
    uint64_t carry = 0;
    for (size_t i = 0; i < hi.limbs_.size(); ++i) {
        uint64_t s = static_cast<uint64_t>(hi.limbs_[i]) + carry;
        if (i < lo.limbs_.size()) s += lo.limbs_[i];
        r.limbs_[i] = static_cast<uint32_t>(s);
        carry = s >> 32;
    }
    r.limbs_[hi.limbs_.size()] = static_cast<uint32_t>(carry);
    r.normalize();
    return r;
}

BigInt operator-(const BigInt& a, const BigInt& b) {
    if (a < b) throw std::underflow_error("BigInt: negative result (unsigned subtraction)");
    BigInt r;
    r.limbs_.resize(a.limbs_.size());
    int64_t borrow = 0;
    for (size_t i = 0; i < a.limbs_.size(); ++i) {
        int64_t d = static_cast<int64_t>(a.limbs_[i]) - borrow;
        if (i < b.limbs_.size()) d -= b.limbs_[i];
        borrow = d < 0 ? 1 : 0;
        if (d < 0) d += static_cast<int64_t>(BASE);
        r.limbs_[i] = static_cast<uint32_t>(d);
    }
    r.normalize();
    return r;
}

BigInt operator*(const BigInt& a, const BigInt& b) {
    if (a.isZero() || b.isZero()) return BigInt();
    BigInt r;
    r.limbs_.assign(a.limbs_.size() + b.limbs_.size(), 0);
    for (size_t i = 0; i < a.limbs_.size(); ++i) {
        uint64_t carry = 0;
        for (size_t j = 0; j < b.limbs_.size(); ++j) {
            uint64_t t = static_cast<uint64_t>(a.limbs_[i]) * b.limbs_[j] + r.limbs_[i + j] + carry;
            r.limbs_[i + j] = static_cast<uint32_t>(t);
            carry = t >> 32;
        }
        r.limbs_[i + b.limbs_.size()] = static_cast<uint32_t>(carry);
    }
    r.normalize();
    return r;
}

BigInt BigInt::operator<<(size_t bits) const {
    if (isZero()) return BigInt();
    size_t ws = bits / 32, bs = bits % 32;
    BigInt r;
    r.limbs_.assign(limbs_.size() + ws + 1, 0);
    for (size_t i = 0; i < limbs_.size(); ++i) {
        uint64_t v = static_cast<uint64_t>(limbs_[i]) << bs;
        r.limbs_[i + ws] |= static_cast<uint32_t>(v);
        r.limbs_[i + ws + 1] |= static_cast<uint32_t>(v >> 32);
    }
    r.normalize();
    return r;
}

BigInt BigInt::operator>>(size_t bits) const {
    size_t ws = bits / 32, bs = bits % 32;
    if (ws >= limbs_.size()) return BigInt();
    BigInt r;
    r.limbs_.assign(limbs_.size() - ws, 0);
    for (size_t i = 0; i < r.limbs_.size(); ++i) {
        uint64_t v = limbs_[i + ws];
        if (i + ws + 1 < limbs_.size()) v |= static_cast<uint64_t>(limbs_[i + ws + 1]) << 32;
        r.limbs_[i] = static_cast<uint32_t>(v >> bs);
    }
    r.normalize();
    return r;
}

// -------------------------------------------------------------
// 除法
// -------------------------------------------------------------
uint32_t BigInt::divmodSmall(uint32_t d, BigInt* quotient) const {
    if (d == 0) throw std::domain_error("BigInt: division by zero");
    BigInt q;
    q.limbs_.resize(limbs_.size());
    uint64_t rem = 0;
    for (size_t i = limbs_.size(); i-- > 0;) {
        uint64_t cur = (rem << 32) | limbs_[i];
        q.limbs_[i] = static_cast<uint32_t>(cur / d);
        rem = cur % d;
    }
    q.normalize();
    if (quotient) *quotient = q;
    return static_cast<uint32_t>(rem);
}

// Knuth, TAOCP Vol.2 §4.3.1 Algorithm D（寫法參考 Hacker's Delight 的 divmnu）。
// 想法就是「直式除法」：每次估一位商 qhat，乘回去相減；估太大就加回來。
// 先把除數左移到最高位為 1（normalize），qhat 最多只會多估 2。
void BigInt::divmod(const BigInt& a, const BigInt& b, BigInt& q, BigInt& r) {
    if (b.isZero()) throw std::domain_error("BigInt: division by zero");
    if (a < b) {
        q = BigInt();
        r = a;
        return;
    }
    if (b.limbs_.size() == 1) {
        BigInt qq;
        uint32_t rem = a.divmodSmall(b.limbs_[0], &qq);
        q = qq;
        r = BigInt(rem);
        return;
    }

    const size_t n = b.limbs_.size();
    const size_t m = a.limbs_.size() - n;
    const int s = countLeadingZeros32(b.limbs_.back());

    std::vector<uint32_t> vn(n), un(a.limbs_.size() + 1);
    for (size_t i = n - 1; i > 0; --i)
        vn[i] = (b.limbs_[i] << s) | static_cast<uint32_t>(static_cast<uint64_t>(b.limbs_[i - 1]) >> (32 - s));
    vn[0] = b.limbs_[0] << s;
    un[a.limbs_.size()] = static_cast<uint32_t>(static_cast<uint64_t>(a.limbs_.back()) >> (32 - s));
    for (size_t i = a.limbs_.size() - 1; i > 0; --i)
        un[i] = (a.limbs_[i] << s) | static_cast<uint32_t>(static_cast<uint64_t>(a.limbs_[i - 1]) >> (32 - s));
    un[0] = a.limbs_[0] << s;

    BigInt quot;
    quot.limbs_.assign(m + 1, 0);

    for (size_t jj = m + 1; jj-- > 0;) {
        const size_t j = jj;
        uint64_t num = (static_cast<uint64_t>(un[j + n]) << 32) | un[j + n - 1];
        uint64_t qhat = num / vn[n - 1];
        uint64_t rhat = num % vn[n - 1];
        while (qhat >= BASE || qhat * vn[n - 2] > ((rhat << 32) | un[j + n - 2])) {
            --qhat;
            rhat += vn[n - 1];
            if (rhat >= BASE) break;
        }

        // un[j..j+n] -= qhat * vn
        int64_t k = 0, t = 0;
        for (size_t i = 0; i < n; ++i) {
            uint64_t p = qhat * vn[i];
            t = static_cast<int64_t>(un[i + j]) - k - static_cast<int64_t>(p & 0xFFFFFFFFu);
            un[i + j] = static_cast<uint32_t>(t);
            k = static_cast<int64_t>(p >> 32) - (t >> 32);
        }
        t = static_cast<int64_t>(un[j + n]) - k;
        un[j + n] = static_cast<uint32_t>(t);

        quot.limbs_[j] = static_cast<uint32_t>(qhat);
        if (t < 0) {  // 估太大了：商減 1，把除數加回去
            quot.limbs_[j]--;
            uint64_t c = 0;
            for (size_t i = 0; i < n; ++i) {
                uint64_t sum = static_cast<uint64_t>(un[i + j]) + vn[i] + c;
                un[i + j] = static_cast<uint32_t>(sum);
                c = sum >> 32;
            }
            un[j + n] = static_cast<uint32_t>(un[j + n] + c);
        }
    }

    BigInt rem;
    rem.limbs_.resize(n);
    for (size_t i = 0; i < n; ++i)
        rem.limbs_[i] = (un[i] >> s) | static_cast<uint32_t>(static_cast<uint64_t>(un[i + 1]) << (32 - s));
    quot.normalize();
    rem.normalize();
    q = quot;
    r = rem;
}

BigInt operator/(const BigInt& a, const BigInt& b) {
    BigInt q, r;
    BigInt::divmod(a, b, q, r);
    return q;
}

BigInt operator%(const BigInt& a, const BigInt& b) {
    BigInt q, r;
    BigInt::divmod(a, b, q, r);
    return r;
}

// -------------------------------------------------------------
// 數論與亂數
// -------------------------------------------------------------
// lecture11 §1.3：gcd(r0, r1) = gcd(r1, r0 mod r1)，直到餘數為 0
BigInt BigInt::gcd(BigInt a, BigInt b) {
    while (!b.isZero()) {
        BigInt r = a % b;
        a = b;
        b = r;
    }
    return a;
}

BigInt BigInt::random(size_t bits, const RandomSource& rng) {
    if (bits == 0) return BigInt();
    BigInt r;
    r.limbs_.resize((bits + 31) / 32);
    for (auto& w : r.limbs_) w = rng();
    size_t topBits = bits % 32;
    if (topBits) r.limbs_.back() &= (1u << topBits) - 1;
    r.limbs_.back() |= 1u << ((bits - 1) % 32);  // 保證恰好 bits 位
    r.normalize();
    return r;
}

BigInt BigInt::randomBelow(const BigInt& bound, const RandomSource& rng) {
    if (bound.isZero()) throw std::domain_error("BigInt::randomBelow: bound is zero");
    size_t bits = bound.bitLength();
    while (true) {
        BigInt r;
        r.limbs_.resize((bits + 31) / 32);
        for (auto& w : r.limbs_) w = rng();
        if (bits % 32) r.limbs_.back() &= (1u << (bits % 32)) - 1;
        r.normalize();
        if (r < bound) return r;  // 機率 >= 1/2，平均試不到 2 次
    }
}

}  // namespace crypto
