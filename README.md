# PRODIGY_CS_02
# Pixel Manipulation Image Encryption

This project is a simple Image Encryption & Decryption tool using pixel manipulation in Python.

## How it works
- The program encrypts an image by applying XOR operation to each pixel value using a secret key (0–255).
- The same key is used again to decrypt the image back to its original form.

## Tech Used
- Python
- Pillow (PIL)
- NumPy

## Installation
```bash
pip install pillow numpy
Run the Program
python image_encryptor.py

Example

Encrypt:

Input Image: photo.png

Output: encrypted.png

Key: 123

Decrypt:

Input Image: encrypted.png

Output: decrypted.png

Key: 123

---
