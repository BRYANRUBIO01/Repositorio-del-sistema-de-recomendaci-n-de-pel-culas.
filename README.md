# Sistema de Recomendación de Películas

Este proyecto implementa un sistema de recomendación de películas utilizando técnicas de machine learning. El modelo principal está basado en un autoencoder para generar representaciones latentes de los usuarios y las películas.

## Estructura del Proyecto

- **app.py**: El archivo principal que contiene el backend de la aplicación.
- **templates/**: Carpeta que contiene los archivos HTML para la interfaz de usuario.
- **static/**: Carpeta que contiene los archivos CSS 
- **data/**: Carpeta que contiene las bases de datos utilizadas en el proyecto.
  - `user_movie_matrix.csv`: Matriz usuario-película con calificaciones.
  - `item_similarity.npy`: Matriz de similitud de ítems.
- **README.md**: Este archivo, que describe el proyecto.

## Requisitos

- Python
- TensorFlow
- Keras
- Pandas
- Numpy

## MODO DE USO 

correr el archivo app.py con las documentacion y archivos user e item lo cual los mandara a una pagina web local en el cual pueden colocar cualquier nombre de usuario y en automatico se les recomendara 5 peliculas de acurdo a sus gustos similares con otros clientes .

Se encuentra en version base.