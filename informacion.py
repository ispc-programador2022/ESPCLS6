import main                 #Se importa el archivos main, para regresar la ejecución

#Se importan los módulos a utilizar:
import webbrowser                    #Se utiliza para abrir páginas web en el explorador
import time                          #Se usa para pausar, por un tiempo definido la ejecución
from os import system                #Se usa el modulo os para pausar la ejecución hasta que se oprima una tecla


#Respecto al trabajo realizado
def LibreríasUtilizadas(de):
    if de == 'WS':
        print('Acá se indican las librerías utilizadas en Web Scraping')

        print(' > Librería Requests: es una librería de Python que facilita realizar las peticiones con protocolo HTTP. En el Web Scraping la utilizamos para hacer la petición GET al sitio web a scrapear.')
        print('\tDesea acceder a la Documentación? (1.SI o 2.NO): ')
        documentacion = int(input(': '))
        if documentacion == 1:
            webbrowser.open("https://requests.readthedocs.io/en/latest/user/quickstart/", new=2, autoraise=True)
            system('pause')
        
        print(' > Beautiful Soup: es una librería de Python para extraer datos de archivos HTML y XML. Funciona con su analizador favorito para proporcionar formas idiomáticas de navegar, buscar y modificar el esquema de análisis. La utilizamos en este proyecto para extraer los datos de la web y la combinamos con el “HTML parser” LXML.')
        print('\tDesea acceder a la Documentación? (1.SI o 2.NO): ')
        documentacion = int(input(': '))
        if documentacion == 1:
            webbrowser.open("https://www.crummy.com/software/BeautifulSoup/bs4/doc/", new=2, autoraise=True)
            system('pause')
        
        print(' > LXML: es un módulo de Python que se encarga de  procesar documentos XML y HTML y convertirlos en datos. Este módulo lo utilizamos para el Web Scraping al momento de extraer el contenido HTML de una web. LXML es conocido como un “HTML parser”')
        print('\tDesea acceder a la Documentación? (1.SI o 2.NO): ')
        documentacion = int(input(': '))
        if documentacion == 1:
            webbrowser.open("https://lxml.de/", new=2, autoraise=True)
            system('pause')
        
        print(' > Pandas: es una librería de Python especializada en el manejo y análisis de estructuras de datos. Permite leer y escribir fácilmente Dataframes, ficheros en formato CSV, Excel y bases de datos SQL. Crea estructuras de datos en formato array. Además posee métodos para reordenar, dividir y combinar conjuntos de datos. En nuestro caso, usamos Pandas para la creación y el manejo de Dataframes y archivos .csv, como así también para la visualización de esos datos.')
        print('\tDesea acceder a la Documentación? (1.SI o 2.NO): ')
        documentacion = int(input(': '))
        if documentacion == 1:
            webbrowser.open("https://pandas.pydata.org/docs/", new=2, autoraise=True)
            system('pause')
        
    if de == 'BD':
        print(' > Mysql Connector: MySQL Connector/Python permite que los programas de Python accedan a las bases de datos de MySQL mediante una API. Está escrito en Python puro y no tiene dependencias, excepto la biblioteca estándar de Python.')
        print('\tDesea acceder a la Documentación? (1.SI o 2.NO): ')
        documentacion = int(input(': '))
        if documentacion == 1:
            webbrowser.open("https://dev.mysql.com/doc/connector-python/en/", new=2, autoraise=True)
            system('pause')

    if de == 'INF':
        print(' > Pandas: es una librería de Python especializada en el manejo y análisis de estructuras de datos. Permite leer y escribir fácilmente Dataframes, ficheros en formato CSV, Excel y bases de datos SQL. Crea estructuras de datos en formato array. Además posee métodos para reordenar, dividir y combinar conjuntos de datos. En nuestro caso, usamos Pandas para la creación y el manejo de Dataframes y archivos .csv, como así también para la visualización de esos datos.')
        print('\tDesea acceder a la Documentación? (1.SI o 2.NO): ')
        documentacion = int(input(': '))
        if documentacion == 1:
            webbrowser.open("https://pandas.pydata.org/docs/", new=2, autoraise=True)
            system('pause')


def Script_BD():
    print('********* Script Base de Datos *********')
    print('Se realiza la conexion a la base de datos, y se puede crear una nueva base de datos. A partir del archivo CSV creado, se pueden crear las tablas y exportar los datos a la base de datos.')
    time.sleep(2)
    print(' ---> LIBRERÍAS UTILIZADAS: <--- ')
    LibreríasUtilizadas('BD')
    time.sleep(2)
    print('\n>> Regresando. Aguarde un momento por favor...')

def Script_WS():
    print('********* Script Web Scraping *********')
    print('\tA partir de una URL, se realiza el mapeo del sitio con la librería Request, luego con la librería BeautifulSoup se ejecuta el scraping y utilizando la librearía Pandas, se obtiene un Data Frame.')
    print('\tA continuación, se crea un archivo CSV con los datos seleccionados del Data Frame previamente obtenido.')
    print('\tAdemás, se posibilita la opción de ver el archivo CSV generado.')
    time.sleep(2)
    print(' ---> LIBRERÍAS UTILIZADAS: <--- ')
    LibreríasUtilizadas('WS')
    time.sleep(2)
    print('\n>> Regresando. Aguarde un momento por favor...')

