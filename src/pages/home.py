"""Home page shown when the user enters the application"""
import streamlit as st

import awesome_streamlit as ast


# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Cargando ..."):
        ast.shared.components.title_awesome("")
        st.write(
            """
            Con SAM **Haz seguimiento de tu plan de desarrollo** en tiempo real y desde cualquier lugar.

Conoce como ha ido cambiando la destinación de los recursos del municipio, y el comportamiento de las principales áreas de interés:  Educación, Justicia y Seguridad, Salud y Medio Ambiente.

Conoce cuales son las principales peticiones o solicitudes de la ciudadanía, y cuáles son los temas principales que les interesa comentar en la plataforma Twitter en relación al municipio.

La aplicación permitira responder:

- Cómo ha cambiado la distribución de los recursos en el municipio considerando el análisis histórico de los planes de desarrollo, con énfasis en los principales sectores: Educación, Justicia y Seguridad, Salud y Medio Ambiente?
- Análisis de los planes de desarrollo, y el cumplimiento de las metas en cada uno de los períodos, y ver la relación entre los indicadores Razón Eficiencia / Eficacia del plan de desarrollo y calificar el desempeño de la gestión del municipio.
- Cómo puedo conocer la percepción en tiempo real de la población que vive en Bello, Antioquia o a través de sus peticiones y solicitudes en las entidades municipales sobre el comportamiento de los sectores específicos como Educación, Salud, Justicia y Seguridad, y Medio Ambiente.

## La magia de SAM

Encuentras información de tus indicadores en un solo lugar…

Te puedes enterar de que están hablando tus ciudadanos en las redes..

Es una plataforma, escalable, y fácil de usar que te permite ver la información desde otra perspectiva, con un alto potencial de crecimiento.


    """
    
       )
    #    ast.shared.components.video_youtube(
    #        src="https://www.youtube.com/embed/B2iAodr0fOo"
    #    )
