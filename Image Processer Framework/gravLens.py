"""The implementations of the gravitational lensing
calculations for Looking Mass.

This file contains the functions that implement the gravitational lensing 
generation for Looking Mass. It includes functions to impose 
gravitational lensing on images, to convert between polar and cartesian 
coordinates, to find color averages, and change pixel values.

  Typical usage example:

  modifiedImageArray = gravLens(self.imageArray, loadMetadata.pixelCoordinates[1], loadMetadata.pixelCoordinates[0], 0.15)
  self.ExitPopup(title = "Title Text", text = "Contents Text")
  theta, t = polarCoords(dx, dy)
  dx_, dy_ = cartCoords(beta, t)
  aveColor = averageColor(imageArray)
  modifiedImageArray[x, y, 0:3] = getPixel(imageArray, dx_ + centerX, dy_ + centerY, aveColor)
  modifiedImageArray[x, y, 0:3] = magnifyIntensity(modifiedImageArray[x, y, 0:3], mag)

"""

from PIL import Image as PIL_Image # "as PIL_Image" needed as we now have multiple libraries that use "Image"
import numpy as np
import math

def gravLens(imageArray, centerX = 0.5, centerY = 0.5, thetaE = 0.1):
    """Generates gravitational lensing in an image.

        This function... 

        Args:

            imageArray: An array of pixels, assumed to be in RGB or RGBA 0-255 format
            centerX: x-coordinate center of gravlens effect, ranging 0-1
            centerY: y-coordinate center of gravlens effect, ranging 0-1
            thetaE: Einstein ring radius, expressed as a fraction of the image's smallest dimension (min of height and width)

        Returns:
            A duplicated array of pixels, with the appropriate image processing performed.
            
    """

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


def polarCoords(x, y):
        """Converts cartesian coordinates to polar coordinates.

        This function... 

        Args:

            x: Distance from the origin in the +x-direction
            y: Distance from the origin in the +y-direction

        Returns: A tuple (r, th)

            r: Radial distance from the origin
            th: Counterclockwise angle from the +x-axis, in radians
            
        """

        return (math.sqrt(x**2 + y**2), math.atan2(y, x))

def cartCoords(r, th):
    """Converts polar coordinates to cartesian coordinates.

    This function... 

    Args:

        r: Radial distance from the origin
        th: Counterclockwise angle from the +x-axis, in radians

    Returns: A tuple (x, y)

        x: Distance from the origin in the +x-direction
        y: Distance from the origin in the +y-direction
            
    """

    return (r*math.cos(th), r*math.sin(th))


def averageColor(imageArray):
    """Finds color averages.

    This function... 

    Args:

        imageArray: An array of pixels, assumed to be in RGB or RGBA

    Returns:
        
        An RGB pixel with the arithmetic mean of the RGB values of the image
            
    """

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
    """Gets image pixels.

    This function... 

    Args:

        imageArray: An array of pixels, assumed to be in RGB or RGBA
        x: The x'th pixel (floats are rounded down)
        y: The y'th pixel (floats are rounded down)
        oobColor: The pixel to return if an out-of-bounds pixel is requested

    Returns:
        
        Either a pixel chosen from the image, or oobColor

    """

    try:
        return imageArray[math.floor(x), math.floor(y), 0:3]
    except:
        return oobColor

def magnifyIntensity(pixel, mag):
    """Magnifies the intensity.

    This function... 

    Args:

        pixel: A pixel, assumed to be in RGB or RGBA, 0-255 format
        mag: Scaling factor; 1 produces no change

    Returns:
        
        The pixel, scaled by the scaling factor
            
    """
    for color in range(3):
        if pixel[color] * mag > 255:
            pixel[color] = 255
        else:
            pixel[color] *= mag
    return pixel


