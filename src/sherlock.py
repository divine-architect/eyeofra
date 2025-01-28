import requests
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time

# small list for now
platforms = {
    "Instagram": "https://www.instagram.com/{}/",
    "TikTok": "https://www.tiktok.com/@{}",
    "YouTube": "https://www.youtube.com/@{}",
    "GitHub": "https://github.com/{}",
    "Replit": "https://replit.com/@{}",
    "Twitter": "https://twitter.com/{}",
    "Pinterest": "https://www.pinterest.com/{}/",
    "Reddit": "https://www.reddit.com/user/{}/",
    "Medium": "https://medium.com/@{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Telegram": "https://t.me/{}"
}

def check_username(username):
    results = {}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    for platform, url_pattern in platforms.items():
        url = url_pattern.format(quote(username))
        try: # a saner way to do this perhaps?
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                results[platform] = f"[+] {url}"
            elif response.status_code == 404:
                results[platform] = f"[-] {url}"
            else:
                results[platform] = f"Could not determine (HTTP {response.status_code})"
        except requests.RequestException:
            results[platform] = "Error accessing the platform"

    return results

def screenshot(username, results):
    
    driver = webdriver.Chrome()

   #dir for scrshots
    directory = f"screenshots/{username}"
    os.makedirs(directory, exist_ok=True)

    for platform, result in results.items():
        if result.startswith("[+]"):  
            url = result.split(" ")[1]
            try:
                print(f"Opening {url} for {platform}...")
                driver.get(url)  
                time.sleep(5) 
                screenshot_path = os.path.join(directory, f"{platform}.png")
                driver.save_screenshot(screenshot_path)
                print(f"Screenshot saved: {screenshot_path}")
            except Exception as e:
                print(f"Error capturing screenshot for {platform}: {e}")

    driver.quit()

username_to_check = input("Enter the username to check: ").strip()
results = check_username(username_to_check)

print("\nResults:")
for platform, result in results.items():
    print(f"{platform}: {result}")
screenshot(username_to_check, results)
