from popup import *
from gravLens import *

from PIL import Image as PIL_Image #needed as we now have multiple libraries that use "Image"
import numpy as np
from kivy.core.window import Window
from kivy.uix.widget import Widget
import os

folderIn = os.getcwd()
folderOut = "./data_output/"
filename = "hubbledeepspace.jpg"

class Widgets(Widget):

    def uploadImage(self):
        self.startPopup = LoadDialog(filters = '', path = folderIn)
        self.startPopup.open()
        # def on_mouse_pos(self, pos):

    def showImage(self):
        pass
        # UPLOAD IMAGE NOT IMPLEMENTED YET
        self.ids.pre_processed_image_label.opacity = 1
        self.ids.pre_processed_image.source = loadMetadata.sourceFile # change to actual file path
        self.ids.pre_processed_image.opacity = 1
        self.ids.post_processed_image_label.opacity = 0
        self.ids.post_processed_image.opacity = 0
    
    def load(self, filename):
        try:
            self.imageArray = np.array(PIL_Image.open(filename))
            return True
        except Exception as error:
            self.errorPopup = ErrorPopup(text="Error in reading file:\n" + type(error).__name__ + ":\n" + error.__str__())
            self.errorPopup.show()
            return False

    def save(self, filename):
        try:
            self.pil_img.save(filename)
            return True
        except Exception as error:
            self.errorPopup = ErrorPopup(text="Error in writing file:\n" + type(error).__name__ + ":\n" + error.__str__())
            self.errorPopup.show()
            return False
        pass
    
    def loadImage(self):
        success = self.load(loadMetadata.sourceFile) # change to actual file path
        if not success:
            return

    def saveImage(self):
        self.pil_img = PIL_Image.fromarray(self.imageArray2)
        self.save(folderOut + filename) # change to actual file path
        self.unsavedData = False

    def processImage(self):
        self.startPopup = ImageProcessingStartPopup("Image Processor")
        self.startPopup.show()

        # IMAGE PROCESSING CODE HERE
        self.loadImage()
        modifiedImageArray = gravLens(self.imageArray, loadMetadata.pixelCoordinates[1], loadMetadata.pixelCoordinates[0], 0.15)

        pil_img = PIL_Image.fromarray(modifiedImageArray)
        file_out = folderOut + filename # change to actual file path
        pil_img.save(file_out)

        self.ids.post_processed_image_label.opacity = 1
        self.ids.post_processed_image.source = file_out # change to actual file path
        self.ids.post_processed_image.opacity = 1
        self.startPopup.end()
        self.endPopup = ImageProcessingEndPopup("Image Processor")
        self.endPopup.show()

    def requestMetadata(self):
        self.metaPopup = MetadataEntryPopup("Metadata")
        self.metaPopup.show()

    def GravLens_Generator(self):
        self.startPopup = GravLens_GeneratorPopup("Lensing Coordinate Entry")
        self.startPopup.show()
        imageSize = self.startPopup.ids.GravLens_Image.size
        
        def on_mouse_pos(self, pos): # move the zero right 15 and down 5
            newWindowSize = ( (Window.size[0] - imageSize[0])//2, (Window.size[1] - imageSize[1])//2 + imageSize[1])
            newOrigin = (int(pos[0] - newWindowSize[0] - 15), int(newWindowSize[1] - pos[1] - 2))
            # print(pos)
            # print(Window.size)
            # print(POPUPSIZE)
            # print(newWindowSize)
            if newOrigin[0] >= 0 and newOrigin[1] >= 0 and newOrigin[0] + 30 <= imageSize[0] and newOrigin[1] + 2 <= imageSize[1]:
                # print(newOrigin)
                if(loadMetadata.saveCoordinate == True):
                    loadMetadata.pixelCoordinates = (2 * newOrigin[0], 2 * newOrigin[1])
                    loadMetadata.saveCoordinate = False
                # print(loadMetadata.pixelCoordinates)
            
        # self.startPopup.ids.GravLens_Image.PixelCoord = PixelCoord
        Window.bind(mouse_pos = on_mouse_pos)
        self.startPopup.ids.GravLens_Image.source = loadMetadata.sourceFile # change to actual file path      
   

