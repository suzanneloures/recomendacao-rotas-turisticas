from distance import *
import json


def loadJson():
    with open('src/data/poi-dataset-pub.json', encoding="utf8") as f:
        return json.load(f)

'''
Dado um ponto, pesquisar na base de pontos de interesse, os que estao ate determinada distancia
'''
def poisInDistance(startPoint,pois,distance):
    for p in pois:
        #print("Distancia:" + str(p['name']) )
        distanceBetween(startPoint,(p['latitude'],p['longitude']))
    r =  [p for p in pois if distanceBetween(startPoint,(p['latitude'],p['longitude'])) <= distance ]

    return r