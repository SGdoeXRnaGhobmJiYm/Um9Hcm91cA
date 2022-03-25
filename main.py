import os
import requests
import time

de = open("proxies.txt", "a")
be = open("proxies.txt", "w")

def main():
  global de, be
  be.truncate(0)
  x = requests.get('https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/http%2Bs.txt')
  b = x.text
  de.write(b)
  time.sleep(0.1)
  url = "https://sslproxies.org"
  r = requests.get(url)
  proxies = r.text.split("UTC.\n\n")[1].split("</textarea>")[0]
  de.write(proxies)
  time.sleep(0.1)
  url = "https://free-proxy-list.net/"
  r = requests.get(url)
  proxies = r.text.split("UTC.\n\n")[1].split("</textarea>")[0]
  de.write(proxies)
  time.sleep(0.1)
  xs = requests.get("https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt")
  t = xs.text
  de.write(t)
  time.sleep(0.1)
  d = requests.get("https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt")
  i = d.text
  de.write(i)
  time.sleep(0.1)
  f = requests.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt")
  e = f.text
  de.write(e)
  time.sleep(0.1)
  a = requests.get("https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt")
  ru = a.text
  de.write(ru)
  time.sleep(0.1)
  a = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt")
  n = a.text
  de.write(n)
  os.system(' clear ')
  os.system(' python finder.py -w 16 -t 58 -p proxies.txt ')
  
while True:
  main()
  time.sleep(21600)
