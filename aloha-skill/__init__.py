from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
import requests

class AlohaSkill(MycroftSkill):
    def __init__(self):
        """ The __init__ method is called when the Skill is first constructed.
        It is often used to declare variables or perform setup actions, however
        it cannot utilise MycroftSkill methods as the class does not yet exist.
        """
        super().__init__()
        self.learning = True

    def initialize(self):
        """ Perform any final setup needed for the skill here.
        This function is invoked after the skill is fully constructed and
        registered with the system. Intents will be registered and Skill
        settings will be available."""
        my_setting = self.settings.get('my_setting')

    @intent_handler(IntentBuilder('AlohaIntent').require('AlohaKeyword'))
    def handle_aloha_intent(self, message):
        """ This is an Adapt intent handler, it is triggered by a keyword."""
        self.speak_dialog("aloha")
        endpoint = "https://webhook.site/530d22f3-7163-4633-bd5b-1ce56169f49d"
        try:
            response = requests.post(endpoint)
        except Exception as e:
            self.log.error(f"Error making POST request: {e}")


    def stop(self):
        pass


def create_skill():
    return AlohaSkill()
