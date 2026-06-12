import argparse
import requests
import time
from colorama import Fore, Style, init
from bs4 import BeautifulSoup

init()
parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-u" ,"--url" , help="url")
group.add_argument("-f" , "--file", help="txt file")
parser.add_argument("-r", "--rate",type=int,default=500,help="Requests per second")

args = parser.parse_args()

def face_check(lk):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    resp = requests.get(lk, headers=headers, timeout=10, allow_redirects=True)
    html = resp.text

    if "og:title" in html:
        print(Fore.GREEN +"facebook: " + Fore.LIGHTBLUE_EX + str(lk) + Fore.RED + " ---> Cooked.")
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN + "facebook : " + Fore.LIGHTBLUE_EX + str(lk) + Fore.YELLOW + " ---> UNCLAIMED!!")
        print(Style.RESET_ALL)
        
def yout_check(lk):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    response = requests.get( lk, headers=headers)

    if response.status_code == 200:
        print(Fore.GREEN + "youtube : " + Fore.LIGHTBLUE_EX + str(lk) + Fore.RED + " ---> Cooked.")
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN + "youtube: " + Fore.LIGHTBLUE_EX + str(lk) + Fore.YELLOW + " ---> UNCLAIMED!!")
        print(Style.RESET_ALL)
        
def insta_check(lk):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    resp = requests.get(lk, headers=headers, timeout=10, allow_redirects=True)
    html = resp.text

    if "og:title" in html:
        print(Fore.GREEN+"instagram : " + Fore.LIGHTBLUE_EX + str(lk) + Fore.RED + " ---> Cooked.")
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN+"instagram : " + Fore.LIGHTBLUE_EX + str(lk) + Fore.YELLOW + " ---> UNCLAIMED!!")
        print(Style.RESET_ALL)
        
def gith_check(lk):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    response = requests.get( lk, headers=headers)

    if response.status_code == 200:
        print(Fore.GREEN+"Github : " + Fore.LIGHTBLUE_EX + str(lk) + Fore.RED + " ---> Cooked.")
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN+"Github : " + Fore.LIGHTBLUE_EX + str(lk) + Fore.YELLOW + " ---> UNCLAIMED!!")
        print(Style.RESET_ALL)
        
def linked_check(lk):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    response = requests.get( lk, headers=headers)

    if response.status_code == 200:
        print(Fore.GREEN+"LinkedIn : " + Fore.LIGHTBLUE_EX + str(lk) + Fore.RED + " ---> Cooked.")
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN + "LinkedIn : " + Fore.LIGHTBLUE_EX + str(lk) + Fore.YELLOW + " ---> UNCLAIMED!!")
        print(Style.RESET_ALL)


SonicExE =r"""
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
      """

if args.rate != 500  and args.file is None:
    parser.error("-r/--rate can only be used with -f/--file")
if args.rate is not None and args.rate < 1:
    parser.error("-r/--rate must be at least 1")


if args.file:
    print(SonicExE) 
    print("------------------------------------------")
    print("    File mode:", args.file)
    
    
    facebook_links = []
    youtube_links = []
    instagram_links = []
    github_links = []
    linkedin_links = []
    
    lines = []
    
    if args.rate:
        print("    rate:", str(args.rate) + " req/s")
        print("------------------------------------------")
        
    if args.rate > 0:
        delay = 1 / args.rate
        
    else:
        delay = 1 / 500
        
    with open(str(args.file), "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line.strip())
            
        for url in lines:
            try:
                response = requests.get(url)
                full_page = response.text
                time.sleep(delay)
                soup = BeautifulSoup(full_page, "html.parser")
                for a in soup.find_all("a"):
                    href = a.get("href")
                    if "facebook.com" in href:
                        facebook_links.append(href)
                    elif "youtube.com" in href:
                        youtube_links.append(href)
                    elif "instagram.com" in href:
                        instagram_links.append(href)
                    elif "github.com" in href:
                        github_links.append(href)
                    elif "linkedin.com" in href:
                        linkedin_links.append(href)
    
                facebook_links = list(set(facebook_links))
                youtube_links = list(set(youtube_links))
                instagram_links = list(set(instagram_links))
                github_links = list(set(github_links))
                linkedin_links = list(set(linkedin_links))
            
                print ("\nUrl : " + str(url +"\n"))
            
                for l in facebook_links:
                    face_check(l)
                for l in instagram_links:
                    insta_check(l)
                for l in youtube_links:
                    yout_check(l)
                for l in github_links:
                    gith_check(l)
                for l in linkedin_links:
                    linked_check(l)
                
                facebook_links.clear()
                instagram_links.clear()
                youtube_links.clear()
                github_links.clear()
                linkedin_links.clear()

            except:
                print("Request failed or invalid URL : " + str(url))
                print("link format : http://example.com/") 
            
elif args.url:
    print("URL mode:", args.url)
    url = args.url

    facebook_links = []
    youtube_links = []
    instagram_links = []
    github_links = []
    linkedin_links = []
    
    lines = []
    try:
        response = requests.get(url)   
        full_page = response.text
        soup1 = BeautifulSoup(full_page, "html.parser")
        for a in soup1.find_all("a"):
            href = a.get("href")
            if "facebook.com" in href:
                facebook_links.append(href)
            elif "youtube.com" in href:
                youtube_links.append(href)
            elif "instagram.com" in href:
                instagram_links.append(href)
            elif "github.com" in href:
                github_links.append(href)
            elif "linkedin.com" in href:
                linkedin_links.append(href)
            
        facebook_links = list(set(facebook_links))
        youtube_links = list(set(youtube_links))
        instagram_links = list(set(instagram_links))
        github_links = list(set(github_links))
        linkedin_links = list(set(linkedin_links))
    
        print(SonicExE)     
        print("\n------------------ Facebook ------------------")
        for l in facebook_links:
            face_check(l)
        
        print("\n------------------ Instagram ------------------")
        for l in instagram_links:
            insta_check(l)
    
        print("\n------------------ Youtube ------------------")
        for l in youtube_links:
            yout_check(l)
        
        print("\n------------------ Github------------------")
        for l in github_links:
            gith_check(l)
        
        print("\n------------------ LinkedIN ------------------")
        for l in linkedin_links:
            linked_check(l)  
    except:
        print("Invalid URL or request failed")
        print("link format : http://example.com/") 
