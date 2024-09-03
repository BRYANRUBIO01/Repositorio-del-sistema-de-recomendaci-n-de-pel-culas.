from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

# Cargamos los datos
user_movie_matrix = pd.read_csv("user_movie_matrix.csv")
item_similarity = pd.read_csv("item_similarity.csv", index_col=0)  # Cargar como DataFrame

test_data=pd.read_csv('C:\\Users\\DAYRA\\Desktop\\PROYECTOS BRYAN\\PELICULAS BASE DE DATOS\\ml-1m\\ml-1m\\ratings.dat',delimiter='::',engine='python',header=None, encoding='latin1')
test_data.columns = ['UserID', 'MovieID', 'Rating', 'Timestamp']
def get_recommendations(user_id, n_recommendations=5):
    # Verificar que el ID de usuario es válido
    if user_id < 1 or user_id > user_movie_matrix.shape[0]:
        return "ID de usuario no válido. Debe estar entre 1 y {}".format(user_movie_matrix.shape[0])

    user_index = user_id - 1
    user_ratings = user_movie_matrix.iloc[user_index]

    # Obtener índices de películas que el usuario ha calificado
    rated_movies_indices = user_ratings[user_ratings > 0].index.tolist()

    # Verificar si rated_movies_indices no está vacío
    if not rated_movies_indices:
        return "Este usuario no ha calificado ninguna película."

    # Calcular las puntuaciones para las películas no calificadas por el usuario
    scores = item_similarity.iloc[user_index].values  # Accede a la fila correspondiente del DataFrame

    # Obtener las películas recomendadas que no ha visto el usuario
    recommended_indices = np.argsort(scores)[::-1][:n_recommendations]

    # Asegúrate de que recommended_indices estén en el rango correcto
    recommended_movies = user_movie_matrix.columns[recommended_indices].tolist()  # Convertir a lista

    return recommended_movies



@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    precision = None
    actual_movies = []
    
    if request.method == "POST":
        user_id = int(request.form["user_id"])
        recommendations = get_recommendations(user_id)
        actual_movies = test_data[test_data["UserID"] == user_id]["MovieID"].values.tolist()  # Obtener las películas actuales
        precision = evaluate_recommendations(user_id)
        
    return render_template("index.html", recommendations=recommendations, precision=precision, actual_movies=actual_movies)


def evaluate_recommendations(user_id, n_recommendations=5):
    recommended_movies = get_recommendations(user_id, n_recommendations)
    actual_movies = test_data[test_data["UserID"] == user_id]["MovieID"].values
    precision = np.isin(recommended_movies, actual_movies).mean()  # calcula la precisión
    return precision

if __name__ == "__main__":
    app.run(debug=True)

# Solo para verificar test_data
test_data=pd.read_csv('C:\\Users\\DAYRA\\Desktop\\PROYECTOS BRYAN\\PELICULAS BASE DE DATOS\\ml-1m\\ml-1m\\ratings.dat',delimiter='::',engine='python',header=None, encoding='latin1')
print(test_data.columns)