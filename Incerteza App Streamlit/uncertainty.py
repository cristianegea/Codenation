# Projeto Final - AceleraDev Data Science Codenation

# Análise inicial dos dados de incerteza de política econômica de 20 países (fonte: http://www.policyuncertainty.com/)

# conda create -n projetofinal
# conda activate projetofinal
# streamlit run uncertainty.py

# Se aparecer a mensagem abaixo, então o processo foi executado com êxito
# Local URL: http://localhost:8501
# Network URL: http://192.168.0.112:8501

# Importação dos pacotes
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import base64
import matplotlib.pyplot as plt

from prettytable import PrettyTable

import plotly.offline as py
import plotly.graph_objs as go

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    return href

def main():
    st.title('Codenation - AceleraDev Data Science')
    st.subheader('Processamento de Dados em Python')
    st.subheader('Autora: Cristiane Gea')
    df = pd.read_excel('EPU.xlsx')
    if df is not None:
        st.subheader('Análise dos dados de Incerteza de Política Econômica (EPU)')
        # st.markdown('**Número de linhas:**')
        # st.markdown(df.shape[0])
        # st.markdown('**Número de colunas:**')
        # st.markdown(df.shape[1])
        # st.markdown('**Visualizando o dataframe**')        
        # st.dataframe(df.head())
        # st.markdown('**Resumo estatístico**')        
        # st.dataframe(round(df.describe(), 2))

        select_method1 = st.sidebar.selectbox('Selecione o índice de incerteza desejado:', ('EPU Global (PIB a preços correntes)', 'EPU Global (PIB a PPP)', 'Austrália', 'Brasil', 'Canadá', 'Chile', 'China', 'Colômbia', 'França', 'Alemanha', 'Grécia', 'Índia', 'Irlanda', 'Itália', 'Japão', 'Coréia', 'México', 'Holanda', 'Rússia', 'Espanha', 'Singapura', 'Reino Unido', 'Estados Unidos', 'Suécia'))
        if select_method1 == 'EPU Global (PIB a preços correntes)':
            s_epu = df['GEPU_current']
        if select_method1 == 'EPU Global (PIB a PPP)':
            s_epu = df['GEPU_ppp']
        if select_method1 == 'Austrália':
            s_epu = df['Australia']
        if select_method1 == 'Brasil':
            s_epu = df['Brazil']
        if select_method1 == 'Canadá':
            s_epu = df['Canada']
        if select_method1 == 'Chile':
            s_epu = df['Chile']
        if select_method1 == 'China':
            s_epu = df['China']
        if select_method1 == 'Colômbia':
            s_epu = df['Colombia']
        if select_method1 == 'França':
            s_epu = df['France']
        if select_method1 == 'Alemanha':
            s_epu = df['Germany']
        if select_method1 == 'Grécia':
            s_epu = df['Greece']
        if select_method1 == 'Índia':
            s_epu = df['India']
        if select_method1 == 'Irlanda':
            s_epu = df['Ireland']
        if select_method1 == 'Italia':
            s_epu = df['Italy']
        if select_method1 == 'Japão':
            s_epu = df['Japan']
        if select_method1 == 'Coréia':
            s_epu = df['Korea']
        if select_method1 == 'México':
            s_epu = df['Mexico']
        if select_method1 == 'Holanda':
            s_epu = df['Netherlands']
        if select_method1 == 'Rússia':
            s_epu = df['Russia']
        if select_method1 == 'Espanha':
            s_epu = df['Spain']
        if select_method1 == 'Singapura':
            s_epu = df['Singapore']
        if select_method1 == 'Reino Unido':
            s_epu = df['UK']
        if select_method1 == 'Estados Unidos':
            s_epu = df['US']
        if select_method1 == 'Suécia':
            s_epu = df['Sweden']

        select_method2 = st.sidebar.selectbox('Selecione o tipo de análise desejada:', ('Univariada', 'Bivariada'))
        if select_method2 == 'Univariada':
            # Visualização dos dados
            st.markdown('**Visualização dos dados**')        
            
            df_univariate = pd.DataFrame()
            df_univariate['Date'] = df['Date']
            df_univariate[f'{s_epu.name}'] = s_epu
                        
            st.dataframe(df_univariate)
            
            # Gráfico Univariado
            st.markdown('**Evolução da Incerteza de Política Econômica (EPU)**')

            s_date = df['Date']
            plt.figure(figsize = (12, 6))
            plt.plot(s_date, s_epu, color='black')
            plt.title(f'{s_epu.name}')
            plt.xlabel('Data')
            plt.ylabel('EPU')
            plt.show()
            st.pyplot()

            # plot_epu = go.Scatter(
            #     x = df['Date'],
            #     y = s_epu,
            #     mode = 'lines',
            #     name = f'EPU {s_epu.name}',
            #     line = {'color': '#ee5253'}
            #     )
            # # layout
            # layout = go.Layout(
            #     xaxis = {'title': 'Data'},
            #     yaxis = {'title': f'EPU {s_epu.name}'},
            #     barmode = 'stack',
            #     title = f'EPU {s_epu.name}'
            #     )
            # fig = go.Figure(data = plot_epu, layout = layout)
            # st.pyplot(fig)
            
            # Cálculo da estatística descritiva
            st.markdown('**Resumo Estatístico da Incerteza de Política Econômica (EPU)**')
            
            st.dataframe(round(s_epu.describe(), 2))
            
            # stat1 = round(s_epu.mean(), 2)
            # stat2 = round(s_epu.std(), 2)
            # stat3 = round(s_epu.min(), 2)
            # stat4 = round(s_epu.quantile(q=0.25), 2)
            # stat5 = round(s_epu.median(), 2)
            # stat6 = round(s_epu.quantile(q=0.75), 2)
            # stat7 = round(s_epu.max(), 2)
            # stat8 = round(s_epu.kurtosis(), 2)
            # stat9 = round(s_epu.skew(), 2)
            # # Cria a tabela
            # table1 = PrettyTable()
            # # Deixa um espaço entre a borda das colunas e o conteúdo (default)
            # table1.padding_width = 1
            # # Adiciona as linhas
            # table1.add_column('stat', ['mean', 'std', 'min', '25%', '50%', '75%', 'max', 'kurt', 'skew'])
            # table1.add_column(s_epu.name, [stat1, stat2, stat3, stat4, stat5, stat6, stat7, stat8, stat9])
            # st.table1

        if select_method2 == 'Bivariada':
            # Visualização dos dados
            st.markdown('**Visualização dos dados**')        
            
            df_bivariate = pd.DataFrame()
            df_bivariate['Date'] = df['Date']
            df_bivariate[f'{s_epu.name}'] = s_epu
            df_bivariate['Brazil'] = df['Brazil']
                        
            st.dataframe(df_bivariate)
            
            # Gráfico comparativo
            st.markdown('**Evolução da Incerteza de Política Econômica (EPU)**')

            s_date = df['Date']
            s_br = df['Brazil']
            plt.style.use('ggplot')
            plt.figure(figsize = (12, 6))
            plt.plot(s_date, s_epu, color='black', label=f'{s_epu.name}')
            plt.plot(s_date, s_br, color='red', label='Brazil')
            plt.title(f'{s_epu.name} vs Brazil')
            plt.xlabel('Data')
            plt.ylabel('EPU')
            plt.legend()
            plt.show()
            st.pyplot()

            # trace1 = go.Scatter(x = df['Date'],
            #                     y = s_epu,
            #                     mode = 'lines',
            #                     name = f'EPU {s_epu.name}',
            #                     line = {'color': '#ee5253'})

            # trace2 = go.Scatter(x = df['Date'],
            #                     y = df['Brazil'],
            #                     mode = 'lines',
            #                     name = 'Brasil',
            #                     line = {'color': '#341f97'})

            # data = [trace1, trace2]
            # # layout
            # layout = go.Layout(xaxis = {'title': 'Data'},
            #                 yaxis = {'title': 'EPU'},
            #                 barmode = 'stack',
            #                 title = f'EPU {s_epu.name} vs. EPU Brazil'
            # )
            # fig = go.Figure(data = data, layout = layout)
            # st.dataframe((py.iplot(fig)))
            
            # Cálculo da estatística descritiva
            st.markdown('**Resumo Estatístico da Incerteza de Política Econômica (EPU)**')
            
            bivariate = pd.DataFrame()
            bivariate[f'{s_epu.name}'] = s_epu
            bivariate['Brazil'] = s_br

            st.dataframe(round(bivariate.describe(), 2))

            # epu_stat1 = round(s_epu.mean(), 2)
            # epu_stat2 = round(s_epu.std(), 2)
            # epu_stat3 = round(s_epu.min(), 2)
            # epu_stat4 = round(s_epu.quantile(q=0.25), 2)
            # epu_stat5 = round(s_epu.median(), 2)
            # epu_stat6 = round(s_epu.quantile(q=0.75), 2)
            # epu_stat7 = round(s_epu.max(), 2)
            # epu_stat8 = round(s_epu.kurtosis(), 2)
            # epu_stat9 = round(s_epu.skew(), 2)

            # br_stat1 = round(df['Brazil'].mean(), 2)
            # br_stat2 = round(df['Brazil'].std(), 2)
            # br_stat3 = round(df['Brazil'].min(), 2)
            # br_stat4 = round(df['Brazil'].quantile(q=0.25), 2)
            # br_stat5 = round(df['Brazil'].median(), 2)
            # br_stat6 = round(df['Brazil'].quantile(q=0.75), 2)
            # br_stat7 = round(df['Brazil'].max(), 2)
            # br_stat8 = round(df['Brazil'].kurtosis(), 2)
            # br_stat9 = round(df['Brazil'].skew(), 2)

            # # Cria a tabela
            # table2 = PrettyTable()

            # # Deixa um espaço entre a borda das colunas e o conteúdo (default)
            # table2.padding_width = 1

            # # Adiciona as linhas
            # table2.add_column('stat', ['mean', 'std', 'min', '25%', '50%', '75%', 'max', 'kurt', 'skew'])
            # table2.add_column(s_epu.name, [epu_stat1, epu_stat2, epu_stat3, epu_stat4, epu_stat5, epu_stat6, epu_stat7, epu_stat8, epu_stat9])
            # table2.add_column('Brazil', [br_stat1, br_stat2, br_stat3, br_stat4, br_stat5, br_stat6, br_stat7, br_stat8, br_stat9])

            # st.dataframe((table2))

if __name__ == '__main__':
	main()