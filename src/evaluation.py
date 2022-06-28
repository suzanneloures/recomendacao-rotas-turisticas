import json
from route import Route


def loadJsonRoutes():
    with open('src/data/route.json', encoding="utf8") as f:
        return json.load(f)


def routes_filtred(routes, user_id, route_name):
    routes_filtred = [];
    for route in routes:
        if (route['route_name'] == route_name and  route['user_id'] == int(user_id) ):
            routes_filtred.append(route)
    return routes_filtred


def convert_to_object_routes(route_json):
    #adiciona os pois
    route_pois = json.loads(route_json['pois'])
    #obj_route.pois = route_pois
    #adiciona a rota
    route_gmaps = json.loads(route_json['json'])
    #obj_route.google_route = route_gmaps
    
    return Route(route_gmaps,route_pois,route_json['user_score'])

