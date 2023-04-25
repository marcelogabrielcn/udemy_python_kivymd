from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:

    MDTextField:
        id: text_field_error
        hint_text: "Helper text on error (press 'Enter')"
        helper_text: "There will always be a mistake"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint_x: .5
    MDTextField:
        hint_text: "Informe sua senha (teste, vai aparecer na tela): "
        max_text_length: 8
        pos_hint: {"center_x": .5, "center_y": .4}
        size_hint_x: .5
    MDTextField:
        hint_text: "Rectangle mode"
        mode: "rectangle"
        pos_hint: {"center_x": .5, "center_y": .3}
        size_hint_x: .5
'''


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.screen.ids.text_field_error.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )
        return self.screen

    def set_error_message(self, instance_textfield):
        self.screen.ids.text_field_error.error = True


Test().run()