import pandas as pd


class DataSource:

    # definição dos caminhos dos dados de treino, dos dados de teste e da label (target do modelo)
    def __init__(self):
        self.path_train = '../data/train.csv'
        self.path_test = '../data/test.csv'
        self.path_label = '../data/sample_submission.csv'

    # Na inicialização do "data source" os caminhos acima são criados.

    # Nesta etapa há a definição se a etapa é de treino ou de teste
    def read_data(self, etapa_treino=True):
        '''
            Read data from data sources
            :param etapa_treino: Boolean specifing if is train or test.
            :return: pd.DataFrame with values and pd.Series with labels
        '''

        # encapsulamento do "pd.read_csv"
        if etapa_treino:
            df = pd.read_csv(self.path_train)
            return df

        df = pd.read_csv(self.path_test)
        y = pd.read_csv(self.path_label)
        return df, y
