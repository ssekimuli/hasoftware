
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('views/dashboard/dashboard.kv')
class Dashboard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)