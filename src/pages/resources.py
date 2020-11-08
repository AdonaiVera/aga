"""Esta página te permite convertir excel en datos valiosos con un solo clic"""
import logging

import streamlit as st
from listener_twitter import TwStreamListener
import awesome_streamlit as ast
from awesome_streamlit.core.services import resources
import pandas as pd
from Preprocess import DF_prep
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

STYLE = """
<style>
img {
    max-width: 100%;
}
</style>
"""
bBandera = True

def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)

def write():
    global bBandera
    global df_total_x
    """Writes content to the app"""
    ast.shared.components.title_awesome("Estadistica general")

    
    tags = ast.shared.components.multiselect(
        "Selecciona la fuente de los datos", options=['SIEE'], default=[]
    )

    if not tags:
        st.info(
             """Para continuar por favor **selecciona la fuente de datos que te gustaria analizar**"""
        )
    if tags:
        if bBandera:
            st.info(__doc__)
            st.markdown(STYLE, unsafe_allow_html=True)
            file = st.file_uploader("Sube el archivo del SIEE", type=["csv"])
            show_file = st.empty()
            if not file:
                show_file.info("Por favor sube el archivo en formato: " + ", ".join(["csv"]))
                return

            
        with st.spinner("Analizando tu data en segundos  ..."):

            years = st.multiselect(
                "Selecciona los años que deseas visualizar", options=['2016', '2017', '2018', '2019'], default=['2016', '2017', '2018', '2019']
            )

            author = st.selectbox("Selecciona un sector", options=['Salud', 'Medio ambiente', 'Educación', 'Seguridad'])
            
            if not years:
                st.info(
                     """Para continuar por favor **selecciona los años que te gustaria analizar**"""
                )
            if years:
                if bBandera:
                   cleaner_obj = DF_prep()
                   cleaner_obj.load_file(file)
                   df_total_x = cleaner_obj.get_concat_df()
                   bBandera = False
                
                fig, ax = plt.subplots(figsize=(12, 5))
                
                if author == 'Salud':
                    nSector = 2
                elif author == 'Medio ambiente':
                    nSector = 10
                elif author == 'Educación':
                    nSector = 1
                else:
                    nSector = 18
                    
                df_total = df_total_x
                fig, ax = plt.subplots(figsize=(12, 5))
                df_total['ratio_avance'] = df_total['valor_esperado'] / df_total['valor_ejecutado']
                sns.barplot(data=df_total, x='sector', y='ratio_avance', hue='year', estimator=np.mean, order=df_total['sector'].unique())
                st.write("## **Avance general por sectores y años::**")
                st.pyplot(fig)
                
                
                fig, ax = plt.subplots(figsize=(12, 5))
                df_salud = df_total[df_total['sector'] == nSector].copy()
                
                df_salud = df_salud[df_salud['year'].isin(years) == True]
                df_salud = df_salud[(df_salud['valor_esperado'] != 0) & (df_salud['valor_ejecutado'] != 0)]
                df_salud['ratio_avance'] = df_salud['valor_esperado'] / df_salud['valor_ejecutado']
                df_salud.sort_values('year', inplace=True)
                df_salud.reset_index(drop=True, inplace=True)
                sns.barplot(data=df_salud, x='year', y='ratio_avance', estimator=np.mean, order=df_salud['year'].unique())
                
                st.write("## **Avance segmentado por sector {}:**".format(author))
                st.pyplot(fig)
                                
                
                df_cleaned = df_total[df_total['sector'] == nSector].copy()
                df_cleaned = df_cleaned[df_cleaned['year'].isin(years) == True]
                fig, ax = plt.subplots(figsize=(12, 5))
                sns.barplot(data=df_cleaned, x='sector', ax=ax,y='ejec_total', hue='year', estimator=sum, order=df_cleaned['sector'].unique())
                st.write("## **Total de recursos ejecutados por sector, por año:**")
                st.pyplot(fig)
                
               
    
    tags = None
    

if __name__ == "__main__":
    write()
