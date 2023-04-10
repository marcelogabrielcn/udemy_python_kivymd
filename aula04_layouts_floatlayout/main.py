from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.metrics import dp
from screens import appmobile_screen

Window.size = (600, 500)

class HomePage(Screen):
    pass

class Pagina2(Screen):
    pass

class TabPage(TabbedPanel):
    pass

class Layouts(Screen):
    pass

sm = ScreenManager()
sm.add_widget(HomePage(name='home'))
sm.add_widget(Pagina2(name='pagina2'))
sm.add_widget(Layouts(name='layouts'))

class AppMobile(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.accent_palette = "Blue"

        return Builder.load_string(appmobile_screen)
    
AppMobile().run()
