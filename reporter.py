import time
from colorama import Fore

def fake_report(username, reason):
    print(Fore.MAGENTA + f"\n📍 Fetching profile: @{username}...")
    time.sleep(1)
    print(Fore.YELLOW + f"📤 Submitting report for: @{username}...")
    time.sleep(1)
    print(Fore.CYAN + f"🛡️ Reason: {reason}")
    time.sleep(1)
    print(Fore.BLUE + "🧠 Processing request...\n")
    time.sleep(1)
