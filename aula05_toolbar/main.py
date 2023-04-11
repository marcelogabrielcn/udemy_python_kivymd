from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivymd.icon_definitions import md_icons
from kivymd.uix.button import MDRaisedButton, MDIconButton
from screens import appmobile_screen

Window.size = (600, 500)

class HomePage(Screen):
    pass

class PainelTabs(Screen):
    pass

class TabPage(TabbedPanel):
    pass

class Layouts(Screen):
    pass

class BLayout(Screen):
    pass

class BMDLayout(Screen):
    pass

class FLayout(Screen):
    pass

class FMDLayout(Screen):
    pass

class GLayout(Screen):
    pass

class GMDLayout(Screen):
    pass

class Scroll(Screen):
    pass

sm = ScreenManager()
sm.add_widget(HomePage(name='home'))
sm.add_widget(PainelTabs(name='paineltabs'))
sm.add_widget(Layouts(name='layouts'))
sm.add_widget(BLayout(name='blayout'))
sm.add_widget(BMDLayout(name='bmdlayout'))
sm.add_widget(FLayout(name='flayout'))
sm.add_widget(FMDLayout(name='fmdlayout'))
sm.add_widget(GLayout(name='glayout'))
sm.add_widget(GMDLayout(name='gmlayout'))
sm.add_widget(Scroll(name='scroll'))

class AppMobile(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.accent_palette = "Blue"

        return Builder.load_string(appmobile_screen)

AppMobile().run()
