# josue-mora-proyecto1
# Proyecto de Data Science: Sistema de Recomendación de Videojuegos 🎮
[![portada](https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png "portada")](https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png "portada")
¡Bienvenido a mi proyecto de Data Science centrado en el mundo de los videojuegos! Este proyecto es una amalgama de pasión por los datos y el amor por los videojuegos. Desde la limpieza y exploración de datos hasta el despliegue de un sistema de recomendación, ¡cada paso ha sido emocionante y gratificante!

## Descripción del Proyecto

Este proyecto se centra en la creación de un sistema de recomendación de videojuegos utilizando técnicas de Data Science. Incluye:

1. **ETL (Extracción, Transformación y Carga):** Proceso para limpiar y preparar los datos de los videojuegos.
2. **EDA (Análisis Exploratorio de Datos):** Exploración detallada de los datos para comprender mejor las tendencias y patrones.
3. **Desarrollo de un sistema de recomendación:** Implementación de un algoritmo que sugiere juegos similares a uno dado por el usuario.
4. **Despliegue con FastAPI:** Uso de FastAPI para crear una API que ofrece la funcionalidad de recomendación de videojuegos.

## Funciones Adicionales

Además del sistema de recomendación, también se desarrollaron las siguientes funciones para proporcionar más información y análisis:

1. **userdata(User_id: str):** Devuelve la cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews.recommend y la cantidad de items.
   
2. **UserForGenre(genero: str):** Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.

3. **best_developer_year(año: int):** Devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos)

4. **recomendacion_juego(nombre_juego: str):** Ingresando el nombre de un juego, deberías recibir una lista con 5 juegos recomendados similares al ingresado.

## Tecnologías Utilizadas

- **Lenguaje de Programación:** Python
- **Librerías Principales:** Pandas, NumPy, Seaborn, Matplotlib, scikit-learn
- **Framework para API:** FastAPI
- **Servidor ASGI:** Uvicorn
- **Entre otras**

## Pasos Realizados

1. **ETL:**
   - Extraje datos de 3 fuentes csv , teniendo que unirlas y haciendo por comodidad csv nuevos para cada endpoint.
   - Realicé la limpieza de datos para eliminar valores nulos y duplicados, así como para estandarizar formatos.
   - Transformé los datos en un formato adecuado para el análisis y modelado.

2. **EDA:**
   - Exploré los datos utilizando gráficos y estadísticas descriptivas.
   - Identifiqué patrones, tendencias y relaciones entre variables relevantes.
   - Utilicé visualizaciones para comunicar hallazgos de manera efectiva.

3. **Desarrollo del Sistema de Recomendación:**
   - Implementé algoritmos de recomendación, como filtrado colaborativo o basado en contenido, dependiendo de los requisitos del proyecto.
   - Entrené modelos utilizando técnicas de aprendizaje automático para predecir juegos similares.
   - Optimicé el rendimiento del modelo y evalué su precisión utilizando métricas adecuadas.

4. **Despliegue con FastAPI:**
   - Configuré una API utilizando FastAPI para ofrecer servicios de recomendación a los usuarios.
   - Desplegué la API en un servidor ASGI (Uvicorn) para que esté disponible en línea.
   - Probé la funcionalidad de la API para garantizar su correcto funcionamiento.

## Instrucciones de Uso

Para utilizar el sistema de recomendación y las funciones adicionales, sigue estos pasos:

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias utilizando `pip install -r requirements.txt`.
3. Ejecuta el servidor FastAPI utilizando el comando `uvicorn main:app --reload`.
4. Accede a la API a través de tu navegador o cliente de API preferido.

¡Disfruta explorando y descubriendo nuevos juegos con nuestro sistema de recomendación!

## Contribuciones

Las contribuciones son bienvenidas. Si tienes sugerencias para mejorar este proyecto, por favor crea un pull request o abre un issue para discutir tus ideas.

## Contacto

Si tienes alguna pregunta o comentario sobre este proyecto, no dudes en ponerte en contacto conmigo a través de mi correo electrónico [josuekarimmr@gmail.com](mailto:tu@email.com).

¡Gracias por tu interés en mi proyecto!
