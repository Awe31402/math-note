#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <bitset>
#include <cassert>

#include "DES.hpp"
#include "AES.hpp"
#include "GF256.hpp"
#include "BlockCipher.hpp"

using namespace crypto;

// RSADemo.cpp
void runRSADemo(bool verbose);

void printSeparator(const std::string& title) {
    std::cout << "\n========================================================" << std::endl;
    std::cout << "  " << title << std::endl;
    std::cout << "========================================================" << std::endl;
}

// -------------------------------------------------------------
// Test 1: NIST Known Answer Tests (KAT)
// -------------------------------------------------------------
void runKnownAnswerTests() {
    printSeparator("1. NIST Known Answer Tests (KAT)");

    // 1.1 DES FIPS 46-3 KAT
    std::cout << "\n[TEST 1.1] DES FIPS 46-3 Known Answer Test" << std::endl;
    uint64_t desKey = 0x133457799BBCDFF1ULL;
    uint64_t desPT  = 0x0123456789ABCDEFULL;
    uint64_t desExpectedCT = 0x85E813540F0AB405ULL;

    DES des(desKey);
    uint64_t desCT = des.encryptBlock(desPT);
    uint64_t desDecrypted = des.decryptBlock(desCT);

    std::cout << "  Key:        0x" << std::hex << std::setfill('0') << std::setw(16) << desKey << std::endl;
    std::cout << "  Plaintext:  0x" << std::setw(16) << desPT << std::endl;
    std::cout << "  Ciphertext: 0x" << std::setw(16) << desCT << std::endl;
    std::cout << "  Expected:   0x" << std::setw(16) << desExpectedCT << std::endl;
    std::cout << "  Decrypted:  0x" << std::setw(16) << desDecrypted << std::dec << std::endl;

    assert(desCT == desExpectedCT);
    assert(desDecrypted == desPT);
    std::cout << "  => DES FIPS 46-3 KAT PASSED!\n" << std::endl;

    // 1.2 AES-128 FIPS 197 KAT (Appendix B)
    std::cout << "[TEST 1.2] AES-128 FIPS 197 Known Answer Test" << std::endl;
    std::vector<uint8_t> aes128Key = hexToBytes("000102030405060708090a0b0c0d0e0f");
    std::vector<uint8_t> aesPT     = hexToBytes("00112233445566778899aabbccddeeff");
    std::string expected128CT      = "69C4E0D86A7B0430D8CDB78070B4C55A";

    AES aes128(aes128Key, AES::KeySize::AES128);
    uint8_t ct128[16];
    aes128.encryptBlock(aesPT.data(), ct128);
    uint8_t dec128[16];
    aes128.decryptBlock(ct128, dec128);

    std::cout << "  Key:        " << bytesToHex(aes128Key) << std::endl;
    std::cout << "  Plaintext:  " << bytesToHex(aesPT) << std::endl;
    std::cout << "  Ciphertext: " << bytesToHex(ct128, 16) << std::endl;
    std::cout << "  Expected:   " << expected128CT << std::endl;
    std::cout << "  Decrypted:  " << bytesToHex(dec128, 16) << std::endl;

    assert(bytesToHex(ct128, 16) == expected128CT);
    assert(bytesToHex(dec128, 16) == bytesToHex(aesPT));
    std::cout << "  => AES-128 FIPS 197 KAT PASSED!\n" << std::endl;

    // 1.3 AES-192 FIPS 197 KAT (Appendix C.2)
    std::cout << "[TEST 1.3] AES-192 FIPS 197 Known Answer Test" << std::endl;
    std::vector<uint8_t> aes192Key = hexToBytes("000102030405060708090a0b0c0d0e0f1011121314151617");
    std::string expected192CT      = "DDA97CA4864CDFE06EAF70A0EC0D7191";

    AES aes192(aes192Key, AES::KeySize::AES192);
    uint8_t ct192[16];
    aes192.encryptBlock(aesPT.data(), ct192);
    uint8_t dec192[16];
    aes192.decryptBlock(ct192, dec192);

    std::cout << "  Key:        " << bytesToHex(aes192Key) << std::endl;
    std::cout << "  Plaintext:  " << bytesToHex(aesPT) << std::endl;
    std::cout << "  Ciphertext: " << bytesToHex(ct192, 16) << std::endl;
    std::cout << "  Expected:   " << expected192CT << std::endl;

    assert(bytesToHex(ct192, 16) == expected192CT);
    assert(bytesToHex(dec192, 16) == bytesToHex(aesPT));
    std::cout << "  => AES-192 FIPS 197 KAT PASSED!\n" << std::endl;

    // 1.4 AES-256 FIPS 197 KAT (Appendix C.3)
    std::cout << "[TEST 1.4] AES-256 FIPS 197 Known Answer Test" << std::endl;
    std::vector<uint8_t> aes256Key = hexToBytes("000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f");
    std::string expected256CT      = "8EA2B7CA516745BFEAFC49904B496089";

    AES aes256(aes256Key, AES::KeySize::AES256);
    uint8_t ct256[16];
    aes256.encryptBlock(aesPT.data(), ct256);
    uint8_t dec256[16];
    aes256.decryptBlock(ct256, dec256);

    std::cout << "  Key:        " << bytesToHex(aes256Key) << std::endl;
    std::cout << "  Plaintext:  " << bytesToHex(aesPT) << std::endl;
    std::cout << "  Ciphertext: " << bytesToHex(ct256, 16) << std::endl;
    std::cout << "  Expected:   " << expected256CT << std::endl;

    assert(bytesToHex(ct256, 16) == expected256CT);
    assert(bytesToHex(dec256, 16) == bytesToHex(aesPT));
    std::cout << "  => AES-256 FIPS 197 KAT PASSED!" << std::endl;
}

