import json
import os
from idlelib.iomenu import encoding

from models.pilot import Pilot
from models.aircraft import Aircraft
from models.target import Target

current_dir = os.path.dirname(__file__)

def read_aircraft_from_json():
    with open(os.path.join(current_dir, "../assets/aircraft.json"), 'r', encoding="utf8") as jsonfile:
        data = json.load(jsonfile)
    return [Aircraft(**aircraft) for aircraft in data["aircraft"]]


def read_pilot_from_json():
    with open(os.path.join(current_dir, "../assets/pilots.json"), 'r', encoding="utf8") as jsonfile:
        data = json.load(jsonfile)
    return [Pilot(**pilot) for pilot in data["pilots"]]

def read_target_from_json():
    with open(os.path.join(current_dir, "../assets/targets.json"), 'r', encoding="utf8") as jsonfile:
        data = json.load(jsonfile)
    return [Target(**target) for target in data["targets"]]
