from math import cos, asin, sqrt
import pandas as pd


def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))


def build_distance_tuples():
    df = pd.read_csv('https://raw.githubusercontent.com/sonnyparlin/gym_research/master/rkbjj_florida.csv')
    site_lat = df.lat
    site_lon = df.lon
    locations_name = df.text
    dh={}
    final=[]
    last=0
    for i in range(len(site_lat)):
        lat1=site_lat[i]
        lon1=site_lon[i]
        dist_array=[]
    
        for x in range(len(site_lat -1)):
            if site_lat[x] == site_lat[i]:
                continue
            else:
                lat2=site_lat[x]
                lon2=site_lon[x]
        
            dist = int(distance(lat1, lon1, lat2, lon2) / 1.609)
            if (dist < 20) and (locations_name[x],locations_name[i], dist) not in final:
                final.append((locations_name[i],locations_name[x], dist))

    final = list(set(final))
    final = sorted(final, key=lambda x: x[2])
    return final
    
final = build_distance_tuples()