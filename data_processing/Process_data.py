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

def readjson(city, fileName):
    basePath = "cities_photos/"+ city +"/"
    cityFile = open(basePath + fileName, 'r')
    return json.loads(cityFile.read())  
def process_restaurant(city):
    cityData = readjson(city, "Madison.json")
    labelsData = readjson(city, "Madision_lables.json")
    mappingData = readjson(city, "Madisonmapping.json")
    healthData = readjson(city, "Madision_health_index.json")
    problemRestaurantsIds = []
    for restaurant in cityData:
        business_id = restaurant["business_id"]
        images = mappingData[business_id]
        if len(images) == 0:
            problemRestaurantsIds.append(business_id)
        else:
            for image in images:
                try:
                    lables = [lable["description"] for lable in labelsData[image]]
                    if "food" not in lables:
                        images.remove(image)
                except:
                    images.remove(image)
            images_healthindex = [{'image': image, 'health_index': healthData[image]} for image in images]
            restaurant["images"] = images_healthindex
    cityData = [restaurant for restaurant in cityData if restaurant['business_id'] not in problemRestaurantsIds]
    writeFile = open('Madision_with_healthindex.json', 'w')
    writeFile.write(json.dumps(cityData, indent = 4))
    writeFile.close()
if __name__ == "__main__":
    #process_prediction("Cleveland")
    process_restaurant("Madision")