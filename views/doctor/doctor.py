
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('views/doctor/doctor.kv')
class Doctor(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)