
# JAQUEZ ANDRES 0074
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Problema 6: Películas (Título, recaudación en billones USD, ganó Oscar a mejor película, año)
avt = ['Avatar', 2.9, False, 2009]
end = ['Avengers: Endgame', 2.7, False, 2019]
ttn = ['Titanic', 2.2, True, 1997]
sw7 = ['Star Wars VII', 2.0, False, 2015]
inf = ['Avengers: Infinity War', 2.0, False, 2018]

# Creamos una lista de listas (conformando la tabla)
lista_peliculas = [avt, end, ttn, sw7, inf]

# Utilizar pandas para organizar la tabla (dataframe o marco de datos)
df_peliculas = pd.DataFrame(lista_peliculas, columns=["Nombre", "Recaudación", "Ganó Oscar", "Año"])
print(df_peliculas)

# Creamos el archivo CSV y lo guardamos
# df_peliculas.to_csv("Peliculas.csv", index=False)

# Crea gráfica de línea
# Donde x es nombre en el eje horizontal
# Donde y es recaudación en el eje vertical
plt.plot(df_peliculas["Nombre"], df_peliculas["Recaudación"])
plt.title("Gráfica de películas")
plt.xlabel("Nombre de las películas")
plt.ylabel("Recaudación en billones USD")
plt.show()

# Creamos una gráfica de puntos
plt.scatter(df_peliculas["Nombre"], df_peliculas["Recaudación"])
plt.show()

# Gráfica de barras
plt.bar(df_peliculas["Nombre"], df_peliculas["Recaudación"])

# Etiquetas y título
plt.title("Películas")
plt.xlabel("Las películas")
plt.ylabel("Recaudación en billones USD")

# Mostrar gráfica
plt.show()

# Ahora ordenar las gráficas de barras de manera descendente
# De la más grande a la pequeña

df_peliculas_ordenar = df_peliculas.sort_values("Recaudación", ascending=False)
plt.bar(df_peliculas_ordenar["Nombre"], df_peliculas_ordenar["Recaudación"])
plt.show()

# Coloreando la gráfica
plt.bar(df_peliculas_ordenar["Nombre"], df_peliculas_ordenar["Recaudación"],
        color=["b", "g", "c", "m", "y"])
plt.show()

# Gráfica de pastel
plt.pie(df_peliculas["Recaudación"], labels=df_peliculas["Nombre"])
plt.show()
# JAQUEZ ANDRES 0074