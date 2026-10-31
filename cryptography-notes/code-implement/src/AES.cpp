#include "AES.hpp"
#include <iostream>
#include <iomanip>
#include <cstring>

namespace crypto {

// Standard Rijndael S-Box (FIPS 197)
const std::array<uint8_t, 256> AES::S_BOX = {
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
};

// Standard Inverse Rijndael S-Box (FIPS 197)
const std::array<uint8_t, 256> AES::INV_S_BOX = {
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
};

// Round constants Rcon (powers of x in GF(2^8))
const std::array<uint8_t, 15> AES::RCON = {
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D
};

AES::AES(KeySize keySize) : keySize_(keySize) {
    if (keySize == KeySize::AES128) {
        nk_ = 4; nr_ = 10;
    } else if (keySize == KeySize::AES192) {
        nk_ = 6; nr_ = 12;
    } else {
        nk_ = 8; nr_ = 14;
    }
}

AES::AES(const std::vector<uint8_t>& key, KeySize keySize) : AES(keySize) {
    setKey(key, keySize);
}

AES::AES(const std::string& keyStr, KeySize keySize) : AES(keySize) {
    setKey(keyStr, keySize);
}

void AES::setKey(const std::vector<uint8_t>& key, KeySize keySize) {
    keySize_ = keySize;
    if (keySize == KeySize::AES128) {
        nk_ = 4; nr_ = 10;
        if (key.size() != 16) throw std::invalid_argument("AES-128 key must be 16 bytes.");
    } else if (keySize == KeySize::AES192) {
        nk_ = 6; nr_ = 12;
        if (key.size() != 24) throw std::invalid_argument("AES-192 key must be 24 bytes.");
    } else {
        nk_ = 8; nr_ = 14;
        if (key.size() != 32) throw std::invalid_argument("AES-256 key must be 32 bytes.");
    }
    keyExpansion(key);
}

void AES::setKey(const std::string& keyStr, KeySize keySize) {
    size_t expectedLen = (keySize == KeySize::AES128) ? 16 : ((keySize == KeySize::AES192) ? 24 : 32);
    std::vector<uint8_t> keyBytes;
    if (keyStr.size() == expectedLen * 2) {
        try {
            keyBytes = hexToBytes(keyStr);
        } catch (...) {
            keyBytes.assign(keyStr.begin(), keyStr.end());
        }
    } else {
        keyBytes.assign(keyStr.begin(), keyStr.end());
    }
    setKey(keyBytes, keySize);
}

uint32_t AES::rotWord(uint32_t w) {
    return (w << 8) | (w >> 24);
}

uint32_t AES::subWord(uint32_t w) {
    return (static_cast<uint32_t>(S_BOX[(w >> 24) & 0xFF]) << 24) |
           (static_cast<uint32_t>(S_BOX[(w >> 16) & 0xFF]) << 16) |
           (static_cast<uint32_t>(S_BOX[(w >>  8) & 0xFF]) <<  8) |
           (static_cast<uint32_t>(S_BOX[ w        & 0xFF]));
}

void AES::keyExpansion(const std::vector<uint8_t>& key) {
    int totalWords = NB * (nr_ + 1);
    expandedKey_.resize(totalWords);

    for (int i = 0; i < nk_; ++i) {
        expandedKey_[i] = (static_cast<uint32_t>(key[4 * i])     << 24) |
                          (static_cast<uint32_t>(key[4 * i + 1]) << 16) |
                          (static_cast<uint32_t>(key[4 * i + 2]) <<  8) |
                          (static_cast<uint32_t>(key[4 * i + 3]));
    }

    for (int i = nk_; i < totalWords; ++i) {
        uint32_t temp = expandedKey_[i - 1];
        if (i % nk_ == 0) {
            temp = subWord(rotWord(temp)) ^ (static_cast<uint32_t>(RCON[i / nk_]) << 24);
        } else if (nk_ > 6 && (i % nk_ == 4)) {
            temp = subWord(temp);
        }
        expandedKey_[i] = expandedKey_[i - nk_] ^ temp;
    }

    if (verbose_) {
        std::cout << "[AES KeyExpansion] Generated " << totalWords << " words (" 
                  << (nr_ + 1) << " round keys):" << std::endl;
        for (int r = 0; r <= nr_; ++r) {
            std::cout << "  Round " << std::setw(2) << r << ": ";
            for (int c = 0; c < NB; ++c) {
                std::cout << std::hex << std::setfill('0') << std::setw(8) 
                          << expandedKey_[r * NB + c] << " ";
            }
            std::cout << std::dec << std::endl;
        }
    }
}

void AES::subBytes(uint8_t state[4][4]) {
    for (int r = 0; r < 4; ++r) {
        for (int c = 0; c < 4; ++c) {
            state[r][c] = S_BOX[state[r][c]];
        }
    }
}

void AES::invSubBytes(uint8_t state[4][4]) {
    for (int r = 0; r < 4; ++r) {
        for (int c = 0; c < 4; ++c) {
            state[r][c] = INV_S_BOX[state[r][c]];
        }
    }
}

void AES::shiftRows(uint8_t state[4][4]) {
    // Row 0: no shift
    // Row 1: circular left shift by 1
    uint8_t t1 = state[1][0];
    state[1][0] = state[1][1];
    state[1][1] = state[1][2];
    state[1][2] = state[1][3];
    state[1][3] = t1;

    // Row 2: circular left shift by 2
    uint8_t t20 = state[2][0], t21 = state[2][1];
    state[2][0] = state[2][2];
    state[2][1] = state[2][3];
    state[2][2] = t20;
    state[2][3] = t21;

    // Row 3: circular left shift by 3 (right shift by 1)
    uint8_t t3 = state[3][3];
    state[3][3] = state[3][2];
    state[3][2] = state[3][1];
    state[3][1] = state[3][0];
    state[3][0] = t3;
}

void AES::invShiftRows(uint8_t state[4][4]) {
    // Row 0: no shift
    // Row 1: circular right shift by 1
    uint8_t t1 = state[1][3];
    state[1][3] = state[1][2];
    state[1][2] = state[1][1];
    state[1][1] = state[1][0];
    state[1][0] = t1;

    // Row 2: circular right shift by 2
    uint8_t t20 = state[2][0], t21 = state[2][1];
    state[2][0] = state[2][2];
    state[2][1] = state[2][3];
    state[2][2] = t20;
    state[2][3] = t21;

    // Row 3: circular right shift by 3 (left shift by 1)
    uint8_t t3 = state[3][0];
    state[3][0] = state[3][1];
    state[3][1] = state[3][2];
    state[3][2] = state[3][3];
    state[3][3] = t3;
}

void AES::mixColumns(uint8_t state[4][4]) {
    for (int c = 0; c < 4; ++c) {
        uint8_t a0 = state[0][c], a1 = state[1][c], a2 = state[2][c], a3 = state[3][c];
        state[0][c] = GF256::multiply(0x02, a0) ^ GF256::multiply(0x03, a1) ^ a2 ^ a3;
        state[1][c] = a0 ^ GF256::multiply(0x02, a1) ^ GF256::multiply(0x03, a2) ^ a3;
        state[2][c] = a0 ^ a1 ^ GF256::multiply(0x02, a2) ^ GF256::multiply(0x03, a3);
        state[3][c] = GF256::multiply(0x03, a0) ^ a1 ^ a2 ^ GF256::multiply(0x02, a3);
    }
}

void AES::invMixColumns(uint8_t state[4][4]) {
    for (int c = 0; c < 4; ++c) {
        uint8_t a0 = state[0][c], a1 = state[1][c], a2 = state[2][c], a3 = state[3][c];
        state[0][c] = GF256::multiply(0x0E, a0) ^ GF256::multiply(0x0B, a1) ^ 
                      GF256::multiply(0x0D, a2) ^ GF256::multiply(0x09, a3);
        state[1][c] = GF256::multiply(0x09, a0) ^ GF256::multiply(0x0E, a1) ^ 
                      GF256::multiply(0x0B, a2) ^ GF256::multiply(0x0D, a3);
        state[2][c] = GF256::multiply(0x0D, a0) ^ GF256::multiply(0x09, a1) ^ 
                      GF256::multiply(0x0E, a2) ^ GF256::multiply(0x0B, a3);
        state[3][c] = GF256::multiply(0x0B, a0) ^ GF256::multiply(0x0D, a1) ^ 
                      GF256::multiply(0x09, a2) ^ GF256::multiply(0x0E, a3);
    }
}

void AES::addRoundKey(uint8_t state[4][4], int round) const {
    for (int c = 0; c < NB; ++c) {
        uint32_t roundWord = expandedKey_[round * NB + c];
        state[0][c] ^= static_cast<uint8_t>((roundWord >> 24) & 0xFF);
        state[1][c] ^= static_cast<uint8_t>((roundWord >> 16) & 0xFF);
        state[2][c] ^= static_cast<uint8_t>((roundWord >>  8) & 0xFF);
        state[3][c] ^= static_cast<uint8_t>( roundWord        & 0xFF);
    }
}

void AES::printRoundState(int round, const std::string& step, const uint8_t state[4][4]) const {
    std::cout << "  Round " << std::setw(2) << round << " [" << step << "]: ";
    for (int c = 0; c < 4; ++c) {
        for (int r = 0; r < 4; ++r) {
            std::cout << std::hex << std::setfill('0') << std::setw(2) 
                      << static_cast<int>(state[r][c]);
        }
    }
    std::cout << std::dec << std::endl;
}

void AES::encryptBlock(const uint8_t in[16], uint8_t out[16]) const {
    if (expandedKey_.empty()) {
        throw std::runtime_error("Key has not been set for AES encryption.");
    }

    uint8_t state[4][4];
    // Map 16-byte block into 4x4 column-major state matrix
    for (int c = 0; c < NB; ++c) {
        for (int r = 0; r < 4; ++r) {
            state[r][c] = in[r + 4 * c];
        }
    }

    if (verbose_) {
        std::cout << "[AES EncryptBlock] Starting Encryption:" << std::endl;
        printRoundState(0, "Input", state);
    }

    // Round 0: Initial Key Whitening
    addRoundKey(state, 0);
    if (verbose_) printRoundState(0, "AddRoundKey", state);

    // Rounds 1 to Nr - 1: Standard SPN Rounds
    for (int r = 1; r < nr_; ++r) {
        subBytes(state);
        if (verbose_) printRoundState(r, "SubBytes   ", state);

        shiftRows(state);
        if (verbose_) printRoundState(r, "ShiftRows  ", state);

        mixColumns(state);
        if (verbose_) printRoundState(r, "MixColumns ", state);

        addRoundKey(state, r);
        if (verbose_) printRoundState(r, "AddRoundKey", state);
    }

    // Round Nr: Final Round (MixColumns omitted)
    subBytes(state);
    if (verbose_) printRoundState(nr_, "SubBytes   ", state);

    shiftRows(state);
    if (verbose_) printRoundState(nr_, "ShiftRows  ", state);

    addRoundKey(state, nr_);
    if (verbose_) printRoundState(nr_, "AddRoundKey", state);

    // Map 4x4 state matrix back to 16-byte array
    for (int c = 0; c < NB; ++c) {
        for (int r = 0; r < 4; ++r) {
            out[r + 4 * c] = state[r][c];
        }
    }
}

void AES::decryptBlock(const uint8_t in[16], uint8_t out[16]) const {
    if (expandedKey_.empty()) {
        throw std::runtime_error("Key has not been set for AES decryption.");
    }

    uint8_t state[4][4];
    for (int c = 0; c < NB; ++c) {
        for (int r = 0; r < 4; ++r) {
            state[r][c] = in[r + 4 * c];
        }
    }

    if (verbose_) {
        std::cout << "[AES DecryptBlock] Starting Decryption:" << std::endl;
        printRoundState(nr_, "Input", state);
    }

    // Initial inverse round key addition
    addRoundKey(state, nr_);
    if (verbose_) printRoundState(nr_, "AddRoundKey", state);

    // Rounds Nr - 1 down to 1: InvShiftRows -> InvSubBytes -> AddRoundKey -> InvMixColumns
    for (int r = nr_ - 1; r >= 1; --r) {
        invShiftRows(state);
        if (verbose_) printRoundState(r, "InvShiftRow", state);

        invSubBytes(state);
        if (verbose_) printRoundState(r, "InvSubBytes", state);

        addRoundKey(state, r);
        if (verbose_) printRoundState(r, "AddRoundKey", state);

        invMixColumns(state);
        if (verbose_) printRoundState(r, "InvMixCol  ", state);
    }

    // Round 0 (Final inverse round)
    invShiftRows(state);
    if (verbose_) printRoundState(0, "InvShiftRow", state);

    invSubBytes(state);
    if (verbose_) printRoundState(0, "InvSubBytes", state);

    addRoundKey(state, 0);
    if (verbose_) printRoundState(0, "AddRoundKey", state);

    for (int c = 0; c < NB; ++c) {
        for (int r = 0; r < 4; ++r) {
            out[r + 4 * c] = state[r][c];
        }
    }
}

std::vector<uint8_t> AES::encrypt(const std::vector<uint8_t>& plaintext, 
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
            throw std::invalid_argument("CBC mode requires a 16-byte IV for AES.");
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

std::vector<uint8_t> AES::decrypt(const std::vector<uint8_t>& ciphertext, 
                                  CipherMode mode, 
                                  const std::vector<uint8_t>& iv) const {
    if (ciphertext.empty() || ciphertext.size() % BLOCK_SIZE != 0) {
        throw std::invalid_argument("Ciphertext length must be a non-zero multiple of 16 bytes.");
    }
    std::vector<uint8_t> plaintext(ciphertext.size());

    if (mode == CipherMode::ECB) {
        for (size_t i = 0; i < ciphertext.size(); i += BLOCK_SIZE) {
            decryptBlock(&ciphertext[i], &plaintext[i]);
        }
    } else if (mode == CipherMode::CBC) {
        if (iv.size() != BLOCK_SIZE) {
            throw std::invalid_argument("CBC mode requires a 16-byte IV for AES.");
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

std::string AES::encryptString(const std::string& plaintext, 
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

std::string AES::decryptString(const std::string& ciphertextHex, 
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
