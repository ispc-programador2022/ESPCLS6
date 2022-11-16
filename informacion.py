import main                 #Se importa el archivos main, para regresar la ejecución

#Se importan los módulos a utilizar:
import webbrowser                    #Se utiliza para abrir páginas web en el explorador
import time                          #Se usa para pausar, por un tiempo definido la ejecución
from os import system                #Se usa el modulo os para pausar la ejecución hasta que se oprima una tecla


#Respecto al trabajo realizado
def LibreríasUtilizadas(de):
    if de == 'WS':
        print('Acá se indican las librerías utilizadas en Web Scraping')
        print(' > Librería Requests:')
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
    print('Acá se citan los miembros del grupo y se indican sus respectivos roles')
    Recursos('Trello')
    Recursos('Github')
    print('\n>> Regresando. Aguarde un momento por favor...')

def Recursos(ver):
    if ver == 'Trello':
        print('Acá va el link al tablero de Trello')
    if ver == 'Github':
        print('Acá va el link al repo de Github')

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
    