import pandas as pd

rios_df = pd.read_csv('C:\\Users\\Dell\\Document\\pepepe.csv') # Ruta y nombre de archivo.csv

#print(rios_df.columns) # columnas

print(rios_df.dtypes) # tipo de datos

rios_df=rios_df.astype({'Variación': 'float64'})

print(rios_df.dtypes)

mean_df = rios_df['Variación'].mean()
print(mean_df)


