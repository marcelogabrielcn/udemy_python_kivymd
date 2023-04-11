from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDBoxLayout:
    orientation: "vertical"
    md_bg_color: app.theme_cls.accent_color

    MDTopAppBar:
        title: "MDTopAppBar"
        right_action_items: [["dots-vertical", lambda x: app.callback_1()], ["clock", lambda x: app.callback_2()]]

    MDLabel:
        text: "Content"
        halign: "center"
    
    
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()