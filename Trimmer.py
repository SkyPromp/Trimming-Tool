import cv2 as cv
import numpy as np
import sys


def cropper(path):
    img = cv.imread(path, cv.IMREAD_UNCHANGED)
    print(len(img), len(img[0]), sep="x", end=" -> ")

    def xrem(image):
        while not sum(i[3] if not isinstance(i, np.uint8) else 255 for i in image[0]):
            image = image[1:]

        return image

    def yrem(image):
        tot = 0
        for i in range(len(image)):
            if not isinstance(image[i][0], np.uint8):
                tot += image[i][0][3]
            else:
                tot += 255
        while not tot:
            image = np.delete(image, 0, 1)
            tot = 0
            for i in range(len(image)):
                if not isinstance(i, np.uint8):
                    tot += image[i][0][3]
                else:
                    tot += 255

        return image

    img = xrem(img)
    img = xrem(img[::-1])[::-1]
    img = yrem(img)
    img = np.fliplr(yrem(np.fliplr(img)))

    print(len(img), len(img[0]), sep="x")
    cv.imwrite(path, img)


for arg in sys.argv[1:]:
    cropper(arg)
    
