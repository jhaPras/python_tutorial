import requests
from bs4 import BeautifulSoup as bs

page = requests.get('https://www.yellowpages.com/')
print(page)
