from PIL import Image as PIL_Image #needed as we now have multiple libraries that use "Image"
import numpy as np
import math

def gravLens(imageArray, centerX = 0.5, centerY = 0.5, thetaE = 0.1):
    imageWidth = len(imageArray)
    imageHeight = len(imageArray[0])
    # centerX = imageWidth
    # centerY = imageHeight
    thetaE *= min(imageWidth, imageHeight)

    modifiedImageArray = imageArray.copy()

    aveColor = averageColor(imageArray)

    for x in range(imageWidth):
        for y in range(imageHeight):
            dx = x - centerX
            dy = y - centerY
            # theta is the "angle" coordinate from the gravlens source to the image, using small angle approximation
            # t is the angle from the +x axis
            theta, t = polarCoords(dx, dy)

            if theta < 1.e-7:
                beta = math.inf
                u = 1
                mag = 0
            else:
                # beta is the "angle" coordinate from the gravlens source to the source, using small angle approximation
                beta = (theta**2 - thetaE**2) / theta

                dx_, dy_ = cartCoords(beta, t)
                modifiedImageArray[x, y, 0:3] = getPixel(imageArray, dx_ + centerX, dy_ + centerY, aveColor)

                u = abs(beta) / math.sqrt(beta**2 + 4*thetaE**2)

                mag = 1
                if u < 1.e-7:
                    pass
                elif True:
                    mag = (u + 1/u + 2)/4

            cap = 5
            mag = cap * mag / (cap + mag)

            modifiedImageArray[x, y, 0:3] = magnifyIntensity(modifiedImageArray[x, y, 0:3], mag)

    return modifiedImageArray


def polarCoords(dx, dy):
        return (math.sqrt(dx**2 + dy**2), math.atan2(dy, dx))

def cartCoords(r, th):
    return (r*math.cos(th), r*math.sin(th))


def averageColor(imageArray):
    aveColor = (0, 0, 0)
    imageWidth = len(imageArray)
    imageHeight = len(imageArray[0])
    for x in range(imageWidth):
        for y in range(imageHeight):
            aveColor += imageArray[x, y, 0:3]
    for color in range(2):
        aveColor[color] /= imageWidth*imageHeight
    return aveColor

def getPixel(imageArray, x, y, oobColor = (0, 0, 0)):
    try:
        return imageArray[math.floor(x), math.floor(y), 0:3]
    except:
        return oobColor

def magnifyIntensity(pixel, mag):
    for color in range(3):
        if pixel[color] * mag > 255:
            pixel[color] = 255
        else:
            pixel[color] *= mag
    return pixel


