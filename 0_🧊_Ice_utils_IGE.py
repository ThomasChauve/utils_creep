import streamlit as st
import numpy as np
from function import*
from PIL import Image


st.set_page_config(
    page_title="Compute surface of truncated cylinder.",
    page_icon="🧊",
    layout="wide",
)

st.title('Compute surface of truncated cylinder.')


col1, col2 = st.columns(2)

with col1:
    image = Image.open('truncated_cylinder.png')
    st.image(image)

with col2:
    st.subheader("Enter $\Phi_l$ value")
    Ld=st.number_input('Large diameter (mm)',value=45.5)
    st.subheader("Enter $\Phi_s$ value")
    Sd=st.number_input('Small length (mm)',value=38.9)

    Af=area_tronc_cyl(Ld,Sd)

    
    st.subheader("Surface $(mm^2)$")
    st.metric(label="Surface", value=np.round(Af))

    st.subheader("Mass to apply")

    st.warning("The mass is computed for a given configuration at IGE were the relation between the mass ($M\sim g$) and the force ($F\sim N=kg.m.s^{-2}$) is given by : $F=0.14*M+22.38$", icon="⚠️")

    stress=st.number_input('Expected macro stress (MPa)',value=0.8)

    ww=theor_weight(Af,stress=stress)
    
    st.metric(label="Mass (g)", value=np.round(ww))

    st.write('The larger of the flat surface is : '+str(round(length_surface_dic(Ld,Sd),2))+' mm.' )