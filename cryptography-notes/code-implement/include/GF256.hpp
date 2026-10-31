#ifndef GF256_HPP
#define GF256_HPP

#include <cstdint>
#include <array>
#include <vector>

namespace crypto {

/**
 * @brief Galois Field GF(2^8) arithmetic implementation.
 * Uses irreducible polynomial P(x) = x^8 + x^4 + x^3 + x + 1 (0x11B).
 * Directly correlates with Lecture 07 and Book Chapter 6.
 */
class GF256 {
public:
    // AES Irreducible Polynomial: x^8 + x^4 + x^3 + x + 1
    static constexpr uint16_t IRREDUCIBLE_POLY = 0x11B;

    // Generator element in GF(2^8): g(x) = x + 1 (0x03)
    static constexpr uint8_t GENERATOR = 0x03;

    // Addition in GF(2^8) is bitwise XOR
    static inline uint8_t add(uint8_t a, uint8_t b) {
        return a ^ b;
    }

    // xtime: Multiplication by x (0x02) modulo P(x)
    static uint8_t xtime(uint8_t a);

    // Multiplication via shift-and-add (polynomial modulo P(x))
    static uint8_t multiply(uint8_t a, uint8_t b);

    // Multiplication via Log/Alog tables (generator g=0x03, as used in Book Chapter 6)
    static uint8_t mulLogAlog(uint8_t a, uint8_t b);

    // Multiplicative inverse in GF(2^8): a^(-1) where 0^(-1) = 0
    static uint8_t inverse(uint8_t a);

    // Affine transformation for AES S-box generation (Lecture 08 §4.3)
    static uint8_t affineTransform(uint8_t b);

    // Inverse affine transformation for Inv S-box (Lecture 08 §9.2)
    static uint8_t invAffineTransform(uint8_t b);

    // Compute S-box byte dynamically: Inv + Affine
    static uint8_t computeSBox(uint8_t b);

    // Compute Inverse S-box byte dynamically: InvAffine + Inv
    static uint8_t computeInvSBox(uint8_t b);

    // Tables used for fast log/alog multiplication (Book Chapter 6)
    static const std::array<uint8_t, 256> LogTable;
    static const std::array<uint8_t, 256> AlogTable;
};

} // namespace crypto

#endif // GF256_HPP
