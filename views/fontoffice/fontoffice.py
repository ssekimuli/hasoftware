
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('views/fontoffice/fontoffice.kv')
class Fontoffice(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)