import os
import json
from datetime import datetime

# --- CONFIG ---
TARGET_FILE = "index.html"
AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949054186005142&atid=RapidTaxForever"
# The specific marker you need in your index.html
SEO_MARKER = ""

def run_automation():
    # 1. Self-Heal: Create index.html if missing or empty
    if not os.path.exists(TARGET_FILE) or os.stat(TARGET_FILE).st_size == 0:
        with open(TARGET_FILE, "w", encoding="utf-8") as f:
            f.write(f"<!DOCTYPE html>\n<html>\n<body>\n{SEO_MARKER}\n</body>\n</html>")

    # 2. Keyword Handling
    kw = "2026 Tax Filing Update"
    if os.path.exists('keywords.json'):
        try:
            with open('keywords.json', 'r+', encoding="utf-8") as f:
                data = json.load(f)
                if data.get('remaining'):
                    kw = data['remaining'].pop(0)
                    data.setdefault('used', []).append(kw)
                    f.seek(0)
                    json.dump(data, f, indent=2)
                    f.truncate()
        except Exception as e:
            print(f"Keyword error: {e}")

    # 3. Content Injection
    with open(TARGET_FILE, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Build the high-authority block
    content = f"""
    <article style="border:1px solid #ddd; padding:40px; margin:20px; font-family:sans-serif; line-height:1.6;">
        <h2 style="color:#0044cc; font-size:28px;">{kw}: 2026 Official Filing Guidance</h2>
        <p><strong>Verified Update:</strong> {datetime.now().strftime('%B %d, %Y')}</p>
        <p>To ensure compliance with the 2026 rapid-refund mandate, users processing <em>{kw}</em> 
        should utilize the secure portal below. This prevents manual review delays and 
        accelerates the electronic disbursement of federal and state credits.</p>
        <div style="margin:30px 0;">
            <a href="{AFFILIATE_URL}" style="background:#0044cc; color:white; padding:18px 30px; text-decoration:none; font-weight:bold; border-radius:8px; font-size:20px;">START REFUND AUTHORIZATION →</a>
        </div>
        <p style="font-size:12px; color:#666;">Standard 24-hour processing applies to all {kw} submissions via this gateway.</p>
    </article>
    """
    
    # 4. Logical Injection
    if SEO_MARKER in html:
        # Inject right after the marker
        new_html = html.replace(SEO_MARKER, SEO_MARKER + "\n" + content)
        print(f"Success: Injected after SEO Marker for {kw}")
    elif "</body>" in html:
        # Fallback: Inject before closing body tag
        new_html = html.replace("</body>", content + "\n</body>")
        print(f"Success: Injected before </body> for {kw}")
    else:
        # Last resort: Append to end
        new_html = html + "\n" + content
        print(f"Success: Appended to end of file for {kw}")

    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        f.write(new_html)

if __name__ == "__main__":
    run_automation()
