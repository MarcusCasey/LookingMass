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


class MetadataEntryPopup(FloatLayout):
    pass

class ProcessStartPopup(FloatLayout):
    OK = ObjectP.ObjectProperty(None)
    def show(self):
        self.popupWindow = Popup(title="Image Processor", content=self, size_hint=(None,None),size=(400,400))
        self.popupWindow.open()
    def end(self):
        self.popupWindow.dismiss()

class ProcessEndPopup(FloatLayout):
    OK = ObjectP.ObjectProperty(None)
    def show(self):
        self.popupWindow = Popup(title="Image Processor", content=self, size_hint=(None,None),size=(400,400))
        self.popupWindow.open()
    def end(self):
        self.popupWindow.dismiss()

class MetadataEntryPopup(FloatLayout):
    #add method that saves text inputs to metadata class when "save" button is pressed
    Save = ObjectP.ObjectProperty(None)

class Widgets(Widget):
    def dismiss_popup(self):
        self._popup.dismiss()
#    def Upload_btn(self):
    # UPLOAD IMAGE NOT IMPLEMENTED YET
    def Process_btn(self):
        self.startPopup = ProcessStartPopup(OK=self.dismiss_popup)
        self.startPopup.show()

        # IMAGE PROCESSING CODE HERE

        self.endPopup = ProcessStartPopup(OK=self.dismiss_popup)
        self.endPopup.show()
    def Metadata_btn(self):
        content = MetadataEntryPopup(Save=self.Save)
        self._popup = Popup(title="Image Processor", content=content,
                               size_hint=(None,None),size=(400,400))
        self._popup.open()
    def Save():
        pass

class MyApp(App):
    def build(self):
        return Widgets()


if __name__ == "__main__":
    MyApp().run()