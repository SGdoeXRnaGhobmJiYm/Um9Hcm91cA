import json
import queue
import threading
import urllib.request
import socks
from requests import get
from sockshandler import SocksiPyHandler
import socket
import os
import re
import time


test_url = "https://www.google.com"
thread = 300
timeout = 3

socket.setdefaulttimeout(timeout)
working = 0
startTime = time.time()

def scraper():
    name = "github.com"
    urls = [
        "raw.githubusercontent.com/almroot/proxylist/master/list.txt",
        "raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
        "raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
        "raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt",
        "raw.githubusercontent.com/IshanSingla/proxy-list/main/proxys/http.txt",
        "raw.githubusercontent.com/IshanSingla/proxy-list/main/proxys/https.txt",
        "raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
        "raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
        "raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
        "raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
        "raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
        "raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
        "raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
        "raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
        "raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
        "raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
        "raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
        "raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt",
        "raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt"
    ]
    resp = []
    for url in urls:
        try:
            print(f"Request: {url}")
            for x in re.findall(r"\d+\.\d+\.\d+\.\d+\:\d+", get(url).text):
                resp.append(x)
        except Exception as e:
            print(e, "Failed")

    return list(set(resp))
    
def start(proxy_type:str, url_type:str, proxies:list):
    
    threads = []
    _proxies = iter(proxies)
    q = queue.Queue()

    if test_url.startswith("http://") or test_url.startswith("https://"): url = f"{test_url}"
    else: url = f"{url_type}://{test_url}"

    req = urllib.request.Request(url)
    text = urllib.request.urlopen(req, timeout=timeout).read()

    for x in range(thread):
        threads.append(threading.Thread(target=job, args=[proxy_type, _proxies, url_type, url, timeout, text, q]))

    for x in threads:
        try: x.start()
        except Exception as e: print(e)

    for x in threads:
        try: x.join()
        except Exception as e: print(e)

    resp = []
    while not q.empty(): resp.append(q.get_nowait())

    return resp

def job(proxy_type:str, _proxies, url_type:str, url:str, timeout:int, text:str, q):
    while True:
        try:
            _proxy = next(_proxies)
            if (proxy_type == "http") or (proxy_type == "https"):
                proxy = urllib.request.ProxyHandler({url_type: f"{proxy_type}://{_proxy}"})
            elif proxy_type == "socks4":
                ip, port = _proxy.split(":")
                proxy = SocksiPyHandler(socks.SOCKS4, str(ip), int(port))
            elif proxy_type == "socks5":
                ip, port = _proxy.split(":")
                proxy = SocksiPyHandler(socks.SOCKS5, str(ip), int(port))
              
            opener = urllib.request.build_opener(proxy)
            resp = opener.open(url, timeout=timeout).read()
            opener.close()
            if resp == text:
                q.put(_proxy)

        except StopIteration: break
        except: pass
        
        continue
    return

        for url in urls:
        try:
            print(f"Request: {url}")
            for x in re.findall(r"\d+\.\d+\.\d+\.\d+\:\d+", get(url).text):
                resp.append(x)
        except Exception as e:
            print(e, "Failed")

    return list(set(resp))

def checker(proxies):
    checked_http = []
    checked_https = []
    for checked, proxy_type in zip([checked_http, checked_https], ["http", "https"]):
        checked.append(list(set(start(proxies, x, config))))
    return checked

if __name__ == "__main__":
    with open("checked.txt") as fp:
        for x in checker(scraper()):
            fp.write(x + "\n")
    print(time.time() - startTime)
