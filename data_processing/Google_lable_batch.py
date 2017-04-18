import io
import os
import json
import time
from google.cloud.vision.feature import Feature
from google.cloud.vision.feature import FeatureTypes

def getLables(city):
    # Imports the Google Cloud client library
    from google.cloud import vision
    
    # Instantiates a client
    vision_client = vision.Client()
    # The name of the image file to annotate
    result = {}
    files = os.listdir(city)
    for i in range(1, 1490):
        time.sleep(1)
        batch = vision_client.batch()
        print("images from "+str(i*10-10)+"to " +str(i*10))
	start = (i-1)*10
	end = i * 10
	file_names = files[start:end]
	for file_name in file_names:
	    # Loads the image into memory
	    with io.open(city + "/" +file_name, 'rb') as image_file:
		content = image_file.read()
		image = vision_client.image(content=content)
		batch.add_image(image, [Feature(FeatureTypes.LABEL_DETECTION,10)])
		# Performs label detection on the image file
	allLables = batch.detect()
	for index, image in enumerate(allLables):
	    labelArr = []
	    for label in image.labels:
		labelObj = {}
		labelObj['description'] = label.description
		labelObj['score'] = label.score
		labelArr.append(labelObj)
		#print(label.description + ": " + str(label.score))
	    result[file_names[index]] = labelArr
            tempDict = {}
	    tempDict[file_names[index]] = labelArr
            f = open("tem_cleveland_lables.json", "a+")
            f.write(json.dumps(tempDict))
            f.write("\n")
    with open(city+"_lables.json", 'w') as writeFile:
        jsonStr = json.dumps(result, indent=4)
        writeFile.write(jsonStr)
        print("finish writing")

if __name__ == "__main__":
    currTime = time.time()
    getLables("Cleveland")
    print("total Time: " + str(time.time() - currTime))
    
