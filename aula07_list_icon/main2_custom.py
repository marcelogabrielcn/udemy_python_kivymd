from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.list import MDList
from kivymd.icon_definitions import md_icons
from screens2_custom import *


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return (
            MDScrollView(
                MDList(
                    id="scroll"
                )
            )
        )

    def on_start(self):
        icons = list(md_icons.keys())
        for i in range(30):
            self.root.ids.scroll.add_widget(
                OneLineAvatarIconListItem(
                    IconLeftWidget(
                        icon=icons[i]
                    ),
                    RightCheckbox(),
                    text=f"Item {i}",
                )
            )


Example().run()
