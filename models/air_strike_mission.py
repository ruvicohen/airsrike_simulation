class AirStrikeMission:
    def __init__(self, target_city, priority, pilot, aircraft, distance, weather, pilot_skill, speed, fuel_capacity, fit_score):
        self.target_city = target_city
        self.priority = priority
        self.pilot = pilot
        self.aircraft = aircraft
        self.distance = distance
        self.weather = weather
        self.pilot_skill = pilot_skill
        self.speed = speed
        self.fuel_capacity = fuel_capacity
        self.fit_score = fit_score

    def __repr__(self):
        return (f"AirStrikeMission(target_city={self.target_city}, priority={self.priority}, pilot={self.pilot}, "
                f"aircraft={self.aircraft}, distance={self.distance}km, weather={self.weather}, "
                f"pilot_skill={self.pilot_skill}, speed={self.speed}km/h, fuel_capacity={self.fuel_capacity}km, "
                f"fit_score={self.fit_score})")

