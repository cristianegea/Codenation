import category_encoders as ce
import pandas as pd
from sklearn.preprocessing import StandardScaler

# O pré-processamento envolve muitos testes (para ver se há gasnho de performance nas métricas)

class Preprocessing:
    # Criação dos objetos que serão salvos junto com a classe para serem aproveitados depois
    def __init__(self):
        self.feature_names = None
        self.std_scaler = None
        self.categoric_features = None
        self.numeric_features = None
        self.catb = None
        self.scaler = None
        self.train_features = None

    def process(self, df, etapa_treino=True):
        '''
        Process data for training the model.
        :param df: Pandas DataFrame
        :param etapa_treino: Boolean
        :return: processed Pandas Data Frame
        '''
        print('Creating DataFrame for Data Manipulation')
        # Criação de dataframe de consistência
        cons = pd.DataFrame({'column': df.columns,
                             'missing_perc': (df.isna().sum() / df.shape[0]) * 100,
                             'dtype': df.dtypes })
        # Filtragem dos missing values
        print('Droping columns with missing values')
        cons = cons[cons['missing_perc'] == 0]
        # Filtragem dos id's
        print('Dropping column with Id')
        cons = cons[cons['column'] != 'Id']
        # Criação de lista com features numéricas
        print('Creating list with numeric features')
        numeric_features = list(cons[(cons['dtype'] == 'int64') | (cons['dtype'] == 'float')]['column'])
        # Criação de lista com features categóricas
        print('Creating list with categoric features')
        categoric_features = list(cons[(cons['dtype'] == 'object')]['column'])
        print('Removing target')
        if etapa_treino == True:
            numeric_features.remove('SalePrice')        # SalePrice = target do modelo
        else:
            pass
        print('Feature encoder')
        print('Feature Normalization and Encoding')
        # Criação do objeto "std_scaler"
        std_scaler = StandardScaler()
        if etapa_treino == True:
            y = df['SalePrice']
            df = df.drop(columns={'SalePrice'})
            self.numeric_features = numeric_features
            self.categoric_features = categoric_features
            self.feature_names = self.numeric_features + self.categoric_features
            self.scaler = std_scaler                                        # para feature numérica
            self.catb = ce.CatBoostEncoder(cols=self.categoric_features)    # para feature categórica
            df[self.numeric_features] = self.scaler.fit_transform(df[self.numeric_features])
            df[self.categoric_features] = self.catb.fit_transform(df[self.categoric_features], y=y)
            self.train_features = self.numeric_features + self.categoric_features
            return df[self.categoric_features + self.numeric_features], y
        else:
            df[self.numeric_features] = self.scaler.transform(df[self.numeric_features])
            df[self.categoric_features] = self.catb.transform(df[self.categoric_features])
            for column in df[self.categoric_features + self.numeric_features].columns:
                df[column] = df[column].fillna(df[column].mean())
            return df[self.categoric_features + self.numeric_features]
