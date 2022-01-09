# This program is used to preprecess the food images,
# making them of the same sizes: 3 (channel) * 100 (height) * 100 (width)

from PIL import Image
from numpy import asarray
import os
from os import listdir
from os.path import isfile, join

FINAL_SIZE = 100

def main():
    for idx in range(10):
        path = str(idx)
        fileNames = [file for file in listdir(path) if isfile(join(path, file))]
        newDirPath = "resized_images/" + str(idx)
        # os.mkdir(newDirPath)
        for j, fileName in enumerate(fileNames):
            image = Image.open(path + "/" + fileName)
            # Step 1. crop the intial image
            width, height = image.size
            cropped_width = int(2 / 3 * width)
            width_start = width // 6
            box = (width_start, 0, width_start + cropped_width, cropped_width)
            cropped_image = image.crop(box)
            # Step 2. resize the image
            final_image = cropped_image.resize((FINAL_SIZE, FINAL_SIZE))
            final_image.save(newDirPath + "/" + str(j) + ".png")


if __name__ == "__main__":
    main()
