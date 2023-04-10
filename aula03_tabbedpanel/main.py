from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from screens import appmobile_screen

Window.size = (600, 500)

class HomePage(Screen):
    pass

class Pagina2(Screen):
    pass

class TabPage(TabbedPanel):
    pass

sm = ScreenManager()
sm.add_widget(HomePage(name='home'))
sm.add_widget(Pagina2(name='pagina2'))

class AppMobile(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.accent_palette = "Blue"

        return Builder.load_string(appmobile_screen)
    
AppMobile().run()
