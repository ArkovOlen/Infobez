def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes([x^y for x, y in zip(a,b)])

def to_hex(b: bytes) -> str:
    return b.hex().upper()

def from_hex(s: str) -> bytes:
    return bytes.fromhex(s)

def print_hex(label, b):
    print(f"{label} (hex): {to_hex(b)}")

def main():
    P1 = "НаВашисходящийот1204"
    P2 = "ВСеверныйфилиалБанка"
    P2 = "ВСеверныйфилиалБанка"

    print("Открытие сообщения: ")
    print(f"P1: {P1}")
    print(f"P2: {P2}")

    p1_bytes = P1.encode("utf-8")[:20]
    p2_bytes = P2.encode("utf-8")[:20]

    if len(p1_bytes) != len(p2_bytes):
        raise ValueError("Cообщения должны быть одинаковой длинны в байтах")

    key_hex = "050C177F0E4E37D29410092E2257FFC80BB27054"
    key = from_hex(key_hex)

    if len(key) != len(p1_bytes):
        raise ValueError("Ключ не совпадает по длине с сообщениями")

    c1 = xor_bytes(p1_bytes, key)
    c2 = xor_bytes(p2_bytes, key)

    print("\nШифртексты:")
    print_hex("C1", c1)
    print_hex("C2", c2)

    p1_xor_p2 = xor_bytes(c1, c2)
    print("\nP1 ⊕ P2 (Может получить злоумышленник): ")
    print_hex("P1 ⊕ P2", p1_xor_p2)

    recovered_p2 = xor_bytes(p1_xor_p2, p1_bytes)
    print("\nP2, восстановление без ключа (по формуле С1⊕С2⊕Р1): ")
    print(f"P2 восстановлено: {recovered_p2.decode("utf-8")}")

    assert recovered_p2 == p2_bytes

if __name__ == "__main__":
    main()