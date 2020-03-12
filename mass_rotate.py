import os
from PIL import Image
from imutils import paths

dir = input("Enter dir: ")
imagePaths = list(paths.list_images(dir))
for imgPath in imagePaths:
    image = Image.open(imgPath)
    image = image.transpose(Image.ROTATE_90)
    print(imgPath)
    image.save(imgPath)
print("Done")
