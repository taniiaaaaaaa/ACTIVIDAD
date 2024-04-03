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
st.text('La presente página permite visualizar la actividad de los socios en el tiempo.')
st.markdown(f' Actividad')
df=pd.read_csv('ACTIVIDAD (1).csv',encoding='latin-1')
df=df.set_index('FECHAS')
df=df[['SOCIOS','ACTIVOS','INACTIVOS']]
#fig = px.funnel(data, x='number', y='stage')
#st.ploty_chart(fig)
#fig.show()
#st.image('FUNNEL.png',caption='ACTIVIDAD REGISTRADA PARA CADA UNA DE LAS PANTALLAS')
#data = dict(
 #   number=[39, 27.4, 20.6, 11, 2],
  #  stage=["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"])
#fig = px.funnel(df, x=df['FRECUENCIA'], y=df['PASO'])
st.line_chart(df)


