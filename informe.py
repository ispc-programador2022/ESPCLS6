import main

import web_scraping as ws
import pandas as pd
import time
import os

def generaDf(rutacsv):
    df = pd.read_csv(rutacsv) # Ruta y nombre de archivo.csv
    return df

def Retorna(direccion):
    main.menu(True, direccion)

def Error(archivo):
    print('*==========================*')
    print('*     Opción no válida     *')
    print('*==========================*')
    os.system('pause')
    print('\n>> Regresando. Aguarde un momento por favor...')
    menu(True, archivo)

def menu(b, ruta):
    bandera = b

    #Si el archivo no esta creado, retorna al menu para crearlo
    if ruta == 'lalala':
        print('\n\t||            ----> ERROR <----            ||')
        print('\t|| Debe realizar scraping en primer lugar  ||')
        print('\t||    ---------------------------------    ||')
        print('\n>> Regresando. Aguarde un momento por favor...')
        time.sleep(4)
        Retorna(ruta)

    while bandera:
        df = generaDf(ruta)
        print("\n\t-->  SUBMENU INFORME  <--\n")
        print("\t1. Mostrar tabla de datos")
        print("\t2. Informar cual fue la SUBA MAXIMA")
        print("\t3. Informar cual fue la BAJA MAXIMA")
        print("\t4. Calcular la media de variación")
        print("\t5. Volver al menu principal\n")
                
        while True:
            try:
                opc = int(input("Seleccione una opción: "))
                break
            except ValueError:
                print("Oops! Seleccione una opción numérica por favor: ")
                Error(ruta)
                    
        if opc > 5 or opc < 1:
            Error(ruta)
            
        if opc == 1:
            print('\n\t*===================================*')
            print('\t*===========Tabla de datos=========== *')
            print('\t*====================================*')
            print(df)
            time.sleep(2)
        if opc == 2:
            df['Variación'] = df['Variación'].astype('string')
            df['Variación']=df['Variación'].str.ljust(2, "0")
            niveles_df=df[['Variación']]
            df = df.astype({'Variación': 'float64'})

            max_df = df['Variación'].max()      #calcula el maximo
            print("La SUBA MAXIMA fue: ", max_df)
            time.sleep(2)
        if opc == 3:
            df['Variación'] = df['Variación'].astype('string')
            df['Variación']=df['Variación'].str.ljust(2, "0")

            niveles_df=df[['Variación']]
            df = df.astype({'Variación': 'float64'})
            
            min_df = df['Variación'].min()      #calcula el minimo
            print("La BAJA MAXIMA fue: ", min_df)
            time.sleep(2)
        if opc == 4:
            df['Variación'] = df['Variación'].astype('string')
            df['Variación']=df['Variación'].str.ljust(2, "0")

            niveles_df=df[['Variación']]
            df = df.astype({'Variación': 'float64'})

            mean_df = df['Variación'].mean()       #calcula el promedio (media aritmética)
            print("La media de variación fue: ", mean_df)
            time.sleep(2)
        if opc == 5:
            bandera = False                
            Retorna(ruta)
