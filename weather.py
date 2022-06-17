import requests
def Weather(city):
    API_key = "http://api.openweathermap.org/data/2.5/weather?appid=12c2be6f00d60769df0dace1036caa95="
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    Final_url = base_url + "appid=" + API_key + "&q=" + city + "&units=metric"
    weather_data = requests.get(Final_url).json()
    
    return weather_data['main']
