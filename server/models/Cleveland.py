import json

class Cleveland():

    dataURL = './data/Cleveland_Full.json'

    @classmethod
    def get_data(cls):
        with open(cls.dataURL, 'r') as jsonFile:
            json_data = json.load(jsonFile)
            json_data = cls.filter_data(json_data)
            return json.dumps(json_data)

    @classmethod
    def filter_data(cls, data):
        res = data
        # point_table = []
        # for point in res['pointTable']:
        #     if point['year'] == '2008':
        #         point_table.append(point)
        # res['pointTable'] = point_table
        return res