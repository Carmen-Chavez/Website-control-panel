import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Inventario de Autos Usados")

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
car_copy=car_data.copy()
car_copy["model"]=car_copy["model"].str.split()
car_copy["brand"] = car_copy["model"].apply(lambda x: x.pop(0) if len(x) > 0 else x)

hist_button = st.button('Inventario por marca de auto') # crear un botón
     
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Autos disponibles por marca')
         
    # crear un histograma
    fig_1 = px.histogram(car_copy, x="brand")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_1, use_container_width=True)

build_scatter = st.checkbox("Marca vs Condición vs Precio")

if build_scatter:
    st.write("Marca vs Condición vs Precio")

    fig_2= px.scatter(car_copy, x="brand", y="price", color="condition")
    st.plotly_chart(fig_2, use_container_width=True)
     