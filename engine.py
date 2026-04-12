import os
import json
from datetime import datetime

# --- CONFIG ---
TARGET_FILE = "index.html"
SITEMAP_FILE = "sitemap.xml"
BASE_URL = "https://brightlane.github.io/OnlineTaxFiling/" 
AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949054186005142&atid=RapidTaxForever"

def run_automation():
    # 1. KEYWORD LOGIC
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

    # 2. FRESH BUILD HTML (Do not remove this!)
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{kw} | 2026 Rapid Tax Portal</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-50 text-slate-900 font-sans">
    <div class="max-w-4xl mx-auto py-20 px-6">
        <header class="mb-12 border-b pb-8">
            <h1 class="text-4xl font-black text-blue-900 uppercase tracking-tighter italic">OnlineTaxFiling</h1>
            <p class="text-slate-500 font-bold uppercase text-xs tracking-widest mt-2">Authorized 2026 Disbursement Gateway</p>
        </header>
        <main>
            <article class="bg-white p-10 rounded-[40px] shadow-2xl border border-slate-200">
                <div class="inline-block bg-blue-600 text-white text-[10px] font-black px-4 py-1 rounded-full mb-6 uppercase">
                    System Verified: {datetime.now().strftime('%B %d, %Y')}
                </div>
                <h2 class="text-4xl md:text-6xl font-black text-slate-900 mb-6 leading-none tracking-tight">{kw}</h2>
                <div class="bg-slate-900 p-8 rounded-3xl text-center shadow-xl mt-8">
                    <a href="{AFFILIATE_URL}" class="inline-block bg-green-500 hover:bg-green-600 text-white text-2xl font-black py-6 px-12 rounded-2xl transition-all hover:scale-105 shadow-lg">START FILING NOW →</a>
                </div>
            </article>
        </main>
    </div>
</body>
</html>"""

    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        f.write(full_html)

    # 3. THE SITEMAP DETECTOR ENGINE
    print("Detecting files for sitemap...")
    now_iso = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+00:00')
    
    # Detect all .html files
    detected_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    sitemap_entries = ""
    for file in detected_files:
        url_path = "" if file == "index.html" else file
        sitemap_entries += f"""
  <url>
    <loc>{BASE_URL}{url_path}</loc>
    <lastmod>{now_iso}</lastmod>
    <changefreq>daily</changefreq>
    <priority>{"1.0" if file == "index.html" else "0.8"}</priority>
  </url>"""

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.1">
{sitemap_entries}
</urlset>"""

    with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    
    print(f"Success: Rebuilt index and detected {len(detected_files)} pages for sitemap.")

if __name__ == "__main__":
    run_automation()
