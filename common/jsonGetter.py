import json


class GetJson:
    '''
    Use .get("element") to get element from .json
    '''

    def getConfig(getELEMENT):
        '''
        :return: element from config
        '''

        with open('resources/config.json', "rb") as config_file:
            data = json.load(config_file)
        ELEMENT = data[getELEMENT]
        return (ELEMENT)

    def getData(getELEMENT):
        '''
        :return: element from DataFile
        '''

        with open('resources/data.json', "rb") as config_file:
            data = json.load(config_file)
        ELEMENT = data[getELEMENT]
        return (ELEMENT)
