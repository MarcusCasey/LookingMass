#!/usr/bin/env python3
#!/usr/bin/env python2

import kivy
kivy.require('1.11.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.factory import Factory
import kivy.properties as ObjectP

from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.button import Button 

class MyPopup(FloatLayout):
    title = "Default Title"
    def __init__(self, title):
        FloatLayout.__init__(self)
        self.title = title
    def show(self):
        self.popup = Popup(title=self.title, content=self, size_hint=(None,None),size=(400,400))
        self.popup.open()
    def end(self):
        self.popup.dismiss()

class MetadataEntryPopup(MyPopup):
    pass

class ImageProcessingStartPopup(MyPopup):
    pass

class ImageProcessingEndPopup(MyPopup):
    pass

class MetadataEntryPopup(MyPopup):
    #add method that saves text inputs to metadata class when "save" button is pressed
    Save = ObjectP.ObjectProperty(None)

class Widgets(Widget):
    def uploadImage(self):
        pass
        # UPLOAD IMAGE NOT IMPLEMENTED YET
    
    def processImage(self):
        self.startPopup = ImageProcessingStartPopup("Image Processor")
        self.startPopup.show()
        
        # IMAGE PROCESSING CODE HERE

        self.startPopup.end()
        self.endPopup = ImageProcessingEndPopup("Image Processor")
        self.endPopup.show()

    def requestMetadata(self):
        self.metaPopup = MetadataEntryPopup("Metadata")
        self.metaPopup.show()

    def Save():
        pass

class MyApp(App):
    def build(self):
        return Widgets()


if __name__ == "__main__":
    MyApp().run()