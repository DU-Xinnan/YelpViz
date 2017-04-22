import json

def process_prediction(city):
    f = open("cities_photos/"+ city +"/"+city + "_prediction.json", 'r')
    lines = f.readlines()
    data = {}
    for line in lines:
        obj = json.loads(line)
        key = obj.keys()[0]
        data[key] = obj[key]
    with open(city+"_health_index.json", 'w') as writeFile:
        writeFile.write(json.dumps(data, indent = 4))
if __name__ == "__main__":
    process_prediction("Cleveland")