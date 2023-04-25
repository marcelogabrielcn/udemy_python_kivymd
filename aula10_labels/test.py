from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "MDLabel - Top App Bar"

        MDLabel:
            text: "MDLabel exemple"
            halign: "center"
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()