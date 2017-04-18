import PIL
from PIL import Image
import os
def reshape(Img_Path, size):
    img = Image.open(Img_Path)
    img = img.resize((size,size), PIL.Image.ANTIALIAS)
    img.save(Img_Path)
def reshapeFolder(folderName, size):
    images = os.listdir(folderName)
    for image in images:
        reshape(folderName + image, size)
if __name__ == "__main__":
    reshapeFolder("dataset/5/", 227)
