import stream lit as st
import numpy as np
import matplotlib.pyplot as plt
st sliderbar.title('Software Educativo para el estudio de fenomenos ondulatorios')
op1=st.sidebar.radio("",['Ondas Estacionarias','Interferencia de Ondas','Onda general'])
if op1=='Ondas Estacionarias':
  st.title(op1)
  n=st.sider('',1,10)
  x=np.linspace(0,2*np.pi,150)
  #st.write(x)
  y=np.sin(n*x/2)
  fig,ax = plt.sublots()
  ax.plot(x,y)
  st.pyplot(fig)
