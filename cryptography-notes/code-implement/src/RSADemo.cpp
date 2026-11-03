// =============================================================
// RSA 展示與驗證（對照 lecture11_note.md、lecture12_note.md）
// =============================================================
#include <cassert>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <memory>
#include <string>
#include <vector>

#include "BigInt.hpp"
#include "BlockCipher.hpp"
#include "RSA.hpp"

using namespace crypto;

namespace {

void subTitle(const std::string& t) { std::cout << "\n[" << t << "]" << std::endl; }

void check(bool ok, const std::string& what) {
    std::cout << "  => " << what << (ok ? " PASSED!" : " FAILED!") << std::endl;
    assert(ok);
}

// 固定亂數來源（只給可重現的展示用；真正產生金鑰要用 systemRandom()）
RandomSource fixedRandom(uint32_t seed) {
    auto state = std::make_shared<uint32_t>(seed);
    return [state]() {  // xorshift32
        uint32_t x = *state;
        x ^= x << 13;
        x ^= x >> 17;
        x ^= x << 5;
        return *state = x;
    };
}

// ---------------------------------------------------------------
// 5.1 lecture11 §2.3–2.5：EEA 表格 gcd(973, 301)
// ---------------------------------------------------------------
void demoEEA() {
    subTitle("TEST 5.1 Extended Euclidean Algorithm (Lecture 11 §2.5)");
    auto rows = extendedEuclidTrace(973, 301);
    std::cout << "   i | q_{i-1} |   s_i |   t_i |  r_i" << std::endl;
    std::cout << "  ---+---------+-------+-------+-----" << std::endl;
    for (size_t i = 0; i < rows.size(); ++i) {
        std::cout << "  " << std::setw(2) << i << " | " << std::setw(7) << (i < 2 ? std::string("") : std::to_string(rows[i].q))
                  << " | " << std::setw(5) << rows[i].s << " | " << std::setw(5) << rows[i].t << " | " << std::setw(4)
                  << rows[i].r << std::endl;
    }
    const EEARow& last = rows.back();
    std::cout << "  gcd = " << last.r << " = " << last.s << "·973 + (" << last.t << ")·301" << std::endl;
    check(last.r == 7 && last.s == 13 && last.t == -42 && last.s * 973 + last.t * 301 == 7,
          "7 = 13·973 - 42·301 (matches lecture11 table)");

    // lecture12 §3.3：d = 3^{-1} mod 20
    BigInt inv = modInverse(BigInt(3), BigInt(20));
    std::cout << "  3^{-1} mod 20 = " << inv.toDec() << "   (3·7 = 21 ≡ 1 mod 20)" << std::endl;
    check(inv == BigInt(7), "modInverse(3, 20) = 7");
}

// ---------------------------------------------------------------
// 5.2 lecture12 §3.3：玩具例子 p=3, q=11, e=3, x=4
// ---------------------------------------------------------------
void demoToyRSA() {
    subTitle("TEST 5.2 Toy RSA example (Lecture 12 §3.3)");
    RSA k = RSA::fromPrimes(BigInt(3), BigInt(11), BigInt(3));
    std::cout << "  p = 3, q = 11, n = " << k.n().toDec() << ", Φ(n) = " << k.phi().toDec() << ", e = "
              << k.e().toDec() << ", d = " << k.d().toDec() << std::endl;
    BigInt x(4);
    BigInt y = k.encrypt(x);
    BigInt x2 = k.decrypt(y);
    std::cout << "  Alice: y = 4^3 mod 33 = " << y.toDec() << std::endl;
    std::cout << "  Bob:   x = 31^7 mod 33 = " << x2.toDec() << "   (心算：31 ≡ -2，(-2)^7 = -128 ≡ 4)" << std::endl;
    check(k.d() == BigInt(7) && y == BigInt(31) && x2 == x, "Toy RSA n=33");

    // 教科書《Practical Cryptography》§8.2.3 的例子
    RSA b = RSA::fromPrimes(BigInt(17), BigInt(13), BigInt(131));
    BigInt by = b.encrypt(BigInt(8));
    std::cout << "  Azad & Pathan §8.2.3: p=17, q=13, e=131 → d = " << b.d().toDec() << ", 8^131 mod 221 = "
              << by.toDec() << ", 70^107 mod 221 = " << b.decrypt(by).toDec() << std::endl;
    check(b.d() == BigInt(107) && by == BigInt(70) && b.decrypt(by) == BigInt(8), "Textbook RSA n=221");

    // 筆記 §2.1 步驟 4：e 和 Φ(n) 不互質要換一個
    bool threw = false;
    try {
        RSA::fromPrimes(BigInt(3), BigInt(11), BigInt(4));
    } catch (const std::invalid_argument&) {
        threw = true;
    }
    check(threw, "e = 4 rejected because gcd(4, 20) = 2");
}

// ---------------------------------------------------------------
// 5.3 lecture12 §4.4：x^26，指數 11010
// ---------------------------------------------------------------
void printExpTrace(const std::vector<ExpStep>& tr) {
    std::cout << "  step | op  | exponent (binary) | value" << std::endl;
    for (size_t i = 0; i < tr.size(); ++i) {
        std::cout << "  " << std::setw(4) << i + 1 << " | " << (tr[i].op == 'S' ? "SQ " : "MUL") << " | "
                  << std::setw(17) << tr[i].expBits << " | " << tr[i].value.toDec() << std::endl;
    }
}

void demoSquareAndMultiply(bool verbose) {
    subTitle("TEST 5.3 Square-and-Multiply (Lecture 12 §4.4–4.6)");
    // 用 mod 一個大數，讓 x^26 不會被 mod 掉，方便看出指數
    std::vector<ExpStep> tr;
    BigInt r = modPow(BigInt(2), BigInt(26), BigInt(1) << 64, &tr);
    std::cout << "  x = 2, H = 26 = 11010₂" << std::endl;
    printExpTrace(tr);
    std::string ops;
    for (auto& s : tr) ops += (s.op == 'S' ? "SQ " : "MUL ");
    std::cout << "  順序：" << ops << "  （筆記：平方、乘、平方、平方、乘、平方）" << std::endl;
    check(r == BigInt(1ULL << 26) && ops == "SQ MUL SQ SQ MUL SQ " && tr.size() == 6,
          "2^26 with 4 SQ + 2 MUL (naive needs 25)");

    // 短的公開指數（§5.1）
    std::cout << "  operations for e = 3, 17, 2^16+1:";
    for (uint64_t e : {3ULL, 17ULL, 65537ULL}) {
        std::vector<ExpStep> t2;
        modPow(BigInt(5), BigInt(e), BigInt(1000003), &t2);
        std::cout << "  e=" << e << " → " << t2.size();
    }
    std::cout << "   （筆記 §5.1 表：2, 5, 17）" << std::endl;

    if (verbose) {
        std::cout << "\n  [trace] 31^7 mod 33（玩具例子的解密）" << std::endl;
        std::vector<ExpStep> t3;
        modPow(BigInt(31), BigInt(7), BigInt(33), &t3);
        printExpTrace(t3);
    }
}

// ---------------------------------------------------------------
// 5.4 固定的 RSA-1024 向量（由 Python 內建大整數獨立算出）
// ---------------------------------------------------------------
void demoRSA1024KAT() {
    subTitle("TEST 5.4 RSA-1024 fixed test vector (cross-checked with Python pow())");
    BigInt p = BigInt::fromHex(
        "D248B7744F1DBF6D305FB62465C5F5FBBB89053E2361288111342F9C78D253E93D6959A16C89576F96BE8F424561ABCD587223719F1645CEC30C150786AB2867");
    BigInt q = BigInt::fromHex(
        "CB9AC269918483DC2CAB65AD726D1169561329542D373B3E01BBA9EE0EBDCA98F9BDAC87C56187D25373D37FB8F8BE7EDC7E2D69238687F4E04304B15F0AB3C3");
    const std::string expN =
        "A73EC8E969159B1145275C4742E7D1D886F527A9C4825BC89AB4A5706D413B4DF3E798A789400DC3E08845B6BD4B506B207B7B326CFDB2301828EEC6742AF273A0FAEDF798B921F2E247ABF4FFDEF636563D7253CBD3B23F445EECDFE7819D64812707F2416B5BD45A9E28E84BCEA15E4A6C9EAD301356C71E1A99CA0EA5CB75";
    const std::string expD =
        "51B85D05A842556607EB66ACAF6584E50F74C4EFB0449E42944D86B53BBD6F13F5050A537ABE20BBC07FF5C888103FF84883EDBBC303E7C8965591EEC89E9F9ED421E6AA16889E3E290B61C6BBC0C84DDB020D9081FD85AB1FFC8D6EDF15AA9139E56CF9E8A838B6795640194129732B53F24C387122456ABCDAA8F639919BD5";
    const std::string expY =
        "94B3EF5669D0CFA447B1805B9BDCE588798F4C6A47F2E013E7C4C29A488D904CC4B652F7851EF37402FE2F68CAA47C5F70CCAD7398E82AA99C05249318D50E0F6D9C6A03D1AB57757BF9F0EDBF708711CD41B27213DC635A695F908094EEE95A122BA5108045C926CAFF8E76D6622E51DCD62E0DBCEE74F6AC8EFB749919061D";

    RSA k = RSA::fromPrimes(p, q, BigInt(65537));
    std::string msg = "Introduction to Cryptography - Lecture 12 RSA";
    BigInt x = BigInt::fromBytes(std::vector<uint8_t>(msg.begin(), msg.end()));
    BigInt y = k.encrypt(x);
    BigInt x1 = k.decrypt(y);
    BigInt x2 = k.decryptCRT(y);

    std::cout << "  n (" << k.n().bitLength() << " bit) = " << k.n().toHex().substr(0, 32) << "..." << std::endl;
    std::cout << "  d (" << k.d().bitLength() << " bit) = " << k.d().toHex().substr(0, 32) << "..." << std::endl;
    std::cout << "  x = \"" << msg << "\"" << std::endl;
    std::cout << "  y = x^e mod n = " << y.toHex().substr(0, 32) << "..." << std::endl;
    check(k.n().toHex() == expN, "n = p·q");
    check(k.d().toHex() == expD, "d = e^{-1} mod Φ(n) (EEA)");
    check(y.toHex() == expY, "y = x^65537 mod n");
    check(x1 == x && x2 == x, "y^d mod n = x (plain & CRT)");
}

// ---------------------------------------------------------------
// 5.5 隨機產生 RSA-1024 金鑰，比較一般解密與 CRT 解密速度
// ---------------------------------------------------------------
void demoKeyGenAndCRT() {
    subTitle("TEST 5.5 Random RSA-1024 key generation + CRT speed-up (Lecture 12 §2, §5.2, §6)");
    RandomSource rng = systemRandom();
    auto t0 = std::chrono::steady_clock::now();
    RSA k = RSA::generate(1024, rng);
    auto t1 = std::chrono::steady_clock::now();
    std::cout << "  keygen time: " << std::chrono::duration_cast<std::chrono::milliseconds>(t1 - t0).count() << " ms"
              << std::endl;
    std::cout << "  p: " << k.p().bitLength() << " bit, q: " << k.q().bitLength() << " bit, n: " << k.n().bitLength()
              << " bit  （p, q 長度相加 = n 的長度，§2.2）" << std::endl;
    std::cout << "  e = " << k.e().toDec() << ", d: " << k.d().bitLength() << " bit, popcount(d) = " << k.d().popcount()
              << std::endl;
    check((k.d() * k.e()) % k.phi() == BigInt(1), "d·e ≡ 1 (mod Φ(n))");

    const int N = 20;
    std::vector<BigInt> ys;
    for (int i = 0; i < N; ++i) ys.push_back(k.encrypt(BigInt::randomBelow(k.n(), rng)));

    auto a0 = std::chrono::steady_clock::now();
    std::vector<BigInt> plain;
    for (auto& y : ys) plain.push_back(k.decrypt(y));
    auto a1 = std::chrono::steady_clock::now();
    std::vector<BigInt> crt;
    for (auto& y : ys) crt.push_back(k.decryptCRT(y));
    auto a2 = std::chrono::steady_clock::now();

    double tPlain = std::chrono::duration<double, std::milli>(a1 - a0).count() / N;
    double tCRT = std::chrono::duration<double, std::milli>(a2 - a1).count() / N;
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "  decrypt (mod n)    : " << tPlain << " ms / op" << std::endl;
    std::cout << "  decrypt (CRT p, q) : " << tCRT << " ms / op   → " << tPlain / tCRT
              << "x faster（筆記預估約 4 倍）" << std::endl;
    std::cout << std::defaultfloat;
    bool same = true;
    for (int i = 0; i < N; ++i) same = same && plain[i] == crt[i] && k.encrypt(plain[i]) == ys[i];
    check(same, "CRT result == plain result, and Enc(Dec(y)) == y");

    // §6.2：質數多常見？數一數 512-bit 奇數要試幾個
    RandomSource frng = fixedRandom(12345);
    size_t tries = 0, found = 0;
    for (int s = 0; s < 5; ++s) {
        while (true) {
            BigInt c = BigInt::random(512, frng);
            if (!c.isOdd()) c = c + BigInt(1);
            ++tries;
            if (isProbablePrime(c, 20, frng)) break;
        }
        ++found;
    }
    std::cout << "  找 " << found << " 個 512-bit 質數共試了 " << tries << " 個奇數，平均 " << tries / found
              << " 個（筆記 §6.2：約 177）" << std::endl;
}

// ---------------------------------------------------------------
// 5.6 lecture12 §7：Schoolbook RSA 的弱點，以及 padding
// ---------------------------------------------------------------
void demoWeaknessesAndPadding() {
    subTitle("TEST 5.6 Schoolbook RSA weaknesses & PKCS#1 v1.5 padding (Lecture 12 §7, §8.1)");
    RandomSource rng = fixedRandom(2026);
    RSA k = RSA::generate(1024, rng);

    // (1) 確定性
    BigInt x = BigInt::fromBytes({'Y', 'E', 'S'});
    bool deterministic = k.encrypt(x) == k.encrypt(x);
    std::cout << "  [確定性] Enc(\"YES\") 兩次相同？ " << (deterministic ? "是 → 攻擊者猜得出明文" : "否") << std::endl;

    // (2) 小明文
    std::cout << "  [小明文] Enc(0) = " << k.encrypt(BigInt(0)).toDec() << ", Enc(1) = " << k.encrypt(BigInt(1)).toDec()
              << ", Enc(n-1) == n-1 ? " << (k.encrypt(k.n() - BigInt(1)) == k.n() - BigInt(1) ? "是" : "否") << std::endl;

    // (3) 可塑性：y' = y·s^e → 解密得到 s·x
    BigInt salary(1000);
    BigInt y = k.encrypt(salary);
    BigInt s(3);
    BigInt yForged = (y * k.encrypt(s)) % k.n();  // Oscar 只用公鑰
    BigInt xForged = k.decrypt(yForged);
    std::cout << "  [可塑性] Oscar 把 Enc(1000) 乘上 3^e，Bob 解出來 = " << xForged.toDec() << std::endl;
    check(deterministic && xForged == BigInt(3000), "schoolbook RSA is deterministic and malleable");

    // PKCS#1 v1.5：加入隨機 → 同一明文每次密文都不同
    std::string m = "YES";
    std::vector<uint8_t> mv(m.begin(), m.end());
    auto c1 = k.encryptPKCS1(mv, rng);
    auto c2 = k.encryptPKCS1(mv, rng);
    auto d1 = k.decryptPKCS1(c1);
    auto d2 = k.decryptPKCS1(c2);
    std::cout << "  [PKCS#1] c1 = " << bytesToHex(c1).substr(0, 32) << "..." << std::endl;
    std::cout << "  [PKCS#1] c2 = " << bytesToHex(c2).substr(0, 32) << "..." << std::endl;
    check(c1 != c2 && d1 == mv && d2 == mv, "PKCS#1 v1.5: randomized ciphertexts, both decrypt to \"YES\"");

    // 被竄改的密文，padding 檢查會失敗
    BigInt forged = (BigInt::fromBytes(c1) * k.encrypt(BigInt(2))) % k.n();
    bool rejected = false;
    try {
        k.decryptPKCS1(forged.toBytes(k.modulusBytes()));
    } catch (const std::runtime_error&) {
        rejected = true;
    }
    check(rejected, "malleated PKCS#1 ciphertext rejected by structure check");
}

// ---------------------------------------------------------------
// 5.7 lecture12 §8.3：旁通道 —— 從 SQ / MUL 順序讀出私鑰
// ---------------------------------------------------------------
void demoSideChannel() {
    subTitle("TEST 5.7 Side-channel: reading d from the SQ/MUL pattern (Lecture 12 §8.3)");
    RandomSource rng = fixedRandom(7);
    RSA k = RSA::generate(64, rng);  // 小金鑰，印得下
    std::vector<ExpStep> tr;
    modPow(BigInt(12345), k.d(), k.n(), &tr);

    // 「耗電曲線」：S = 短區間，SM = 長區間
    std::string power;
    for (auto& s : tr) power += (s.op == 'S' ? " S" : "M");
    // 攻擊者：每個 S 開一個新 bit，後面跟著 M 就是 1，否則是 0；最高位一定是 1
    std::string recovered = "1";
    for (size_t i = 0; i < tr.size(); ++i) {
        if (tr[i].op == 'S') recovered.push_back((i + 1 < tr.size() && tr[i + 1].op == 'M') ? '1' : '0');
    }
    std::cout << "  power trace :" << power.substr(0, 60) << " ..." << std::endl;
    std::cout << "  recovered d : " << recovered << std::endl;
    std::cout << "  real d      : " << k.d().toBin() << std::endl;
    check(recovered == k.d().toBin(), "private exponent fully recovered from operation sequence");
    std::cout << "  （對策：Montgomery ladder / 每個 bit 都做一樣的運算，課本未展開）" << std::endl;
}

}  // namespace

void runRSADemo(bool verbose) {
    std::cout << std::setfill(' ') << std::dec;
    std::cout << "\n========================================================" << std::endl;
    std::cout << "  5. RSA Public-Key Cryptosystem (Lectures 11 & 12)" << std::endl;
    std::cout << "========================================================" << std::endl;
    demoEEA();
    demoToyRSA();
    demoSquareAndMultiply(verbose);
    demoRSA1024KAT();
    demoKeyGenAndCRT();
    demoWeaknessesAndPadding();
    demoSideChannel();
}
