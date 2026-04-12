import os
import json
import requests
import random
from datetime import datetime

# --- 1. CORE CONFIGURATION ---
# Your fixed LinkConnector heartbeat
AFFILIATE_BASE = "https://www.linkconnector.com/ta.php?lc=007949054186005142"
TRACKING_ID = "RapidTaxForever" 
TARGET_FILE = "index.html"
SITEMAP_FILE = "sitemap.xml"

# --- 2. THE DYNAMIC KNOWLEDGE BASE (LAW ROTATION) ---
TAX_LAWS_2026 = [
    "the new OBBB 24-hour rapid refund mandate for digital filers",
    "updated standard deductions for independent contractors under the 2026 Act",
    "new audit-flags for digital currency transactions and overseas assets",
    "the emergency filing extension protocols for high-volume 2026 traffic",
    "Section 402(b) compliance regarding automated refund routing"
]

TAX_LAWS_2027_PREVIEW = [
    "early directives for the 2027 season indicating a shift toward AI-verified filing",
    "proposed increases in child tax credits for the upcoming 2027 fiscal cycle",
    "new electronic signature requirements taking effect after December 31st",
    "the 2027 'Smart-File' initiative for multi-state income earners"
]

def get_dynamic_law():
    """Pivots content based on the calendar to keep SEO fresh forever."""
    month = datetime.now().month
    # If it's late in the year (Oct-Dec), start talking about 2027
    if month > 9: 
        return random.choice(TAX_LAWS_2027_PREVIEW)
    return random.choice(TAX_LAWS_2026)

# --- 3. AUTOMATION LOGIC ---
def get_next_keyword():
    if not os.path.exists('keywords.json'):
        print("Error: keywords.json not found!")
        return None
        
    with open('keywords.json', 'r+') as f:
        data = json.load(f)
        if not data.get('remaining'):
            print("No keywords left in 'remaining' list.")
            return None
        
        kw = data['remaining'].pop(0)
        data.setdefault('used', []).append(kw)
        
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()
    return kw

def build_monster_block(kw):
    law_snippet = get_dynamic_law()
    full_url = f"{AFFILIATE_BASE}&atid={TRACKING_ID}"
    timestamp = datetime.now().strftime("%B %d, %Y")
    
    return f"""
    <article class="bg-white p-8 md:p-12 rounded-3xl shadow-sm border border-slate-200 mb-12 transform transition hover:shadow-md">
        <div class="flex items-center space-x-3 mb-6">
            <span class="bg-blue-600 text-white text-xs font-black px-3 py-1 rounded-full uppercase">Update: {timestamp}</span>
            <span class="text-slate-400 text-xs font-bold uppercase tracking-widest border-l pl-3">OBBB Verified</span>
        </div>
        
        <h2 class="text-3xl md:text-5xl font-black text-blue-900 mb-6 tracking-tighter leading-tight">
            {kw}: Critical 2026 Compliance Update
        </h2>
        
        <div class="prose prose-slate max-w-none text-slate-600 text-lg leading-relaxed">
            <p class="mb-6">
                Analyzing <strong>{kw}</strong> requires staying current with federal mandates. 
                As of {timestamp}, our systems have prioritized <strong>{kw}</strong> for 
                rapid-channel processing to avoid common 2026 audit triggers.
            </p>
            
            <div class="my-8 p-6 bg-blue-50 border-l-8 border-blue-600 rounded-r-xl italic font-medium text-blue-900">
                "Technical Directive: Integration of {law_snippet} is critical for ensuring 
                immediate refund authorization during the current cycle."
            </div>

            <p class="mb-8">
                By utilizing our authorized {kw} submission portal, filers can leverage 
                {law_snippet} to bypass manual review queues. This ensures your data 
                meets the highest security standards for 2026.
            </p>

            <div class="text-center bg-slate-900 p-8 rounded-2xl shadow-2xl">
                <h3 class="text-white text-2xl font-bold mb-4 uppercase">Authorized {kw} Portal</h3>
                <a href="{full_url}" class="inline-block bg-green-500 hover:bg-green-600 text-white text-2xl font-black py-5 px-12 rounded-xl transition transform hover:scale-105">
                    CLAIM MY REFUND NOW →
                </a>
            </div>
        </div>
    </article>
    """

def run_automation():
    kw = get_next_keyword()
    if not kw: return

    new_content = build_monster_block(kw)
    
    # 1. Update HTML
    with open(TARGET_FILE, "r", encoding="utf-8") as f:
        html = f.read()
    
    marker = ''
    if marker in html:
        updated_html = html.replace(marker, marker + "\n" + new_content)
        with open(TARGET_FILE, "w", encoding="utf-8") as f:
            f.write(updated_html)
    
    # 2. Update Sitemap
    now = datetime.now().strftime("%Y-%m-%d")
    sitemap = f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.1"><url><loc>https://brightlane.github.io/</loc><lastmod>{now}</lastmod><priority>1.0</priority></url></urlset>'
    with open(SITEMAP_FILE, "w") as f:
        f.write(sitemap)

    # 3. Ping Google/Bing
    sitemap_url = "https://brightlane.github.io/sitemap.xml"
    try:
        requests.get(f"https://www.google.com/ping?sitemap={sitemap_url}", timeout=10)
        requests.get(f"https://www.bing.com/ping?sitemap={sitemap_url}", timeout=10)
    except:
        pass
    
    print(f"✅ Success: {kw} deployed.")

if __name__ == "__main__":
    run_automation()
