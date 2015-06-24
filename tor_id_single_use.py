''' Python Tor '''
import socks, socket, urllib2, requests

# Tor magic --> Remember to open Tor Browser
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150)
socket.socket = socks.socksocket

# BeautifulSoup magic --> Copied from my previous work
user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
heads = {'User-Agent': user_agent}

req = urllib2.Request("http://whatismyipaddress.com/", headers=heads)
url_f = urllib2.urlopen(req)
soup = BeautifulSoup(url_f)

for i in soup.find_all("a",style="font-weight:bold;color:#007cc3;font-size:26px;text-decoration: none;"):
    print i.text
