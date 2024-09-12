import math
from toolz import pipe, groupby, first, compose
from toolz.curried import partial, unique, reduce
from repository.json_repository import read_target_from_json, read_aircraft_from_json, read_pilot_from_json
from service.location_service import get_geo_location_for_target
from service.score_service import get_score
from models.air_strike_mission import AirStrikeMission
from service.weather_service import get_weather

def haversine_distance(lat1, lon1, lat2, lon2):
    r = 6371.0
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon /
                                                                                     2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = r * c
    return distance


def missions():
    location_israel = get_geo_location_for_target("Israel")
    targets = read_target_from_json()
    aircrafts = read_aircraft_from_json()
    pilots = read_pilot_from_json()

    return pipe(
        generate_missions(location_israel, targets, aircrafts, pilots),
        partial(sorted, key=lambda m: m.fit_score, reverse=True)
    )

def generate_missions(location_israel, targets, aircrafts, pilots):
    target_infos = [prepare_target_info(location_israel, target) for target in targets]
    return [calculate_mission(aircraft, pilot, target_info)
            for target_info in target_infos
            for aircraft in aircrafts
            for pilot in pilots]

def prepare_target_info(location_israel, target):
    location_target = get_geo_location_for_target(target.city)
    weather = get_weather(target.city)
    distance = haversine_distance(location_israel.lat, location_israel.lon, location_target.lat, location_target.lon)
    return (location_target, weather, distance, target)

def calculate_mission(aircraft, pilot, target_info):
    location_target, weather, distance, target = target_info
    score = get_score(aircraft, pilot, target, weather, distance)
    return create_airstrike_mission(target, aircraft, pilot, weather, distance, score)

def create_airstrike_mission(target, aircraft, pilot, weather, distance, score):
    return AirStrikeMission(
        target_city=target.city,
        priority=target.priority,
        pilot=pilot.name,
        aircraft=aircraft.type,
        distance=distance,
        weather=weather,
        pilot_skill=pilot.skill,
        speed=aircraft.speed,
        fuel_capacity=aircraft.fuel_capacity,
        fit_score=score
    )


def unique_mission(missions):
    return pipe(
        missions,
        lambda x: reduce(
            lambda dict, n: dict if any(k in dict for k in [n.aircraft, n.target_city, n.pilot])
            else {**dict, n.aircraft: n, n.target_city: n, n.pilot: n}, x, {} ),
        dict.values,
        set,
        partial(sorted, key = lambda m: m.fit_score, reverse=True),
        list
    )






