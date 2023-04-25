from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:

    MDIconButton:
        icon: "language-python"
        pos_hint: {"center_x": .5, "center_y": .5}
    MDIconButton:
        icon: "android"
        icon_size: "64sp"
        pos_hint: {"center_x": .5, "center_y": .4}
        on_press: print('Clicou aqui!')
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)


Example().run()