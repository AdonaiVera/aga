"""This page is for searching and viewing the list of awesome resources"""
import logging

import streamlit as st
from listener_twitter import TwStreamListener
import awesome_streamlit as ast
from awesome_streamlit.core.services import resources

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def write():
    """Writes content to the app"""
    ast.shared.components.title_awesome("Análisis Twitter")
    tags = ast.shared.components.multiselect(
        "Selecciona un sector", options=['Salud', 'Medio ambiente', 'Educación', 'Seguridad'], default=[]
    )

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
            myStreamListener = TwStreamListener()
            myStreamListener.connect()
            LOCATION_BELLO = [-75.623604,6.303511,-75.493611,6.373763]
            myStreamListener.run(tags, LOCATION_BELLO)
    
    tags = None


if __name__ == "__main__":
    write()
