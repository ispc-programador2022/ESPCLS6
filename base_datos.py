import main                 #Se importa el archivos main, para regresar la ejecución

#Se importan los módulos a utilizar:
import mysql.connector      #Se utiliza para conectar con la base de datos y ejecutar las sentencias en la misma ()
import time                 #Se usa para pausar, por un tiempo definido la ejecución
import os                   #Se usa el modulo os para pausar la ejecución hasta que se oprima una tecla
import pandas               #Se usa para importar los resultados de una consulta en SQL


class BaseDatos():
    
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                port=3306,
                password=input('Ingrese la contraseña para conectarse a la base de datos: '),
            )
            print('\n\t*===================*')
            print('\t* CONEXION EXITOSA! *')
            print('\t*===================*')
            time.sleep(3)

        except mysql.connector.Error as descripcionError:
            print('\n\t||    ----> ERROR <----    ||')
            print('\n\t', descripcionError)
            print('\t||    -----------------    ||')
            os.system('pause')
    
    def CrearBaseDatos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "CREATE DATABASE altura_rios;"   #indicamos la sentencia a ejecutar
                cursor.execute(sentenciaSQL)                    #ejecutamos la sentencia
                
                print('\n\t*=====================================*')        #confirma con un mensaje en pantalla
                print('\t* Base de datos creada correctamente! *')
                print('\t*=====================================*')
                
                self.conexion.close()                           #cierra la conexión
                time.sleep(3)
                
            except mysql.connector.Error as descripcionError:
                print('\n\t||    ----> ERROR <----    ||')
                print('\n\t', descripcionError)
                print('\t||    -----------------    ||')
                os.system('pause')
        print('\n>> Regresando. Aguarde un momento por favor...')
    
    def CrearTablas(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute('use altura_rios;')
                cursor.execute('DROP TABLE IF EXISTS altura_rios_data;')
                print('\n\t*==============================*')
                print('\t* Conectado a la base de datos *')
                print('\t*==============================*')
                
                #crea las tablas:
                print('\n>> Creando tablas...')
                cursor.execute('CREATE TABLE altura_rios_data(puerto varchar(25), rio varchar(25), variacion varchar(10), estado varchar(20))')
                
                print('\n\t*===============================*')
                print('\t* Tablas creadas correctamente! *')
                print('\t*===============================*')
                
                self.conexion.close()
                time.sleep(3)
                
            except mysql.connector.Error as descripcionError:
                print('\n\t||    ----> ERROR <----    ||')
                print('\n\t', descripcionError)
                print('\t||    -----------------    ||')
                os.system('pause')
        
        print('\n>> Regresando. Aguarde un momento por favor...')
    
    def InsertarDatos(self, dir):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                archivo = pandas.read_csv(dir, index_col=False, delimiter=',')  #se indica el archivo a utilizar
                archivo.head()
                
                for i, row in archivo.iterrows():       #recorre el archivo y carga los datos en la base de datos
                    sentencia = 'INSERT INTO altura_rios.altura_rios_data VALUES (%s,%s,%s,%s)'
                    cursor.execute(sentencia, tuple(row))
                    print('Nuevo dato cargado correctamente! ')
                    self.conexion.commit()              #guarda los cambios en la base de datos
                print('\n\t*===============================================================*')
                print('\t*Los datos fueron importados correctamente en la base de datos! *')
                print('\t*===============================================================*')

                self.conexion.close()
                time.sleep(2)

            except mysql.connector.Error as descripcionError:
                print('\n\t||    ----> ERROR <----    ||')
                print('\n\t', descripcionError)
                print('\t||    -----------------    ||')
                os.system('pause')

        print('\n>> Regresando. Aguarde un momento por favor...')
        
    def VerTablaCompleta(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM altura_rios.altura_rios_data"
                cursor.execute(sentenciaSQL)
                
                #muestra los datos de la tabla:
                print('\n------------- DATOS -------------')
                for dato in cursor:                         
                        print(dato)
                
                self.conexion.close()
                os.system('pause')
            
            except mysql.connector.Error as descripcionError:
                print('\n\t||    ----> ERROR <----    ||')
                print('\n\t', descripcionError)
                print('\t||    -----------------    ||')
                os.system('pause')
        print('\n>> Regresando. Aguarde un momento por favor...')
    

def Retorna(direccion):
    main.menu(True, direccion)

def Error(archivo):
    print('*==========================*')
    print('*     Opción no válida     *')
    print('*==========================*')
    os.system('pause')
    print('\n>> Regresando. Aguarde un momento por favor...')
    menu(True, archivo)

def menu(a, ruta):
    bandera = a
    

    #Si el archivo no esta creado, retorna al menu para crearlo
    if ruta == 'lalala':
        print('\n\t||            ----> ERROR <----            ||')
        print('\t|| Debe realizar scraping en primer lugar  ||')
        print('\t||    ---------------------------------    ||')
        print('\n>> Regresando. Aguarde un momento por favor...')
        time.sleep(4)
        Retorna(ruta)


    while bandera:
        print("\n\t-->  SUBMENU BASE DE DATOS  <--\n")
        print("\t1. Crear Base de Datos")
        print("\t2. Crear tablas en la Base de Datos")
        print("\t3. Importar datos desde el archivo CSV")
        print("\t4. Ver tabla cargada")
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
            bd = BaseDatos()                #Instancia de la clase
            bd.CrearBaseDatos()
            time.sleep(2)
        if opc == 2:
            bd = BaseDatos()  
            bd.CrearTablas()
            time.sleep(2)
        if opc == 3:
            bd = BaseDatos()                #Instancia de la clase
            bd.InsertarDatos(ruta)
            time.sleep(2)
        if opc == 4:
            bd = BaseDatos()                #Instancia de la clase
            bd.VerTablaCompleta()
            
        if opc == 5:
            bandera = False                
            Retorna(ruta)