"""The classes and functions necessary to implement the pop ups of Looking Mass.

This file contains the classes and functions that implment the pop ups of 
Looking Mass. It includes the class MyPopup which serves as a template that 
several other pop up classes inherit from. The other classes implement pop ups 
for metadata entry, loading images, saving images, errors, image processing 
start, image processing stop, and coordinate selection.

  Typical usage example:

  self.metaPopup = MetadataEntryPopup("Enter Metadata")
  self.ExitPopup(title = "Title Text", text = "Contents Text")
  self.startPopup = LoadDialog(filters='', path=folderIn, onSelection=self.sourceSelected)
  self.startPopup = SaveDialog(filters='', path=folderOut)
  self.errorPopup = ErrorPopup(text="Error in reading file:\n" + type(error).__name__ + ":\n" + error.__str__())
  self.startPopup = ImageProcessingStartPopup("Image Processor")
  self.endPopup = ImageProcessingEndPopup("Image Processor")
  self.coordPopup = CoordinateSelectorPopup("Lensing Coordinate Entry")

"""

from metadata import *

import os
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from kivy.uix.switch import Switch
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ListProperty, BooleanProperty

loadMetadata = physicsMetadata()

class MyPopup(FloatLayout):
    """Holds methods and attributes for pop ups in Looking Mass.

    This class inherits from Kivy's FloatLayout class and serves as a template 
    for several other pop up classes in Looking Mass. It contains the methods 
    to intialize, show, and remove a pop up.

    Attributes:

        title: A string indicating the title of the pop up.
        self.popup: Contains the attributes of the Popup class it inherits from.
    """

    title = "Default Title"

    def __init__(self, title):
        """Initializes MyPopup.

        This function initializes the classs MyPopup. It does so by
        setting the title attribute and calling the initialization 
        function.

        Args:

            self: Variable refering to the class this function is a part of
                (MyPopup).
            title: String containing the title of the pop up.

        """
        FloatLayout.__init__(self)
        self.title = title

    def show(self):
        """Shows pop up.

        This function shows the popup created from the MyPopup class. It does 
        so by contstructing and opening the pop up.

        Args:

            self: Variable refering to the class this function is a part of
                (MyPopup).

        """
        self.popup = Popup(title=self.title, content=self, size_hint=(None,None),size=(500,500))
        self.popup.open()

    def end(self):
        """Removes pop up.

        This function removes the popup created from the MyPopup class. It does so by dismissing the pop up.

        Args:

            self: Variable refering to the class this function is a part of
                (MyPopup).

        """
        self.popup.dismiss()

class MetadataEntryPopup(MyPopup):
    """Holds methods and attributes for pop ups in Looking Mass.

    This class inherits from Kivy's FloatLayout class and serves as a template 
    for several other pop up classes in Looking Mass. It contains the methods 
    to intialize, show, and remove a pop up.

    Attributes:

        Metadata1: Holds metadata temorarily.
        Metadata2: Holds metadata temorarily.
        Metadata3: Holds metadata temorarily.
        data1: holds the metadata of the first entry field
        data2: holds the metadata of the second entry field
        data3: holds the metadata of the third entry field
    """
    Metadata1 = ObjectProperty()
    Metadata2 = ObjectProperty()
    Metadata3 = ObjectProperty()
    Metadata4 = ObjectProperty()


    data1 = ObjectProperty()
    data2 = ObjectProperty()
    data3 = ObjectProperty()
    data4 = ObjectProperty()

   
    def store_metadata(self):
        """Stores metadata.

        This function stores the metadata entered by the user.

        Args:

            self: Variable refering to the class this function is a part of
                (store_metadata).

        """
        data1 = self.Metadata1
        data2 = self.Metadata2
        data3 = self.Metadata3
        data4 = self.Metadata4
        print("Saving metadata")
        self.save()
        print("Resetting metadata")
        self.data1 = ''
        self.data2 = ''
        self.data3 = ''
        self.data4 = ''
        print("Loading metadata")
        self.load()

    def save(self):
        """Saves metadata.

        This function saves the metadata entered by the user to a text file.

        Args:

            self: Variable refering to the class this function is a part of
                (store_metadata).

        """
        with open("physics_metadata.txt", "w") as fout:
            fout.write(str(self.data1) + str(';'))
            fout.write(str(self.data2) + str(';'))
            fout.write(str(self.data3) + str(';'))
            fout.write(str(self.data4) + str(';'))
    
    def load(self):
        """Loads metadata.

        This function loads the metadata entered by the user from a text file.

        Args:

            self: Variable refering to the class this function is a part of
                (store_metadata).

        """
        with open("physics_metadata.txt") as fin:
            for each_line in fin:
                loaddata = each_line
                splitdata = loaddata.split(";")
                loadMetadata.massofGS = splitdata[0]
                loadMetadata.distanceOtoS = splitdata[1]
                loadMetadata.distanceOtoI = splitdata[2]
                loadMetadata.arcwidthOfImage = splitdata[3]

    # checks if batch processing switch is on or off
    def switch_callback(self, switchObject, switchValue): 
        """Checks batch processing switch.

        This function checks whether or not the batch processing switch was 
        changed and updates the corresponding boolean accordingly.

        Args:

            self: Variable refering to the class this function is a part of
                (store_metadata).
            switchObject: Variable representing the switch itself
            switchValue: Variable representing the value of the switch.

        """
        if(switchValue): 
            #print('Switch is ON') 
            loadMetadata.batchProcessing = True
        else: 
            #print('Switch is OFF') 
            loadMetadata.batchProcessing = False

    pass

