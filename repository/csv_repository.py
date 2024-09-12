import csv

from models.air_strike_mission import AirStrikeMission
def read_missins_from_csv():
    with open('assets/missins.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)

def write_missions_to_csv(missions):
    header = ['target_city', 'priority', 'pilot', 'aircraft', 'distance', 'weather', 'pilot_skill', 'speed', 'fuel_capacity', 'fit_score']

    with open("assets/missins.csv", mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(header)

        for mission in missions:
            writer.writerow([
                mission.target_city,
                mission.priority,
                mission.pilot,
                mission.aircraft,
                mission.distance,
                mission.weather,
                mission.pilot_skill,
                mission.speed,
                mission.fuel_capacity,
                mission.fit_score
            ])