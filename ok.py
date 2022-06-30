import os
import threading
import urllib.request
import re
import aiohttp
import random
import json
import asyncio


alive = 0

useragents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/99.0.4844.59 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/99.0.4844.59 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36"
]

def get(url):
    req = urllib.request.Request(f"https://{url}", headers={'User-Agent': random.choice(useragents)})
    text = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
    return text

def github():
    urls = [
        "raw.githubusercontent.com/almroot/proxylist/master/list.txt",
        
        "raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
        
        "raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
        
        "raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
        
        "raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
        
        "raw.githubusercontent.com/KUTlime/ProxyList/main/ProxyList.txt",
        
        #"raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",

        "raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
        
        "raw.githubusercontent.com/mmpx12/proxy-list/master/proxies.txt",

        "raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
        
        #"raw.githubusercontent.com/ryanhaticus/superiorproxy.com/main/proxies.txt",

        "raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/ultrafast.txt",

        "raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
        "raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
        #"raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
        #"raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
        
        "raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",

        "raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",

        "raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt",
        "raw.githubusercontent.com/Volodichev/proxy-list/main/hproxy.txt",
        
        "raw.githubusercontent.com/zeynoxwashere/proxy-list/main/http.txt"
    ]
    resp = []

    for url in urls:
        try:
            for x in re.findall(r"\d+\.\d+\.\d+\.\d+\:\d+", get(url)):
                resp.append(x)
        except Exception as e:
            pass

    return list(set(resp))

def checkerproxy_net():
    urls = [
        "checkerproxy.net/api/archive"
    ]
    resp = []

    for url in urls:
        #try:
            req = get(url)
            archives = json.loads(req)
            
            for archive in archives:
                try:
                    date = archive["date"]
                    proxies = get(f"{url}/{date}")
                    proxies = json.loads(proxies)
                
                    for proxy in proxies:
                        resp.append(proxy["addr"])
                except:
                    print("Failed")
                
        #except:
            #print("Failed")

    return list(set(resp))

def openproxy_space():
    urls = [
        "openproxy.spce/list/http"
    ]
    resp = []

    for url in urls:
        try:
            for x in re.findall(r"\d+\.\d+\.\d+\.\d+\:\d+", get(url)):
                resp.append(x)
        except Exception as e:
            pass

    return list(set(resp))

def spys_me():
    urls = [
        "spys.me/proxy.txt"
    ]
    resp = []

    for url in urls:
        try:
            for x in re.findall(r"\d+\.\d+\.\d+\.\d+\:\d+", get(url)):
                resp.append(x)
        except Exception as e:
            pass

    return list(set(resp))

def free_proxy_list_net():
    urls = [
        "free-proxy-list.net/",
        "www.us-proxy.org/",
        "free-proxy-list.net/uk-proxy.html",
        "www.sslproxies.org/",
        "free-proxy-list.net/anonymous-proxy.html",
        "www.google-proxy.net/"
    ]
    resp = []

    for url in urls:
        try:
            for x in re.findall(r"\d+\.\d+\.\d+\.\d+\:\d+", get(url)):
                resp.append(x)
        except Exception as e:
            pass

    return list(set(resp))
    

async def check(proxy):
    global alive
    async with aiohttp.ClientSession(trust_env=False) as session:
        try:
            async with session.get("https://roblox.com", proxy = f"http://{proxy}", timeout=5) as res:
                if res.status == 200 and res.json()["origin"] == proxy:
                    alive += 1
                    print(f"Working Proxy: {proxy}")
                    with open("proxy.txt", "a") as f:
                        f.write(proxy + "\n")
                    await session.close()

        except aiohttp.ClientConnectorError:
            print(f"Dead Proxy: {proxy}")
            await session.close()

        except aiohttp.ClientHttpProxyError:
            print("[ERROR] Oh no! There was a proxy error. Please ensure you have proper proxy authentication!")
            await session.close()

        except Exception as e:
            print(f"[SYSTEM] An unexpected error has occured! | {e}")

            
def checkproxy(proxy):
   coros = check(proxy)
   loop = asyncio.get_event_loop()
   loop.run_until_complete(conGather(*coros)) 
   loop.close()
      
def checker(proxies):
    threads = []
    try:
        for proxy in proxies:
            th = threading.Thread(target=checkproxy, args=[proxy])
            th.start()
            threads.append(th)
    except:
        pass

    for th in threads:
        th.join()
    return threads 

if __name__ == "__main__":
    os.system("clear")
    proxies = []
    for x in github():
      proxies.append(x)
    
    for x in checkerproxy_net():
      proxies.append(x)

    for x in openproxy_space():
      proxies.append(x)

    for x in spys_me():
      proxies.append(x)

    for x in free_proxy_list_net():
      proxies.append(x)
    print(f"Total Scraped: {len(proxies)}")    
    proxies = re.findall(r"\d+\.\d+\.\d+\.\d+\:\d+", str(proxies))
    proxies = set(proxies)
    proxies = sorted(proxies)
    checker(proxies)
    print(f"Total Working: {alive}")
