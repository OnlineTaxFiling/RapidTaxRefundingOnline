import os
import json
import requests
import random
from datetime import datetime

# --- 1. CONFIGURATION ---
AFFILIATE_BASE = "https://www.linkconnector.com/ta.php?lc=007949054186005142"
TRACKING_ID = "RapidTaxForever" 
TARGET_FILE = "index.html"
SITEMAP_FILE = "sitemap.xml"

# --- 2. THE AUTHORITY CONTENT ENGINE ---
# These are used to hit the 2,500+ word "Expertise" requirement
TECH_PHRASES = [
    "utilizing the Section 402(b) digital filing mandate",
    "integrated OBBB 24-hour refund authorization protocols",
    "advanced 256-bit AES encryption for tax data transmission",
    "compliance with the 2026 Federal Rapid-Channel processing initiative",
    "automated audit-risk mitigation using ID.me compatible verification"
]

def get_next_keyword():
    # Emergency fallback if keywords.json is missing or broken
    if not os.path.exists('keywords.json'):
        return "2026 Tax Refund Status"
        
    try:
        with open('keywords.json', 'r+') as f:
            data = json.load(f)
            if not data.get('remaining'):
                return "IRS Refund Schedule 2026"
            kw = data['remaining'].pop(0)
            data.setdefault('used', []).append(kw)
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()
            return kw
    except Exception:
        return "2026 Tax Filing Portal"

def build_monster_block(kw):
    """Generates the high-authority HTML block."""
    full_url = f"{AFFILIATE_BASE}&atid={TRACKING_ID}"
    timestamp = datetime.now().strftime("%B %d, %Y")
    tech = random.choice(TECH_PHRASES)
    
    return f"""
    <article class="bg-white p-8 md:p-12 rounded-3xl shadow-sm border border-slate-200 mb-12">
        <div class="flex items-center space-x-3 mb-6">
            <span class="bg-blue-600 text-white text-xs font-black px-3 py-1 rounded-full uppercase">Update: {timestamp}</span>
            <span class="text-slate-400 text-xs font-bold uppercase tracking-widest border-l pl-3">OBBB Verified</span>
        </div>
        
        <h2 class="text-3xl md:text-5xl font-black text-blue-900 mb-6 tracking-tighter leading-tight">
            {kw}: Official 2026 Security & Refund Briefing
        </h2>
        
        <div class="prose prose-slate max-w-none text-slate-600 text-lg leading-relaxed">
            <p class="mb-6">
                When processing <strong>{kw}</strong>, it is imperative to align with the latest federal directives. 
                As of {timestamp}, our systems have integrated <strong>{tech}</strong> to ensure 
                your filing avoids the standard manual review queues common in the 2026 cycle.
            </p>
            
            <div class="my-8 p-6 bg-blue-50 border-l-8 border-blue-600 rounded-r-xl italic font-medium text-blue-900">
                "Technical Directive: The use of {tech} is a critical component for filers seeking 
                immediate refund authorization before the April 15 deadline."
            </div>

            <p class="mb-8 font-bold">
                Why use this portal for {kw}?
            </p>
            <ul class="list-disc ml-6 mb-8 space-y-2">
                <li>Direct integration with {tech}</li>
                <li>Real-time verification of 2026 tax credits</li>
                <li>Priority processing for 24-hour refund disbursement</li>
            </ul>

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
    if not os.path.exists(TARGET_FILE):
        print(f"FAILED: {TARGET_FILE} not found in root.")
        return

    kw = get_next_keyword()
    content = build_monster_block(kw)
    
    with open(TARGET_FILE, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Check for the SEO injection marker
    marker = ''
    
    if marker in html:
        new_html = html.replace(marker, marker + "\n" + content)
    else:
        # Fallback: Put it before the closing body tag if marker is missing
        new_html = html.replace("</body>", content + "\n</body>")
        
    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        f.write(new_html)
    
    # 3. Update Sitemap
    now = datetime.now().strftime("%Y-%m-%d")
    sitemap_content = f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.1"><url><loc>https://brightlane.github.io/</loc><lastmod>{now}</lastmod><priority>1.0</priority></url></urlset>'
    with open(SITEMAP_FILE, "w") as f:
        f.write(sitemap_content)

if __name__ == "__main__":
    run_automation()
