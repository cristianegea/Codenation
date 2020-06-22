import streamlit as st
import pandas as pd
import base64

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    return href

# definição de uma função "main"
def main():
    # estruturas de uma página web
    st.image('logo.png', width=200)
    st.title('AceleraDev Data Science')                # título principal da página
    st.subheader('Semana 2 - Pré-processamento de dados em Python')
    
    # upload dos dados
    st.subheader('Importação da base de dados')
    file = st.file_uploader('Escolha a base de dados que deseja analisar (formato csv)', type='csv')
    
    # criação do objeto dataframe
    if file is not None:
        df = pd.read_csv(file)                      # dataframe utilizado
        slider = st.slider('Valores', 0, 100)       # fatia parte do dataframe
        
        # resumo da base de dados
        st.subheader('Resumo dos dados')
        st.markdown('**Número de linhas:**')
        st.markdown(df.shape[0])
        st.markdown('**Número de colunas:**')
        st.markdown(df.shape[1])
        
        # plotando os dados no formato de data frame
        st.subheader('Apresentação dos dados')        
        st.markdown('Formato: Dataframe')
        st.dataframe(df.head(slider))               # visualização dos dados do dataframe    
        
        # plotando os dados no formato de table
        st.markdown('Formato: Table')
        st.table(df.head(slider))

        # exploração dos dados
        exploracao = pd.DataFrame({'nomes' : df.columns, 'tipos' : df.dtypes, 'NA #': df.isna().sum(), 'NA %' : (df.isna().sum() / df.shape[0]) * 100})
        st.markdown('**Contagem dos tipos de dados:**')
        st.write(exploracao.tipos.value_counts())
        st.markdown('Nomes das colunas do tipo int64:')
        st.markdown(list(exploracao[exploracao['tipos'] == 'int64']['nomes']))
        st.markdown('**Nomes das colunas do tipo float64:**')
        st.markdown(list(exploracao[exploracao['tipos'] == 'float64']['nomes']))
        st.markdown('**Nomes das colunas do tipo object:**')
        st.markdown(list(exploracao[exploracao['tipos'] == 'object']['nomes']))
        st.markdown('**Tabela com coluna e percentual de dados faltantes :**')
        st.table(exploracao[exploracao['NA #'] != 0][['tipos', 'NA %']])
        st.subheader('Inputaçao de dados númericos :')
        percentual = st.slider('Escolha o limite de percentual faltante limite para as colunas vocë deseja inputar os dados', min_value=0, max_value=100)
        lista_colunas = list(exploracao[exploracao['NA %']  < percentual]['nomes'])
        select_method = st.radio('Escolha um metodo abaixo :', ('Média', 'Mediana'))
        st.markdown('Você selecionou : ' +str(select_method))
        if select_method == 'Média':
            df_inputado = df[lista_colunas].fillna(df[lista_colunas].mean())
            exploracao_inputado = pd.DataFrame({'nomes': df_inputado.columns, 'tipos': df_inputado.dtypes, 'NA #': df_inputado.isna().sum(),
                                       'NA %': (df_inputado.isna().sum() / df_inputado.shape[0]) * 100})
            st.table(exploracao_inputado[exploracao_inputado['tipos'] != 'object']['NA %'])
            st.subheader('Dados Inputados faça download abaixo : ')
            st.markdown(get_table_download_link(df_inputado), unsafe_allow_html=True)
        if select_method == 'Mediana':
            df_inputado = df[lista_colunas].fillna(df[lista_colunas].mean())
            exploracao_inputado = pd.DataFrame({'nomes': df_inputado.columns, 'tipos': df_inputado.dtypes, 'NA #': df_inputado.isna().sum(),
                                       'NA %': (df_inputado.isna().sum() / df_inputado.shape[0]) * 100})
            st.table(exploracao_inputado[exploracao_inputado['tipos'] != 'object']['NA %'])
            st.subheader('Dados Inputados faça download abaixo : ')
            st.markdown(get_table_download_link(df_inputado), unsafe_allow_html=True)

if __name__ == '__main__':
    main()

# no terminal, executar:
#   1. "conda create -n Semana2"
#   2. "conda activate Semana2"
#   3. "pip install -r requirements.txt"
#      Obs.: se der erro, executar "pip install streamlit" e "pip install seaborn"  
#   4. "streamlit run alunos.py"

# Se aparecer a mensagem abaixo, então o processo foi executado com êxito
# Local URL: http://localhost:8501
# Network URL: http://192.168.0.112:8501

# # definição de uma função "main"
# def main():
#     # estruturas de uma página web
#     st.title('Hello World!')                # título principal da página
    
#     # criação de um botão
#     st.markdown('Botão')                    # célula de texto markdown
#     botao = st.button('Botão')              # definição do nome do botão
#     if botao:                               # definição do comportamento do botão
#         st.markdown('Botão Clicado')        # definição da ação ao clicar no botão
    
#     # criação de checkbox
#     st.markdown('Checkbox')                 
#     check = st.checkbox('Checkbox')
#     if check:
#         st.markdown('Check!')
    
#     # criação de lista de opções
#     st.markdown('Lista de Opções')
#     radio = st.radio('Escolha uma opção:', ('Opção 1', 'Opção 2', 'Opção 3', 'Opção 4'))
#     if radio == 'Opção 1':
#         st.markdown('Opção 1')
#     if radio == 'Opção 2':
#         st.markdown('Opção 2')
#     if radio == 'Opção 3':
#         st.markdown('Opção 3')
#     if radio == 'Opção 4':
#         st.markdown('Opção 4')
    
#     # criação de caixa de seleção
#     st.markdown('Caixa de Seleção')             # o selectbox segue o estilo do radio
#     selectbox = st.selectbox('Escolha uma opção:', ('Opção 1', 'Opção 2', 'Opção 3', 'Opção 4'))
#     if selectbox == 'Opção 1':
#         st.markdown('Opção 1')
#     if selectbox == 'Opção 2':
#         st.markdown('Opção 2')
#     if selectbox == 'Opção 3':
#         st.markdown('Opção 3')
#     if selectbox == 'Opção 4':
#         st.markdown('Opção 4')
    
#     # criação de multiselect (ideal para comparações)
#     st.markdown('Multiselction')             
#     multiselect = st.multiselect('Escolha:', ('Opção 1', 'Opção 2', 'Opção 3', 'Opção 4'))
#     if multiselect == 'Opção 1':
#         st.markdown('Opção 1')
#     if multiselect == 'Opção 2':
#         st.markdown('Opção 2')
#     if multiselect == 'Opção 3':
#         st.markdown('Opção 3')
#     if multiselect == 'Opção 4':
#         st.markdown('Opção 4')

#     # criação de file upload
#     st.markdown('File Uploader')
#     fileupload = st.file_uploader('Escolha o arquivo:', type = 'csv')
#     if fileupload is not None:
#         st.markdown('Não está vazio')

# if __name__ == '__main__':
#     main()