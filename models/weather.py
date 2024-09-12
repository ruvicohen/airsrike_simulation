class Wheathr:
    def __init__(self, main = None, cloudsall = None, windspeed = None):
        self.main = main
        self.cloudsall = cloudsall
        self.windspeed = windspeed

    def __str__(self):
        return f"main: {self.main}, cloudsall: {self.cloudsall}, windspeed: {self.windspeed}"


