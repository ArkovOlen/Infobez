import os


def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes([x^y for x, y in zip(a,b)])
    
def encrypt(plaintext: str, key: bytes) -> bytes:
    plaintext_bytes = plaintext.encode("utf-8")
    if len(plaintext_bytes) != len(key):
        raise ValueError("Длина ключа должна совпадать с длиной текста в байтах")
    return xor_bytes(plaintext_bytes, key)

def decrypt(ciphertext: bytes, key: bytes) -> str:
    if len(ciphertext) != len(key):
        raise ValueError("Длины шифртекста и ключа должны совпадать")
    decrypted_bytes = xor_bytes(ciphertext, key)
    return decrypted_bytes.decode("utf-8", errors = "replace")
    
def find_key(ciphertext: bytes, plaintext: str) -> bytes:
    plaintext_bytes = plaintext.encode("utf-8")
    if len(ciphertext) != len(plaintext_bytes):
        raise ValueError("Длины текста и шифртекста должны совпадать")
    return xor_bytes(ciphertext, plaintext_bytes)
    
def main():
    plaintext = "С Новым Годом, друзья!"
    print(f"Открытый текст: {plaintext}")
    
    plaintext_bytes = plaintext.encode("utf-8")
    print(f"Длина в байтах: {len(plaintext_bytes)}")
    
    key = os.urandom(len(plaintext_bytes))
    print(f"Случайный ключ (hex): {key.hex().upper()}")
    
    ciphertext = encrypt(plaintext, key)
    print(f"Зашифрованный текст (hex): {ciphertext.hex().upper()}")
    
    recovered_key = find_key(ciphertext, plaintext)
    print(f"Восстановленый ключ (hex): {recovered_key.hex().upper()}")
    
    decrypted = decrypt(ciphertext, key)
    print(f"Восстановленный ключ (hex): {recovered_key.hex().upper()}")
    
    print("Ключи совпадают:", key == recovered_key)
    


if __name__ == "__main__":
    main()