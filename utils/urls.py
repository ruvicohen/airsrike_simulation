key = "335ad2a109935f55529042bcc5ab76a6"

def get_geo_location_url(location):
    return f"https://api.openweathermap.org/geo/1.0/direct?q={location}&appid=335ad2a109935f55529042bcc5ab76a6"

def get_weather_url(location):
    return f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid=335ad2a109935f55529042bcc5ab76a6"