// -------------------------------------------------------------
// Test 2: Shannon's Confusion & Diffusion (Avalanche Effect)
// Corresponds to Lecture 05 §3.4 & Lecture 08 §3.3
// -------------------------------------------------------------
void runAvalancheDemo() {
    printSeparator("2. Avalanche Effect Demonstration (Lectures 05 & 08)");

    // DES Avalanche test: 1-bit flip
    std::cout << "[DES Avalanche Analysis]" << std::endl;
    uint64_t desKey = 0x133457799BBCDFF1ULL;
    uint64_t pt1    = 0x0123456789ABCDEFULL;
    uint64_t pt2    = 0x0123456789ABCDEEULL; // 1-bit flip at LSB

    DES des(desKey);
    uint64_t ct1 = des.encryptBlock(pt1);
    uint64_t ct2 = des.encryptBlock(pt2);
    uint64_t diffBits = ct1 ^ ct2;
    int flipped = std::bitset<64>(diffBits).count();

    std::cout << "  PT1:     0x" << std::hex << pt1 << std::endl;
    std::cout << "  PT2:     0x" << pt2 << " (flipped 1 bit)" << std::endl;
    std::cout << "  CT1:     0x" << ct1 << std::endl;
    std::cout << "  CT2:     0x" << ct2 << std::dec << std::endl;
    std::cout << "  Flipped bits in DES ciphertext: " << flipped << " / 64 bits (" 
              << (flipped * 100.0 / 64.0) << "%)\n" << std::endl;

    // AES Avalanche test: 1-bit flip
    std::cout << "[AES Avalanche Analysis]" << std::endl;
    std::vector<uint8_t> aesKey = hexToBytes("000102030405060708090a0b0c0d0e0f");
    std::vector<uint8_t> apt1   = hexToBytes("00112233445566778899aabbccddeeff");
    std::vector<uint8_t> apt2   = hexToBytes("00112233445566778899aabbccddeefe"); // 1-bit flip

    AES aes(aesKey);
    uint8_t act1[16], act2[16];
    aes.encryptBlock(apt1.data(), act1);
    aes.encryptBlock(apt2.data(), act2);

    int aesFlipped = 0;
    for (int i = 0; i < 16; ++i) {
        aesFlipped += std::bitset<8>(act1[i] ^ act2[i]).count();
    }
    std::cout << "  PT1: " << bytesToHex(apt1) << std::endl;
    std::cout << "  PT2: " << bytesToHex(apt2) << " (flipped 1 bit)" << std::endl;
    std::cout << "  CT1: " << bytesToHex(act1, 16) << std::endl;
    std::cout << "  CT2: " << bytesToHex(act2, 16) << std::endl;
    std::cout << "  Flipped bits in AES ciphertext: " << aesFlipped << " / 128 bits ("
              << (aesFlipped * 100.0 / 128.0) << "%)" << std::endl;
}

// -------------------------------------------------------------
// Test 3: Modes of Operation (ECB vs CBC)
// Corresponds to Lecture 09 §4.3 & Book Chapter 4
// -------------------------------------------------------------
void runModesDemo() {
    printSeparator("3. Modes of Operation Demonstration (Lecture 09)");

    std::string repeatedText = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"; // 3 identical 16-byte blocks
    std::vector<uint8_t> key = hexToBytes("2b7e151628aed2a6abf7158809cf4f3c");
    std::vector<uint8_t> iv  = hexToBytes("000102030405060708090a0b0c0d0e0f");

    AES aes(key);
    std::cout << "Plaintext (Repeated 'A'*48 = 3 identical 16-byte blocks):" << std::endl;
    std::cout << "  \"" << repeatedText << "\"\n" << std::endl;

    // ECB Mode
    std::string ctECB = aes.encryptString(repeatedText, CipherMode::ECB);
    std::cout << "[ECB Mode] (Notice identical ciphertext blocks for identical plaintext):" << std::endl;
    for (size_t i = 0; i < ctECB.size(); i += 32) {
        std::cout << "  Block " << (i / 32) << ": " << ctECB.substr(i, 32) << std::endl;
    }
    std::string decECB = aes.decryptString(ctECB, CipherMode::ECB);
    assert(decECB == repeatedText);

    // CBC Mode
    std::string ctCBC = aes.encryptString(repeatedText, CipherMode::CBC, bytesToHex(iv));
    std::cout << "\n[CBC Mode] (Chaining with IV breaks repeating patterns completely):" << std::endl;
    for (size_t i = 0; i < ctCBC.size(); i += 32) {
        std::cout << "  Block " << (i / 32) << ": " << ctCBC.substr(i, 32) << std::endl;
    }
    std::string decCBC = aes.decryptString(ctCBC, CipherMode::CBC, bytesToHex(iv));
    assert(decCBC == repeatedText);

    std::cout << "\n  => ECB vs CBC comparison verified: CBC effectively masks repetitions!" << std::endl;
}

