from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path).convert("RGB")
    img_array = np.array(img)

    # XOR encryption (pixel manipulation)
    encrypted_array = img_array ^ key

    encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))
    encrypted_img.save(output_path)

    print(f"✅ Image encrypted successfully!\nSaved as: {output_path}")


def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path).convert("RGB")
    img_array = np.array(img)

    # XOR again to decrypt
    decrypted_array = img_array ^ key

    decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))
    decrypted_img.save(output_path)

    print(f"✅ Image decrypted successfully!\nSaved as: {output_path}")


def main():
    print("\n--- Pixel Manipulation Image Encryption Tool ---")
    print("1. Encrypt Image")
    print("2. Decrypt Image")

    choice = input("Enter your choice (1/2): ").strip()

    input_path = input("Enter image path: ").strip()
    output_path = input("Enter output file name (with extension): ").strip()

    try:
        key = int(input("Enter key (0 to 255): ").strip())
        if key < 0 or key > 255:
            print("❌ Key must be between 0 and 255")
            return
    except ValueError:
        print("❌ Key must be a number")
        return

    if choice == "1":
        encrypt_image(input_path, output_path, key)
    elif choice == "2":
        decrypt_image(input_path, output_path, key)
    else:
        print("❌ Invalid choice. Enter 1 or 2.")


if __name__ == "__main__":
    main()
