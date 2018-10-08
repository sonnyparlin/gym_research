import geopy.distance

def distance(lat1, lon1, lat2, lon2):
    coords_1 = (lat1, lon1)
    coords_2 = (lat2, lon2)

    return geopy.distance.vincenty(coords_1, coords_2).miles