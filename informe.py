import main
import web_scraping as ws
import pandas as pd
import time
import os

#r = web_scraping.CrearCSV()

rios_df = pd.read_csv("C:\\Users\\Dell\\Desktop\\ESPCLS6\\datos.csv") # Ruta y nombre de archivo.csv

#print(rios_df.columns) # columnas
#tipo de datos print(rios_df.dtypes)

rios_df['Variación'] = rios_df['Variación'].astype('string')
rios_df['Variación']=rios_df['Variación'].str.ljust(2, "0")

niveles_df=rios_df[['Variación']]
rios_df=rios_df.astype({'Variación': 'float64'})

def Retorna():
    main.menu(True)

def Error():
    print('*==========================*')
    print('*     Opción no válida     *')
    print('*==========================*')
    os.system('pause')
    print('\n>> Regresando. Aguarde un momento por favor...')
    menu()

def menu(b):
    ruta = "C:\\Users\\Dell\\Desktop\\ESPCLS6\\datos.csv"              
    bandera = b
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
                
        while True:
            try:
                opc = int(input("Seleccione una opción: "))
                break
            except ValueError:
                print("Oops! Seleccione una opción numérica por favor: ")
                Error()
                    
        if opc > 5:
            Error()
        if opc < 1:
            Error()
            
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
      
