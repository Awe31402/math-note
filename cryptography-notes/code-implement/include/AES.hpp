#ifndef AES_HPP
#define AES_HPP

#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include "BlockCipher.hpp"
#include "GF256.hpp"

namespace crypto {

/**
 * @brief Advanced Encryption Standard (AES) Implementation.
 * 
 * Compliant with NIST FIPS 197.
 * Substitution-Permutation Network (SPN) with 128-bit block size.
 * Supports AES-128 (10 rounds), AES-192 (12 rounds), and AES-256 (14 rounds).
 * Corresponds to Lectures 07 & 08 and Book Chapter 6.
 */
class AES {
public:
    enum class KeySize {
        AES128 = 128,
        AES192 = 192,
        AES256 = 256
    };

    static constexpr size_t BLOCK_SIZE = 16; // 128 bits = 16 bytes
    static constexpr int NB = 4;             // Block size in 32-bit words (always 4)

    explicit AES(KeySize keySize = KeySize::AES128);
    explicit AES(const std::vector<uint8_t>& key, KeySize keySize = KeySize::AES128);
    explicit AES(const std::string& keyStr, KeySize keySize = KeySize::AES128);

    // Key management and key expansion
    void setKey(const std::vector<uint8_t>& key, KeySize keySize = KeySize::AES128);
    void setKey(const std::string& keyStr, KeySize keySize = KeySize::AES128);

    // Single 128-bit block operations
    void encryptBlock(const uint8_t in[16], uint8_t out[16]) const;
    void decryptBlock(const uint8_t in[16], uint8_t out[16]) const;

    // Multi-block encryption and decryption (ECB or CBC, with PKCS#7 padding)
    std::vector<uint8_t> encrypt(const std::vector<uint8_t>& plaintext, 
                                 CipherMode mode = CipherMode::ECB, 
                                 const std::vector<uint8_t>& iv = {}) const;

    std::vector<uint8_t> decrypt(const std::vector<uint8_t>& ciphertext, 
                                 CipherMode mode = CipherMode::ECB, 
                                 const std::vector<uint8_t>& iv = {}) const;

    // Helper functions for string processing
    std::string encryptString(const std::string& plaintext, 
                              CipherMode mode = CipherMode::ECB, 
                              const std::string& iv = "") const;

    std::string decryptString(const std::string& ciphertextHex, 
                              CipherMode mode = CipherMode::ECB, 
                              const std::string& iv = "") const;

    // Verbose logging for pedagogical demonstration (round-by-round state)
    void setVerbose(bool verbose) { verbose_ = verbose; }
    bool isVerbose() const { return verbose_; }

    // Inspect expanded key words
    const std::vector<uint32_t>& getExpandedKey() const { return expandedKey_; }
    int getNr() const { return nr_; }
    int getNk() const { return nk_; }

    // Static standard lookup tables (FIPS 197)
    static const std::array<uint8_t, 256> S_BOX;
    static const std::array<uint8_t, 256> INV_S_BOX;
    static const std::array<uint8_t, 15> RCON;

private:
    KeySize keySize_ = KeySize::AES128;
    int nk_ = 4;  // Key length in 32-bit words (4, 6, 8)
    int nr_ = 10; // Number of rounds (10, 12, 14)
    std::vector<uint32_t> expandedKey_;
    bool verbose_ = false;

    // Core algorithmic steps
    void keyExpansion(const std::vector<uint8_t>& key);
    static uint32_t rotWord(uint32_t w);
    static uint32_t subWord(uint32_t w);

    // Round operations
    static void subBytes(uint8_t state[4][4]);
    static void invSubBytes(uint8_t state[4][4]);
    static void shiftRows(uint8_t state[4][4]);
    static void invShiftRows(uint8_t state[4][4]);
    static void mixColumns(uint8_t state[4][4]);
    static void invMixColumns(uint8_t state[4][4]);
    void addRoundKey(uint8_t state[4][4], int round) const;

    void printRoundState(int round, const std::string& step, const uint8_t state[4][4]) const;
};

} // namespace crypto

#endif // AES_HPP
