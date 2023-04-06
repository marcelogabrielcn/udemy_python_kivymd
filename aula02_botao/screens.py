appmobile_screen = '''
ScreenManager:
    id: screen_manager
    HomePage:
        id: home
    Pagina2:
        id: pagina2

<HomePage>:
    name: "home"
    MDRaisedButton:
        id: btn
        text: "Next page"
        size_hint_x: 0.2
        pos_hint: {'center_x': 0.7, 'center_y': 0.5}
        font_size: 16
        md_bg_color: app.theme_cls.primary_color
        on_press: root.manager.current = "pagina2"

<Pagina2>:
    name: "pagina2"
    MDRaisedButton:
        id: btn2
        text: "Previous page"
        size_hint_x: 0.2
        pos_hint: {'center_x': 0.3, 'center_y': 0.5}
        font_size: 16
        md_bg_color: app.theme_cls.accent_color
        on_press: root.manager.current = "home"


'''