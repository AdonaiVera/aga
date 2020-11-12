"""This page is for searching and viewing the list of awesome resources"""
import logging

import streamlit as st
from listener_twitter import TwStreamListener
import awesome_streamlit as ast
from awesome_streamlit.core.services import resources
from sqlalchemy import create_engine, text
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import plotly.express as px


logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def write():
    """Writes content to the app"""
    ast.shared.components.title_awesome("Análisis Twitter")
        
    tags = st.selectbox("Selecciona tu municipio", options=['Salud', 'Medio ambiente', 'Educación', 'Seguridad'])
    

    author_all = ast.shared.models.Author(name="Todos", url="")
    author = st.selectbox("Selecciona tu municipio", options=['Municipio de Bello'])
    if author == author_all:
        author = None
    
    if not tags:
        st.info(
             """Para continuar por favor **selecciona el municipio que te gustaria analizar**"""
        )
        
    if tags:
        with st.spinner("Analizando post de tu comunidad en tiempo real en Twitter ..."):
            engine = create_engine('postgresql://postgres:vu44qnBW2xQxYXYQNiVv@ds4a-extended.cqwg91rhslbj.us-east-1.rds.amazonaws.com/ds4a_project', max_overflow=20)
            query = 'SELECT * FROM twitter_deep'
            df_total = pd.read_sql(query, engine)
            
            df_clasificacion = df_total[df_total['sector'] == tags].copy()
            st.write("**Diez ultimos post del sector {}:**".format(tags))
            st.table(df_clasificacion['text'].head(10))
            
 
            b = len(df_clasificacion[df_clasificacion['emotions']=='Positivo'])
            a = len(df_clasificacion[df_clasificacion['emotions']=='Negativo'])
            c = len(df_clasificacion[df_clasificacion['emotions']=='Neutro'])

            sizes=[a, b, c]

            df0=pd.DataFrame()
            df0['experiencia']=[ 'Negativos', 'Positivos', 'Neutrales']
            df0['cantidad']=sizes
            
            fig, ax = plt.subplots(figsize=(12, 5))
            fig = px.pie(df0, values='cantidad', names='experiencia',hole=0.5,title='ANÁLISIS DE LA PERCEPCIÓN DEL USUARIO EN EL SECTOR:'+' '+str.upper(tags),color_discrete_sequence=["lightseagreen","palegoldenrod","darkseagreen"])
            
            st.plotly_chart(fig)
            
            sentimental = st.selectbox("Selecciona tu municipio", options=['Positivo', 'Negativo', 'Neutro'])
            
            if sentimental:
                with st.spinner("Analizando tweets {} de tu comunidad ...".format(sentimental)):
                    df_sent = df_clasificacion[df_total['emotions'] == sentimental].copy()
                    st.table(df_sent['text'].head(10))
                    
    
    tags = None


if __name__ == "__main__":
    write()
