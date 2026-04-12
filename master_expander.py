import os
import json
import sys
import random
from datetime import datetime

# --- CONFIG ---
TARGET_FILE = "index.html"
SITEMAP_FILE = "sitemap.xml"

def run_automation():
    print("--- Starting Debugger Mode ---")
    
    # Check 1: Does index.html exist?
    if not os.path.exists(TARGET_FILE):
        print(f"CRITICAL ERROR: {TARGET_FILE} not found in root directory!")
        sys.exit(1)

    # Check 2: Load/Create Keywords
    if not os.path.exists('keywords.json'):
        print("Warning: keywords.json missing. Creating emergency file.")
        data = {"remaining": ["Tax Refund 2026", "IRS Deadline"], "used": []}
        with open('keywords.json', 'w') as f:
            json.dump(data, f)
    
    try:
        with open('keywords.json', 'r+') as f:
            data = json.load(f)
            if not data.get('remaining'):
                kw = "2026 Tax Filing"
            else:
                kw = data['remaining'].pop(0)
                data.setdefault('used', []).append(kw)
                f.seek(0)
                json.dump(data, f, indent=2)
                f.truncate()
    except Exception as e:
        print(f"ERROR reading keywords: {e}")
        kw = "2026 Tax Update"

    # Check 3: Read HTML and Inject
    try:
        with open(TARGET_FILE, "r", encoding="utf-8") as f:
            html = f.read()
        
        content = f"\n\n<div style='padding:20px; border:1px solid #ccc; margin-bottom:20px;'><h2>{kw}</h2><p>Updated for {datetime.now().strftime('%Y-%m-%d')}</p></div>"
        
        # Look for body tag if marker is missing
        if "</body>" in html:
            new_html = html.replace("</body>", content + "</body>")
            with open(TARGET_FILE, "w", encoding="utf-8") as f:
                f.write(new_html)
            print(f"SUCCESS: Injected content for {kw}")
        else:
            print("CRITICAL ERROR: No </body> tag found in index.html!")
            sys.exit(1)

    except Exception as e:
        print(f"CRITICAL ERROR during injection: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_automation()
