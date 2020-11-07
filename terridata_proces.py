
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

class terridata:
    ##funcion donde entre sector, indicador o indicadores y año o años y grafique
    def get_results_td(df, sector, years, indicadores):
        terridata_df_sector = df[(df['sector'] == sector) & (df['year'].isin(years))]
        terridata_df_m_g = terridata_df_sector[['td_indicador','year','td_ind_value']]
        terridata_df_m_g = terridata_df_m_g[terridata_df_m_g.td_indicador.notnull()]
        if terridata_df_m_g.shape[0] > 0:
            graph = terridata_df_m_g.pivot(index='td_indicador',columns='year',values='td_ind_value')
        
        '''
        plt.figure(figsize=(10,10))
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=graph.loc[indicadores,:].T.index,y=graph.loc[indicadores,:].T[indicadores[0]],mode='lines+markers',name="Increasing"))
        fig.update_layout(
            xaxis = dict(
                tickmode = 'linear',
                tick0 = 2013,
                dtick = 1
            ),
            legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig.update_layout(legend_title_text='Trend')
        '''
        
        fig, ax = plt.subplots(figsize=(12, 5))
        sns.lineplot(data=graph.loc[indicadores,:].T)
        st.write("## **Indicador {}:**".format(indicadores))
        st.pyplot(fig)
       
