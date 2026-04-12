import os
import json
from datetime import datetime

# --- CONFIG ---
TARGET_FILE = "index.html"
AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949054186005142&atid=RapidTaxForever"

def run_automation():
    # 1. Create index.html if it's missing (The "Self-Heal")
    if not os.path.exists(TARGET_FILE):
        with open(TARGET_FILE, "w", encoding="utf-8") as f:
            f.write("<!DOCTYPE html><html><body></body></html>")

    # 2. Setup Keyword
    kw = "2026 Tax Filing Update"
    if os.path.exists('keywords.json'):
        try:
            with open('keywords.json', 'r+') as f:
                data = json.load(f)
                if data.get('remaining'):
                    kw = data['remaining'].pop(0)
                    data.setdefault('used', []).append(kw)
                    f.seek(0); json.dump(data, f, indent=2); f.truncate()
        except: pass

    # 3. Inject Content
    with open(TARGET_FILE, "r", encoding="utf-8") as f:
        html = f.read()
    
    content = f"""
    <article style="border:1px solid #ddd; padding:20px; margin:20px; font-family:sans-serif;">
        <h2>{kw}</h2>
        <p>Verified for {datetime.now().strftime('%B %d, %Y')} - Secure Authorized Portal</p>
        <a href="{AFFILIATE_URL}" style="background:#0044cc; color:white; padding:15px; text-decoration:none; font-weight:bold; border-radius:5px;">START REFUND AUTHORIZATION →</a>
    </article>
    """
    
    marker = ''
    if marker in html:
        new_html = html.replace(marker, marker + content)
    else:
        new_html = html.replace("</body>", content + "</body>")

    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"Success: Deployed {kw}")

if __name__ == "__main__":
    run_automation()
