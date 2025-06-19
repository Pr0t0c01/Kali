#!/usr/bin/python3

import argparse
import base64
import codecs
from itertools import permutations

# Function to decode Base64
def decode_base64(ciphertext):
    try:
        return base64.b64decode(ciphertext).decode('utf-8')
    except Exception:
        return None

# Function to decode base32
def decode_base32(ciphertext):
    try:
        decoded = base64.b32decode(encoded_text).decode("utf-8")
        return decoded
    except Exception:
        return None

# Function to decode base16
def decode_base16(ciphertext):
    try:
        decoded = base64.b16decode(encoded_text).decode("utf-8")
        return decoded
    except Exception:
        return None

# Function to decode Hexadecimal
def decode_hex(ciphertext):
    try:
        return bytes.fromhex(ciphertext).decode('utf-8')
    except Exception:
        return None

# Function for Caesar Cipher
def decode_caesar(ciphertext):
    results = []
    for shift in range(1, 26):
        decoded = ''.join(
            chr(((ord(char) - shift - 65) % 26) + 65) if char.isupper() else
            chr(((ord(char) - shift - 97) % 26) + 97) if char.islower() else char
            for char in ciphertext
        )
        results.append(f"Shift {shift}: {decoded}")
    return results

# Function to decode ROT13
def decode_rot13(ciphertext):
    return codecs.decode(ciphertext, 'rot_13')

# Function to brute-force XOR
def decode_xor(ciphertext):
    results = []
    for key in range(256):  # Iterate through all possible 1-byte keys
        decoded = ''.join(chr(ord(c) ^ key) for c in ciphertext)
        if all(32 <= ord(char) <= 126 for char in decoded):  # Printable ASCII check
            results.append(f"Key {key}: {decoded}")
    return results

# Function for Atbash Cipher
def decode_atbash(ciphertext):
    decoded = ''.join(
        chr(219 - ord(char)) if char.islower() else
        chr(155 - ord(char)) if char.isupper() else char
        for char in ciphertext
    )
    return decoded

# Main function to decode the input
def decode_all_methods(ciphertext):
    print("[*] Trying Base64 decoding...")
    base64_result = decode_base64(ciphertext)
    if base64_result:
        print(f"Base64 decoded: {base64_result}")
    else:
        print("Base64 decoding failed.")

    print("\n[*] Trying Base32 decoding...")
    base32_result = decode_base32(ciphertext)
    if base32_result:
        print(f"Base32 decoded: {base32_result}")
    else:
        print("Base32 decoding failed.")

    print("\n[*] Trying Base16 decoding...")
    base16_result = decode_base16(ciphertext)
    if base16_result:
        print(f"Base16 decoded: {base16_result}")
    else:
        print("Base16 decoding failed.")

    print("\n[*] Trying Hexadecimal decoding...")
    hex_result = decode_hex(ciphertext)
    if hex_result:
        print(f"Hexadecimal decoded: {hex_result}")
    else:
        print("Hexadecimal decoding failed.")

    print("\n[*] Trying Caesar Cipher decoding...")
    caesar_results = decode_caesar(ciphertext)
    for result in caesar_results:
        print(result)

    print("\n[*] Trying ROT13 decoding...")
    print(f"ROT13 decoded: {decode_rot13(ciphertext)}")

    print("\n[*] Trying XOR brute force...")
    xor_results = decode_xor(ciphertext)
    for result in xor_results[:10]:  # Print first 10 results to avoid overload
        print(result)

    print("\n[*] Trying Atbash decoding...")
    print(f"Atbash decoded: {decode_atbash(ciphertext)}")

# Argument parser setup
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decode cipher text using various methods.")
    parser.add_argument("ciphertext", type=str, help="Cipher text to decode")
    args = parser.parse_args()

    print(f"[*] Decoding ciphertext: {args.ciphertext}\n")
    decode_all_methods(args.ciphertext)
