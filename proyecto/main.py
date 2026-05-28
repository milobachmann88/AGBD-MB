import pandas as pd
#importando csv
df=pd.read_csv("fifa_23_280922.csv")
print("OKEY! Archivo cargado correctamente")

#Mostrando las primeras filas del dataframe
print(df.head())

#cuenta el total de filas y columnas que tiene el archivo
filas,columnas= df.shape
print(f"El dataframe tiene {filas} filas y {columnas} columnas")

#Cuenta la cantidad de filas de una columna
total_performance= df['Performance'].count()
print(f"Cantidad de filas con Performance: {total_performance}")

#Cuenta la cantidad de filas de una columna con una condicion
print("Analisis avanzado de datos")

filtro_avanzado= df['Pays'].str.startswith('F', na=False)
df_filtrado=df[filtro_avanzado]

total_registros= df_filtrado['Pays'].count()
print(f"Cantidad de paises con F: {total_registros}")

#Suma los valores de una columna
suma_fuerza= df_filtrado['Force'].sum()
print(f"Valor total de fuerzas: {suma_fuerza}")

print("Reporte automatizado")
print(f"Valor total de fuerzas: {suma_fuerza}")

if Default_limite_alto:=(suma_fuerza>80000):
    print("Alerta: el volumen de fuerzas es muy alto")
    print("Requiere revisión inmediata")

elif suma_fuerza>20000:
    print("Aviso: volumen de fuerzas moderado")
    print("Monitorear comportamiento")

else:
    print("Estado: volumen de fuerza bajo")
    print("No requiere accion adicional")