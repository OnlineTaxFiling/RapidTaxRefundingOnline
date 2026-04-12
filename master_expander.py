import os
import json
from datetime import datetime

# --- CONFIG ---
TARGET_FILE = "index.html"
AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949054186005142&atid=RapidTaxForever"

def run_automation():
    # 1. FORCE FILE EXISTENCE
    # If the file doesn't exist, create a clean one so the script doesn't crash
    if not os.path.exists(TARGET_FILE):
        with open(TARGET_FILE, "w", encoding="utf-8") as f:
            f.write("<!DOCTYPE html><html><head><title>Tax Prep 2026</title></head><body></body></html>")

    # 2. KEYWORD PICKER
    kw = "2026 Tax Filing Update"
    if os.path.exists('keywords.json'):
        try:
            with open('keywords.json', 'r+', encoding="utf-8") as f:
                data = json.load(f)
                if data.get('remaining'):
                    kw = data['remaining'].pop(0)
                    data.setdefault('used', []).append(kw)
                    f.seek(0); json.dump(data, f, indent=2); f.truncate()
        except: pass

    # 3. CONTENT GENERATION
    content = f"""
    <div style="border:2px solid #0044cc; padding:30px; margin:20px; font-family:sans-serif;">
        <h2 style="color:#0044cc;">{kw}</h2>
        <p><strong>Verified:</strong> {datetime.now().strftime('%B %d, %Y')}</p>
        <p>Official 2026 processing for {kw} is now active. Use the secure gateway to ensure your refund is authorized within the 24-hour rapid window.</p>
        <a href="{AFFILIATE_URL}" style="background:#0044cc; color:white; padding:15px; text-decoration:none; font-weight:bold; border-radius:5px; display:inline-block; margin-top:10px;">START REFUND NOW →</a>
    </div>
    """

    # 4. INJECTION (Simple & Safe)
    with open(TARGET_FILE, "r", encoding="utf-8") as f:
        html = f.read()
    
    # We look for the SEO marker, but if it's missing, we just shove it in the body
    if "" in html:
        new_html = html.replace("", "" + content)
    elif "</body>" in html:
        new_html = html.replace("</body>", content + "</body>")
    else:
        new_html = html + content # Last resort

    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        f.write(new_html)
    
    print(f"Success: Deployed {kw}")

if __name__ == "__main__":
    run_automation()
