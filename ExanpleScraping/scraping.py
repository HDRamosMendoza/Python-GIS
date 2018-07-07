import request
from bs4 import BeautifulSoup
import urllib

def run()										
  for i in range(1,6):
   response = request.get('https://xkcd.com/{}'.format(i))
   """ Parceamos html """
   soup = BeatifulSoup(response.content, 'html.parser')
   """ Buscamos el ID """
   image_tag = soup.find(id = 'comic')
   """ Buscamos la etoqueta imagen """
   image_url = image_container.find('img')['src']
   """ La url dividimos la url y obtenemos elutlimo elemento -1 """
   image_name = image_url.split('/')[-1]
   """ fromateamos la url """
   print('Descargando la imagen {}'.format(image_name))
   urllib.urlretrieve('https:{}'.format(image_url), image_name)
   
   
   
if( __name__ == '__main__'):
	run()
