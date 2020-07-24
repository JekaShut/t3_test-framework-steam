import json


class GetJson:
    with open('resources/config.json') as config_file:
        data = json.load(config_file)
    actualBrowser = data["actualBrowser"]
    SITE = data["SITE"]
