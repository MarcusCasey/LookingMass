from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ListProperty


class LoadDialog(Popup):
    filters = ListProperty()
    path = StringProperty()

    def __init__(self, **var):
        self.filters = var['filters']
        self.path = var['path']
        super().__init__(**var)


class SaveDialog(Popup):
    filters = ListProperty()
    path = StringProperty()

    def __init__(self, **var):
        self.filters = var['filters']
        self.path = var['path']
        super().__init__(**var)
