#tp

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#importando csv
df=pd.read_csv("fifa_23_280922.csv")
print("OKEY! Archivo cargado correctamente")

#1
filas,columnas= df.shape
print(f"El dataframe tiene {filas} filas y {columnas} columnas")

#2
total_aceleracion= df['Acceleration'].count()
print(f"Cantidad de filas con Aceleración: {total_aceleracion}")

#3
filtro_avanzado= df['Nom'].str.startswith('A', na=False)
df_filtrado=df[filtro_avanzado]

total_registros= df_filtrado['Nom'].count()
print(f"Cantidad de nombres con A: {total_registros}")

#4
print(df_filtrado.head())

#5
datos_torta= df_filtrado.groupby("Nom")["Acceleration"].sum()

#6
suma_aceleracion= df_filtrado['Acceleration'].sum()
print(f"Valor total de aceleración: {suma_aceleracion}")

print("Reporte automatizado")
print(f"Valor total de aceleraciones: {suma_aceleracion}")

if Default_limite_alto:=(suma_aceleracion>80000):
    print("Alerta: el volumen de aceleración es muy alto")
    print("Prioridad alta")

else:
    print("Estado: volumen de aceleración normal")
    print("Estado normal")

#7
df_top_50=df.nlargest(50,'Acceleration')

sns.set_theme(style="whitegrid")
plt.figure(figsize=(9,5))
sns.barplot(
    data=df_top_50,
    x="Nom",
    y="Acceleration",
    estimator= sum,
    errorbar=None,
    hue= "Nom",
    palette="magma",
)
plt.title(
    "Distribucion de aceleración de cada club", fontsize=14
)
plt.xlabel("Nombre", fontsize=11)
plt.ylabel("Aceleracion", fontsize=11)

plt.tight_layout()
plt.xticks(rotation=50, fontsize=3)
plt.savefig("grafico_aceleración.png", dpi=300, bbox_inches="tight")
plt.close()
print("Gráfico guardado como grafico_aceleración.png")

#8 
df_top_5=df.nlargest(5,'Acceleration')
plt.figure(figsize=(7,7))
plt.pie(
    df_top_5["Acceleration"],
    labels=df_top_5["Nom"],
    autopct="%1.1f%%",
    colors=sns.color_palette("Set2"),
    startangle=140,
    wedgeprops={"edgecolor":"white", "linewidth":2}
)
plt.title("Jugadores con más aceleración")
plt.tight_layout()
plt.xticks(rotation=50, fontsize=3)
plt.savefig("grafico_aceleracion2.png", dpi=300, bbox_inches="tight")
plt.close()
print("Gráfico guardado como grafico_aceleracion2.png")

#9
condicion_extra= df['Général']>70
resultado=df.loc[filtro_avanzado & condicion_extra,
                   ["Nom", "Général", "Pays"]]
print(resultado)
print(f"\nFilas seleccionadas: {len(resultado)}")