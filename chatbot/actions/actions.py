# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import random
import requests
import json

from datetime import datetime

BASE_API = 'http://api:4040//RyazMax/BaumanBotApi/1.0.0'

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

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

week_types = {
    'even': 'знаменатель',
    'odd': 'числитель',
}

class GetWeekAction(Action):
    def name(self) -> Text:
        return "get_week_type"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        now = datetime.now()
        resp = requests.get(BASE_API + f'/week?date={now.day}.{now.month}.{now.year}')
        obj = json.loads(resp.json())

        dispatcher.utter_message(text=f'Cейчас {obj["num"]}я неделя - {week_types[obj["type"]]}')
        return []