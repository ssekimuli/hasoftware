from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
# from kivy.clock import Clock

import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib as mpl
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.properties import StringProperty
import matplotlib.pyplot as plt

from widgets.kivyplt import MatplotFigure

Builder.load_file('views/home/home.kv')
class Home(BoxLayout):
    username = StringProperty("Samuel M")
    avatar = StringProperty("assets/imgs/avatar.jpg")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)


class NavTab(ToggleButtonBehavior, BoxLayout):
    text = StringProperty("")
    icon = StringProperty("")
    icon_active = StringProperty("")
    def __init__(self, **kw):
        super().__init__(**kw)
