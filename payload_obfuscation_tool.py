import base64
import argparse
import random
import string

# ----------------------------
# Encoding Functions
# ----------------------------
def base64_encode(data):
    return base64.b64encode(data.encode()).decode()

def xor_encode(data, key):
    encoded = ""
    for i in range(len(data)):
        encoded += chr(ord(data[i]) ^ ord(key[i % len(key)]))
    return encoded

def rot13_encode(data):
    result = ""
    for char in data:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + 13) % 26 + offset)
        else:
            result += char
    return result

# ----------------------------
# Obfuscation
# ----------------------------
def random_insertion(data):
    junk = random.choice(string.ascii_letters)
    return junk.join(data)

def split_concat(data):
    mid = len(data) // 2
    return data[:mid] + data[mid:]

# ----------------------------
# Detection Logic
# ----------------------------
def signature_detect(data):
    signatures = ["cmd.exe", "powershell", "whoami", "bash"]
    for sig in signatures:
        if sig in data.lower():
            return "Detected"
    return "Bypassed"

# ----------------------------
# Main Tool
# ----------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Custom Payload Encoder & Obfuscation Framework"
    )
    parser.add_argument(
        "-p", "--payload",
        required=True,
        help="Payload string to test"
    )
    parser.add_argument(
        "-k", "--key",
        default="key",
        help="XOR encoding key (optional)"
    )

    args = parser.parse_args()
    payload = args.payload
    key = args.key

    results = []

    results.append(("Original Payload", payload, signature_detect(payload)))

    b64 = base64_encode(payload)
    results.append(("Base64 Encoded", b64, signature_detect(b64)))

    xor = xor_encode(payload, key)
    results.append(("XOR Encoded", xor, signature_detect(xor)))

    rot = rot13_encode(payload)
    results.append(("ROT13 Encoded", rot, signature_detect(rot)))

    obf = random_insertion(rot)
    results.append(("ROT13 + Obfuscation", obf, signature_detect(obf)))

    print("\n--- Payload Evasion Test Results ---\n")
    for name, data, status in results:
        print(f"{name}: {status}")

    with open("results.txt", "w") as f:
        for name, data, status in results:
            f.write(f"{name}: {status}\n")

if __name__ == "__main__":
    main()
