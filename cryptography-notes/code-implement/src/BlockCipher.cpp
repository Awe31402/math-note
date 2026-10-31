#include "BlockCipher.hpp"
#include <sstream>
#include <cctype>

namespace crypto {

std::string bytesToHex(const uint8_t* data, size_t len, bool upper) {
    std::ostringstream oss;
    oss << std::hex << std::setfill('0');
    if (upper) oss << std::uppercase;
    for (size_t i = 0; i < len; ++i) {
        oss << std::setw(2) << static_cast<int>(data[i]);
    }
    return oss.str();
}

std::string bytesToHex(const std::vector<uint8_t>& data, bool upper) {
    return bytesToHex(data.data(), data.size(), upper);
}

std::vector<uint8_t> hexToBytes(const std::string& hexStr) {
    std::vector<uint8_t> bytes;
    std::string clean;
    for (char c : hexStr) {
        if (!std::isspace(static_cast<unsigned char>(c)) && c != ':' && c != '-') {
            clean.push_back(c);
        }
    }
    if (clean.size() >= 2 && clean[0] == '0' && (clean[1] == 'x' || clean[1] == 'X')) {
        clean = clean.substr(2);
    }
    if (clean.size() % 2 != 0) {
        throw std::invalid_argument("Hex string must have an even number of hex digits.");
    }
    for (size_t i = 0; i < clean.size(); i += 2) {
        std::string byteString = clean.substr(i, 2);
        char* endPtr = nullptr;
        unsigned long byteVal = std::strtoul(byteString.c_str(), &endPtr, 16);
        if (*endPtr != '\0') {
            throw std::invalid_argument("Invalid hex character in string: " + byteString);
        }
        bytes.push_back(static_cast<uint8_t>(byteVal));
    }
    return bytes;
}

std::vector<uint8_t> addPKCS7Padding(const std::vector<uint8_t>& data, size_t blockSize) {
    if (blockSize == 0 || blockSize > 255) {
        throw std::invalid_argument("Invalid block size for PKCS#7 padding.");
    }
    size_t padLen = blockSize - (data.size() % blockSize);
    if (padLen == 0) {
        padLen = blockSize;
    }
    std::vector<uint8_t> padded = data;
    padded.insert(padded.end(), padLen, static_cast<uint8_t>(padLen));
    return padded;
}

std::vector<uint8_t> removePKCS7Padding(const std::vector<uint8_t>& data) {
    if (data.empty()) {
        throw std::invalid_argument("Data is empty, cannot remove padding.");
    }
    uint8_t padLen = data.back();
    if (padLen == 0 || padLen > data.size()) {
        throw std::runtime_error("Invalid PKCS#7 padding length.");
    }
    for (size_t i = data.size() - padLen; i < data.size(); ++i) {
        if (data[i] != padLen) {
            throw std::runtime_error("Invalid PKCS#7 padding pattern.");
        }
    }
    return std::vector<uint8_t>(data.begin(), data.end() - padLen);
}

void printStateMatrix(const uint8_t state[4][4], const std::string& label) {
    if (!label.empty()) {
        std::cout << label << ":" << std::endl;
    }
    for (int r = 0; r < 4; ++r) {
        std::cout << "  ";
        for (int c = 0; c < 4; ++c) {
            std::cout << std::hex << std::setfill('0') << std::setw(2)
                      << static_cast<int>(state[r][c]) << " ";
        }
        std::cout << std::dec << std::endl;
    }
}

} // namespace crypto
