"""The class that holds the metadata needed for Looking Mass.

This file contains the class that is need to hold the physics and
file I/O metadata for Looking Mass.

  Typical usage example:

  massofGS = 0.6
  distanceOtoS = 0.8
  distanceOtoI = 0.3
  arcwidthOfImage = 1.0
  inDirectory = '/user/desktop/input_images'
  inFilename = 'input_image.jpg'
  outDirectory = '/user/desktop/output_images'
  outFilename = 'output_image.jpg'
  pixelCoordinates = (44,89)
  saveCoordinate = True
  batchProcessing = False
"""

class physicsMetadata:
    """Holds attributes of metadata.

    This class holds the the attributes for the physics and file I/O metadata 
    needed for Looking Mass.

    Attributes:
    
        massofGS: float that holds the mass of the gravitational lensing source.
        distanceOtoS: float that holds the destance of the observer from the    
            graviational lensing source
        distanceOtoI: float that holds the distance from the observer to the 
            image.
        arcwidthOfImage: float that holds the arcwidth of the image
        inDirectory: String that holds the path to the directory of the input 
            image.
        inFilename: String that hods the name of the input image.
        outDirectory: String that holds the path to the directory of the output 
            image.
        outFilename: String that hods the name of the output image.
        pixelCoordinates: Integer pair that holds the pixel coordinates of 
            where the gravitational lensing will be produced
        saveCoordinate: Boolean that determines whether or not the coordinates 
            will be saved. 
        batchProcessing: Boolean that determines whether or not all images in 
            the currently selected image's directory will also be processed.

    """
    # Mass of the Gravitational Source (in millions of solar masses)
    # 4
    massofGS = 0.0

    # Distance from Observer to Source (in millions of lightyears)
    # 2.5
    distanceOtoS = 0.0

    # Distance from Observer to Image (in millions of lightyears)
    # 5
    distanceOtoI = 0.0

    # the arcwidth of the image (in arcseconds)
    # 1
    arcwidthOfImage = 0.0

    # Source directory of image from User
    inDirectory = ' '

    # Name of source image from User
    inFilename = ' '

    # Destination directory of image from User
    outDirectory = ' '

    # Name of destination image from User
    outFilename = ' '

    # Pixel Coordinates associated with gravitaional lensing
    pixelCoordinates = (0,0)

    saveCoordinate = False

    # determines whether the image processor will perform batch processing
    batchProcessing = False


