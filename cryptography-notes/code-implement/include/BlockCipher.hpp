#ifndef BLOCK_CIPHER_HPP
#define BLOCK_CIPHER_HPP

#include <cstdint>
#include <vector>
#include <string>
#include <stdexcept>
#include <iostream>
#include <iomanip>

namespace crypto {

enum class CipherMode {
    ECB, // Electronic Codebook
    CBC  // Cipher Block Chaining
};

// Utilities for hexadecimal conversions
std::string bytesToHex(const uint8_t* data, size_t len, bool upper = true);
std::string bytesToHex(const std::vector<uint8_t>& data, bool upper = true);
std::vector<uint8_t> hexToBytes(const std::string& hexStr);

// Utilities for PKCS#7 padding
std::vector<uint8_t> addPKCS7Padding(const std::vector<uint8_t>& data, size_t blockSize);
std::vector<uint8_t> removePKCS7Padding(const std::vector<uint8_t>& data);

// Debug helper for 4x4 AES state matrix
void printStateMatrix(const uint8_t state[4][4], const std::string& label = "");

} // namespace crypto

#endif // BLOCK_CIPHER_HPP
