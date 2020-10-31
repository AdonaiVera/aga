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

Conoce cómo ha cambiado la distribución de los recursos en el municipio considerando el análisis histórico por areas de interes.

Conoce cómo se podrían invertir los recursos en los diferentes sectores o poblaciones.

La aplicación permitira responder:

- ¿Cómo ha cambiado la distribución de recursos en el municipio considerando el análisis histórico de los planes de desarrollo de los principales temas: sectores (Educación, Salud, Justicia y Seguridad, Medio Ambiente, etc.)
- Análisis de los planes de desarrollo, y cumplimiento de metas en cada uno de los periodos, y ver la relación entre los indicadores Relación Eficiencia / Efectividad del plan de desarrollo y calificar el desempeño de la gestión del municipio.
- ¿Cómo puedo conocer la percepción en tiempo real de las personas que viven en Bello, Antioquia en sectores específicos como Educación, Salud, Justicia y Seguridad y Medio Ambiente?

## La magia de SAM

Genera mapas de calor, e identifica si existe patrones de inversión en un sector específico del municipio.

Programa actividades para cumplir tus objetivos.

Entérate de lo que hablan tus ciudadanos en redes sociales y asigna tareas .

Analizas los PQRSD de tus ciudadanos de forma automática. Para mas información mira este video:


    """
    
       )
    #    ast.shared.components.video_youtube(
    #        src="https://www.youtube.com/embed/B2iAodr0fOo"
    #    )
