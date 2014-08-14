__author__ = 'Dmitry'
import cookielib, shutil, os

from mechanize import Browser, ParseResponse
from BeautifulSoup import BeautifulSoup
import html2text

br = Browser()
br._factory.encoding= "windows"
br._factory._forms_factory.encoding = "cp1251"
br._factory._links_factory._encoding = "cp1251"
# Create cookie jar and attach it to Browser
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Add some headers
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; ru-RU; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
# Open url in Browser instance
response = br.open('http://my.kievnet.ua/index.php')

#br.encoding="windows-1251"
# Select form for modification and "enter" login info
# print response.read
br.select_form(nr=0)
br["u_login"] = "melaz"
br["pass"] = ""
# Submit form
br.submit()
#forms = ParseResponse(test.read)
#print (forms)
test = br.response().read()
u = test.decode('windows-1251')
soup = BeautifulSoup(u)
#soup = soup.prettify()
#print(soup.body())
#for i in soup.body:
#    print i
#a = soup.find_all('')
a= soup.findAll('tr')
#firstPTag, secondPTag = soup.findAll('td')
#print (a.)
for i in soup.findAll('tr'):
    if i coprint (i)

#test.encode('cp1251')
#br.open('http://my.kievnet.ua/index.php?mode=page&_pn=6')
#test2 = br.response().read()
#print (test2.decode('windows-1251'))
