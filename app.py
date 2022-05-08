import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

st.sidebar.title('Software Educativo para el estudio de fenomenos ondulatorios')
op1=st.sidebar.radio("",['Ondas Estacionarias','Interferencia de Ondas','Onda general'])
if op1=='Ondas Estacionarias':
  st.title(op1)

  n=st.slider('',10^4,10^20)
  x=np.linspace(0*np.pi,10^20)#DECLARAR VARIABLE, PUNTOS A GRAFICAR
 #st.write(x)
  y=np.sin(x)
  fig, ax = plt.subplots()
  ax.plot(x,y)
  st.pyplot(fig)
