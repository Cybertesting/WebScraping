import request
from bs4 import BeautifulSoup

results=requests.get("")
src=result.content
soup = BeautifulSoup(src, 'lxml')

urls=[]
for h2_tag in soup.find_all("h2"):
  a_tag = h2_tag.find('a')
  urls.append  
