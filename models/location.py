class Location:
    def __init__(self, lat=None, lon=None):
        self.lat = lat
        self.lon = lon


    def __str__(self):
        return f"lat: {self.lat}, lon: {self.lon}"
