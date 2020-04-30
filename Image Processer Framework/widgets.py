"""The classes and functions necessary to implment the main functionality of 
the GUI of Looking Mass.

This file has the main class and functions that have direct control over the 
GUI. Widgets create buttons that allow the user to click upon. Once clicked a 
popup will be called and open allowing the user to further interact with the 
interface. Creating new buttons through popup.py and the constraints through my.
kv. 

  Typical usage example:

  self.startPopup = popupName(filters = '', path = folderIn, onSelection =   self.sourceSelected)
  self.startPopup.open()
"""

from popup import *
from gravLens import *

# needed as we now have multiple libraries that use "Image"
from PIL import Image as PIL_Image
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
    """Holds all the interface functions.

    This class will inherit from Kivy's Widget class. It creates the main 
    interface the user is able to see and interact with.

    Attributes:

        self.startPopup: A popup when called is created and opened.
        self.ids: Refers to the id set in my.kv mainly used as get or set.
    """

    # Launches a file selector popup.
    def selectSource(self):
        """Starts the file selector popup.

        This will open a popup that will let the user choose a directory and 
        load in an image. Once loaded it will then call sourceSelected and 
        close the popup.

        Args:

            self: Variable refering to the class this function is a part of
                (Widgets).
            self.startPopup.open(): Opens the popup by inheriting from the
                Popup class through LoadDialog.
        """
        self.startPopup = LoadDialog(filters='', path=folderIn, onSelection=self.sourceSelected)
        self.startPopup.open()

    # Called when the source is selected
    def sourceSelected(self, directory, filename):
        """Displays the image when a file is selected.

        Once a file is selected, sourceSelected is called from selectSource and 
        opens the image chosen by the user in the interface. It will save the 
        path for the filename and directory in the metadata class imported 
        through popup.

        Args:

            self: Variable refering to the class this function is a part of
                (Widgets).
            directory: A string containing the loaded images root file
                directory.
            filename: A string containing the loaded images file name.
        """
        loadMetadata.inDirectory = directory
        loadMetadata.inFilename = filename
        #print("Source file selected: " + directory + filename)
        self.showPreImage()

    def selectDestination(self):
        """Starts Select Destination pop up.

        This will open a popup allowing the user to select a destination folder 
        and filename to save the doctored images created through the program.

        Args:

            self: Variable refering to the class this function is a part of
                (Widgets).
        """
        self.startPopup = SaveDialog(filters='', path=folderOut)
        self.startPopup.open()

    # Called when the destination is selected
    def destinationSelected(self, directory, filename):
        """Displays the image once its processed and selected.

        This will open a popup allowing the user to select a destination folder 
        and filename to save the doctored images created through the program.

        Args:

            self: Variable refering to the class this function is a part of
                (Widgets).
            directory: A string containing the loaded images root file
                directory.
            filename: A string containing the loaded images file name.
        """
        loadMetadata.outDirectory = directory
        loadMetadata.outFilename = filename
        #print("Destination file selected: " + directory + filename)
        self.showPostImage()

    # Displays the image selected in self.uploadImage().
    def showPreImage(self):
        """Sets the input image information so it can display properly through 
        my.kv.

        This calls directly to my.kv using id's to set information needed to 
        display the input image.

        Args:

            self: Variable refering to the class this function is a part of
                (Widgets).
            self.ids: Variable that can call my.kv id's for the given popups.
        """
        self.ids.pre_processed_image_label.opacity = 1
        self.ids.pre_processed_image.source = loadMetadata.inDirectory + loadMetadata.inFilename
        self.ids.pre_processed_image.opacity = 1

    # Displays the modified image.
    def showPostImage(self, outDirectory, outFilename):
        """Sets the output image information so it can display properly through 
        my.kv.

        This calls directly to my.kv using id's to set information needed to 
        display the output image.

        Args:

            self: Variable refering to the class this function is a part of
                (Widgets).
            self.ids: Variable that can call my.kv id's for the given popups.
            outDirectory: A string that is for saving and outputting the
                directory in the metadata class.
            outFilename: A string that is for saving and outputting the 
                filename in the metadata class.
        """
        print("showing")
        self.ids.post_processed_image_label.opacity = 1
        self.ids.post_processed_image.source = outDirectory + outFilename

        self.ids.post_processed_image.opacity = 1
        self.ids.post_processed_image.reload()

    # Loads the requested file and stores it as a numpy array of pixels (format 
    # may vary).
    # There is an error popup in case of exceptions.
    # Returns a boolean signifying success.
    def load(self, filename):
        """Error Handler for loading in the image.

        This checks to see if the image filename can be found. If it is then it 
        will load the image into a PIL image and then return true. If not found 
        then it will output an error and show a popup for it.

        Args:

            self: Variable refering to the class this function is a part of
                (Widgets).
            filename: A string containing the loaded images file name.

        Raises:

            errorPopup: An error occured opening the input filename. A popup
                will open prompting the user.
        """
        try:
            self.imageArray = np.array(PIL_Image.open(filename))
            return True
        except Exception as error:
            self.errorPopup = ErrorPopup(
                text="Error in reading file:\n" + type(error).__name__ + ":\n" + error.__str__())
            self.errorPopup.show()
            return False

    # Saves the modified image into the requested file.
    # There is an error popup in case of exceptions.
    # Returns a boolean signifying sucess.
    def save(self, filename):
        """Error Handler for loading in the image.

        This checks to see if the image filename can be found. If it is then it 
        will load the image into a PIL image and then return true. If not found 
        then it will output an error and show a popup for it.

        Args:

            self: Variable refering to the class this function is a part of
                (Widgets).
            filename: A string containing the loaded images file name.

        Returns:

            A boolean value true of false determined by if the filename was 
            able to be saved.

        Raises:

            errorPopup: An error occured opening the output filename. A popup
                will open prompting the user.
        """
        try:
            self.modifiedImage.save(filename)
            return True
        except Exception as error:
            self.errorPopup = ErrorPopup(
                text="Error in writing file:\n" + type(error).__name__ + ":\n" + error.__str__())
            self.errorPopup.show()
            return False
        pass

    # Requests loading of data using the the stored filename.
    # This function is called by self.processImage().
    def loadImage(self, inDirectory, inFilename):
        """Sets the input image information so it can display properly through 
        my.kv.

        This calls directly to my.kv using id's to set information needed to 
        display the output image.

        Args:

            self: Variable refering to the class this function is a part of
                (Widgets).
            inDirectory: A string that is for saving and inputting the
                directory in the metadata class.
            inFilename: A string that is for saving and inputting the 
                filename in the metadata class.
        """
        success = self.load(inDirectory + inFilename)
        self.imageLoaded = success

    # Requests saving of data.
    # This function is called by self.processImage().
    def saveImage(self, outDirectory, outFilename):
        """Sets the output image information so it can display properly through 
        my.kv.

        This calls directly to my.kv using id's to set information needed to 
        display the output image.

        Args:

            self: Variable refering to the class this function is a part of
                (Widgets).
            outDirectory: A string that is for saving and outputting the
                directory in the metadata class.
            outFilename: A string that is for saving and outputting the 
                filename in the metadata class.
        """
        print("saveImage(): " + outDirectory + outFilename)
        success = self.save(outDirectory + outFilename)
        if success:
            self.unsavedData = False

    def test(self):
        print("test")
    # MDS = Modify, Display, Save
    # This function is completed in a separate thread.

    def MDS(self):
        """This function is responsible for calling the appropriate image 
        porcessing, making the program display the modified image, and saving 
        the image. This function is meant to be called in a separate thread as 
        to not lock up the main program during its (prolonged) execution.
        
        Args:
            
            self: Variable refering to the class this function is a part of
                (Widgets).

        Raises:

            error: An error occured when trying to process an image.
        """

        # The magic constant is derived from the equation for the Einstein ring radius, with the units assumed to be in millions of solar masses, millions of light years, and arcseconds.
        M = float(loadMetadata.massofGS)
        D_OS = float(loadMetadata.distanceOtoS)
        D_OI = float(loadMetadata.distanceOtoI)
        D_SI = D_OI - D_OS
        arcwidth = float(loadMetadata.arcwidthOfImage)
        thE = 0.11526 * math.sqrt(M * D_SI / (D_OS * D_OI)) / arcwidth

        if (loadMetadata.batchProcessing == False):
            try:
                self.imageLoaded = False
                self.loadImage(loadMetadata.inDirectory,
                               loadMetadata.inFilename)
                if self.imageLoaded:
                    self.modifiedImageArray = gravLens(
                        self.imageArray, loadMetadata.pixelCoordinates[1], loadMetadata.pixelCoordinates[0], thE) 
                    self.modifiedImage = PIL_Image.fromarray(
                        self.modifiedImageArray)
                    self.saveImage(loadMetadata.outDirectory,
                                   loadMetadata.outFilename)
                    self.startPopup.end()
            except Exception as error:
                self.startPopup.end()
                self.errorPopup = ErrorPopup(
                    text="Error in processing image:\n" + type(error).__name__ + ":\n" + error.__str__())
                self.errorPopup.show()
            else:
                if self.imageLoaded:
                    def on_dismiss(instance):
                        self.showPostImage(
                            loadMetadata.outDirectory, loadMetadata.outFilename)
                    box = BoxLayout(orientation='vertical')
                    box.add_widget(Label(text="Process Finished."))
                    button = Button(text='Okay')
                    box.add_widget(button)
                    self.endPopup = Popup(title="Image Processor", content=box, size_hint=(None, None),
                                                size=(600, 200))
                    button.bind(on_release=self.endPopup.dismiss)
                    self.endPopup.bind(on_dismiss=on_dismiss)
                    self.endPopup.open()
        else:
            imageList = os.listdir(loadMetadata.inDirectory)
            count = 1
            for i in imageList:
                print(i)
                try:
                    self.imageLoaded = False
                    self.loadImage(loadMetadata.inDirectory, i)
                    if self.imageLoaded:
                        self.modifiedImageArray = gravLens(
                            self.imageArray, loadMetadata.pixelCoordinates[1], loadMetadata.pixelCoordinates[0], 0.15)
                        self.modifiedImage = PIL_Image.fromarray(
                            self.modifiedImageArray)
                        temp = 'b' + str(count) + '_' + \
                            loadMetadata.outFilename
                        count = count + 1
                        print("batch: " + temp)
                        self.saveImage(loadMetadata.outDirectory, temp)
                        self.startPopup.end()
                except Exception as error:
                    self.startPopup.end()
                    self.errorPopup = ErrorPopup(
                        text="Error in processing image:\n" + type(error).__name__ + ":\n" + error.__str__())
                    self.errorPopup.show()
                else:
                    if self.imageLoaded:
                        def on_dismiss(instance):
                            self.showPostImage(loadMetadata.outDirectory, temp)

            box = BoxLayout(orientation='vertical')
            box.add_widget(Label(text="Process Finished."))
            button = Button(text='Okay')
            box.add_widget(button)
            self.endPopup = Popup(title="Image Processor", content=box, size_hint=(None, None),
                                  size=(600, 200))
            button.bind(on_release=self.endPopup.dismiss)
            self.endPopup.bind(on_dismiss=on_dismiss)
            self.endPopup.open()

    # Responsible for processing the image when the user requests such from the 
    # main GUI.
    # This function both loads the file selected from self.uploadImage() using 
    # self.loadImage()
    # and saves it upon completion using self.saveImage().

    def processImage(self):
        """Once image processing is selected it will display a popup.

        This function begins the prompt to tell the user processing has begun. 
        It will call mds which will push the processing onto a seperate thread.

        Args:

            self: Variable refering to the class this function is a part of
                (Widgets).
        """
        self.startPopup = ImageProcessingStartPopup("Image Processor")
        self.startPopup.bind(on_dismiss=self.test)
        self.startPopup.show()
        mds = threading.Thread(target=self.MDS, args=(), daemon=True)
        mds.start()

    # Display the popup where users can enter metadata.

    def requestMetadata(self):
        """Prompt for user entry on Metadata.

        This function calls the MetadataEntryPopup and prompts the user to fill 
        out additional information about the input image.

        Args:

            self: Variable refering to the class this function is a part of
                (Widgets).
        """
        self.metaPopup = MetadataEntryPopup("Enter Metadata")
        self.metaPopup.ids.Metadata1 = "asdfasdf"
        self.metaPopup.show()

    # Display the popup where users can select the coordinates using a GUI.
    def selectCoordinates(self):
        """Prompt for user to fill out the placement for gravitational lensing 
        on the input image.

        This function will call the coordinateSelectorPopup and prompt the 
        user. It also stores the size of the image for later calculations.

        Args:
        
            self: Variable refering to the class this function is a part of
                (Widgets).
            imageSize: A integer value that stores the size of the image in
                terms of height and width.
        """
        self.coordPopup = CoordinateSelectorPopup("Lensing Coordinate Entry")
        self.coordPopup.ids.GravLens_Image.source = loadMetadata.inDirectory + \
            loadMetadata.inFilename
        self.coordPopup.show()
        imageSize = self.coordPopup.ids.GravLens_Image.size

        def on_mouse_pos(self, pos):  # move the zero right 15 and down 5
            """Tells the user their exact mouse position on the interface.

            This function calculates the image position on the current popup by 
            taking the size of the entire window and subtracting it from the 
            popup size divided by 2, since its centered on the window. Then it 
            will subtract that current value by the old value to start the 
            coordinate of the image at 0,0 in the top left corner. The value 
            then is stored once a click is obtained and multiplied by two to 
            store it into the metadata for the real image.

            Args:
            
                self: Variable refering to the class this function is a part of
                    (Widgets).
                pos: A integer value of the mouse position in the GUI.
            """
            newWindowSize = ((Window.size[0] - imageSize[0])//2,
                             (Window.size[1] - imageSize[1])//2 + imageSize[1])
            newOrigin = (int(pos[0] - newWindowSize[0] - 15),
                         int(newWindowSize[1] - pos[1] - 2))
            # print(pos)
            # print(Window.size)
            # print(POPUPSIZE)
            # print(newWindowSize)
            if newOrigin[0] >= 0 and newOrigin[1] >= 0 and newOrigin[0] + 30 <= imageSize[0] and newOrigin[1] + 2 <= imageSize[1]:
                # print(newOrigin)
                if(loadMetadata.saveCoordinate == True):
                    loadMetadata.pixelCoordinates = (
                        2 * newOrigin[0], 2 * newOrigin[1])
                    loadMetadata.saveCoordinate = False
                    setNewPixel()
                # print(loadMetadata.pixelCoordinates)

        def setNewPixel():
            self.coordPopup.ids.PixelCoord1.text = str(loadMetadata.pixelCoordinates)

        # self.coordPopup.ids.GravLens_Image.PixelCoord = PixelCoord
        Window.bind(mouse_pos=on_mouse_pos)
        self.coordPopup.ids.GravLens_Image.source = loadMetadata.inDirectory + \
            loadMetadata.inFilename
