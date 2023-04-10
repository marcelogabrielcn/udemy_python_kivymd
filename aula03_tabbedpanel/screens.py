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
    TabPage:
        size_hint: (1, 1)
        do_default_tab: False
        background_color: (1, 0, 0, .5)

        TabbedPanelItem:
            text: 'Buttons'
            background_color: (1, 1, 1, .4)
            Label:
                text: 'Mostraremos as opções de botões disponíveis no KivyMD'
        TabbedPanelItem:
            text: 'Labels'
            Label:
                text: 'Mostraremos as opções de Labels disponíveis no KivyMD'
        TabbedPanelItem:
            text: 'TextField'
            background_color: (0, 1, 1, .4)
            Label:
                text: 'Mostraremos as opções de textos disponíveis no KivyMD'

'''