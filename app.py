import pandas as pd
import plotly.express as px
import streamlit as st
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header("Análisis de datos de anuncios de venta de vehículos en EE.UU.")
hist_button = st.button('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de vehículos')
    fig = px.histogram(car_data, x="odometer") 
    st.plotly_chart(fig, use_container_width=True) # mostrar un gráfico Plotly interactivo

disp_button = st.button('Construir gráfico de dispersión') # crear un botón
if disp_button: # al hacer clic en el botón
    st.write('Creación de un gráfico de dispersión kilometraje vs precio')
    fig2 = px.scatter(car_data, x="odometer", y="price", color="model_year")
    st.plotly_chart(fig2, use_container_width=True) # mostrar un gráfico Plotly interactivo

build_bubble = st.checkbox('Construir un diagrama de burbujas') # crear una casilla de verificación
if build_bubble: # si la casilla de verificación está seleccionada
    st.write('Creación de un gráfico de burbujas')
    fig3 = px.scatter(car_data, x="model_year", y="condition", size="price", color="type", hover_name="model", size_max=60)
    st.plotly_chart(fig3, use_container_width=True) # mostrar un gráfico Plotly interactivo

