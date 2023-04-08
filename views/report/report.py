
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('views/report/report.kv')
class Report(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)