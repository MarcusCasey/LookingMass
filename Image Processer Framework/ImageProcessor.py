#!/usr/bin/env python3
#!/usr/bin/env python2

from metadata import *
from PIL import Image as PIL_Image #needed as we now have multiple libraries that use "Image"
import numpy as np

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image as Kivy_Image
import kivy.properties as ObjectP
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.app import App
import kivy
kivy.require('1.11.1')  # replace with your current kivy version !

class TestBox(BoxLayout):
    pass

class FCTest(App):
    pass

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
import kivy.properties as ObjectP
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput
from kivy.base import EventLoop

class MyPopup(FloatLayout):
    defaultText = "Default text"
    defaultTitle = "Default title"
    def __init__(self, text = defaultText, title = defaultTitle):
        self.text = text
        FloatLayout.__init__(self)
        self.title = title
    def show(self):
        self.popup = Popup(content=self, title = self.title, size_hint=(None,None), size=(400,400))
        self.popup.open()
    def end(self):
        self.popup.dismiss()
    def getText(self):
        return self.text

class MetadataEntryPopup(MyPopup):
    defaultTitle = "Metadata Entry"

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
       
    def __init__(self, text, title = defaultTitle):
        MyPopup.__init__(self, text, title)

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
    defaultTitle = "Image Processing has Begun"
    def __init__(self, text, title = defaultTitle):
        MyPopup.__init__(self, text, title)
    pass

class ImageProcessingEndPopup(MyPopup):
    defaultTitle = "Image Processing has Ended"
    def __init__(self, text, title = defaultTitle):
        MyPopup.__init__(self, text, title)
    pass

class ErrorPopup(MyPopup):
    defaultTitle = "An Error has Occurred"
    def __init__(self, text, title = defaultTitle):
        MyPopup.__init__(self, text, title)
    pass

def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

class Widgets(Widget):

    unsavedData = False

    def uploadImage(self):
        pass
        # UPLOAD IMAGE NOT IMPLEMENTED YET
        self.ids.pre_processed_image_label.opacity = 1
        self.ids.pre_processed_image.source = './data_input/lenna_1.png' # change to actual file path
        self.ids.pre_processed_image.opacity = 1
        self.ids.post_processed_image_label.opacity = 0
        self.ids.post_processed_image.opacity = 0
    
    def load(self, filename):
        try:
            self.imageArray = np.array(Image.open(filename))
            return True
        except Exception as error:
            self.errorPopup = ErrorPopup(text="Error in reading file:\n" + type(error).__name__ + ":\n" + error.__str__());
            self.errorPopup.show()
            return False

    def save(self, filename):
        try:
            self.pil_img.save(filename)
            return True
        except Exception as error:
            self.errorPopup = ErrorPopup(text="Error in writing file:\n" + type(error).__name__ + ":\n" + error.__str__());
            self.errorPopup.show()
            return False
        pass
    
    def loadImage(self):
        success = self.load("./data_input/lenna_1.png") # change to actual file path
        if not success:
            return

    def saveImage(self):
        self.pil_img = Image.fromarray(self.imageArray2)
        self.save("./data_output/red.png") # change to actual file path
        self.unsavedData = False

    def processImage(self):
        self.startPopup = ImageProcessingStartPopup("Image Processor")
        self.startPopup.show()
        
        # IMAGE PROCESSING CODE HERE

        
        self.imageArray2 = self.imageArray.copy()
        self.imageArray2[:, :, (1, 2)] = 0

        self.unsavedData = True

        file_in = "./data_input/lenna_1.png" # change to actual file path
        image = np.array(PIL_Image.open(file_in))

        red = image.copy()
        red[:, :, (1, 2)] = 0

        pil_img = PIL_Image.fromarray(red)
        file_out = "./data_output/red.png" # change to actual file path
        pil_img.save(file_out)


        self.ids.post_processed_image_label.opacity = 1
        self.ids.post_processed_image.source = './data_output/red.png' # change to actual file path
        self.ids.post_processed_image.opacity = 1

        self.startPopup.end()
        self.endPopup = ImageProcessingEndPopup("Image Processor")
        self.endPopup.show()

    def requestMetadata(self):
        self.metaPopup = MetadataEntryPopup("Metadata")
        self.metaPopup.show()


class MyApp(App):
    def build(self):
        self.title = 'Looking Mass'
        Window.bind(on_request_close=self.on_request_close)
        self.widget = Widgets()
        return self.widget

    def on_request_close(self, *args):
        if(self.widget.unsavedData):
            self.ExitPopup(title = "Exit", text = "Are you sure you want to exit? Unsaved work may be lost.")
        else:
            self.stop()
        return True

    def ExitPopup(self, title='', text=''):
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text=text))
        button1 = Button(text='Yes')
        button2 = Button(text='No')
        box.add_widget(button1)
        box.add_widget(button2)
        popup = Popup(title=title, content=box, size_hint=(None, None), 
                                    size=(600, 200), auto_dismiss=False)
        button1.bind(on_release=self.stop)
        button2.bind(on_release=popup.dismiss)
        popup.open()

if __name__ == "__main__":
    MyApp().run()
    # FCTest().run()

