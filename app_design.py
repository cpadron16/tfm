import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

datos = pd.read_csv('./datos_app.csv', index_col = [0])


st.set_page_config(layout="wide")
st.write("""
# App Detección de Ofertas de Inversión Inmobiliaria
""")
st.write("""
### Lista de ofertas encontradas:
""")
st.sidebar.header('Especifique los criterios')
price = st.sidebar.slider("Seleccione su presupuesto máximo:", 0, +2000000, 100000)
superficie = st.sidebar.slider("Seleccione la superficie mínima del inmueble:", 0, 1000)
habitaciones = st.sidebar.slider("Seleccione el mínimo de habitaciones:", 1, 6)
baños = st.sidebar.slider("Seleccione el mínimo de baños:", 1, 5)
otros = st.sidebar.multiselect('Seleccione otros requerimientos:', ['Piscina','Terraza','Lujo','Cerca del metro','Garaje','Exterior','Chalet','Zonas verdes'],
                       [])

filtro = datos.loc[(datos['price']<= price) & (datos['superficie_construida']>= superficie) &
                   (datos['n_habitaciones']>= habitaciones) & (datos['n_baños']>= baños)]

if 'Piscina' in otros:
    filtro = filtro.loc[datos['piscina'] == 'Yes']
else:
    pass

if 'Lujo' in otros:
    filtro = filtro.loc[datos['lujo'] == 'Yes']
else:
    pass

if 'Cerca del metro' in otros:
    filtro = filtro.loc[datos['dist_metro'] == 'Yes']
else:
    pass

if 'Exterior' in otros:
    filtro = filtro.loc[datos['es_exterior'] == 'Yes']
else:
    pass

if 'Chalet' in otros:
    filtro = filtro.loc[datos['es_chalet'] == 'Yes']
else:
    pass

if 'Zonas Verdes' in otros:
    filtro = filtro.loc[datos['zonas_verdes'] == 'Yes']
else:
    pass

if 'Garaje' in otros:
    filtro = filtro.loc[datos['garaje'] == 'Yes']
else:
    pass

if 'Terraza' in otros:
    filtro = filtro.loc[datos['terraza'] == 'Yes']
else:
    pass

if len(filtro) == 0:
    st.write('Lo siento. No se han encontrado ofertas según sus criterios')
    image = Image.open('C:/Users/cpadron/Pictures/alert.jpg')
    st.image(image, width=480)

else:
    st.write(filtro[['barrio','price','prediccion_modelo','superficie_construida','n_habitaciones','n_baños',
                 'piscina','lujo','es_exterior']])
    st.write('---------------------------')
    st.write('Puede conocer más información en la página Idealista.com')

