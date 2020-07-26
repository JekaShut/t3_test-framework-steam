import json


class GetJson:
    '''
    Use .get("config element") to get element from config.json
    '''
    def get(getELEMENT):
        '''
        :return: element from config
        '''
        with open('resources/config.json') as config_file:
            data = json.load(config_file)
        ELEMENT = data[getELEMENT]
        return(ELEMENT)
