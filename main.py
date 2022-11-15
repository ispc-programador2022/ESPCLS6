#Se importan los archivos que se ejecutarán en el menu de opciones:
import informacion as info
import base_datos as bd
import web_scraping as ws
#import informe

#Se importan los módulos a utilizar:
import os   #Se usa el modulo os para pausar la ejecución hasta que se oprima una tecla
import time     # Se usa para pausar, por un tiempo definido la ejecución


def Error():
    print('*==========================*')
    print('*     Opción no válida     *')
    print('*==========================*')
    os.system('pause')
    print('\n>> Regresando. Aguarde un momento por favor...')
    menu(True)

def menu(bandera, archivo='lalala'):
    while bandera:
        print("\n==>  MENU PRINCIPAL  <==\n")
        print("1. Información sobre el trabajo desarrollado")
        print("2. Realizar Web Scraping")
        print("3. Cargar Base de Datos")
        print("4. Generar informe")
        print("5. Salir")
        print(' ')
        opcion_menu = int(input("Seleccione una opción: "))
            
        if opcion_menu > 5:
            Error()
        if opcion_menu < 1:
            Error()
       
        if opcion_menu == 1:
            info.menu(True)

        if opcion_menu == 2:
            print('Ejecutando Scraping. Aguarde un momento por favor...')
            df = ws.Ejecutar()
            os.system('pause')
            print('A continuación se creará el archivo csv')
            time.sleep(2)
            ws.CrearCSV(df)

        if opcion_menu == 3:
            bd.menu(True, archivo)
            
        if opcion_menu == 4:
            print("FALTA HACER ESTO!!!")
            print('Generando informe. Aguarde un momento por favor...')
            df = ws.Ejecutar()
            os.system('pause')
            print('A continuación se muestra el informe solicitado:')
            time.sleep(2)
            ws.CrearCSV(df)

        if opcion_menu == 5:
            bandera = False
            print('\n')
            print('\t\t*===================================*')
            print('\t\t*===================================*')
            print('\t\t* GRACIAS POR SU UTILIZAR EL SCRIPT *')
            print('\t\t*          PONGANOS 10! :D          *')
            print('\t\t*===================================*')
            print('\t\t*===================================*')
        break
            

if __name__ == '__main__':
    menu(True)    