from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionPerformOperation(Action):
    def name(self) -> Text:
        return "utter_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        operation = tracker.latest_message['text']
        number1 = float(tracker.get_slot('number'))
        number2 = float(tracker.get_slot('number'))

        if operation in ['add', 'addition', 'plus', 'sum']:
            result = number1 + number2
        elif operation in ['subtract', 'subtraction', 'minus']:
            result = number1 - number2
        elif operation in ['multiply', 'multiplication', 'times']:
            result = number1 * number2
        elif operation in ['divide', 'division']:
            if number2 == 0:
                dispatcher.utter_message(text="Can't be 0, enter a valid operand!")
                return []
            else:
                result = number1 / number2

        dispatcher.utter_message(text=f"{operation} of {number1} and {number2} is {result}")
        return []


class ActionAskFirstOperand(Action):
    def name(self) -> Text:
        return "utter_number1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        operation = tracker.latest_message['text']
        dispatcher.utter_message(text=f"What is the first operand for {operation}?")
        return []


class ActionAskSecondOperand(Action):
    def name(self) -> Text:
        return "utter_number2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        operation = tracker.latest_message['text']
        dispatcher.utter_message(text=f"What is the second operand for {operation}?")
        return []


class ActionShowResult(Action):
    def name(self) -> Text:
        return "utter_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        operation = tracker.latest_message['text']
        number1 = float(tracker.get_slot('number1'))
        number2 = float(tracker.get_slot('number2'))
        result = float(tracker.get_slot('result'))

        dispatcher.utter_message(text=f"{operation} of {number1} and {number2} is {result}")
        return []
