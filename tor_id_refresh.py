import socks, socket, urllib2, requests
from bs4 import BeautifulSoup
from stem import Signal
from stem.control import Controller

with Controller.from_port(port = 9151) as controller:
    controller.authenticate()
    controller.signal(Signal.NEWNYM)

    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150)
    socket.socket = socks.socksocket

    user_agent = 'Chrome'
    heads = {'User-Agent': user_agent}

    req = urllib2.Request("http://whatismyipaddress.com/", headers=heads)
    url_f = urllib2.urlopen(req)
    soup = BeautifulSoup(url_f)

    for i in soup.find_all("a",style="font-weight:bold;color:#007cc3;font-size:26px;text-decoration: none;"):
        print i.text

    controller.signal(Signal.HUP) # Resetting IP address through Tor

    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150)
    socket.socket = socks.socksocket

    # Using BeautifulSoup again
    user_agent = 'Chrome'
    heads = {'User-Agent': user_agent}

    req = urllib2.Request("http://whatismyipaddress.com/", headers=heads)
    url_f = urllib2.urlopen(req)
    soup = BeautifulSoup(url_f)

    for i in soup.find_all("a",style="font-weight:bold;color:#007cc3;font-size:26px;text-decoration: none;"):
        print i.text

