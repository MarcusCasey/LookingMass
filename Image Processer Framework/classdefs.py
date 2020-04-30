"""The classes and functions necessary to implment the file I/O of Looking Mass.

This file contains the classes and functions that implment the file I/O of 
Looking Mass. It includes the LoadDialog and SaveDialog classes as well as 
their initialization methods. The LoadDialog class inherits from the Popup 
class and is resposible for creating a pop up that allows users to select the 
input directory and image. The SaveDialog class inherits from the Popup class 
and is resposible for creating a pop up that allows users to select the output 
directory and image.

  Typical usage example:

  self.startPopup = LoadDialog(filters = '', path = folderIn)
  self.startPopup = SaveDialog(filters = '', path = folderOut)
"""

from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ListProperty


class LoadDialog(Popup):
    """Holds methods and attributes for file input.

    This class inherits from the Kivy class Popup. It contains the methods 
    and attributes needed to load an image into the Looking Mass application. 
    The methods implemented initializes the LoadDialog class.

    Attributes:

        filters: List holding the filters needed for the LoadDialog class.
        path: string holding the filepath needed for the LoadDialog class
    """

    filters = ListProperty()
    path = StringProperty()

    def __init__(self, **var):
        """Initializes LoadDialog.

        This function initializes the classs LoadDialog. It does so by
        setting the filters and path attributes and calling the initialization 
        function.

        Args:

            self: Variable refering to the class this function is a part of
                (LoadDialog).
            **var: variables needed to initalize the LoadDialog class.

        """
        self.filters = var['filters']
        self.path = var['path']
        super().__init__(**var)


class SaveDialog(Popup):
    """Holds methods and attributes for file output.

    This class inherits from the Kivy class Popup. It contains the methods 
    and attributes needed to write an image from the Looking Mass application. 
    The methods implemented initializes the SaveDialog class.

    Attributes:

        filters: List holding the filters needed for the SaveDialog class.
        path: string holding the filepath needed for the SaveDialog class
    """
    filters = ListProperty()
    path = StringProperty()

    def __init__(self, **var):
        """Initializes SaveDialog.

        This function initializes the classs SaveDialog. It does so by
        setting the filters and path attributes and calling the initialization 
        function.

        Args:
        
            self: Variable refering to the class this function is a part of
                (SaveDialog).
            **var: variables needed to initalize the SaveDialog class.

        """
        filters = var['filters']
        path = var['path']
        super().__init__(**var)
