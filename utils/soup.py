import  lxml
import requests
from bs4 import BeautifulSoup

def winter():
   url = "https://yandex.kz/pogoda/pavlodar"
   response = requests.get(url)
   soup = BeautifulSoup(response.text, 'lxml')
   quotes = soup.find_all(class_="title-icon__text")

   for __quote in quotes:
      return __quote.text 

print (winter())

