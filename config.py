import json


class Config:
    def __init__(self, rest_url, api_token, alarm_path):
        self.restUrl = rest_url
        self.apiToken = api_token
        self.alarmPath = alarm_path


def load_config():
    with open("config.json", "r") as file:
        data = json.load(file)
    return Config(data["restUrl"], data["apiToken"], data["alarmPath"])
