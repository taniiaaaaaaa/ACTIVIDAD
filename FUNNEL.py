from datetime import datetime, timedelta
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px
import pip 

def reemplazos(v):
  v=str(v)
  v=v.replace(',','')
  return v

pip.main(['install', 'plotly_express'])
pip.main(["install","openpyxl"])

st.title("ACTIVIDAD")
st.text('La presente página permite visualizar la actividad de los socios en el tiempo, tal como se puede ver en la siguiente tabla de valores.')
st.markdown(f' Tabla de actividad de socios')
df=pd.read_csv('ACTIVIDAD (1).csv',encoding='latin-1')
df=df.drop('Unnamed: 0',axis=1)
st.write(df)

st.text('La cual puede ser representada por medio de la siguiente gráfica.')
df=df.set_index('FECHAS')
df=df.drop('ALTAS SOCIOS',axis=1)
df=df.drop('BAJAS SOCIOS',axis=1)
st.line_chart(df)

st.text('Por otro lado se realizó un código capaz de identificar a las personas propensas a la inactividad, el modelo es conocido como XGBoost y fue capáz de tener una exactitud del 87.52%, resultados corroborados al identificar de manera correcta a 75449 socios activos y a 98777 socios inactivos, tal y como se ve en la siguiente gráfica.')


