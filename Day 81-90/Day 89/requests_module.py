import requests
from bs4 import BeautifulSoup

url = "https://pypi.org/project/beautifulsoup4/"

r = requests.get(url)
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')

for heading in soup.find_all("h2"):
    print(heading.text)