import os
import sys
import time
import requests

# SiegFried Sama Auto Share / Spam Share Tool
# Note: Designed for automated Facebook post sharing via graph API tokens.

def main():
    print("--- Sinzu Auto Share ---")
    token = input("Enter Facebook Token: ")
    link = input("Enter Post Link/ID: ")
    limit = int(input("Enter Share Limit: "))
    
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    count = 0
    while count < limit:
        try:
            response = requests.post(
                f"https://graph.facebook.com/me/feed?link={link}&access_token={token}",
                headers=headers
            )
            if response.status_code == 200:
                count += 1
                print(f"[{count}] Shared successfully.")
            else:
                print(f"Failed to share. Status: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(1)

if __name__ == '__main__':
    main()
