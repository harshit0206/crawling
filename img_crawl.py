import requests
from bs4 import BeautifulSoup as bs
url="http://harshit0206.pythonanywhere.com"
r=requests.get(url)
htmlContent=r.content
soup=bs(htmlContent,"html.parser")
#print(soup.prettify)
images=soup.find_all('img')
all_links=set()
for link in images:
    if link.get('src')=='#':
        continue
    elif link.get('src')==None:
        continue
    else:
        lnk=str(link.get('src'))
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
