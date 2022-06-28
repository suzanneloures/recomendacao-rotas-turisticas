import poi
from evaluation import *
import polyline
from route import Route
import googlemaps
from datetime import datetime
from flask import Flask, render_template, request, url_for, flash, redirect
from key import *
from geopy.distance import geodesic
from recommender import *

app = Flask(__name__)
app.config['SECRET_KEY'] = KEY_FLASK
gmaps = googlemaps.Client(key=KEY_MAPS)

@app.route('/')
def index():
    return render_template('index.html')

def get_formatted_locations(adress):
    geocode_result = gmaps.geocode(adress)
    return geocode_result[0]["formatted_address"]

def get_directions(start_location,end_location):
    directions_result = gmaps.directions(start_location,end_location, alternatives=True, waypoints=None, mode= "driving", arrival_time=datetime.now())
    return directions_result

@app.route('/buscar', methods=('GET', 'POST'))
def index_search():
    if request.method == 'POST':
        start_location = request.form['partida']
        start_loc_formatted = get_formatted_locations(start_location)
        end_location = request.form['chegada']
        end_loc_formatted = get_formatted_locations(end_location)
        routes = get_directions(start_loc_formatted,end_loc_formatted)
        pois = poi.loadJson() #carrega os pontos de interesse
        resultado = [];
        for route in routes: # para cada rota nas possiveis rotas, procurar por pois dentro de cada rota
            obj_route_pois = poisPorRota(route,pois,300)
            obj_route_scores_por_rota = score_by_route(obj_route_pois, request.form['id_user'])
            obj_com_rec_score = recommender(obj_route_scores_por_rota)
            resultado.append(obj_com_rec_score)
            #print ("Rota via: " + obj_com_rec_score.google_route['summary'] + "--" + str(obj_com_rec_score.rec_score) )
        resultado.sort(key=lambda x: x.rec_score, reverse=True)
    else:
        start_location = None
        end_location = None
        return render_template('search.html')
    return render_template('search.html', resultado = resultado)

'''
    rota: rota do gmaps
    pois: lista de pois
    distance: distancia maxima
'''
def poisPorRota(rota_gmaps,pois,distance):
    print (">> Carregando POIS por rota ...")
    coordenadas_perimetro_rota = polyline.decode(rota_gmaps['overview_polyline']['points']) #cada pequeno ponto de uma rota do google tem uma coordenada
    pois_retorno = []
    for par_coord in coordenadas_perimetro_rota:
        pois_add = poi.poisInDistance(par_coord,pois,distance)
        for poi_to_add in pois_add:
            if poi_to_add not in pois_retorno:
                pois_retorno.append(poi_to_add)
    print (">> POIS por rota OK ...")
    return Route(rota_gmaps,pois_retorno)


@app.route('/evaluation', methods=('GET', 'POST'))

def page_evaluation():
    if request.method == 'POST':
        all_evaluation_routes = loadJsonRoutes() #carrega as avaliações das rotas
        routes = routes_filtred(all_evaluation_routes, request.form['id_user'], request.form['route_name'])
        resultado = [];
        for route in routes: # para cada rota nas possiveis rotas, procurar por pois dentro de cada rota
            obj_route = convert_to_object_routes(route)
            obj_route_scores_por_rota = score_by_route_evaluation(obj_route, route['user_id'])
            obj_com_rec_score = recommender(obj_route_scores_por_rota)
            resultado.append(obj_com_rec_score)
        resultado.sort(key=lambda x: x.rec_score, reverse=True)
        rank = 0;
        for obj in resultado:
            rank += 1 
            obj.rank = rank
    else:
        return render_template('evaluation.html')
    return render_template('evaluation.html', resultado = resultado)

