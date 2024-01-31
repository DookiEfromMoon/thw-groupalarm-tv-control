import json
import config
import os
import subprocess
import requests

config = config.load_config()

try:
    result = requests.get(config.restUrl, headers={
        "Content-Type": "application/json", "API-TOKEN": config.apiToken
    })
    content = result.content.decode('utf-8')
except requests.exceptions.HTTPError as e:
    print(e.response.status_code)
    print(e.response.raw)
    raise e

data = json.loads(content)
activeAlarm = data["activeAlarmsData"]["activeAlarms"] is not None

alarmFile = config.alarmPath + ".alarm"
isFile = os.path.isfile(alarmFile)

if activeAlarm:
    if not isFile:
        open(alarmFile, "w")
        subprocess.call("./tv_on.sh")
else:
    if isFile:
        os.remove(alarmFile)
        subprocess.call("./tv_standby.sh")
