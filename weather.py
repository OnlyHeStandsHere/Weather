import json


class Weather:
    def __init__(self, filename):
            self.fileName = filename
            self.file = open(self.fileName)
            with open(self.fileName) as file:
                self.weather = json.loads(file.read())

    def get_json(self):
        return self.weather

    def get_city_id(self):
        try:
            return self.weather[0]['city_id']
        except KeyError:
            return 0

    def get_length(self):
        return len(self.weather)

    def get_temp(self, index):
        temps = {}
        try:
            record = self.weather[index]['main']
            temps["temp"] = record['temp']
            temps["temp_min"] = record['temp_min']
            temps["temp_max"] = record['temp_max']
            temps["note"] = "All temperatures found"
        except KeyError:
            print("no temps found")