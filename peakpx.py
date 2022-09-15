# Author : me-mozz
import time
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

a = "\033[96;1m"
p = "\033[97;1m"
h = "\033[92;1m"
k = "\033[93;1m"
m = "\033[91;1m"
d = "\033[90;1m"
u = "\033[95;1m"

page = 1
link_img = []

def get_link(url, key, limit):
    global page
    page+=1
    data = requests.get(url).content
    sop = BeautifulSoup(data, "html.parser")
    ul = sop.find("ul", id="list_ul").find_all("li")
    for mozz in ul:
        try:
            img = mozz.find("img")["data-srcset"]
            link_img.append(img.split(" ")[0])
            print(h+f"\r *{h} Mengambil{k} {len(link_img)}{h} link gambar{p} {key}", end="  ")
            time.sleep(0.01)
            if len(link_img) >= limit:
                break
        except:
            pass
    if len(link_img) >= limit:
        pass
    else:
        url_ = url+f"&page={page}"
        get_link(url_, key, limit)

def download(url_img, key):
    try:
        nama = url_img.split("//")[1].replace("w0.peakpx.com/wallpaper", "").replace("/", "_")
        data = requests.get(url_img).content
        with open(f"image/{key}{nama}", "wb") as simp:
            url_img_ = url_img.replace("https://w0.peakpx.com/wallpaper", "")
            print(h+f"\r {p}*{h} Mendownload{p}: {url_img_}", end="                                ")
            simp.write(data)
    except:
        pass

def banner():
    print(a+f'''
.___                  ________                      .__                    .___            
|   | _____    ____   \______ \   ______  _  ______ |  |   _________     __| _/___________ 
|   |/     \  / ___\   |    |  \ /  _ \ \/ \/ /    \|  |  /  _ \__  \   / __ |/ __ \_  __ \\
|   |  Y Y  \/ /_/  >  |    `   (  <_> )     /   |  \  |_(  <_> ) __ \_/ /_/ \  ___/|  | \/
|___|__|_|  /\___  /  /_______  /\____/ \/\_/|___|  /____/\____(____  /\____ |\___  >__|   
          \//_____/{p}By{m} Mozz{a}\/                  \/                \/      \/    \/       
    ''')
def main():
    try:
        banner()
        key = input(p+" ?"+h+" Key"+k+": ")
        limit = int(input(p+" ?"+h+" Limit"+p+": "))
        url = f"https://www.peakpx.com/en/search?q={key}"
        get_link(url, key, limit)
        print(len(link_img))
        with ThreadPoolExecutor(max_workers=10) as mozz:
            for url_img in link_img:
                mozz.submit(download, url_img, key)
    except KeyboardInterrupt:
        exit(m+"\n Keluar..\n")


if __name__=="__main__":
    main()
