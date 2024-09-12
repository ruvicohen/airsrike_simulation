from repository.csv_repository import write_missions_to_csv, read_missins_from_csv
from repository.json_repository import read_target_from_json, read_pilot_from_json, read_aircraft_from_json
from service.mission_service import missions, all_missions, unique_mission, unique_mission


def menu():
    while True:
        print("\nMenu:")
        print("1. Load files from JSON")
        print("2. Display recommendation table")
        print("3. Save attacks to CSV")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            load_files()
            print("Files loaded successfully.")
        elif choice == '2':
            read_missins_from_csv()
        elif choice == '3':
            all_missions = missions()
            unique_mission = unique_mission(all_missions)
            write_missions_to_csv(unique_mission)
            print("Missions saved to CSV.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")


def load_files():
    read_target_from_json()
    read_pilot_from_json()
    read_aircraft_from_json()