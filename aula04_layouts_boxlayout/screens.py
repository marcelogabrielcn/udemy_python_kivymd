appmobile_screen = '''
ScreenManager:
    id: screen_manager
    HomePage:
        id: home
    Pagina2:
        id: pagina2
    Layouts:
        id: layouts

<HomePage>:
    name: "home"
    MDRaisedButton:
        id: btn
        text: "Next page test"
        size_hint_x: 0.2
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        font_size: 16
        md_bg_color: app.theme_cls.primary_color
        on_press: root.manager.current = "pagina2"
    MDRaisedButton:
        id: btn
        text: "Go to Layouts"
        size_hint_x: 0.2
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        font_size: 16
        md_bg_color: app.theme_cls.primary_color
        on_press: root.manager.current = "layouts"
    MDRaisedButton:
        id: btn
        text: "Return"
        size_hint_x: 0.1
        pos_hint: {'center_x': 0.1, 'center_y': 0.9}
        font_size: 16
        md_bg_color: app.theme_cls.primary_color
        on_press: root.manager.current = "home"

<Pagina2>:
    name: "pagina2"
    TabPage:
        size_hint: (1, 1)
        do_default_tab: False
        background_color: (1, 0, 0, 1)

        TabbedPanelItem:
            text: 'Buttons'
            background_color: (0 ,1, 0, 1)
            Label:
                text: 'Mostraremos as opções de botões disponíveis no KivyMD'
        TabbedPanelItem:
            text: 'Labels'
            Label:
                text: 'Mostraremos as opções de Labels disponíveis no KivyMD'
        TabbedPanelItem:
            text: 'Voltar'
            background_color: (0 ,0 , 1, 1)
            
            MDRaisedButton:
                id: btn
                text: "Return"
                size_hint_x: 0.1
                pos_hint: {'center_x': 0.9, 'center_y': 0.9}
                font_size: 16
                md_bg_color: app.theme_cls.primary_color
                on_press: root.manager.current = "home"
        

<Layouts>:
    name: "layouts"
    BoxLayout:
        orientation: "vertical"
        Button:
            id: btn
            text: "Botãozinho 01"
            color: app.theme_cls.primary_color


        Button:
            id: btn
            text: "Return"
            color: app.theme_cls.primary_color
            on_press: root.manager.current = "home"

'''