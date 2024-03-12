#import requests
#from bs4 import BeautifulSoup

#def wetter ():
   # headers = {
        #'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
   # res= requests.get(
       # f"https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+%D0%BF%D0%B0%D0%B2%D0%BB%D0%BE%D0%B4%D0%B0%D1%80%D0%B5&oq=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+%D0%BF%D0%B0%D0%B2%D0%BB%D0%BE%D0%B4%D0%B0&gs_lcrp=EgZjaHJvbWUqDQgBEAAYgwEYsQMYgAQyBggAEEUYOTINCAEQABiDARixAxiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiPAtIBCDk2NDBqMGo0qAIAsAIA&sourceid=chrome&ie=UTF-8",
      #  headers=headers
       # )
    
   # soup= BeautifulSoup(res.text, "html.parser")

   # time= soup.select('#wod_dts')[0].getText().strip()
    #precipitation = soup.select("#wod_dc").getText().strip()
  # wetters= soup.select('#wod_tm').getText().strip()

   # print(f'''День недели и время:{time}''')
   # Информация об осадках:{precipitation}
   # Темпиратура воздуха:{wetters} *С ''')

#if __name__=='__main__':
    #wetter()