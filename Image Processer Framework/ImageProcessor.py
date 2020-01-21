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

from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.button import Button 

class Widgets(Widget):
    def Process_btn(self):
        process_image()
    def Metadata_btn(self):
        show_metadata_entry_popup()

class ProcessStartPopup(FloatLayout):
    pass

class ProcessEndPopup(FloatLayout):
    pass

class MetadataEntryPopup(FloatLayout):
    #add method that saves text inputs to metadata class when "save" button is pressed
    pass

class MyApp(App):
    def build(self):
        return Widgets()


def process_image():
   show_image_processing_start_popup()

   #PERFORM IMAGE PROCESSING HERE

   show_image_processing_end_popup()


def show_image_processing_start_popup():
    show = ProcessStartPopup()

# cant get pop ups to close when "OK" button is pressed
#    closeButton = Button(text = "OK") 

    popupWindow = Popup(title="Image Processor", content=show, size_hint=(None,None),size=(400,400))

    popupWindow.open()

#    closeButton.bind(on_press = popupWindow.dismiss)


def show_image_processing_end_popup():
    show = ProcessEndPopup()
# cant get pop ups to close when "OK" button is pressed
#    closeButton = Button(text = "OK") 

    popupWindow = Popup(title="Image Processor", content=show, size_hint=(None,None),size=(400,400))

    popupWindow.open()

#    closeButton.bind(on_press = popupWindow.dismiss)

def show_metadata_entry_popup():
    show = MetadataEntryPopup()

    popupWindow = Popup(title="Image Processor", content=show, size_hint=(None,None),size=(400,400))

    popupWindow.open()


if __name__ == "__main__":
    MyApp().run()
