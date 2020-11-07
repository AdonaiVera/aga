"""This page is for searching and viewing the list of awesome resources"""
import logging

import streamlit as st
from listener_twitter import TwStreamListener
import awesome_streamlit as ast
from awesome_streamlit.core.services import resources
from database_process import DATABASE
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from terridata_proces import terridata
logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def write():
    """Writes content to the app"""
    ast.shared.components.title_awesome("Análisis detallado")
    tags = ast.shared.components.multiselect(
        "Selecciona los años que deseas visualizar", options=['2013', '2014', '2015', '2016', '2017', '2018', '2019'], default=[]
    )

    author = st.selectbox("Selecciona un sector", options=['Salud', 'Medio ambiente', 'Educación', 'Seguridad'])
    
    
    if not tags:
        st.info(
             """Para continuar por favor **selecciona el municipio que te gustaria analizar**"""
        )
        
    if tags and author:
        with st.spinner("Analizando tu historico en tiempo real ..."):
            db_obj = DATABASE('ds4a-extended.cqwg91rhslbj.us-east-1.rds.amazonaws.com', 'postgres', 'vu44qnBW2xQxYXYQNiVv', 'ds4a_project')
            df_total = db_obj.db_read('SELECT * FROM main')
            st.dataframe(df_total.head(10))
            
            fig, ax = plt.subplots(figsize=(12, 5))
            if author == 'Salud':
                nSector = 2
            elif author == 'Medio ambiente':
                nSector = 10
            elif author == 'Educación':
                nSector = 1
            else:
                nSector = 18
                
            fig, ax = plt.subplots(figsize=(12, 5))
            df_total['ratio_avance'] = df_total['valor_esperado'] / df_total['valor_ejecutado']
            sns.barplot(data=df_total, x='sector', y='ratio_avance', hue='year', estimator=np.mean, order=df_total['sector'].unique())
            st.write("## **Avance general por sectores y años::**")
            st.pyplot(fig)
            
            
            fig, ax = plt.subplots(figsize=(12, 5))
            df_salud = df_total[df_total['sector'] == nSector].copy()
            
            df_salud = df_salud[df_salud['year'].isin(tags) == True]
            df_salud = df_salud[(df_salud['valor_esperado'] != 0) & (df_salud['valor_ejecutado'] != 0)]
            df_salud['ratio_avance'] = df_salud['valor_esperado'] / df_salud['valor_ejecutado']
            df_salud.sort_values('year', inplace=True)
            df_salud.reset_index(drop=True, inplace=True)
            sns.barplot(data=df_salud, x='year', y='ratio_avance', estimator=np.mean, order=df_salud['year'].unique())
            
            st.write("## **Avance segmentado por sector {}:**".format(author))
            st.pyplot(fig)
            
            test_df = df_total.dropna(subset=['rango_calificacion'])
            test_df = test_df[test_df['year'].isin(tags) == True]
            fig, ax = plt.subplots(figsize=(12, 5))
            sns.histplot(data=test_df, x='rango_calificacion', hue='year', multiple="dodge", shrink=.8)
            
            st.write("## **Rango de clasificación por años:**")
            st.pyplot(fig)
            
            
            df_cleaned = df_total[df_total['sector'] == nSector].copy()
            df_cleaned = df_cleaned[df_cleaned['year'].isin(tags) == True]
            fig, ax = plt.subplots(figsize=(12, 5))
            sns.barplot(data=df_cleaned, x='sector', ax=ax,y='ejec_total', hue='year', estimator=sum, order=df_cleaned['sector'].unique())
            st.write("## **Total de recursos ejecutados por sector, por año:**")
            st.pyplot(fig)
            
            
            indicador = st.selectbox("Selecciona el indicador", ['', 'puntaje promedio pruebas saber 11 - lectura critica', 'Embarazo'], format_func=lambda x: 'Selecciona una opción' if x == '' else x)
            
            if indicador:
                with st.spinner("Analizando el indicador {}: ".format(indicador)):
                
                    terridata.get_results_td(df_total,nSector,tags,indicador)
                
            
    
    tags = None


if __name__ == "__main__":
    write()
