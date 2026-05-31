from colorama import Fore, Style, init
import argparse
import requests
import subprocess
from bs4 import BeautifulSoup
init()
print(r"""
  _________             .__       .__                    
 /   _____/ ____   ____ |__|____  |  |                     
 \_____  \ /  _ \_/ ___\|  \__  \ |  |                            ___------__
 /        (  <_> )  \___|  |/ __ \|  |__                    |\__-- /\       _-
/_______  /\____/ \___  >__(____  /____/                    |/    __      -
        \/            \/        \/                          //\  /  \    /__
      _________ .__                   __                    |  o|  0|__     --_
      \_   ___ \|  |__   ____   ____ |  | __ ___________   \\____-- __ \   ___-
      /    \  \/|  |  \_/ __ \_/ ___\|  |/ // __ \_  __ \  (@@    __/  / /_
      \     \___|   Y  \  ___/\  \___|    <\  ___/|  | \/   -_____---   --_
       \______  /___|  /\___  >\___  >__|_ \\___  >__|      //  \ \\   ___-
              \/     \/     \/     \/     \/    \/         //|\__/  \\  \
                                                           \_-\_____/  \-\ 
                                                              // \\--\|   
                                                          ____//  ||_
                                                         /_____\ /___\   
                                                      ______________________
  
      link format : http://example.com/
      """)
print("----------------------------------------------------------------------------")



parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url",required=True, help="url")
args = parser.parse_args()

response = requests.get(str(args.url))
full_page = response.text
facebook_links = []
youtube_links = []
instagram_links = []
github_links = []
linkedin_links = []


f = 0
i = 0
y = 0
g = 0
l = 0

social_found = []

soup = BeautifulSoup(full_page, "html.parser")

for a in soup.find_all("a"):
    href = a.get("href")
    if href and "facebook.com" in href:
        facebook_links.append(href)
        f = 1
    elif href and "youtube.com" in href:
        youtube_links.append(href)
        y = 1
    elif href and "instagram.com" in href:
        instagram_links.append(href)
        i = 1
    elif href and "github.com" in href:
        github_links.append(href)
        g = 1
    elif href and "linkedin.com" in href:
        linkedin_links.append(href)
        l = 1

print("site : " + Fore.LIGHTBLUE_EX + str(args.url))
print(Style.RESET_ALL)


if f == 1 :
    social_found.append("facebook")
if i == 1 :
    social_found.append("instagram")
if y == 1 :
    social_found.append("youtube")
if g == 1 :
    social_found.append("github")
if l == 1 :
    social_found.append("linkedin")


print("social media Found : ")
for i in social_found:
    print(Fore.LIGHTBLUE_EX + " - " + i )
print(Style.RESET_ALL)



facebook_links = list(set(facebook_links))
youtube_links = list(set(youtube_links))
instagram_links = list(set(instagram_links))
github_links = list(set(github_links))
linkedin_links = list(set(linkedin_links))

def face_check(lk):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    resp = requests.get(lk, headers=headers, timeout=10, allow_redirects=True)
    html = resp.text

    if "og:title" in html:
        print(Fore.GREEN +"Url : " + Fore.LIGHTBLUE_EX + str(lk) + Fore.RED + " ---> Cooked.")
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN + "Url : " + Fore.LIGHTBLUE_EX + str(lk) + Fore.YELLOW + " ---> UNCLAIMED!!")
        print(Style.RESET_ALL)
        
def yout_check(lk):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    response = requests.get( lk, headers=headers)

    if response.status_code == 200:
        print(Fore.GREEN + "Url : " + Fore.LIGHTBLUE_EX + str(lk) + Fore.RED + " ---> Cooked.")
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN + "Url : " + Fore.LIGHTBLUE_EX + str(lk) + Fore.YELLOW + " ---> UNCLAIMED!!")
        print(Style.RESET_ALL)
        
def insta_check(lk):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    resp = requests.get(lk, headers=headers, timeout=10, allow_redirects=True)
    html = resp.text

    if "og:title" in html:
        print(Fore.GREEN+"Url : " + Fore.LIGHTBLUE_EX + str(lk) + Fore.RED + " ---> Cooked.")
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN+"Url : " + Fore.LIGHTBLUE_EX + str(lk) + Fore.YELLOW + " ---> UNCLAIMED!!")
        print(Style.RESET_ALL)
        
def gith_check(lk):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    response = requests.get( lk, headers=headers)

    if response.status_code == 200:
        print(Fore.GREEN+"Url : " + Fore.LIGHTBLUE_EX + str(lk) + Fore.RED + " ---> Cooked.")
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN+"Url : " + Fore.LIGHTBLUE_EX + str(lk) + Fore.YELLOW + " ---> UNCLAIMED!!")
        print(Style.RESET_ALL)
        
def linked_check(lk):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    response = requests.get( lk, headers=headers)

    if response.status_code == 200:
        print(Fore.GREEN+"Url : " + Fore.LIGHTBLUE_EX + str(lk) + Fore.RED + " ---> Cooked.")
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN + "Url : " + Fore.LIGHTBLUE_EX + str(lk) + Fore.YELLOW + " ---> UNCLAIMED!!")
        print(Style.RESET_ALL)

        
print(Fore.GREEN +"""
---------------------------
|    facebook_links       |
---------------------------
      """)
for l in facebook_links:
    face_check(str(l))
    
print(Fore.GREEN+"""
----------------------------
|   youtube_links          |
----------------------------
      """)
for l in youtube_links:
    yout_check(str(l))
    
print(Fore.GREEN+"""
----------------------------
|   instagram_links        |
----------------------------
      """)
for l in instagram_links:
    insta_check(str(l))

print(Fore.GREEN+"""
----------------------------
|   github_links           |
----------------------------
      """)
for l in github_links:
    gith_check(str(l))
    
print(Fore.GREEN+"""
----------------------------
|   linkedin_links         |
----------------------------
      """)
for l in linkedin_links:
    linked_check(str(l))

