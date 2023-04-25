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
from kivymd.uix.list import (IconLeftWidget, IconRightWidget, OneLineListItem, TwoLineListItem, ThreeLineListItem, OneLineAvatarIconListItem,
	OneLineAvatarListItem, TwoLineAvatarListItem, ThreeLineAvatarListItem, OneLineIconListItem, TwoLineIconListItem, ThreeLineIconListItem,
	OneLineAvatarIconListItem, TwoLineAvatarIconListItem, ThreeLineAvatarIconListItem, ILeftBodyTouch, IRightBodyTouch,
    IconLeftWidgetWithoutTouch
)
from kivymd.uix.tab import MDTabsBase
from screen_test import appmobile_screen

Window.size = (800, 600)

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

class Lista(Screen):
    pass

class ItensLista(Screen):
    pass

class TabPageItensLista(TabbedPanel):
    pass

class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    def on_touch_down(self, touch):
        collide_point = self.collide_point(touch.x, touch.y)
        if collide_point:
            touch.grab(self)
            if self.icon == "cat":
                self.icon = "android"
            else:
                self.icon = "cat"
            ret = super(MDIconButton, self).on_touch_down(touch)
            return ret

class IconRightSampleWidget(IRightBodyTouch, MDIconButton):
    def on_touch_down(self, touch):
        collide_point = self.collide_point(touch.x, touch.y)
        if collide_point:
            touch.grab(self)
            mensagem = "Você clicou no Ícone do Robô!"
            self.parent.parent.text = mensagem
            if self.parent.parent.bg_color == [0, 0, 1, 1]:
                self.parent.parent.bg_color = [1, 0, 0, 1]
            else:
                self.parent.parent.bg_color = [0, 0, 1, 1]
            ret = super(MDIconButton, self).on_touch_down(touch)
            return ret

class PageMDTabs(Screen):
    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        pass

class Tab(FloatLayout, MDTabsBase):
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
sm.add_widget(Lista(name='lista'))
sm.add_widget(ItensLista(name='itenslista'))
sm.add_widget(PageMDTabs(name='pagemdtabs'))

class AppMobile(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.accent_palette = "Blue"

        return Builder.load_string(appmobile_screen)

AppMobile().run()
