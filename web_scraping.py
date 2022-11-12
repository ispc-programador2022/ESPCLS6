#Se importan los módulos a utilizar:
import os       # Se usa el modulo os para pausar la ejecución hasta que se oprima una tecla
import time     # Se usa para pausar, por un tiempo definido la ejecución
import lxml
import pandas as pd
import requests
from bs4 import BeautifulSoup

import main     # Se importa el archivos main, para regresar la ejecución


def Ejecutar(): 
    result = requests.get('https://contenidosweb.prefecturanaval.gob.ar/alturas/') 
    content = result.text

    soup = BeautifulSoup(content,'lxml')
    table = soup.find('table', class_='table')
    table_df = pd.read_html(str(table))[0]

    print('\n\t*====================================*')
    print('\t* Scraping realizado correctamente!! *')
    print('\t*====================================*')
    print('\n>> Regresando. Aguarde un momento por favor...')
    return table_df

def CrearCSV(tabla):
    columnas = ['Puerto', 'Río', 'Variación', 'Estado']     #indica las columnas a guardar en el archivo

    carpeta = input('Ingrese la ruta donde desea guardar el archivo (coloque la barra al final): ')
    os.makedirs(carpeta, exist_ok=True)
    nombre = input('Indique el nombre del archivo a crear (sin extensión): ')
    nombre_completo = nombre + ".csv"
    ruta = carpeta + nombre_completo
    
    tabla.to_csv(ruta, sep=';', columns=columnas, encoding='utf-8', index=False)
    print('\n\t*====================================*')
    print('\t* Se creo el archivo correctamente!! *')
    print('\t*====================================*')

    ver = int(input('Desea ver el archivo creado? (1.Si o 2. No): '))
    if ver == 1:
        with open(ruta) as archivo:
            for linea in archivo:
                print(linea)
        os.system('pause')

    time.sleep(3)
    Retorna(ruta)
    
def Retorna(ruta):
    print('\n>> Regresando. Aguarde un momento por favor...')
    time.sleep(2)
    main.menu(True, ruta)
