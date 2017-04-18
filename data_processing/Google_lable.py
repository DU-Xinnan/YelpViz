import io
import os
import json
import time

# Imports the Google Cloud client library
from google.cloud import vision

def getLables(city):
    # Instantiates a client
    vision_client = vision.Client()

    # The name of the image file to annotate
    file_names = os.listdir(city+"/")
    result = {}
    for file_name in file_names:
	# Loads the image into memory
	labelArr = []
	with io.open(city + "/" +file_name, 'rb') as image_file:
		content = image_file.read()
		image = vision_client.image(
			content=content)

	# Performs label detection on the image file
	labels = image.detect_labels()
	labelObj = {}
	for label in labels:
	    labelObj["description"] = label.description
	    labelObj["score"] = label.score
	    labelArr.append(labelObj)
	result[file_name] = labelArr
	time.sleep(0.2)
    with open(city + "_label.json", 'w') as writefile:
	writefile.write(json.dumps(result, indent=4)

if __name__ == '__main__':
    getLables("Madision")
