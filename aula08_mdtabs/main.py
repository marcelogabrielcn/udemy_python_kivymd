from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivymd.uix.tab import MDTabsBase
from screens import appmobile_screen

Window.size = (800, 600)

class PageMDTabs(Screen):
    pass

class AppMobile(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.accent_palette = "Blue"

        return Builder.load_string(appmobile_screen)

sm = ScreenManager()
sm.add_widget(PageMDTabs(name='pagemdtabs'))

    
AppMobile().run()
