import os
import json
from datetime import datetime

# CONFIG
AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949054186005142&atid=RapidTaxRoot"
TARGET_FILE = "index.html"

def get_keywords():
    if not os.path.exists('keywords.json'):
        return None
    with open('keywords.json', 'r+') as f:
        data = json.load(f)
        if not data.get('remaining'):
            return None
        kw = data['remaining'].pop(0)
        data.setdefault('used', []).append(kw)
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()
    return kw

def build_monster_block(kw):
    """Generates the Authority Content Block"""
    return f"""
    <div class="p-8 bg-white rounded-xl shadow-sm border border-slate-200 mb-8 animate-fade-in">
        <h2 class="text-3xl font-extrabold text-blue-900 mb-4">{kw}: 2026 Emergency Filing Update</h2>
        <p class="text-slate-600 mb-6 leading-relaxed text-lg">
            Taxpayers searching for <strong>{kw}</strong> are advised that the OBBB 2026 regulatory window is closing. 
            New audit-flags for the 2026 season specifically target <strong>{kw}</strong> inconsistencies. To ensure 
            your refund is processed within the standard 24-hour rapid window, you must utilize an authorized 
            digital filing partner.
        </p>
        <div class="flex items-center justify-between bg-slate-50 p-4 rounded-lg mb-6">
            <span class="text-sm font-bold text-slate-500 uppercase tracking-widest">Topic Authority: High</span>
            <span class="text-green-600 font-bold">✓ Verified for 2026 Cycle</span>
        </div>
        <a href="{AFFILIATE_URL}" class="block text-center bg-blue-600 text-white py-4 rounded-lg font-bold text-xl hover:bg-blue-700 transition">
            Apply {kw} Strategy & File Now
        </a>
    </div>
    """

def run_expansion():
    kw = get_keywords()
    if not kw:
        print("No keywords left in tank.")
        return

    new_content = build_monster_block(kw)

    with open(TARGET_FILE, "r", encoding="utf-8") as f:
        html_content = f.read()

    # The marker from index.html where we inject the content
    marker = ''
    
    if marker in html_content:
        # We place the NEW content ABOVE the marker so the newest post is always at the top
        updated_html = html_content.replace(marker, new_content + "\n" + marker)
        
        with open(TARGET_FILE, "w", encoding="utf-8") as f:
            f.write(updated_html)
        print(f"✅ Successfully expanded content for: {kw}")
    else:
        print("Error: Could not find injection marker in index.html")

if __name__ == "__main__":
    run_expansion()
