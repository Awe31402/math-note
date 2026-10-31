#include "DES.hpp"
#include <cstring>
#include <sstream>

namespace crypto {

// Standard Initial Permutation (IP) Table
const uint8_t DES::IP_TABLE[64] = {
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17,  9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
};

// Standard Final Permutation (IP^-1) Table
const uint8_t DES::FP_TABLE[64] = {
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41,  9, 49, 17, 57, 25
};

// Permuted Choice 1 (PC-1)
const uint8_t DES::PC1_TABLE[56] = {
    57, 49, 41, 33, 25, 17,  9,
     1, 58, 50, 42, 34, 26, 18,
    10,  2, 59, 51, 43, 35, 27,
    19, 11,  3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
     7, 62, 54, 46, 38, 30, 22,
    14,  6, 61, 53, 45, 37, 29,
    21, 13,  5, 28, 20, 12,  4
};

// Permuted Choice 2 (PC-2)
const uint8_t DES::PC2_TABLE[48] = {
    14, 17, 11, 24,  1,  5,
     3, 28, 15,  6, 21, 10,
    23, 19, 12,  4, 26,  8,
    16,  7, 27, 20, 13,  2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
};

// Expansion Table E
const uint8_t DES::EXPANSION_TABLE[48] = {
    32,  1,  2,  3,  4,  5,
     4,  5,  6,  7,  8,  9,
     8,  9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32,  1
};

// Permutation Table P
const uint8_t DES::P_TABLE[32] = {
    16,  7, 20, 21,
    29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2,  8, 24, 14,
    32, 27,  3,  9,
    19, 13, 30,  6,
    22, 11,  4, 25
};

// Standard 8 S-Boxes (4x16 each)
const uint8_t DES::S_BOXES[8][4][16] = {
    // S1
    {{14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7},
     {0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8},
     {4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0},
     {15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13}},
    // S2
    {{15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10},
     {3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5},
     {0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15},
     {13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9}},
    // S3
    {{10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8},
     {13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1},
     {13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7},
     {1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12}},
    // S4
    {{7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15},
     {13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9},
     {10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4},
     {3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14}},
    // S5
    {{2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9},
     {14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6},
     {4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14},
     {11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3}},
    // S6
    {{12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11},
     {10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8},
     {9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6},
     {4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13}},
    // S7
    {{4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1},
     {13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6},
     {1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2},
     {6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12}},
    // S8
    {{13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7},
     {1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2},
     {7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8},
     {2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11}}
};

// Left shift count per round (Lecture 06 §1.3: rounds 1, 2, 9, 16 shift 1; others shift 2)
const uint8_t DES::SHIFT_SCHEDULE[16] = {
    1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
};

DES::DES() {
    keygen(0);
}

DES::DES(uint64_t key64) {
    keygen(key64);
}

DES::DES(const std::vector<uint8_t>& key) {
    setKey(key);
}

DES::DES(const std::string& keyStr) {
    setKey(keyStr);
}

uint64_t DES::bytesToUint64(const uint8_t bytes[8]) {
    uint64_t val = 0;
    for (int i = 0; i < 8; ++i) {
        val = (val << 8) | bytes[i];
    }
    return val;
}

void DES::uint64ToBytes(uint64_t val, uint8_t bytes[8]) {
    for (int i = 7; i >= 0; --i) {
        bytes[i] = static_cast<uint8_t>(val & 0xFF);
        val >>= 8;
    }
}

uint64_t DES::permute(uint64_t in, const uint8_t* table, int inBits, int outBits) {
    uint64_t res = 0;
    for (int i = 0; i < outBits; ++i) {
        int srcBit = table[i]; // 1-indexed, bit 1 is MSB
        uint64_t bit = (in >> (inBits - srcBit)) & 1ULL;
        res = (res << 1) | bit;
    }
    return res;
}

uint64_t DES::initialPermutation(uint64_t block) {
    return permute(block, IP_TABLE, 64, 64);
}

uint64_t DES::finalPermutation(uint64_t block) {
    return permute(block, FP_TABLE, 64, 64);
}

uint64_t DES::expansion(uint32_t r32) {
    return permute(r32, EXPANSION_TABLE, 32, 48);
}

uint32_t DES::substitution(uint64_t expXorKey) {
    uint32_t sOut = 0;
    for (int i = 0; i < 8; ++i) {
        // Extract 6 bits for box i (from left/MSB to right/LSB)
        uint8_t chunk = static_cast<uint8_t>((expXorKey >> (42 - 6 * i)) & 0x3F);
        // Row: outer 2 bits (bit 5 and bit 0)
        uint8_t row = ((chunk & 0x20) >> 4) | (chunk & 0x01);
        // Col: inner 4 bits (bits 4..1)
        uint8_t col = (chunk >> 1) & 0x0F;
        uint8_t val = S_BOXES[i][row][col];
        sOut = (sOut << 4) | val;
    }
    return sOut;
}

uint32_t DES::permutationP(uint32_t sOut) {
    return static_cast<uint32_t>(permute(sOut, P_TABLE, 32, 32));
}

uint32_t DES::roundFunctionF(uint32_t r32, uint64_t subkey) {
    // 1. Expansion: 32 bits -> 48 bits
    uint64_t expanded = expansion(r32);
    // 2. XOR with 48-bit round subkey
    uint64_t xorKey = expanded ^ subkey;
    // 3. 8 S-Boxes: 48 bits -> 32 bits
    uint32_t substituted = substitution(xorKey);
    // 4. Permutation P: 32 bits -> 32 bits
    return permutationP(substituted);
}

void DES::keygen(uint64_t key64) {
    // 1. PC-1: 64 bits -> 56 bits (discard parity bits)
    uint64_t pc1 = permute(key64, PC1_TABLE, 64, 56);
    // 2. Split into C0 and D0 (28 bits each)
    uint32_t c = static_cast<uint32_t>((pc1 >> 28) & 0x0FFFFFFFULL);
    uint32_t d = static_cast<uint32_t>(pc1 & 0x0FFFFFFFULL);

    if (verbose_) {
        std::cout << "[DES Keygen] Raw Key: 0x" << std::hex << key64 << std::dec << std::endl;
        std::cout << "[DES Keygen] C0: 0x" << std::hex << c << ", D0: 0x" << d << std::dec << std::endl;
    }

    // 3. 16 Rounds of Left Circular Shifts & PC-2
    for (size_t r = 0; r < NUM_ROUNDS; ++r) {
        int shift = SHIFT_SCHEDULE[r];
        // 28-bit circular left shift: (val << s) | (val >> (28 - s))
        c = ((c << shift) | (c >> (28 - shift))) & 0x0FFFFFFFULL;
        d = ((d << shift) | (d >> (28 - shift))) & 0x0FFFFFFFULL;
        uint64_t cd = (static_cast<uint64_t>(c) << 28) | d;
        // PC-2: 56 bits -> 48 bits
        subkeys_[r] = permute(cd, PC2_TABLE, 56, 48);

        if (verbose_) {
            std::cout << "[DES Keygen] Round " << (r + 1)
                      << " (shift " << shift << ") Subkey: 0x"
                      << std::hex << subkeys_[r] << std::dec << std::endl;
        }
    }
}

void DES::setKey(const std::vector<uint8_t>& key) {
    if (key.size() != KEY_SIZE) {
        throw std::invalid_argument("DES key must be exactly 8 bytes (64 bits).");
    }
    keygen(bytesToUint64(key.data()));
}

void DES::setKey(const std::string& keyStr) {
    std::vector<uint8_t> keyBytes;
    if (keyStr.size() == 16) {
        try {
            keyBytes = hexToBytes(keyStr);
        } catch (...) {
            // Not pure hex, treat as ASCII
            keyBytes.assign(keyStr.begin(), keyStr.end());
        }
    } else {
        keyBytes.assign(keyStr.begin(), keyStr.end());
    }
    if (keyBytes.size() != KEY_SIZE) {
        throw std::invalid_argument("DES key must be 8 bytes long.");
    }
    setKey(keyBytes);
}

uint64_t DES::encryptBlock(uint64_t block) const {
    // Initial Permutation
    uint64_t ip = initialPermutation(block);
    uint32_t l = static_cast<uint32_t>((ip >> 32) & 0xFFFFFFFF);
    uint32_t r = static_cast<uint32_t>(ip & 0xFFFFFFFF);

    if (verbose_) {
        std::cout << "[DES EncryptBlock] Plaintext: 0x" << std::hex << block
                  << " -> IP: L0=0x" << l << " R0=0x" << r << std::dec << std::endl;
    }

    // 16 Feistel Rounds
    for (size_t i = 0; i < NUM_ROUNDS; ++i) {
        uint32_t f_res = roundFunctionF(r, subkeys_[i]);
        uint32_t next_l = r;
        uint32_t next_r = l ^ f_res;
        l = next_l;
        r = next_r;

        if (verbose_) {
            std::cout << "  Round " << std::setw(2) << (i + 1)
                      << ": L=0x" << std::hex << std::setw(8) << std::setfill('0') << l
                      << " R=0x" << std::setw(8) << std::setfill('0') << r
                      << " f=0x" << std::setw(8) << std::setfill('0') << f_res
                      << std::dec << std::endl;
        }
    }

    // Pre-output swap: (R16, L16)
    uint64_t rl = (static_cast<uint64_t>(r) << 32) | l;
    uint64_t cipher = finalPermutation(rl);

    if (verbose_) {
        std::cout << "[DES EncryptBlock] Pre-output (R16||L16): 0x" << std::hex << rl
                  << " -> FP: 0x" << cipher << std::dec << std::endl;
    }
    return cipher;
}

uint64_t DES::decryptBlock(uint64_t block) const {
    // Initial Permutation
    uint64_t ip = initialPermutation(block);
    uint32_t l = static_cast<uint32_t>((ip >> 32) & 0xFFFFFFFF);
    uint32_t r = static_cast<uint32_t>(ip & 0xFFFFFFFF);

    if (verbose_) {
        std::cout << "[DES DecryptBlock] Ciphertext: 0x" << std::hex << block
                  << " -> IP: L0=0x" << l << " R0=0x" << r << std::dec << std::endl;
    }

    // 16 Feistel Rounds in REVERSE key order (subkeys_[15] down to subkeys_[0])
    for (int i = static_cast<int>(NUM_ROUNDS) - 1; i >= 0; --i) {
        uint32_t f_res = roundFunctionF(r, subkeys_[i]);
        uint32_t next_l = r;
        uint32_t next_r = l ^ f_res;
        l = next_l;
        r = next_r;

        if (verbose_) {
            std::cout << "  Dec Round " << std::setw(2) << (16 - i)
                      << " (Subkey " << (i + 1) << "): L=0x"
                      << std::hex << std::setw(8) << std::setfill('0') << l
                      << " R=0x" << std::setw(8) << std::setfill('0') << r
                      << std::dec << std::endl;
        }
    }

    // Pre-output swap: (R16, L16)
    uint64_t rl = (static_cast<uint64_t>(r) << 32) | l;
    return finalPermutation(rl);
}

void DES::encryptBlock(const uint8_t in[8], uint8_t out[8]) const {
    uint64_t block = bytesToUint64(in);
    uint64_t cipher = encryptBlock(block);
    uint64ToBytes(cipher, out);
}

void DES::decryptBlock(const uint8_t in[8], uint8_t out[8]) const {
    uint64_t block = bytesToUint64(in);
    uint64_t plain = decryptBlock(block);
    uint64ToBytes(plain, out);
}

std::vector<uint8_t> DES::encrypt(const std::vector<uint8_t>& plaintext, 
                                  CipherMode mode, 
                                  const std::vector<uint8_t>& iv) const {
    std::vector<uint8_t> padded = addPKCS7Padding(plaintext, BLOCK_SIZE);
    std::vector<uint8_t> ciphertext(padded.size());

    if (mode == CipherMode::ECB) {
        for (size_t i = 0; i < padded.size(); i += BLOCK_SIZE) {
            encryptBlock(&padded[i], &ciphertext[i]);
        }
    } else if (mode == CipherMode::CBC) {
        if (iv.size() != BLOCK_SIZE) {
            throw std::invalid_argument("CBC mode requires an 8-byte IV.");
        }
        std::vector<uint8_t> prev = iv;
        for (size_t i = 0; i < padded.size(); i += BLOCK_SIZE) {
            uint8_t block[BLOCK_SIZE];
            for (size_t j = 0; j < BLOCK_SIZE; ++j) {
                block[j] = padded[i + j] ^ prev[j];
            }
            encryptBlock(block, &ciphertext[i]);
            prev.assign(&ciphertext[i], &ciphertext[i + BLOCK_SIZE]);
        }
    }
    return ciphertext;
}

std::vector<uint8_t> DES::decrypt(const std::vector<uint8_t>& ciphertext, 
                                  CipherMode mode, 
                                  const std::vector<uint8_t>& iv) const {
    if (ciphertext.empty() || ciphertext.size() % BLOCK_SIZE != 0) {
        throw std::invalid_argument("Ciphertext length must be a non-zero multiple of 8 bytes.");
    }
    std::vector<uint8_t> plaintext(ciphertext.size());

    if (mode == CipherMode::ECB) {
        for (size_t i = 0; i < ciphertext.size(); i += BLOCK_SIZE) {
            decryptBlock(&ciphertext[i], &plaintext[i]);
        }
    } else if (mode == CipherMode::CBC) {
        if (iv.size() != BLOCK_SIZE) {
            throw std::invalid_argument("CBC mode requires an 8-byte IV.");
        }
        std::vector<uint8_t> prev = iv;
        for (size_t i = 0; i < ciphertext.size(); i += BLOCK_SIZE) {
            uint8_t decrypted[BLOCK_SIZE];
            decryptBlock(&ciphertext[i], decrypted);
            for (size_t j = 0; j < BLOCK_SIZE; ++j) {
                plaintext[i + j] = decrypted[j] ^ prev[j];
            }
            prev.assign(&ciphertext[i], &ciphertext[i + BLOCK_SIZE]);
        }
    }
    return removePKCS7Padding(plaintext);
}

std::string DES::encryptString(const std::string& plaintext, 
                              CipherMode mode, 
                              const std::string& ivStr) const {
    std::vector<uint8_t> pt(plaintext.begin(), plaintext.end());
    std::vector<uint8_t> ivBytes;
    if (!ivStr.empty()) {
        try {
            ivBytes = hexToBytes(ivStr);
        } catch (...) {
            ivBytes.assign(ivStr.begin(), ivStr.end());
        }
    }
    std::vector<uint8_t> ct = encrypt(pt, mode, ivBytes);
    return bytesToHex(ct);
}

std::string DES::decryptString(const std::string& ciphertextHex, 
                              CipherMode mode, 
                              const std::string& ivStr) const {
    std::vector<uint8_t> ct = hexToBytes(ciphertextHex);
    std::vector<uint8_t> ivBytes;
    if (!ivStr.empty()) {
        try {
            ivBytes = hexToBytes(ivStr);
        } catch (...) {
            ivBytes.assign(ivStr.begin(), ivStr.end());
        }
    }
    std::vector<uint8_t> pt = decrypt(ct, mode, ivBytes);
    return std::string(pt.begin(), pt.end());
}

} // namespace crypto
