from metadata import *

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty, StringProperty, NumericProperty

POPUPSIZE = (500,500)
PIXELCOORD = (0,0)

class MyPopup(FloatLayout):
    title = "Default Title"

    def __init__(self, title):
        FloatLayout.__init__(self)
        self.title = title
    def show(self):
        self.popup = Popup(title=self.title, content=self, size_hint=(None,None),size= POPUPSIZE)
        self.popup.open()
    def end(self):
        self.popup.dismiss()

class MetadataEntryPopup(MyPopup):
    Metadata1 = ObjectProperty()
    Metadata2 = ObjectProperty()
    Metadata3 = ObjectProperty()
    Metadata4 = ObjectProperty()
    Metadata5 = ObjectProperty()

    data1 = ObjectProperty()
    data2 = ObjectProperty()
    data3 = ObjectProperty()
    data4 = ObjectProperty()
    data5 = ObjectProperty()

    def store_metadata(self):
        data1 = self.Metadata1
        data2 = self.Metadata2
        data3 = self.Metadata3
        data4 = self.Metadata4
        data5 = self.Metadata5
        print("Saving metadata")
        self.save()
        print("Resetting metadata")
        self.data1 = ''
        self.data2 = ''
        self.data3 = ''
        self.data4 = ''
        self.data5 = ''
        print("Loading metadata")
        self.load()
       


    def save(self):
        with open("physics_metadata.txt", "w") as fout:
            fout.write(str(self.data1) + str(';'))
            fout.write(str(self.data2) + str(';'))
            fout.write(str(self.data3) + str(';'))
            fout.write(str(self.data4) + str(';'))
            fout.write(str(self.data5) + str(';'))
    
    def load(self):
        with open("physics_metadata.txt") as fin:
            for each_line in fin:
                loaddata = each_line
                splitdata = loaddata.split(";")
                loadMetadata = physicsMetadata(splitdata[0], splitdata[1], 
                                               splitdata[2], splitdata[3], 
                                               splitdata[4])
    pass

class ImageProcessingStartPopup(MyPopup):
    pass

class ImageProcessingEndPopup(MyPopup):
    pass

class GravLens_GeneratorPopup(MyPopup):
    # def()
    pass
