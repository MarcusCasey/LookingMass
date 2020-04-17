#!/usr/bin/env python3
#!/usr/bin/env python2

from widgets import *

import numpy as np
import math
from kivy.uix.button import Button
from kivy.uix.image import Image as Kivy_Image
import kivy.properties as ObjectP
from kivy.app import App
from kivy.uix.label import Label
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
import kivy
kivy.require('1.11.1')  # replace with your current kivy version !

class TestBox(BoxLayout):
    pass

class FCTest(App):
    pass

def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

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

