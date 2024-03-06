# ## # def userdata( User_id : str ) # # # # 
# Cargar datos desde el archivo CSV
from fastapi import FastAPI
import pandas as pd
try:

    data = pd.read_csv("csv_parquet/i2do_enpoint.csv")
    
except Exception as e:
    print("Error al cargar el archivo CSV:", e)

app = FastAPI()

@app.get('/')
async def userdata(User_id: str):
    try:
        # Filtrar datos por user_id
        user_data = data[data['user_id'] == User_id]

        print("user_data:", user_data)  # Impresión para verificar el contenido del DataFrame

        # Calcular dinero gastado
        dinero_gastado = user_data['price'].sum()

        # Calcular porcentaje de recomendación
        total_reviews = user_data['recommend'].count()
        if total_reviews > 0:
            recomendados = user_data['recommend'].sum()
            porcentaje_recomendacion = (recomendados / total_reviews) * 100
        else:
            porcentaje_recomendacion = 0

        # Calcular cantidad total de items
        cantidad_items = user_data['items_count'].sum()

        # Convertir los resultados a tipos de datos básicos antes de devolverlos
        dinero_gastado = float(dinero_gastado)
        porcentaje_recomendacion = float(porcentaje_recomendacion)
        cantidad_items = int(cantidad_items)
        
        return {
            "Usuario": User_id,
            "Dinero gastado": f"{dinero_gastado} USD",
            "% de recomendación": f"{porcentaje_recomendacion}%",
            "Cantidad de items": cantidad_items
        }
    except KeyError as e:
        return {"Error": f"La columna '{e.args[0]}' no está presente en el DataFrame."}
    except Exception as e:
        return {"Error": str(e)}
# # ## # ## # ## # ## # ## # ## # ## # ## # #
# # ## # ## # ## # ## # ## # ## # ## # ## # #
# # #def best_developer_year( año : int ) # # #
from fastapi import FastAPI
import pandas as pd


# Leer los datos del archivo CSV
data_final = pd.read_csv("csv_parquet/i4to_endpoint.csv")
@app.get('/best_developer_year/')
def best_developer_year(año: int):
    
    # Filtrar el DataFrame por el año dado
    df_año = data_final[data_final['year'] == año]

    # Filtrar los juegos con recomendaciones positivas y comentarios positivos
    df_filtrado = df_año[(df_año['recommend'] == True) & (df_año['sentiment_analysis'] == 2)]

    # Agrupar por desarrollador y contar el número de juegos recomendados
    df_agrupado = df_filtrado.groupby('developer')['title'].count().reset_index()

    # Ordenar en orden descendente y tomar los primeros 3 desarrolladores
    df_top_3 = df_agrupado.sort_values(by='title', ascending=False).head(3)

    # Construir el resultado en el formato requerido
    resultado = [{"Puesto " + str(i + 1): row['developer']} for i, (_, row) in enumerate(df_top_3.iterrows(), start=0)]

    return resultado

# # ## # ## # ## # ## # ## # ## # ## # ## # #
# # ## # ## # ## # ## # ## # ## # ## # ## # #
#def UserForGenre( genero : str ):
import pandas as pd
from fastapi import FastAPI

# Leer el archivo CSV
data = pd.read_csv("csv_parquet/datos_finales2.csv")



@app.get("/user_for_genre/")
async def get_user_for_genre(genero: str):
    # Verificar si el género especificado está presente en las columnas de géneros
    if genero not in data.columns[4:24]:
        return {"Error": "El género especificado no está presente en los datos."}

    # Filtrar las filas que corresponden al género especificado
    data_genero = data[data[genero] == 1]

    if data_genero.empty:
        return {"Error": "No se encontraron datos para el género especificado."}

    # Encontrar el usuario con la máxima cantidad de horas jugadas para ese género
    max_horas_jugadas = data_genero['playtime_forever'].max()
    usuario_max_horas = data_genero.loc[data_genero['playtime_forever'].idxmax(), 'user_id']

    # Calcular la acumulación de horas jugadas por año de lanzamiento para el género dado
    acumulacion_por_año = data_genero.groupby('year')['playtime_forever'].sum().to_dict()

    # Convertir los valores numéricos a tipos nativos de Python
    max_horas_jugadas = int(max_horas_jugadas)
    usuario_max_horas = str(usuario_max_horas)

    return {
        "Usuario con más horas jugadas": usuario_max_horas,
        "Cantidad máxima de horas jugadas": max_horas_jugadas,
        "Acumulación de horas jugadas por año de lanzamiento": acumulacion_por_año
    }



# # ## # ## # ## # ## # ## # ## # ## # ## # #
# # ## # ## # ## # ## # ## # ## # ## # ## # #
# # # RECOMENDACION DE JUEGOS # # # 
# # # def recomendacion_juego( id de producto )# # # 
from fastapi import FastAPI
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances

# Cargar el archivo CSV
df = pd.read_csv("csv_parquet/ml.csv")

# Convertir las columnas relevantes a una matriz NumPy para el cálculo de similitud
X = df.iloc[:, 3:].to_numpy()

# Calcular la matriz de similitud usando la distancia de Jaccard
jaccard_sim = 1 - pairwise_distances(X, metric='jaccard')

@app.get("/recomendacion_juego/")
async def recomendacion_juego(nombre_producto: str):
    # Convertir la entrada a minúsculas para hacerla insensible a mayúsculas y minúsculas
    nombre_producto = nombre_producto.lower()
    
    # Obtener el índice del juego ingresado
    juego_index = df[df['title'].str.lower() == nombre_producto].index[0]
    
    # Obtener las similitudes del juego ingresado con todos los demás juegos
    sim_scores = list(enumerate(jaccard_sim[juego_index]))
    
    # Ordenar los juegos según su similitud y excluir el propio juego
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:]
    
    # Obtener los nombres de los 5 juegos más similares
    top_similar_juegos = [df.iloc[score[0]]['title'] for score in sim_scores[:5]]
    
    return {"recomendaciones": top_similar_juegos}






