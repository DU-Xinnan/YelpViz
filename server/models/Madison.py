import json

class Madison():

    dataURL = './data/Madison_complete.json'
    cloudURL = './data/Madison_food.json'
    sentimentURL = './data/Madison_senti_count.json'

    @classmethod
    def get_data(cls):
        with open(cls.dataURL, 'r') as jsonFile:
            json_data = json.load(jsonFile)
            json_data = cls.filter_data(json_data)
            return json.dumps(json_data)


    @classmethod
    def get_cloud(cls):
        with open(cls.cloudURL, 'r') as jsonFile:
            json_data = json.load(jsonFile)
            json_data = cls.filter_data(json_data)
            return json.dumps(json_data)

    @classmethod
    def get_sentiment(cls):
        with open(cls.sentimentURL, 'r') as jsonFile:
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