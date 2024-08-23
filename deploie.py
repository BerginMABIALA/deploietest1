import pandas as pd
import streamlit as st

# Lire le fichier texte
data = pd.read_csv('C:/Users/dicko/Desktop/commandes/data.txt')

# Afficher les données sous forme de tableau
st.write("Voici les données du fichier texte:")
st.dataframe(data)

# Créer un graphique simple
st.write("Graphique des âges:")
st.bar_chart(data.set_index('nom'))
