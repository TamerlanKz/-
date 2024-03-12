import requests


def fox():
  url = 'https://randomfox.ca/floof/'
  response = requests.get(url)
  if response.status_code:
     data = response.json()
     return data.get('image')


if __name__ == '__main__':
  fox()


#url = 'https://tengrinews.kz/kazakhstan_news'
#r= requests.get(url).text
#print(r )   Как мне вытащить  главные новости?    
 


#url= 'https://pixabay.com/ru/images/search/хорошего%20дня/'
#res= requests.get(url)
#print(res("image"))

#print (res.json)
#with open('Teng', 'wb') as f:
  # f.write(res.content)
  # print( f.write)
#if response.status_code:
  #  data = response.json()

