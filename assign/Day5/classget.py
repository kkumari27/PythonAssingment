from requests import get
from bs4 import BeautifulSoup
url='http://www.moneycontrol.com/'
resp=get(url)
soup= BeautifulSoup(
    resp.text,'html.parser')
'''lxml'''
# print(type(soup))
tables=soup.find_all('table',class_="rhsglTbl")
# print(table1)
for table in tables:
 links=table.find_all('a')
 print(links)
# print(anchor)

# # print(resp.text)
# print(type(soup))
# print(soup.html.head.meta.title)