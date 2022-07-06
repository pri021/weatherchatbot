# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import requests 
import random 

class ActionTellWeather(Action):

    def name(self) -> Text:
        return 'action_tell_weather'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        place = tracker.get_slot('place')
        y= Weather(place)

        z=y[0]
        temp_desc=z[0]['description']
        t=y[1]
        a=t['temp']
        dispatcher.utter_message(text="temperature in {} is {}.".format(place,int(a-273)))
        dispatcher.utter_message(text="weather is {}".format(temp_desc))
        case_rain=["rain","shower rain","moderate rain","heavy intensity rain","light intensity drizzle","very heavy rain","extreme rain","freezing rain","heavy intensity shower rain","light intensity shower rain","ragged shower rain"]
        case_snow=["light snow","snow", "heavy snow","sleet","Light shower sleet","Shower sleet","Light shower snow","Shower snow","Heavy shower snow"] 
        case_atmosphere=["mist","smoke","haze","sand","fog","dust"]
        case_clear=["clear sky","few clouds","scattered clouds","broken clouds","overcast clouds"]
        case_thunderstorm=["thunderstorm with light rain","thunderstorm"]
        if temp_desc in case_rain:
            response=["please take your umbrella with you","wear a raincoat","it's raining dont forget to dry your clothes inside"]   
            dispatcher.utter_message(text=random.choice(response))

        elif temp_desc in case_snow:
            response=["it's snowing don't forget your sweater","do you want to build a snowman?", "wear your snow gloves"]
            dispatcher.utter_message(text=random.choice(response))

        
        elif temp_desc in case_atmosphere:
            response="wear your mask to protect yourself from dust"
            dispatcher.utter_message(text=response) 
        
        elif temp_desc in case_thunderstorm:
            response="dont go outside it's a thunderstorm"
            dispatcher.utter_message(text=response) 
        
        elif temp_desc in case_clear:
            response=["the sky is clear have a nice day","blue clear skies ahead of you","enjoy a sunny day"]
            dispatcher.utter_message(text=random.choice(response))

        else: 
            dispatcher.utter_message(text="no condition")

        return []

def Weather(city):
    api_address = "http://api.openweathermap.org/data/2.5/weather?appid=12c2be6f00d60769df0dace1036caa95&q="
 
    url = api_address + city
    json_data= requests.get(url).json()
    return [json_data['weather'],json_data['main']]
    



# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
