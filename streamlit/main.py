import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.metrics as Metrics
import pandas as pd
import matplotlib.pyplot as plt

class DF_prep:

    def __init__(self):
        self.__column_lists()
        self.cat_dict = {}
        self.df_long = pd.DataFrame()

    def load_file(self, path):
        self.raw_df = pd.read_csv(path, sep=';', encoding='iso-8859-1')

    def load_df(self, df):
        self.raw_df = df.copy()

    def process_df(self):
        self.__string_cleaner(self.raw_df)
        self.cat_dict = self.__categorize(self.raw_df)
        self.__transform(self.raw_df)
        self.__remove_cols()
        self.__convert_to_float()

    def get_clean_df(self):
        return self.df_long.copy()

    def __column_lists(self):
        self.year_list = ['2016', '2017', '2018', '2019']

        #### List of static columns (shared through years)
        self.static_columns = ['Cod Dpto', 'Departamento', 'Cod Mpio', 'Municipio', 'Resultado', 'Indicador Resultado', \
            'LB Resultado', 'Meta Resultado', 'Codigo Producto', 'Producto', 'Indicador Producto', \
            'LB Producto', 'Meta Producto', 'Orientacion', 'Codigo Sector', 'Sector', 'ODS', \
            'Pilar Plan Marco de Implementación', 'Prog Total Cuatrienio', 'Ejec Total Cuatrienio']

        #### Columns with strings (text)
        self.text_columns = ['departamento', 'municipio', 'resultado', 'indicador resultado', 'producto', 'indicador producto', \
            'orientacion', 'codigo sector', 'sector', 'ods', 'pilar plan marco de implementación', 'rango calificación', \
            'observacionevaluacion', 'bpin', 'priorizada', 'observaciones']

        #### List of string columns to clean
        self.static_text_columns = ['Departamento', 'Municipio', 'Resultado', 'Indicador Resultado', 'Producto', \
            'Indicador Producto', 'Orientacion', 'Codigo Sector', 'Sector', 'ODS', 'Pilar Plan Marco de Implementación']
        self.dynamic_text_columns = ['Rango Calificación', 'ObservacionEvaluacion', 'BPIN', 'Priorizada', 'Observaciones']

        #### List of columns to remove
        self.to_remove = ['cod dpto', 'departamento', 'cod mpio', 'municipio']

        #### List of categorical columns
        self.cat_columns = ['Rango Calificación', 'ObservacionEvaluacion', 'BPIN', 'Priorizada', 'Observaciones']

    def __string_cleaner(self, df):
        for c in self.static_text_columns:
            df[c] = df[c].str.strip().str.lower()
            df[c] = df[c].str.normalize('NFD')
            df[c] = df[c].str.replace(r'([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+', r'\1')
            df[c] = df[c].str.normalize('NFC')
            df[c] = df[c].str.replace('\n', '')
            df[c] = df[c].str.replace('\r', '')

        for column in list(df.columns):
            for c in self.dynamic_text_columns:
                if c in column:
                    df[column] = df[column].str.strip().str.lower()
                    df[column] = df[column].str.normalize('NFD')
                    df[column] = df[column].str.replace(r'([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+', r'\1')
                    df[column] = df[column].str.normalize('NFC')
                    df[column] = df[column].str.replace('\n', '')
                    df[column] = df[column].str.replace('\r', '')

    def __categorize(self, df):
        df_columns = list(df.columns)
        cat_dict = {}
        for c in self.cat_columns:
            temp_df = pd.DataFrame()
            for y in self.year_list:
                dynamic_c = [x for x in df_columns if y in x]
                dynamic_c = [x for x in dynamic_c if c in x]
                new_df = pd.melt(df, id_vars='Producto', value_vars=dynamic_c)
                temp_df = pd.concat([temp_df, new_df])
            temp_df = temp_df['value'].astype('category').reset_index()
            temp_df['index'] = temp_df['value'].cat.codes
            cat_dict[c] = temp_df.drop_duplicates().set_index('index', drop=True).sort_index()['value']

        for c in self.cat_columns:
            for y in self.year_list:
                dynamic_c = [x for x in df_columns if y in x]
                dynamic_c = [x for x in dynamic_c if c in x]
                df[dynamic_c[0]] = df[dynamic_c[0]].apply(lambda x: list(cat_dict[c]).index(x))

        return cat_dict

    def __transform(self, df):
        df_columns = list(df.columns)
        self.df_long = pd.DataFrame()
        for y in self.year_list:
            name_dict = {}
            dynamic_c = [x for x in df_columns if y in x]
            for name in dynamic_c:
                name_dict[name] = name[:-4].strip()
            new_df = df[self.static_columns + dynamic_c]
            new_df.rename(columns=name_dict, inplace=True)
            new_df['year'] = int(y)
            new_df.columns = map(str.lower, new_df.columns)
            self.df_long = pd.concat([self.df_long, new_df])

        self.df_long.reset_index(drop=True)
        self.df_long.head()

    def __remove_cols(self):
        self.df_long.drop(self.to_remove, axis=1, inplace=True)
        self.df_long.replace('-', np.nan, inplace=True)
        self.df_long['valoresperado'].replace('NP', np.nan, inplace=True)   # NP = No programada
        self.df_long['valorejecutado'].replace('NE', np.nan, inplace=True)   # NE = No esperada
        self.df_long['% avance'].replace('SC', np.nan, inplace=True)   #

    def __convert_to_float(self):
        for c in list(self.df_long.columns):
            if c not in self.text_columns:
                self.df_long[c] = self.df_long[c].apply(lambda x: x.replace(',', '.') if isinstance(x, str) else x)
                self.df_long[c] = pd.to_numeric(self.df_long[c])



path = 'https://raw.githubusercontent.com/AdonaiVera/Bello/developer/data/Indicadores_2016-2017-2018-2019.csv'

cleaner_obj = DF_prep()
cleaner_obj.load_file(path)	# si tiene un dataframe puede usar load_df(df)
cleaner_obj.process_df()

df_cleaned = cleaner_obj.get_clean_df()

sectores = ['a.1. educacion', 'a.2. salud', 'a.18. justicia y seguridad', 'a.10. ambiental']

df_cleaned = df_cleaned[df_cleaned['sector'].isin(sectores)]

st.write("# **Bello**")

fig, ax = plt.subplots(figsize=(12, 5))
sns.barplot(data=df_cleaned, ax=ax,x='sector', y='prog total', hue='year', estimator=sum, order=df_cleaned['sector'].unique())
fig.tight_layout()
st.write("## **Total de recursos programados por sector, por año:**")
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(12, 5))
sns.barplot(data=df_cleaned, x='sector', ax=ax,y='ejec total', hue='year', estimator=sum, order=df_cleaned['sector'].unique())
st.write("## **Total de recursos ejecutados por sector, por año:**")
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(12, 5))
sns.histplot(data=df_cleaned, ax=ax,x='rango calificación', hue='year', multiple="dodge", shrink=.8)
st.write("## **Cantidad de productos por calificación, por año:**")
st.pyplot(fig)

df_salud = df_cleaned[df_cleaned['sector'] == 'a.2. salud'].copy()
df_salud['rec_diff'] = df_salud['prog total'] - df_salud['ejec total']

fig, ax = plt.subplots(figsize=(15,5))
graph = sns.barplot(data=df_salud, ax=ax,x='resultado', y='rec_diff', hue='orientacion', estimator=np.mean)
for item in graph.get_xticklabels():
    item.set_rotation(90)
st.write("## **SECTOR SALUD:**")
st.pyplot(fig)
