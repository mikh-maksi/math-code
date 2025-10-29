# Генерація випадкових варіантів/отримання даних із файла-сховища.
import math

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Обчислює відстань між двома точками на Землі за координатами (в кілометрах).

    Параметри:
    lat1, lon1 — широта і довгота першого міста (в градусах)
    lat2, lon2 — широта і довгота другого міста (в градусах)
    """
    R = 6371.0  # Радіус Землі в км

    # Перетворення в радіани
    φ1 = math.radians(lat1)
    φ2 = math.radians(lat2)
    Δφ = math.radians(lat2 - lat1)
    Δλ = math.radians(lon2 - lon1)

    # Формула гаверсина
    a = math.sin(Δφ / 2)**2 + math.cos(φ1) * math.cos(φ2) * math.sin(Δλ / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance
l = haversine_distance(50.45, 30.52, 49.84, 24.03)
print(l)


lat = [52.500556,50.938056,48.139722,51.049259]
lon = [13.398889,6.956944,11.574444,13.73836]
# places = [{"Name":"Berlin","Let":"A","Lat":52.500556,"Lon":13.398889},
# {"Name":"Cologne","Let":"B","Lat":50.938056,"Lon":6.956944},
# {"Name":"München","Let":"C","Lat":48.139722,"Lon":11.574444},
# {"Name":"Dresden","Let":"D","Lat":51.049259,"Lon":13.73836}]
# print(places)

places = [{"Name":"Lassallestraße 1, 1020 Wien","Let":"A","Lat":48.222338,"Lon":16.397722},
{"Name":"Mariahilfer Straße 101, 1060 Wien","Let":"B","Lat":48.19528,"Lon":16.33746},
{"Name":"Landstraßer Hauptstraße 50, 1030 Wien","Let":"C","Lat":48.196056,"Lon":16.396312},
{"Name":"Währinger Straße 120, 1180 Wien","Let":"D","Lat":48.230005,"Lon":16.343063}]



places = [
    {"Name":"Lassallestraße 1, 1020 Wien","Let":"A","Lat":48.222338,"Lon":16.397722},
    {"Name":"Mariahilfer Straße 101, 1060 Wien","Let":"B","Lat":48.195280,"Lon":16.337460},
    {"Name":"Landstraßer Hauptstraße 50, 1030 Wien","Let":"C","Lat":48.196056,"Lon":16.396312},
    {"Name":"Währinger Straße 120, 1180 Wien","Let":"D","Lat":48.230005,"Lon":16.343063},
    {"Name":"Favoritenstraße 150, 1100 Wien","Let":"E","Lat":48.174410,"Lon":16.376297},
    {"Name":"Praterstraße 70, 1020 Wien","Let":"F","Lat":48.216150,"Lon":16.392740},
    {"Name":"Alser Straße 45, 1080 Wien","Let":"G","Lat":48.213160,"Lon":16.348300},
    {"Name":"Margaretenstraße 80, 1050 Wien","Let":"H","Lat":48.193470,"Lon":16.355940},
    {"Name":"Hütteldorfer Straße 120, 1140 Wien","Let":"I","Lat":48.198960,"Lon":16.300700},
    {"Name":"Meidlinger Hauptstraße 50, 1120 Wien","Let":"J","Lat":48.175750,"Lon":16.333280},
    {"Name":"Neubaugasse 70, 1070 Wien","Let":"K","Lat":48.201860,"Lon":16.349910},
    {"Name":"Gumpendorfer Straße 120, 1060 Wien","Let":"L","Lat":48.193810,"Lon":16.343540},
    {"Name":"Simmeringer Hauptstraße 180, 1110 Wien","Let":"M","Lat":48.169870,"Lon":16.427310},
    {"Name":"Wiedner Hauptstraße 90, 1040 Wien","Let":"N","Lat":48.189500,"Lon":16.366200},
    {"Name":"Sechshauser Straße 50, 1150 Wien","Let":"O","Lat":48.192660,"Lon":16.326620},
    {"Name":"Taborstraße 50, 1020 Wien","Let":"P","Lat":48.218870,"Lon":16.383210},
    {"Name":"Josefstädter Straße 120, 1080 Wien","Let":"Q","Lat":48.216920,"Lon":16.343890},
    {"Name":"Ottakringer Straße 150, 1160 Wien","Let":"R","Lat":48.214520,"Lon":16.322640},
    {"Name":"Döblinger Hauptstraße 60, 1190 Wien","Let":"S","Lat":48.241080,"Lon":16.356200},
    {"Name":"Floridsdorfer Hauptstraße 120, 1210 Wien","Let":"T","Lat":48.259540,"Lon":16.402770}
]



def distances(places):
    l = []
    for i in range(len(places)):
      elem = []
      for j in range(len(places)):
        distance = haversine_distance(places[i]["Lat"], places[i]["Lon"], places[j]["Lat"], places[j]["Lon"])
        elem.append(distance)
      l.append(elem)
    return l

d = distances(places)

for row in d:
    print(" ".join(f"{x:.2f}" for x in row))