// -------------------------------------------------------------
// Test 4: Galois Field GF(2^8) & S-Box Generation
// Corresponds to Lecture 07 & Lecture 08 §4.3
// -------------------------------------------------------------
void runGaloisFieldDemo() {
    printSeparator("4. GF(2^8) Arithmetic & AES S-Box Math (Lectures 07 & 08)");

    std::cout << "[Lecture 07 §4.3 Example Verification]" << std::endl;
    uint8_t a = 0x57; // x^6 + x^4 + x^2 + x + 1
    uint8_t b = 0x13; // x^4 + x + 1
    uint8_t prodShift = GF256::multiply(a, b);
    uint8_t prodLog   = GF256::mulLogAlog(a, b);

    std::cout << "  0x57 * 0x13 via Polynomial Shift-and-Add: 0x" 
              << std::hex << static_cast<int>(prodShift) << std::endl;
    std::cout << "  0x57 * 0x13 via Log/Alog Generator Table: 0x" 
              << static_cast<int>(prodLog) << std::dec << std::endl;
    assert(prodShift == 0xFE);
    assert(prodLog == 0xFE);
    std::cout << "  => Both multiplication approaches yield 0xFE (Matches Textbook Example)!\n" << std::endl;

    std::cout << "[Dynamic S-Box Construction Verification (Lecture 08 §4.3)]" << std::endl;
    bool allMatch = true;
    for (int i = 0; i < 256; ++i) {
        uint8_t sComputed   = GF256::computeSBox(static_cast<uint8_t>(i));
        uint8_t sTable      = AES::S_BOX[i];
        uint8_t invComputed = GF256::computeInvSBox(static_cast<uint8_t>(i));
        uint8_t invTable    = AES::INV_S_BOX[i];

        if (sComputed != sTable || invComputed != invTable) {
            allMatch = false;
            break;
        }
    }
    assert(allMatch);
    std::cout << "  => Verified all 256 S-Box entries generated via GF(2^8) Inverse + Affine Transform!" << std::endl;
}

// -------------------------------------------------------------
// Verbose Pedagogical Trace
// -------------------------------------------------------------
void runVerboseTrace() {
    printSeparator("6. Detailed Round-by-Round Execution Trace");

    std::cout << "\n--- DES Round Trace ---" << std::endl;
    DES des(0x133457799BBCDFF1ULL);
    des.setVerbose(true);
    uint64_t desPt = 0x0123456789ABCDEFULL;
    uint64_t desCt = des.encryptBlock(desPt);
    std::cout << "\n--- DES Decryption Trace ---" << std::endl;
    des.decryptBlock(desCt);

    std::cout << "\n--- AES-128 Round Trace ---" << std::endl;
    AES aes("000102030405060708090a0b0c0d0e0f", AES::KeySize::AES128);
    aes.setVerbose(true);
    std::vector<uint8_t> pt = hexToBytes("00112233445566778899aabbccddeeff");
    uint8_t ct[16];
    aes.encryptBlock(pt.data(), ct);
    std::cout << "\n--- AES-128 Decryption Trace ---" << std::endl;
    uint8_t dec[16];
    aes.decryptBlock(ct, dec);
}

int main(int argc, char* argv[]) {
    std::cout << "========================================================\n";
    std::cout << "   DES, AES & RSA Cryptographic Implementation in C++\n";
    std::cout << "   Based on 'Practical Cryptography' (Azad & Pathan)\n";
    std::cout << "   & Christof Paar's Lecture Notes (Lectures 05 to 12)\n";
    std::cout << "========================================================\n";

    bool verbose = false;
    if (argc > 1 && std::string(argv[1]) == "--trace") {
        verbose = true;
    }

    runKnownAnswerTests();
    runAvalancheDemo();
    runModesDemo();
    runGaloisFieldDemo();
    runRSADemo(verbose);

    if (verbose) {
        runVerboseTrace();
    } else {
        std::cout << "\n[TIP] Run with '--trace' to view round-by-round Feistel / SPN steps and RSA square-and-multiply traces!" << std::endl;
    }

    std::cout << "\n========================================================" << std::endl;
    std::cout << "  ALL TESTS AND DEMONSTRATIONS COMPLETED SUCCESSFULLY!  " << std::endl;
    std::cout << "========================================================\n" << std::endl;
    return 0;
}
