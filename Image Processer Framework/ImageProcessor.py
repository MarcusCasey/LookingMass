#!/usr/bin/env python3
#!/usr/bin/env python2

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
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
from kivy.properties import ObjectProperty
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


from PIL import Image
import numpy as np

class MetadataEntryPopup(FloatLayout):
    pass


class ProcessStartPopup(FloatLayout):
    OK = ObjectP.ObjectProperty(None)

    def show(self):
        self.popupWindow = Popup(
            title="Image Processor", content=self, size_hint=(None, None), size=(400, 400))
        self.popupWindow.open()

    def end(self):
        self.popupWindow.dismiss()


class ProcessEndPopup(FloatLayout):
    OK = ObjectP.ObjectProperty(None)

    def show(self):
        self.popupWindow = Popup(
            title="Image Processor", content=self, size_hint=(None, None), size=(400, 400))
        self.popupWindow.open()

    def end(self):
        self.popupWindow.dismiss()


class MetadataEntryPopup(FloatLayout):
    # add method that saves text inputs to metadata class when "save" button is pressed
    Save = ObjectP.ObjectProperty(None)


class Widgets(Widget):

    def dismiss_popup(self):
        self._popup.dismiss()

    def Upload_btn(self):
        pass
    # UPLOAD IMAGE NOT IMPLEMENTED YET

    def Process_btn(self):
        self.startPopup = ProcessStartPopup(OK=self.dismiss_popup)
        self.startPopup.show()

        # IMAGE PROCESSING CODE HERE
        file_in = "./data_input/lenna_1.png" # change to actual file path
        image = np.array(Image.open(file_in))

        red = image.copy()
        red[:, :, (1, 2)] = 0

        pil_img = Image.fromarray(red)
        file_out = "./data_output/red.png" # change to actual file path
        pil_img.save(file_out)

        self.endPopup = ProcessEndPopup(OK=self.dismiss_popup)
        self.endPopup.show()

    def Metadata_btn(self):
        content = MetadataEntryPopup(Save=self.Save)
        self._popup = Popup(title="Image Processor", content=content,
                            size_hint=(None, None), size=(400, 400))
        self._popup.open()

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

