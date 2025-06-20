# 📁 File Sharing with Python + QR Code

This is a lightweight Python project that allows you to **share a file over Wi-Fi** using a simple **HTTP server** and generates a **QR code** so any device (like a smartphone) on the same network can scan and download the file.

No external servers. No complex setup. Just Python and Wi-Fi!

---

## 🚀 Features

- Share any file from your computer with just one script
- Automatically generates a QR code for mobile users
- No need for USB or third-party apps
- Works on LAN/Wi-Fi — ideal for classroom or home networks

---

## 🛠️ Tech Stack

- Python 3.x
- [qrcode](https://pypi.org/project/qrcode/)
- Standard libraries: `http.server`, `socket`, `os`, `webbrowser`

---

## 🔧 Requirements

Install `qrcode` with Pillow (image support):

```bash
pip install qrcode[pil]
