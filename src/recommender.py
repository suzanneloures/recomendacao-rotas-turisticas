import pandas as pd
from plotly.offline import init_notebook_mode, plot, iplot
from surprise import dump
import os
from datetime import datetime


def load_model(model_filename):
    print (">> Carregando Modelo ...")
    file_name = os.path.expanduser(model_filename)
    _, loaded_model = dump.load(file_name)
    print (">> Modelo Carregado")
    return loaded_model

def score_by_route(obj_route, user_id):
    print (">> Gerando predição de poi para rota ...")
    scores = []
    for poi in obj_route.pois:
        prediction = predict(user_id, poi['id'])
        scores.append((0,prediction)) # predizer qual nota o usuario daria para cada poi
    obj_route.scores = scores
    print (">> OK ")
    return obj_route

def score_by_route_evaluation(obj_route, user_id):
    print (">> Gerando predição de poi para rota ...")
    scores = []
    for poi in obj_route.pois:
        prediction = predict(user_id, poi['item_id'])
        scores.append((0,prediction)) # predizer qual nota o usuario daria para cada poi
    obj_route.scores = scores
    print (">> OK ")
    return obj_route

def predict(uid, iid):
    model_filename = "src/model-predict.pickle"
    file_name = os.path.expanduser(model_filename)
    _, loaded_model = dump.load(file_name)
    pred = loaded_model.predict(int(uid), iid)
    rating = pred.est
    print("Score para user " + str(uid) + " para o item " + str(iid) + " : " + str(rating))
    return rating

def recommender(obj_route_scores_por_rota): #aplica a funcao e salva na variavel recScore
    print (">> Gerando Recomendação/RecScore ...")
    sum_score = 0
    qtd_pois = len(obj_route_scores_por_rota.pois) #quantas posicoes existem no arrayde pois
    for score in obj_route_scores_por_rota.scores:
       sum_score += sum(score)
    rec_score = sum_score / qtd_pois #funcao = media entre soma das notas dos pois por quantidade de pontos
    obj_route_scores_por_rota.rec_score = rec_score
    #print(str(rec_score) + "recScore")
    print (">> RecScore Ok ...")
    return obj_route_scores_por_rota


    
    

