import json
from urllib.request import urlopen, Request
import urllib.error
import config
import os
import subprocess

config = config.load_config()

try:
    request = Request(config.restUrl)
    request.add_header('API-TOKEN', config.apiToken)
    request.add_header('Content-Type', 'application/json')
    with urlopen(request) as handle:
        content = handle.read().decode('utf-8')
except urllib.error.URLError as error:
    print(error.reason)
    raise error

data = json.loads(content)
activeAlarm = data["activeAlarmsData"]["activeAlarms"] is not None

alarmFile = config.alarmPath + ".alarm"

if activeAlarm:
    open(alarmFile, "w")
    subprocess.call("tv_on.sh")
else:
    if os.path.isfile(alarmFile):
        os.remove(alarmFile)
        subprocess.call("tv_standby.sh")
