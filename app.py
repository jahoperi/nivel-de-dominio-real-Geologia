# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:24:41 2022

@author: jahop_fz60h0
"""


import streamlit as st
import pandas as pd
import plotly.express as px

from PIL import Image

image = Image.open('pemex.png')
st.image(image)

st.header("Nivel de dominio real - disciplina de Geología")

st.header("Geología Estructural")

# continue loading the data with your excel file, I was a bit too lazy to build an Excel file :)
df = pd.DataFrame(
    [["Mapeo, correlaciones estratigráficas y estructurales", 0, 3, 14, 1, 0], ["Análisis de yacimientos fracturados", 11, 4, 3, 0, 0], ["Geología estructural y restauración", 3, 5, 8, 2, 0], ["Modelo geológico y mapeo de propiedades 3D", 6, 9, 3, 0, 0], ["Tectónica salina y arcilla", 3, 4, 10, 1, 0], ["Análisis de cuencas y sistemas petroleros", 1, 13, 4, 0, 0], ["Análisis de rutas de migración", 11, 7, 0, 0, 0], ["Análisis de sellos", 8, 8, 2, 0, 0], ["Exploración y análisis de plays", 0, 9, 9, 0, 0], ["Reconstrucción estructural, paleogeografía y tectónica", 5, 10, 3, 0, 0], ["Principios sísmicos", 8, 6, 3, 1, 0], ["Construcción de modelos de velocidad y conversión a profundidad", 13, 3, 2, 0, 0], ["Interpretación estructural 2D/3D", 2, 11, 4, 1, 0], ["Migración sísmica", 10, 7, 1, 0, 0], ["Análisis de fracturas usando datos petrofísicos", 12, 6, 0, 0, 0], ["Análisis de riesgo geológico", 7, 8, 3, 0, 0], ["Estimación de recursos y reservas", 9, 9, 0, 0, 0], ["Geomecánica", 13, 5, 0, 0, 0], ["Propiedades geomecánicas de rocas", 10, 8, 0, 0, 0], ["Integración de geociencias", 3, 10, 4, 1, 0]],
    columns=["Competencia", "Elemental", "Básico", "Intermedio", "Avanzado", "Especializado"]
)

fig = px.bar(df, x="Competencia", y=["Elemental", "Básico", "Intermedio", "Avanzado", "Especializado"], barmode='group', labels=dict(variable="Nivel de dominio", value = "Frecuencia"), color_discrete_sequence=["#8C564B", "rgb(127, 60, 141)", "rgb(36, 121, 108)", "blue", "rgb(255, 237, 111)"], height=700, width = 900) #400 900
# st.dataframe(df) # if need to display dataframe



fig.update_layout(yaxis_title='Frecuencia', title='Competencias vs Frecuencia',  font=dict(family="Courier New, monospace", size=14, color="black"))
fig.update_yaxes(range = [0,20])
    

st.plotly_chart(fig)