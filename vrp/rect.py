import json
import random

def generate_points(rect_json, n):
    lat_min = rect_json["Lat_min"]
    lat_max = rect_json["Lat_max"]
    lon_min = rect_json["Lon_min"]
    lon_max = rect_json["Lon_max"]

    points = set()
    while len(points) < n:
        lat = round(random.uniform(lat_min, lat_max), 6)
        lon = round(random.uniform(lon_min, lon_max), 6)
        points.add((lat, lon)) 

    result = [{"Lat": lat, "Lon": lon} for lat, lon in points]
    return json.dumps(result, indent=2, ensure_ascii=False)


rectangle = {
    "Lat_min": 48.15, "Lat_max": 48.30,
    "Lon_min": 16.25, "Lon_max": 16.45
}

print(generate_points(rectangle, 10))