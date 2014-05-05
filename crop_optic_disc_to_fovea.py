#!/usr/bin/python
from SimpleCV import Image, Color
from random import randrange
import os

IMG_TYPES = ['jpg', 'bmp']  # add image types to this list for other extensions

IMG_DIR = raw_input('enter image directory path: ')
if not IMG_DIR.endswith('/'):
    IMG_DIR = IMG_DIR + '/'

CROPPED_IMG_SAVE_DIR = IMG_DIR + 'cropped/'  # directory where cropped images will be saved

def crop_optic_nerve_img(image, image_name):
    binarized = image.binarize(220).invert() # 220 white threshold for finding blobs
    binarized.show()
    raw_input()

    blobs = binarized.findBlobs()

    print(image_name)
    print("-" * len(image_name))
    print('image width: ' + str(image.width))
    print('image height: ' + str(image.height))
    print("")

    print("optic nerve position")
    print("-" * len("optic nerve position"))
    print("x: " + str(blobs.x()[0]))
    print("y: " + str(blobs.y()[0]))
    print("width: " + str(blobs.width()[0]))
    print("height: " + str(blobs.height()[0]) + '\n')

    blobs = sorted(blobs, key=lambda blob: blob.area(), reverse=True)[:2] # sort blobs list based on blob area and limit to top largest 2

    if blobs[0].y > 50:
        blobs = [blobs[0]]  # optic nerve is typically at the centre of the y, around 700-800

    for blob in blobs:
        yield image.crop(blob.x-400, blob.y-40,
                400-blob.width(),
                blob.height()+60)
    

is_supported_img_type = lambda img: img.split('.')[-1] in IMG_TYPES  # used to filter out non-supported images in list
images = filter(is_supported_img_type, os.listdir(IMG_DIR))

if not os.path.exists(CROPPED_IMG_SAVE_DIR):
    os.makedirs(CROPPED_IMG_SAVE_DIR)

for image in images:
    cropped_image = crop_optic_nerve_img(Image(IMG_DIR+image), image)

    for img in cropped_image:
        print("cropped image (left of the optic disc)")
        print("-" * len("cropped image"))
        print("width: " + str(img.width))
        print("height: " + str(img.height))
        img.show()
        raw_input()

        img = img.crop(img.width/3, img.height/4 - ((img.height/3+60)-img.height), 130, 60) 
        print("second cropped image (fovea)")
        print("-" * len("second cropped image"))
        print("width: " + str(img.width))
        print("height: " + str(img.height))
        img.show() 
        
        save = raw_input("save image (y/n) ")
        if save == 'y':
            img.save(CROPPED_IMG_SAVE_DIR + image)
