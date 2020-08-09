import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from joblib import dump, load

from data_source import DataSource
from preprocessing import Preprocessing
from experiments import Experiments 

# Recomendado que sempre que começar um projeto novo começar pelo "model_training", onde vou chamar o "DataSource" e o "preprocessing"

class ModelTraining:
    def __init__(self):
        self.data = DataSource()        
            # os dados são oriundos da classe "DataSource" (arquivo "data_source.py")
        self.preprocessing = None
            # no início ainda não há o pré-processamento da classe que será salva junto com o modelo

    # Criação da função model_training     
    def model_training(self):
        '''
        Train the model.
        :return: Dict with trained model, preprocessing used and columns used in training
        '''
        # no momento em que o modelo é treinado, a classe "Preprocessing" é chamada
        pre = Preprocessing()
        print('Loading data')
        # Leitura dos dados na etapa de treino
        df = self.data.read_data(etapa_treino = True)
        print('Training preprocessing')
        # Pré-processamento dos dados de treino ("X_train" e do "y_train")
        # os dados de treino vêm junto com a label
        X_train, y_train = pre.process(df, etapa_treino = True)
        print('Training Model')
        # Chamando uma regressão linear
        model_obj = LinearRegression()
        # Ajustamento do modelo aos dados (para o modelo começar a aprender com os dados)
        model_obj.fit(X_train, y_train)
        # Retorno da função "model_training" (a função retorna um dicionário)
        model = {'model_obj' : model_obj,           # objeto do modelo treinado        
                 'preprocessing' : pre,             # preprocessamento criado
                 'colunas' : pre.feature_names}     # nome das features que foram treinadas junto com o modelo
        print(model)
        # Salvando o output do modelo
        dump(model, '../output/modelo.pkl')
        return model
    
    