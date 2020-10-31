"""This page is for searching and viewing the list of awesome resources"""
import logging

import streamlit as st
from listener_twitter import TwStreamListener
import awesome_streamlit as ast
from awesome_streamlit.core.services import resources

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def write():
    """Writes content to the app"""
    ast.shared.components.title_awesome("Percepción de los ciudadanos basados en PQRSD")
    st.write("Estamos trabajando para generar mayor valor a tus datos, en proximos días estara disponible esta funcionalidad.")


if __name__ == "__main__":
    write()
