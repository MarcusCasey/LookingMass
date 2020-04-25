from metadata import *

import os
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ListProperty, BooleanProperty

loadMetadata = physicsMetadata()

POPUPSIZE = (500,500)
PIXELCOORD = (0,0)

class MyPopup(FloatLayout):
    title = "Default Title"

    def __init__(self, title):
        FloatLayout.__init__(self)
        self.title = title
    def show(self):
        self.popup = Popup(title=self.title, content=self, size_hint=(None,None),size=POPUPSIZE)
        self.popup.open()
    def end(self):
        self.popup.dismiss()

class MetadataEntryPopup(MyPopup):
    Metadata1 = ObjectProperty()
    Metadata2 = ObjectProperty()
    Metadata3 = ObjectProperty()

    data1 = ObjectProperty()
    data2 = ObjectProperty()
    data3 = ObjectProperty()
   
    def store_metadata(self):
        data1 = self.Metadata1
        data2 = self.Metadata2
        data3 = self.Metadata3
        print("Saving metadata")
        self.save()
        print("Resetting metadata")
        self.data1 = ''
        self.data2 = ''
        self.data3 = ''
        print("Loading metadata")
        self.load()

    def save(self):
        with open("physics_metadata.txt", "w") as fout:
            fout.write(str(self.data1) + str(';'))
            fout.write(str(self.data2) + str(';'))
            fout.write(str(self.data3) + str(';'))
    
    def load(self):
        with open("physics_metadata.txt") as fin:
            for each_line in fin:
                loaddata = each_line
                splitdata = loaddata.split(";")
                loadMetadata.massofGS = splitdata[0]
                loadMetadata.distanceOtoS = splitdata[1]
                loadMetadata.distanceOtoI = splitdata[2]
                
    pass

class FileSelector(Popup):
    filters = ListProperty()
    path = StringProperty()
    source = StringProperty()

    def saveSelection(self, selection = ' '):
        directory, filename = os.path.split(selection)
        directory += os.sep
        self.onSelection(directory, filename)

    def __init__(self, onSelection, **var):
        self.filters = var['filters']
        self.path = var['path']
        self.onSelection = onSelection
        super().__init__(**var)

class ErrorPopup(MyPopup):
    def __init__(self, text, title = "An Error has Occurred"):
        super().__init__(title = title)
        self.ids.error_label.text = text
    pass

class ImageProcessingStartPopup(MyPopup):
    pass

class ImageProcessingEndPopup(MyPopup):
    pass

class CoordinateSelectorPopup(MyPopup):
    def savePixel(self):
        loadMetadata.saveCoordinate = True
    pass