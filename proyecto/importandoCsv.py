import pandas as pd
import seaborn as sns
import matplotlib.pyplot as pit

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

#------------------------------------------
#GRAFICO 1: Grafico de barras (con seaborn)

sns.set_theme(style="whitegrid")
pit.figure(figsize=(9,5))
sns.barplot(
    data=df,
    x="Pays",
    y="Force",
    estimator= sum,
    errorbar=None,
    palette="magma",
)
pit.title(
    "Distribucion de fuerza de cada país", fontsize=14
)
pit.xlabel("País", fontsize=11)
pit.ylabel("Fuerza", fontsize=11)

pit.tight_layout()
pit.xticks(rotation=50, fontsize=3)
pit.savefig("grafico_fuerza.png", dpi=300, bbox_inches="tight")
pit.close()
print("Gráfico guardado como grafico_fuerza.png")

#GRAFICO 2: Grafico de torta

datos_torta= df_filtrado.groupby("Pays")["Force"].sum()

pit.figure(figsize=(7,7))
pit.pie(
    datos_torta,
    labels=datos_torta.index,
    autopct="%1.1f%%",
    colors=sns.color_palette("Set2"),
    startangle=140,
    wedgeprops={"edgecolor":"white", "linewidth":2}
)
pit.title("Distribucion interna de fuerza")
pit.tight_layout()
pit.xticks(rotation=50, fontsize=3)
pit.savefig("grafico_fuerza2.png", dpi=300, bbox_inches="tight")
pit.close()
print("Gráfico guardado como grafico_fuerza2.png")

#GRAFICO 3
sns.set_theme(style="whitegrid")
pit.figure(figsize=(9,5))
sns.barplot(
    data=df,
    x="Nom",
    y="Acceleration",
    estimator= sum,
    errorbar=None,
    palette="magma",
)
pit.title(
    "Distribucion de potencia de cada club", fontsize=14
)
pit.xlabel("Nombre", fontsize=11)
pit.ylabel("Aceleracion", fontsize=11)

pit.tight_layout()
pit.xticks(rotation=50, fontsize=3)
pit.savefig("grafico_potencia.png", dpi=300, bbox_inches="tight")
pit.close()
print("Gráfico guardado como grafico_potencia.png")