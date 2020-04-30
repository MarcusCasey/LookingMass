#!/usr/bin/env python3
#!/usr/bin/env python2

"""The classes and functions necessary to implment the engine of Looking Mass.

This file contains the classes and functions that implment the engine of 
Looking Mass. It includes the class MyApp which inherits from the Kivy class
App and contains methods to build the application, close the application, and
display a warning pop up before closing the application. It also includes the
main function that is executed when Looking Mass is ran. 

  Typical usage example:

  Window.bind(on_request_close=self.on_request_close)
  self.ExitPopup(title = "Title Text", text = "Contents Text")
"""

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
    """Holds methods and attributes for the application.

    This class inherits from the Kivy class App. It contains the methods 
    and attributes needed to run the engine of the Looking Mass
    application. The methods implemented build the application, close the
    application, and display a warning pop up before closing the
    application.

    Attributes:

        self.title: A string indicating the title of the application.
        Window.bind: A function that closes the application when called.
        self.widgets: A Widgets class that contains the widgets of the
            application.
    """
    # This is necessary as an App class
    def build(self):
        """Builds the application.

        This function builds the Looking Mass application. It does so by
        initializing the applicaiton's title and widgets as well as
        designating the function to be called to close the application.
        It returns MyApp's Widgets.

        Args:

            self: Variable refering to the class this function is a part of
                (MyApp).

        Returns:
        
            The Widgets class that it was initialized with.
        """
        self.title = 'Looking Mass'
        Window.bind(on_request_close=self.on_request_close)
        self.widgets = Widgets()
        return self.widgets

    # Behavior when the application is requested to close
    def on_request_close(self, *args):
        """Closes the application.

        This function closes the Looking Mass application. It does so by
        calling the ExitPopup. It returns true if it was completed 
        sucessfully.

        Args:

            self: Variable refering to the class this function is a part of
                (MyApp).
            *args: holds the arguments needed to close the application.


        Returns:

            A boolean that is true if the the applications was sucessfully
            closed and false if not.
        """
        self.ExitPopup(title = "Exit", text = "Are you sure you want to exit? Unsaved work may be lost.")
        return True

    # Opens a popup that confirms if the user wants to exit
    def ExitPopup(self, title='', text=''):
        """Opens pop up for closing confirmation.

        This function opens a popup that warns the users that they are
        about to close the app. It does this by initializing a Popup 
        class with widgets (lables and buttons) needed to make the
        warning pop up. 

        Args:
        
            self: Variable refering to the class this function is a part of
                (MyApp).
            title: String containing the title of the pop up.
            text: String containing the text content of the pop up.


        Returns:
        
            A boolean that is true if the the applications was sucessfully
            closed and false if not.
        """
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
    """The main function that runs when the program is started.

    This function is the main function that is called when when the Looking
    Mass application starts. It creates and intilizes the myApp class and 
    attempts to run it. If the myApp run function fails, an exception is 
    thrown and an error log detailing what went wrong is produced.

    Raises:

        error: An error occured when trying to run the Looking Mass Application
    """
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