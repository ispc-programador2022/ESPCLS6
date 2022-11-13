from bs4 import BeautifulSoup
import requests

sitioWeb = 'https://contenidosweb.prefecturanaval.gob.ar/alturas/'
resultado = requests.get(sitioWeb)
contenido = resultado.text

soup = BeautifulSoup(contenido, 'lxml')
print(soup.prettify())