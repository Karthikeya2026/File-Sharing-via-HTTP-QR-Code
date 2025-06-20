import http.server
import socketserver
import qrcode
import os
import socket
import webbrowser

# === Configuration ===
PORT = 8000
FILE_NAME = "shared_file.txt"

# === Create File (if not exists) ===
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        f.write("This is a sample file for sharing over Wi-Fi.")

# === Get Local IP ===
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# === Generate Download Link ===
url = f"http://{ip_address}:{PORT}/{FILE_NAME}"
print(f"✅ File ready at: {url}")

# === Generate QR Code ===
qr = qrcode.make(url)
qr_file = "qr_code.png"
qr.save(qr_file)
print("📱 QR Code saved as qr_code.png (Scan it to download)")

# === Optionally open QR in default viewer ===
try:
    webbrowser.open(qr_file)
except:
    pass

# === Start HTTP Server ===
handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), handler)
print(f"🌐 Serving file on http://{ip_address}:{PORT} ... Press Ctrl+C to stop.")
httpd.serve_forever()
