import os
import json
import requests
import random
from datetime import datetime

# --- 1. CONFIGURATION ---
# Your fixed affiliate heartbeat
AFFILIATE_BASE = "https://www.linkconnector.com/ta.php?lc=007949054186005142"
TRACKING_ID = "RapidTaxForever"
TARGET_FILE = "index.html"
SITEMAP_FILE = "sitemap.xml"

# --- 2. THE KNOWLEDGE BASE (THE "FRESHNESS" ENGINE) ---
# The bot pulls from these to ensure content isn't just "keyword stuffing"
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
    """Pivots the content based on the calendar to stay relevant forever."""
    month = datetime.now().month
    if month > 9: # From October to December, start focusing on NEXT year
        return random.choice(TAX_LAWS_2027_PREVIEW)
    return random.choice(TAX_LAWS_2026)

# --- 3. CORE LOGIC ---
def get_next_keyword():
    if not os.path.exists('keywords.json'):
        return None
    with open('keywords.json', 'r+') as f:
        data = json.load(f)
        if not data.get('remaining'):
            return None
        kw = data['remaining'].pop(0)
        data.setdefault('used', []).append(kw)
        f.seek(0); json.dump(data, f, indent=2); f.truncate()
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
        
        <h2 class="text-3xl md:text-5xl font-black text-blue-900 mb-6 leading-tight">
            {kw}: Critical 2026 Filing Analysis
        </h2>
        
        <div class="prose prose-slate max-w-none text-slate-600 text-lg leading-relaxed">
            <p class="mb-6">
                Navigating <strong>{kw}</strong> requires a deep understanding of current federal mandates. 
                As of {timestamp}, our internal audit systems have flagged <strong>{kw}</strong> as a 
                priority category for high-speed refund processing.
            </p>
            
            <div class="my-8 p-6 bg-blue-50 border-l-8 border-blue-600 rounded-r-xl italic font-medium text-blue-900">
                "Technical Directive: Implementation of {law_snippet} is now required for all 2026 submissions 
                to ensure same-day verification and deposit."
            </div>

            <p class="mb-8">
                By focusing on {kw}, filers can bypass traditional manual review queues. Our direct-file 
                infrastructure is pre-loaded with the specific logic for {law_snippet}, allowing 
                your data to move directly to the refund authorization stage.
            </p>

            <div class="text-center bg-slate-900 p-8 rounded-2xl shadow-2xl">
                <h3 class="text-white text-2xl font-bold mb-4 uppercase tracking-tighter">Authorized {kw} Submission Portal</h3>
                <p class="text-slate-400 mb-8">Click below to transmit your 2026 return via the Rapid Refund Network.</p>
                <a href="{full_url}" class="inline-block bg-green-500 hover:bg-green-600 text-white text-2xl font-black py-5 px-12 rounded-xl transition transform hover:scale-105">
                    FILE FOR {kw.upper()} NOW →
                </a>
            </div>
        </div>
    </article>
    """

def run_automation():
    kw = get_next_keyword()
    if not kw:
        print("Tank empty. Add more keywords to keywords.json."); return

    new_content = build_monster_block(kw)
    
    # Update HTML Hub
    with open(TARGET_FILE, "r", encoding="utf-8") as f:
        html = f.read()
    
    marker = ''
    if marker in html:
        # We inject the NEWEST content at the top so users (and Google) see it first
        updated_html = html.replace(marker, marker + "\n" + new_content)
        with open(TARGET_FILE, "w", encoding="utf-8") as f:
            f.write(updated_html)
    
    # Update Sitemap for Freshness
    now = datetime.now().strftime("%Y-%m-%d")
    sitemap = f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.1"><url><loc>https://brightlane.github.io/</loc><lastmod>{now}</lastmod><priority>1.0</priority></url></urlset>'
    with open(SITEMAP_FILE, "w") as f:
        f.write(sitemap)

    # Emergency Pings
    sitemap_url = "https://brightlane.github.io/sitemap.xml"
    requests.get(f"https://www.google.com/ping?sitemap={sitemap_url}")
    requests.get(f"https://www.bing.com/ping?sitemap={sitemap_url}")
    
    print(f"✅ Success: {kw} injected with law rotation.")

if __name__ == "__main__":
    run_automation()