def Script_INF():
    print('********* Script Web Scraping *********')
    print('Se accede al archivo CSV generado en el scraping y utilizando la librería Pandas, se obtiene: la máxima suba, la máxima baja y la media.')
    time.sleep(2)
    print(' ---> LIBRERÍAS UTILIZADAS: <--- ')
    LibreríasUtilizadas('INF')
    time.sleep(2)
    print('\n>> Regresando. Aguarde un momento por favor...')

def WebScraping():
    print('*-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-*')
    print('\tWeb Scraping es una técnica utilizada mediante programas de software para extraer información de sitios web.')
    print('Usualmente, estos programas simulan la navegación de un humano en el sitio, ya sea utilizando el protocolo HTTP manualmente, o incrustando un navegador en una aplicación.')
    print('\n\t\tFUENTE: Wikipedia: https://es.wikipedia.org/wiki/Web_scraping')
    print('*-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-*')
    system('pause')


#Respecto al equipo de desarrollo
def Nosotros():
    print('Nuestro grupo es ESPCLS6 y somos estudiantes de primer año de la Tecnicatura Superior en Ciencias de Datos e Inteligencia Artificial del Instituto Superior Politécnico Córdoba.')
    print(' * Cecilia Espada')
    print(' * Luis Siccardi')
    print(' * Laura Peralta')
    print(' * Marilena Castilla')
    print(' * Gabriela López')
    print(' * Martín Solá')
    print(' ')

    Recursos('Trello')
    Recursos('Github')
    time.sleep(2)
    print('\n>> Regresando. Aguarde un momento por favor...')

def Recursos(ver):
    if ver == 'Trello':
        print('https://trello.com/b/6QsPP1hR/desarrollo-web-scraping')
        print('\tDesea acceder? (1.SI o 2.NO): ')
        acceso = int(input(': '))
        if acceso == 1:
            webbrowser.open("https://trello.com/b/6QsPP1hR/desarrollo-web-scraping", new=2, autoraise=True)
            system('pause')
    if ver == 'Github':
        print('https://github.com/ispc-programador2022/ESPCLS6')
        print('\tDesea acceder? (1.SI o 2.NO): ')
        acceso = int(input(': '))
        if acceso == 1:
            webbrowser.open("https://github.com/ispc-programador2022/ESPCLS6", new=2, autoraise=True)
            system('pause')
        

def Retorna(direccion):
    main.menu(True, direccion)

def Error(archivo):
    print('*==========================*')
    print('*     Opción no válida     *')
    print('*==========================*')
    system('pause')
    print('\n>> Regresando. Aguarde un momento por favor...')
    menu(True, archivo)

def menu(a, archivo):
    dir = archivo
    bandera = a

    while bandera:
        
        print("\n\t-->  SUBMENU INFORMACIÓN  <--\n")
        print("\t1. Qué es el Web Scraping?")
        print("\t2. Descripción del Proyecto")
        print("\t3. Quienes somos?")
        print("\t4. Volver al menu principal\n")
        while True:
            try:
                opc = int(input("Seleccione una opción: "))
                break
            except ValueError:
                print("Oops! Seleccione una opción numérica por favor: ")
                Error(dir)
                    
        if opc > 4 or opc < 1:
            Error(dir)

        if opc == 1:
            WebScraping()
            time.sleep(2)
        if opc == 2:
            print('Nuestro proyecto se basa en la información obtenida en la página web de la Prefectura Naval Argentina, de la cual obtendremos la información sobre los niveles de los ríos (link: https://contenidosweb.prefecturanaval.gob.ar/alturas/)')
            print('\n En primer lugar se realiza el scraping sobre el sitio, luego se pueden guardar los datos de interes en la base de datos, y además, se puede obtener la suba máxima, la baja máxima y el promedio (media) de los valores obtenidos.')
            system('pause')
            print('\n')
            print("\t\t|              ========= **** =========               |")
            print('\t\t|                SCRIPTS DESARROLLADOS                |')
            print('\t\t| 1. Cómo funciona el script de Web Scraping?         |')
            print('\t\t| 2. Cómo funciona el script la Base de Datos?        |')
            print('\t\t| 3. Cómo funciona el script para generar el informe? |')
            print("\t\t|              ========= **** =========               |")
            try:
                opcion = int(input("Seleccione una opción: "))
                break
            except ValueError:
                print("Oops! Seleccione una opción numérica por favor: ")
                Error(dir)
            
            if opcion == 1:
                Script_WS()
                time.sleep(2)
            if opcion == 2:
                Script_BD()
                time.sleep(2)
            if opcion == 3:
                Script_INF()
                time.sleep(2)
            if opcion > 3 or opcion < 1:
                Error(dir)

        if opc == 3:
            Nosotros()
            time.sleep(2)
        if opc == 4:
            bandera = False
            Retorna(dir)
    