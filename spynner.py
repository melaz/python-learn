#__author__ = 'Dmitry'
#import cookielib, shutil, os

#from mechanize import Browser

#br = Browser()
# Create cookie jar and attach it to Browser
#cj = cookielib.LWPCookieJar()
#br.set_cookiejar(cj)

# Add some headers
#br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
# Open url in Browser instance
#br.open('http://my.kievnet.ua/index.php')

import cookielib
from mechanize import ParseResponse, urlopen
response = urlopen("http://my.kievnet.ua/index.php")
forms = ParseResponse(response, backwards_compat=False)
form = forms[0]
print form