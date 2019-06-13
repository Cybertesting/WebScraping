#training from freeCodeCamp.org created by Tutorial from Vincent Russo of Lucid Programming. Check out his YouTube channel: 



import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.whitehouse.gov/briefings-statements/")
src = result.content
soup = BeautifulSoup(src, 'lxml')

urls = []
for h2_tag in soup.find_all(h2):
    a_tag = h2_tag.find('a')
    urls.append(a_tag.attrs['href'])
    
print(urls)
