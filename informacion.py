import main                 #Se importa el archivos main, para regresar la ejecución

#Se importan los módulos a utilizar:
import webbrowser                    #Se utiliza para abrir páginas web en el explorador
import time                          #Se usa para pausar, por un tiempo definido la ejecución
from os import system                #Se usa el modulo os para pausar la ejecución hasta que se oprima una tecla


#Respecto al trabajo realizado
def LibreríasUtilizadas(de):
    if de == 'WS':
        print('Acá se indican las librerías utilizadas en Web Scraping')

        print(' > Librería Requests: Requests es una librería de Python que facilita realizar las peticiones con protocolo HTTP. En el Web Scraping la utilizamos para hacer la petición GET al sitio web a scrapear.')
        print(' > Beautiful Soup: Beautiful Soup es una librería de Python para extraer datos de archivos HTML y XML. Funciona con su analizador favorito para proporcionar formas idiomáticas de navegar, buscar y modificar el esquema de análisis. La utilizamos en este proyecto para extraer los datos de la web y la combinamos con el “HTML parser” LXML.')
        print(' > Módulo LXML: LXML es un módulo de Python que se encarga de  procesar documentos XML y HTML y convertirlos en datos. Este módulo lo utilizamos para el Web Scraping al momento de extraer el contenido HTML de una web. LXML es conocido como un “HTML parser”')
        print(' > Pandas Pandas es una librería de Python especializada en el manejo y análisis de estructuras de datos. Permite leer y escribir fácilmente Dataframes, ficheros en formato CSV, Excel y bases de datos SQL. Crea estructuras de datos en formato array. Además posee métodos para reordenar, dividir y combinar conjuntos de datos. En nuestro caso, usamos Pandas para la creación y el manejo de Dataframes y archivos .csv, como así también para la visualización de esos datos.')

        print('\tDesea acceder a la Documentación? (1.SI o 2.NO): ')
        documentacion = int(input(': '))
        if documentacion == 1:
            webbrowser.open("https://requests.readthedocs.io/en/latest/user/quickstart/", new=2, autoraise=True)
            system('pause')
        print(' > Librería ....')
        print('\tDesea acceder a la Documentación? (1.SI o 2.NO): ')
        documentacion = int(input(': '))
        if documentacion == 1:
            webbrowser.open("https://requests.readthedocs.io/en/latest/user/quickstart/", new=2, autoraise=True)
            system('pause')
        
    if de == 'BD':
        print('Acá se indican las librerías utilizadas en Base de Datos')

def Script_BD():
    print('Aca va explicado el script de Base de Datos')
    LibreríasUtilizadas('BD')
    print('\n>> Regresando. Aguarde un momento por favor...')
                        
def Script_WS():
    print('Aca va explicado el script de Web Scraping')
    LibreríasUtilizadas('WS')
    print('\n>> Regresando. Aguarde un momento por favor...')

def WebScraping():
    print('\tWeb Scraping es una técnica utilizada mediante programas de software '
          'para extraer información de sitios web. '
          'Usualmente, estos programas simulan la navegación de un humano en el sitio, '
          'ya sea utilizando el protocolo HTTP manualmente, o incrustando un navegador en una aplicación.'
          '\nFUENTE: Wikipedia: https://es.wikipedia.org/wiki/Web_scraping')
    
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
    if ver == 'Github':
        print('https://github.com/ispc-programador2022/ESPCLS6')

def Retorna():
    main.menu(True)

def Error():
    print('*==========================*')
    print('*     Opción no válida     *')
    print('*==========================*')
    system('pause')
    print('\n>> Regresando. Aguarde un momento por favor...')
    menu()

def menu(a):

    bandera = a

    while bandera:
        
        print("\n\t-->  SUBMENU INFORMACIÓN  <--\n")
        print("\t1. Qué es el Web Scraping?")
        print("\t2. Scripts desarrollados")
        print("\t3. Quienes somos?")
        print("\t4. Volver al menu principal\n")
        while True:
            try:
                opc = int(input("Seleccione una opción: "))
                break
            except ValueError:
                print("Oops! Seleccione una opción numérica por favor: ")
                Error()
                    
        if opc > 4:
            Error()
        if opc < 1:
            Error()
        
        if opc == 1:
            WebScraping()
            time.sleep(2)
        if opc == 2:
            print("\t\t|           ========= **** =========           |\n")
            print('\t\t| 1. Cómo funciona el script de Web Scraping?  |')
            print('\t\t| 2. Cómo funciona el script la Base de Datos? |')
            opcion = int(input('Seleccione una opción: '))
            
            if opcion == 1:
                Script_WS()
                time.sleep(2)
            if opcion == 2:
                Script_BD()
                time.sleep(2)
            if opcion > 2:
                Error()
        if opc == 3:
            Nosotros()
            time.sleep(2)
        if opc == 4:
            bandera = False
            Retorna()
        if opc > 4:
            Error()
    