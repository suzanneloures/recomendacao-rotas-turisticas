from geopy.distance import geodesic


def distanceBetween(p1,p2):
    return geodesic(p1,p2).meters

def inDistance(point_i, points, distance): #ponto de rota, coordenadas pois, raio 
    retorno = []
    for p in points:
        if distanceBetween(point_i, p) <= distance:
            retorno.append(p)
        #return [p for p in points if distanceBetween(point_i,p) <= distance]
    return retorno


def byStep(coordinates, stepMeters):
    result = []
    coord = coordinates[0]
    for c in coordinates:
        if distanceBetween(coord, c) >= stepMeters:
            result.append(c)
            coord = c
        
    return result

