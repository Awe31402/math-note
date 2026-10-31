#ifndef DES_HPP
#define DES_HPP

#include <cstdint>
#include <array>
#include <vector>
#include <string>
#include "BlockCipher.hpp"

namespace crypto {

/**
 * @brief Data Encryption Standard (DES) Implementation.
 * 
 * Compliant with NIST FIPS 46-3.
 * Feistel cipher architecture with 16 rounds, 64-bit block size, and 56-bit effective key.
 * Corresponds to Lectures 05 & 06 and Book Chapter 5.
 */
class DES {
public:
    static constexpr size_t BLOCK_SIZE = 8;  // 64 bits = 8 bytes
    static constexpr size_t KEY_SIZE   = 8;  // 64 bits (56 bits + 8 parity bits)
    static constexpr size_t NUM_ROUNDS = 16; // 16 Feistel rounds

    DES();
    explicit DES(uint64_t key64);
    explicit DES(const std::vector<uint8_t>& key);
    explicit DES(const std::string& keyStr);

    // Key schedule generation (PC-1, left shifts, PC-2)
    void keygen(uint64_t key64);
    void setKey(const std::vector<uint8_t>& key);
    void setKey(const std::string& keyStr);

    // Single 64-bit block operations
    uint64_t encryptBlock(uint64_t block) const;
    uint64_t decryptBlock(uint64_t block) const;
    void encryptBlock(const uint8_t in[8], uint8_t out[8]) const;
    void decryptBlock(const uint8_t in[8], uint8_t out[8]) const;

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

    // Inspect generated subkeys (48 bits each)
    const std::array<uint64_t, NUM_ROUNDS>& getSubkeys() const { return subkeys_; }

    // Helper conversion between byte array and 64-bit integer (Big Endian)
    static uint64_t bytesToUint64(const uint8_t bytes[8]);
    static void uint64ToBytes(uint64_t val, uint8_t bytes[8]);

private:
    std::array<uint64_t, NUM_ROUNDS> subkeys_{};
    bool verbose_ = false;

    // Internal primitive operations matching Lecture 05/06 and Book Chapter 5
    static uint64_t permute(uint64_t in, const uint8_t* table, int inBits, int outBits);
    static uint64_t initialPermutation(uint64_t block);
    static uint64_t finalPermutation(uint64_t block);
    static uint64_t expansion(uint32_t r32);
    static uint32_t substitution(uint64_t expXorKey);
    static uint32_t permutationP(uint32_t sOut);
    static uint32_t roundFunctionF(uint32_t r32, uint64_t subkey);

    // Standard tables from FIPS 46-3
    static const uint8_t IP_TABLE[64];
    static const uint8_t FP_TABLE[64];
    static const uint8_t PC1_TABLE[56];
    static const uint8_t PC2_TABLE[48];
    static const uint8_t EXPANSION_TABLE[48];
    static const uint8_t P_TABLE[32];
    static const uint8_t S_BOXES[8][4][16];
    static const uint8_t SHIFT_SCHEDULE[16];
};

} // namespace crypto

#endif // DES_HPP
