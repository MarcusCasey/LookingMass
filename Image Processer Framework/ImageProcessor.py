#!/usr/bin/env python3
#!/usr/bin/env python2

from metadata import *
from PIL import Image as PIL_Image #needed as we now have multiple libraries that use "Image"
import numpy as np
import math

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

class MyPopup(FloatLayout):
    title = "Default Title"
    def __init__(self, title):
        FloatLayout.__init__(self)
        self.title = title
    def show(self):
        self.popup = Popup(title=self.title, content=self, size_hint=(None,None),size=(500,500))
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

def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

def polarCoords(dx, dy):
        return (math.sqrt(dx**2 + dy**2), math.atan2(dy, dx))

def cartCoords(r, th):
    return (r*math.cos(th), r*math.sin(th))

def averageColor(imageArray):
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
    try:
        return imageArray[math.floor(x), math.floor(y), 0:3]
    except:
        return oobColor

def magnifyIntensity(pixel, mag):
    for color in range(3):
        if pixel[color] * mag > 255:
            pixel[color] = 255
        else:
            pixel[color] *= mag
    return pixel

def gravLens(imageArray, centerX = 0.5, centerY = 0.5, thetaE = 0.1):
    imageWidth = len(imageArray)
    imageHeight = len(imageArray[0])
    centerX *= imageWidth
    centerY *= imageHeight
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

folderIn = "./data_input/"
folderOut = "./data_output/"
filename = "lenna_1.png"

class Widgets(Widget):

    def uploadImage(self):
        pass
        # UPLOAD IMAGE NOT IMPLEMENTED YET
        self.ids.pre_processed_image_label.opacity = 1
        self.ids.pre_processed_image.source = folderIn + filename # change to actual file path
        self.ids.pre_processed_image.opacity = 1
        self.ids.post_processed_image_label.opacity = 0
        self.ids.post_processed_image.opacity = 0
    
    def load(self, filename):
        try:
            self.imageArray = np.array(PIL_Image.open(filename))
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
        success = self.load(folderIn + filename) # change to actual file path
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
        modifiedImageArray = gravLens(self.imageArray, 0.4, 0.4, 0.15)

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

    def Save():
        pass


class MyApp(App):
    def build(self):
        self.title = 'Looking Mass'
        Window.bind(on_request_close=self.on_request_close)
        return Widgets()

    def on_request_close(self, *args):
        self.ExitPopup(title = "Exit", text = "Are you sure you want to exit? Unsaved work may be lost.")
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

