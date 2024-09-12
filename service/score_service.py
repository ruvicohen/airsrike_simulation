def weather_score (weather):
    if weather.main == "Clear":
        return 1.0 # Best condition
    elif weather.main == "Clouds":
        return 0.7
    elif weather.main == "Rain":
        return 0.4 # Rainy weather
    elif weather.main == "Stormy":
        return 0.2
    else:
        return 0 # Unfavorable condition

def pilot_score(pilot):
    return pilot.skill / 10

def plane_score(aircraft, distance):
    if distance < aircraft.fuel_capacity:
        return 1
    return aircraft.fuel_capacity / distance

def target_score(target):
    return target.priority / 10

def get_score(aircraft, pilot, target, weather, distance):
    return (
            weather_score(weather) * 0.2 +
            pilot_score(pilot) * 0.2 +
            plane_score(aircraft, distance) * 0.3 +
            target_score(target) * 0.3
        )