class LoadDialog(Popup):
    """Load Image Popup.

    This class inherits from Kivy's Popup class. It is the opens a popup 
    allowing the user to open and store the filenames and directories of an 
    image for later use. 

    Attributes:

        title: A string indicating the title of the pop up.
        self.popup: Contains the attributes of the Popup class it inherits
            from.
    """
    
    filters = ListProperty()
    path = StringProperty()
    source = StringProperty()

    def saveSelection(self, selection = ' '):
        """Saves the filename and directory of the chosen image.

        This function will store the information into the metadata class. Which 
        is then reused at a later point. 

        Args:

            self: Contains the attributes of the LoadDialog class it inherits
                from.
            selection: A string indicating directory and filename.

        """
        directory, filename = os.path.split(selection)
        directory += os.sep
        loadMetadata.inDirectory = directory
        loadMetadata.inFilename = filename
        # print("saveSelection(): " + loadMetadata.inDirectory)
        # print("saveSelection(): " + loadMetadata.inFilename)
        self.onSelection(directory, filename)


    def __init__(self, onSelection, **var):
        """Initializes LoadDialog.

        This function initializes the class LoadDialog. It does so by
        setting the title attribute and calling the initialization 
        function.

        Args:

            self: Variable refering to the class this function is a part of
                (LoadDialog).
            onSelection: A string indicating directory and filename.
        """
        self.filters = var['filters']
        self.path = var['path']
        self.onSelection = onSelection
        super().__init__(**var)

class SaveDialog(Popup):
    """Save Image Popup.

    This class inherits from Kivy's Popup class. It is the opens a popup 
    allowing the user to open and store the filenames and directories of an 
    image for later use. 

    Attributes:

        title: A string indicating the title of the pop up.
        self.popup: Contains the attributes of the Popup class it inherits
            from.
    """
    filters = ListProperty()
    path = StringProperty()
    source = StringProperty()

    def saveDestinationPath(self, destinationpath = " "):
        """Saves the directory of the chosen image.

        This function will store the information into the metadata class. Which 
        is then reused at a later point. 

        Args:

            self: Contains the attributes of the SaveDialog class it inherits
                from.
            destinationpath: A string indicating directory.
        """
        loadMetadata.outDirectory = destinationpath + "/"

    def saveDestinationName(self, destinationname = ' '):
        """Saves the filename of the chosen image.

        This function will store the information into the metadata class. Which 
        is then reused at a later point. 

        Args:

            self: Contains the attributes of the SaveDialog class it inherits
                from.
            destinationname: A string indicating filename.
        """
        loadMetadata.outFilename = destinationname

    def __init__(self, **var):
        """Initializes SaveDialog.

        This function initializes the class SaveDialog. It does so by
        setting the title attribute and calling the initialization 
        function.

        Args:

            self: Variable refering to the class this function is a part of
                (SaveDialog).
        """
        self.filters = var['filters']
        self.path = var['path']
        super().__init__(**var)

class ErrorPopup(MyPopup):
    """Creates error Popup.

    This class inherits from Kivy's Popup class. It is the opens a popup 
    that shows an error if something goes wrong. 

    Attributes:

        title: A string indicating the title of the pop up.
        self.ids.error_label.text: String that holds error message.
            from.
    """
    def __init__(self, text, title = "An Error has Occurred"):
        """Initializes ErrorPopup.

        This function initializes the class ErrorPopup. It does so by
        setting the title and message attributes and calling the initialization 
        function.

        Args:

            self: Variable refering to the class this function is a part of
                (SaveDialog).
        """
        super().__init__(title = title)
        self.ids.error_label.text = text
    pass

class ImageProcessingStartPopup(MyPopup):
    """Image processing start pop up.

    This class inherits from MyPopup and is a wrapper used show a pop up for 
    the start of image processing.

    """
    pass

class ImageProcessingEndPopup(MyPopup):
    """Image processing end pop up.

    This class inherits from MyPopup and is a wrapper used show a pop up for 
    the end of image processing.

    """
    pass

class CoordinateSelectorPopup(MyPopup):
    """Coordinate slector pop up.

    This class inherits from MyPopup and is a wrapper used show a pop up for 
    the end of coordinate selector.

    """
    def savePixel(self):
        '''This just saves the pixel coordinate value chosen by the user in the 
        metadata class.
        '''
        loadMetadata.saveCoordinate = True
    pass
