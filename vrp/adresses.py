adresses_list = ['Lassallestraße 1, 1020 Wien','Mariahilfer Straße 101, 1060 Wien','Landstraßer Hauptstraße 50, 1030 Wien','Währinger Straße 120, 1180 Wien', 'Mariahilfer Straße 112, 1060 Wien','Favoritenstraße 189, 1100 Wien','Landstraßer Hauptstraße 45, 1030 Wien','Währinger Straße 98, 1180 Wien','Praterstraße 56, 1020 Wien','Simmeringer Hauptstraße 132, 1110 Wien','Hütteldorfer Straße 210, 1140 Wien','Kärntner Ring 15, 1010 Wien','Hernalser Hauptstraße 74, 1170 Wien','Liesinger Platz 3, 1230 Wien']
print(adresses_list)

import requests

def get_coordinates(address: str):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "geo-example-app"  # обовʼязково для Nominatim
    }

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    data = response.json()
    if not data:
        return None

    lat = float(data[0]["lat"])
    lon = float(data[0]["lon"])
    return lat, lon

for address in adresses_list:
    coords = get_coordinates(address)
    print(coords)