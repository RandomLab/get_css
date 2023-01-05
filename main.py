import requests
from bs4 import BeautifulSoup 
from urllib.parse import urljoin
import wget

url = "https://www.lemonde.fr/"

session = requests.Session()

session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

html = session.get(url).content
soup = BeautifulSoup(html, "html.parser")

print(soup)

css_files = []

for css in soup.find_all("link"):
    if css.attrs.get("href"):
        css_url = urljoin(url, css.attrs.get("href"))
        css_files.append(css_url)

for file in css_files:
    wget.download(file, 'test.txt')
   