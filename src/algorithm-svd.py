import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go
## Surprise
from surprise import Reader, Dataset, SVD
from surprise.model_selection import GridSearchCV
import os
from surprise import dump
##CrossValidation
from surprise.model_selection import cross_validate

##Matrix Factorization Algorithms
from surprise import SVD


def train():
    ratings_df = pd.read_csv(open('data/evaluation-csv.csv')) #carrega o csv
    ratings_df = ratings_df.dropna() # remove os nulos
    
    #Carregar o conjunto de dados através de Surprise.Dataset.
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(ratings_df[['user_id', 'poi_id', 'rating']], reader)
    
    #O método build_full_trainset() constrói o conjunto de treinamento a partir de todo o conjunto de dados
    trainset = data.build_full_trainset()
    #SVD() treina o modelo do trainset
    algo_SVD = SVD() #pode ser passado parametros para potencializar o algoritmo
    algo_SVD.fit(trainset)
   
    ##Salvando o modelo
    model_filename = "./model-predict.pickle"
    file_name = os.path.expanduser(model_filename)
    dump.dump(file_name, algo=algo_SVD)

    # Contem as classificações para todos os pares (usuario,item) que NÃO estão no conjunto de treinamento.
    testset = trainset.build_anti_testset()
    predictions = algo_SVD.test(testset) #matriz de avaliações de usuarios para itens que eles nao avaliaram
    #print(predictions[0:10])


def rating_distribution(df):
    data = df['rating'].value_counts().sort_index(ascending=False)
    trace = go.Bar(x = data.index,
                text = ['{:.1f} %'.format(val) for val in (data.values / df.shape[0] * 100)],
                textposition = 'auto',
                textfont = dict(color = '#000000'),
                y = data.values,
                )
    # Create layout
    layout = dict(title = 'Distribution Of {} ratings'.format(df.shape[0]),
                xaxis = dict(title = 'Rating'),
                yaxis = dict(title = 'Count'))
    # Create plot
    fig = go.Figure(data=[trace], layout=layout)
    fig.show()

def reduce_dimensionality(df):

    df.drop(['id'], axis=1, inplace=True)
    df = df.dropna() # remove os nulos
    #df_new = df[(df['poi_id'].isin(filter_items)) & (df['user_id'].isin(filter_users))]
    #print('Columns of ratings_df: {0}'.format(ratings_df.columns))
    #print(df.head())
    #print(df.info())
    print(df.describe())
    #print('The original data frame shape:\t{}'.format(df.shape))
    #print('The new data frame shape:\t{}'.format(df_new.shape))


if __name__ == '__main__':
    train()
    #ratingsdf_df = pd.read_csv(open('data/evaluation-csv.csv')) #carrega o csv
    #reduce_dimensionality(ratingsdf_df)
    #print(loaded_model.predict(uid=22, iid=5896287798 ))
   
   
    

