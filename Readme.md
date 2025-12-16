# Payload Encoder & Obfuscation Framework

A simple Python CLI tool that demonstrates how **encoding and obfuscation** can bypass **basic signature-based detection**.
Built for **educational and lab use only**.

---

## What this tool does

* Encodes a payload using **Base64, XOR, and ROT13**
* Applies basic **string obfuscation**
* Tests each version against a **simulated signature-based detector**
* Shows which payloads are **Detected** or **Bypassed**
* Saves results to a file

---

## Requirements

* Python 3.x
* No external libraries

---

## Setup

### Download

* Click **Code → Download ZIP**, extract it
  **or**

```bash
git clone https://github.com/YOUR_USERNAME/payload-encoder-obfuscation-framework.git
cd payload-encoder-obfuscation-framework
```

---

## Usage

```bash
python payload_obfuscation_tool.py -p "cmd.exe /c whoami"
```

Optional XOR key:

```bash
python payload_obfuscation_tool.py -p "powershell test" -k secret
```

---

## Example Output

```
Original Payload: Detected
Base64 Encoded: Bypassed
XOR Encoded: Bypassed
ROT13 Encoded: Bypassed
ROT13 + Obfuscation: Bypassed
```

---

## How detection works

The tool uses simple keyword matching (e.g. `cmd.exe`, `powershell`) to simulate **signature-based detection**.
Encoded and obfuscated payloads bypass this detection.

---

## Files

```
payload-encoder-obfuscation-framework/
├── payload_obfuscation_tool.py
└── README.md
```

---

## Disclaimer

For **educational purposes only**.
No real malware, no live system testing.

---

## Author

Vedant Hore
