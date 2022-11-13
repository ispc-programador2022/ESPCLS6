import pandas as pd

rios_df = pd.read_csv('C:\\Users\\Dell\\Document\\pepe.csv') # Ruta y nombre de archivo.csv

# print(rios_df.dtypes) # tipos de datos

print(rios_df.columns) # columnas

print(rios_df.dtypes) # tipo de datos

print(pd.unique(rios_df['Puerto']))