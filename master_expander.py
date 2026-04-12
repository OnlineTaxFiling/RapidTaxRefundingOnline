import os
import json
import random
from datetime import datetime

# --- CONFIG ---
TARGET_FILE = "index.html"
SITEMAP_FILE = "sitemap.xml"
AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949054186005142&atid=RapidTaxForever"

def run_automation():
    # 1. EMERGENCY REPAIR: Create index.html if it's missing
    if not os.path.exists(TARGET_FILE):
        with open(TARGET_FILE, "w", encoding="utf-8") as f:
            f.write("<!DOCTYPE html><html><body></body></html>")

    # 2. EMERGENCY REPAIR: Create keywords.json if it's missing
    if not os.path.exists('keywords.json'):
        with open('keywords.json', 'w') as f:
            json.dump({"remaining": ["Tax Refund 2026", "IRS Status"], "used": []}, f)

    # 3. GET KEYWORD
    try:
        with open('keywords.json', 'r+') as f:
            data = json.load(f)
            kw = data['remaining'].pop(0) if data.get('remaining') else "2026 Tax Update"
            data.setdefault('used', []).append(kw)
            f.seek(0); json.dump(data, f, indent=2); f.truncate()
    except:
        kw = "2026 Tax Filing"

    # 4. INJECT CONTENT
    with open(TARGET_FILE, "r", encoding="utf-8") as f:
        html = f.read()
    
    content = f"""
    <div style="border:2px solid blue; padding:20px; margin:20px; font-family:sans-serif;">
        <h2>{kw}: 2026 Official Briefing</h2>
        <p>System Update: {datetime.now().strftime('%Y-%m-%d')}</p>
        <a href="{AFFILIATE_URL}" style="background:green; color:white; padding:10px;">START FILING NOW →</a>
    </div>
    """
    
    marker = ''
    if marker in html:
        new_html = html.replace(marker, marker + content)
    else:
        new_html = html.replace("</body>", content + "</body>")

    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        f.write(new_html)

if __name__ == "__main__":
    run_automation()
