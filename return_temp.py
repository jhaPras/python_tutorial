import requests
from bs4 import BeautifulSoup

if city == 'q':break
else:  
    city = input('enter the city of which temprature required:')

def get_temp(city):
    page = requests.get(f'https://www.google.com/search?q= temprature+{city}')
    soup = BeautifulSoup(page.text,'html.parser')
    temprature = soup.find('div',{'class':'BNeawe iBp4i AP7Wnd'}).get_text()
    print(f'temprature in {city} is {temprature}')


while True:
    get_temp(city)

    
