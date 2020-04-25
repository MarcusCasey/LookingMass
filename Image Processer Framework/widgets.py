from popup import *
from gravLens import *

from PIL import Image as PIL_Image #needed as we now have multiple libraries that use "Image"
import numpy as np
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import os
import threading
import time

folderIn = os.getcwd()
folderOut = "./data_output/"
filename = "hubbledeepspace.jpg"

# This class defines the main GUI and its capabilities.
# See file my.kv for the kivy layout of the components.
class Widgets(Widget):

    # Launches a file selector popup.
    def selectSource(self):
        self.startPopup = FileSelector(filters = '', path = folderIn, onSelection = self.sourceSelected)
        self.startPopup.open()

    # Called when the source is selected
    def sourceSelected(self, directory, filename):
        loadMetadata.inDirectory = directory
        loadMetadata.inFilename = filename
        #print("Source file selected: " + directory + filename)
        self.showPreImage()

    def selectDestination(self):
        self.startPopup = FileSelector(filters = '', path = folderIn, onSelection = self.destinationSelected)
        self.startPopup.open()

    # Called when the destination is selected
    def destinationSelected(self, directory, filename):
        loadMetadata.outDirectory = directory
        loadMetadata.outFilename = filename
        #print("Destination file selected: " + directory + filename)
        self.showPostImage()

    # Displays the image selected in self.uploadImage().
    def showPreImage(self):
        self.ids.pre_processed_image_label.opacity = 1
        self.ids.pre_processed_image.source = loadMetadata.inDirectory + loadMetadata.inFilename
        self.ids.pre_processed_image.opacity = 1
    
    # Displays the modified image.
    def showPostImage(self):
        print("showing")
        self.ids.post_processed_image_label.opacity = 1
        self.ids.post_processed_image.source = loadMetadata.outDirectory + loadMetadata.outFilename
        self.ids.post_processed_image.opacity = 1
        self.ids.post_processed_image.reload()

    # Loads the requested file and stores it as a numpy array of pixels (format may vary).
    # There is an error popup in case of exceptions.
    # Returns a boolean signifying success.
    def load(self, filename):
        try:
            self.imageArray = np.array(PIL_Image.open(filename))
            return True
        except Exception as error:
            self.errorPopup = ErrorPopup(text="Error in reading file:\n" + type(error).__name__ + ":\n" + error.__str__())
            self.errorPopup.show()
            return False

    # Saves the modified image into the requested file.
    # There is an error popup in case of exceptions.
    # Returns a boolean signifying sucess.
    def save(self, filename):
        try:
            self.modifiedImage.save(filename)
            return True
        except Exception as error:
            self.errorPopup = ErrorPopup(text="Error in writing file:\n" + type(error).__name__ + ":\n" + error.__str__())
            self.errorPopup.show()
            return False
        pass
    
    # Requests loading of data using the the stored filename.
    # This function is called by self.processImage().
    def loadImage(self):
        success = self.load(loadMetadata.inDirectory + loadMetadata.inFilename)
        self.imageLoaded = success

    # Requests saving of data.
    # This function is called by self.processImage().
    def saveImage(self):
        success = self.save(loadMetadata.outDirectory + loadMetadata.outFilename)
        if success:
            self.unsavedData = False
    def test(self):
        print("test")
    # MDS = Modify, Display, Save
    # This function is completed in a separate thread.
    def MDS(self):
        try:
            self.imageLoaded = False
            self.loadImage()
            if self.imageLoaded:
                self.modifiedImageArray = gravLens(self.imageArray, loadMetadata.pixelCoordinates[1], loadMetadata.pixelCoordinates[0], 0.15)
                self.modifiedImage = PIL_Image.fromarray(self.modifiedImageArray)
                self.saveImage()
                self.startPopup.end()
        except Exception as error:
            self.startPopup.end()
            self.errorPopup = ErrorPopup(text="Error in processing image:\n" + type(error).__name__ + ":\n" + error.__str__())
            self.errorPopup.show()
        else:
            if self.imageLoaded:
                def on_dismiss(instance):
                    self.showPostImage()
                box = BoxLayout(orientation='vertical')
                box.add_widget(Label(text="Process Finished."))
                button = Button(text='Okay')
                box.add_widget(button)
                self.endPopup = Popup(title="Image Processor", content=box, size_hint=(None, None), 
                                            size=(600, 200))
                button.bind(on_release=self.endPopup.dismiss)
                self.endPopup.bind(on_dismiss=on_dismiss)
                self.endPopup.open()

    # Responsible for processing the image when the user requests such from the main GUI.
    # This function both loads the file selected from self.uploadImage() using self.loadImage()
    # and saves it upon completion using self.saveImage().
    def processImage(self):
        self.startPopup = ImageProcessingStartPopup("Image Processor")
        self.startPopup.bind(on_dismiss=self.test)
        self.startPopup.show()
        mds = threading.Thread(target=self.MDS, args=(), daemon=True)
        mds.start()
            

    # Display the popup where users can enter metadata.
    def requestMetadata(self):
        self.metaPopup = MetadataEntryPopup("Metadata")
        self.metaPopup.show()

    # Display the popup where users can select the coordinates using a GUI.
    def selectCoordinates(self):
        self.coordPopup = CoordinateSelectorPopup("Lensing Coordinate Entry")
        self.coordPopup.ids.GravLens_Image.source = loadMetadata.inDirectory + loadMetadata.inFilename
        self.coordPopup.show()
        imageSize = self.coordPopup.ids.GravLens_Image.size
        
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
            
        # self.coordPopup.ids.GravLens_Image.PixelCoord = PixelCoord
        Window.bind(mouse_pos = on_mouse_pos)
        self.coordPopup.ids.GravLens_Image.source = loadMetadata.inDirectory + loadMetadata.inFilename   
   

