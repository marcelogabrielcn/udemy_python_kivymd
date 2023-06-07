from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from appDataBase import appdb_screen


Window.size = (800,600)

class HomeDB(Screen):
    pass


sm = ScreenManager()
sm.add_widget(HomeDB(name='home'))


class AppDataBase(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Orange"

        return Builder.load_string(appdb_screen)
    
AppDataBase().run()
