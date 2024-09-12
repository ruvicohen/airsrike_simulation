from api.weather_api import get_data
from repository.json_repository import read_target_from_json
from utils.urls import get_geo_location_url
from models.location import Location

def get_geo_location_for_targets():
    targets = read_target_from_json("../assets/targets.json")
    return targets

#print(get_geo_location_for_targets())

def get_geo_location_for_target(target):
    url = get_geo_location_url(target)
    geo_location = get_data(url)
    location = Location()
    location.lat, location.lon = geo_location[0]["lat"], geo_location[0]["lon"]
    return location

print(get_geo_location_for_target("Israel"))