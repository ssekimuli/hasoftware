
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('views/pharmacy/pharmacy.kv')
class Pharmacy(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)