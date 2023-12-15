import streamlit as st
import requests

# Titre de l'application
st.title('Prediction de l\'espèce Iris')

# Interface utilisateur pour saisir les caractéristiques de l'Iris
sepal_length = st.number_input('Sepal Length', min_value=0.1, max_value=10.0, value=5.4, step=0.1)
sepal_width = st.number_input('Sepal Width', min_value=0.1, max_value=10.0, value=3.4, step=0.1)
petal_length = st.number_input('Petal Length', min_value=0.1, max_value=10.0, value=1.7, step=0.1)
petal_width = st.number_input('Petal Width', min_value=0.1, max_value=10.0, value=0.2, step=0.1)

# Bouton pour effectuer la prédiction
if st.button('Predict'):
    # Données pour la requête à l'API
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    # Faire une requête POST à l'API FastAPI
    response = requests.post('http://127.0.0.1:8000/predict', json=payload)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        result = response.json()
        st.write(f"Prédiction: {result['prediction']}")
        st.write(f"Probabilité: {result['probability']}")
    else:
        st.write("Échec de la prédiction. Veuillez réessayer.")
