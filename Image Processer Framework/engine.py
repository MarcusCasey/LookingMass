#!/usr/bin/env python3
#!/usr/bin/env python2

from widgets import *

import numpy as np
import math
import os
import time
import datetime
import traceback
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

# Defines the window of the application, including the title displayed
class MyApp(App):

    # This is necessary as an App class
    def build(self):
        self.title = 'Looking Mass'
        Window.bind(on_request_close=self.on_request_close)
        self.widgets = Widgets()
        return self.widgets

    # Behavior when the application is requested to close
    def on_request_close(self, *args):
        self.ExitPopup(title = "Exit", text = "Are you sure you want to exit? Unsaved work may be lost.")
        return True

    # Opens a popup that confirms if the user wants to exit
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

# This is the main function, from which the whole program starts.
# If there is a critical error, a summary fo the error is appended to a log
# and a detailed description is written to a new file.
if __name__ == "__main__":
    errorDir = "errorLogs"
    if not os.path.exists(errorDir):
        os.mkdir(errorDir)

    myApp = MyApp()
    try:
        myApp.run()
    except Exception as error:
        now = datetime.datetime.now()

        errorLog = open(errorDir + "/" + "errorLog.txt", "a")
        errorLog.write(now.strftime("[%Y-%m-%d] %H:%M:%S: ") + error.__str__() + "\n")
        errorLog.close()

        errorDetailedLog = open(errorDir + "/" + now.strftime("[%Y-%m-%d]_%H-%M-%S.txt"), "w")
        traceback.print_exc(file=errorDetailedLog)
        errorDetailedLog.close()

        raise error
