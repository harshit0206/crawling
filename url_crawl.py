import requests
from bs4 import BeautifulSoup as bs
url="http://codingera.pythonanywhere.com"
r=requests.get(url)
htmlContent=r.content
soup=bs(htmlContent,"html.parser")
anchors=soup.find_all('a')
all_links=set()
for link in anchors:
    if link.get('href')=='#':
        continue
    elif link.get('href')==None:
        continue
    else:
        lnk=str(link.get('href'))
        if lnk[0]=='.' and lnk[1]=='.':
            all_links.add(url+lnk[2:])
        elif lnk[0]=='h' and lnk[1]==lnk[2]=='t' and lnk[3]=='p':
            all_links.add(lnk)
        elif lnk[0]=='/':
            all_links.add(url+lnk)
        else:
            all_links.add(url+'/'+lnk)
for link in all_links:
    print(link)
