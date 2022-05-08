import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.sidebar.title('Software Educativo para el estudio de ondas electromagnéticas')
op1=st.sidebar.radio("",['Ondas Estacionarias','Interferencia de Ondas','Onda general'])
if op1=='Ondas Estacionarias':
  st.title(op1)
  col1, col2, col3 = st.columns([3,6,6])
with col2:
  st.image("https://qph.fs.quoracdn.net/main-qimg-47dfb28477b57ff310db4c3feb3ba157")
n=st.slider('',4,20)
st.write ("""Modifica la potencia """)
x=np.linspace(0,2*np.pi,150)
 #st.write(x)
y=np.sin(n*x/2)
fig, ax = plt.subplots()
ax.plot(x,y)
st.pyplot(fig)
  
