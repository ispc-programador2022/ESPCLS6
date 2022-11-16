import main
import web_scraping as ws
import pandas as pd
import time
import os

#r = web_scraping.CrearCSV()

rios_df = pd.read_csv("C:\\Users\\Dell\\Document\\pepepe.csv") # Ruta y nombre de archivo.csv

#print(rios_df.columns) # columnas
#tipo de datos print(rios_df.dtypes)

rios_df=rios_df.astype({'Variación': 'float64'})

def Retorna():
    main.menu(True)

def Error():
    print('*==========================*')
    print('*     Opción no válida     *')
    print('*==========================*')
    os.system('pause')
    print('\n>> Regresando. Aguarde un momento por favor...')

def menu():
    ruta = "C:\\Users\\Dell\\Document\\pepepe.csv"                #Instancia de la clase
    bandera = True
    #Si el archivo no esta creado, retorna al menu para crearlo
    if ruta == 'lalala':
        print('\n\t||            ----> ERROR <----            ||')
        print('\t|| Debe realizar scraping en primer lugar  ||')
        print('\t||    ---------------------------------    ||')
        print('\n>> Regresando. Aguarde un momento por favor...')
        time.sleep(4)
        Retorna()


    while bandera:
        print("\n\t-->  SUBMENU INFORME  <--\n")
        print("\t1. Mostrar tabla de datos")
        print("\t2. Informar cual fue la SUBA MAXIMA")
        print("\t3. Informar cual fue la BAJA MAXIMA")
        print("\t4. Calcular la media de variación")
        print("\t5. Volver al menu principal\n")
        opc = int(input('Seleccione una opción: '))
        
        if opc == 1:
            print(rios_df)
            time.sleep(2)
        if opc == 2:
            max_df = rios_df['Variación'].max()
            print(max_df)
            time.sleep(2)
        if opc == 3:
            min_df = rios_df['Variación'].min()
            print(min_df)
            time.sleep(2)
        if opc == 4:
            mean_df = rios_df['Variación'].mean()
            print(mean_df)
            time.sleep(2)
        if opc == 5:
            bandera = False                
            Retorna()
        if opc > 5:
            Error()

menu()