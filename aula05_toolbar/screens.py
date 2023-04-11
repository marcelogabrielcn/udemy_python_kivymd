appmobile_screen = '''
ScreenManager:
    id: screen_manager
    HomePage:
        id: home
    PainelTabs:
        id: paineltabs
    Layouts:
        id: layouts
    BLayout:
        id: blayout
    BMDLayout:
        id: bmdlayout
    FLayout:
        id: flayout
    FMDLayout:
        id: fbmdlayout
    GLayout:
        id: glayout
    GMDLayout:
        id: gmdlayout

<HomePage>:
    name: "home"
    BoxLayout:
        orientation: "horizontal"
        MDToolbar:
            title: "App Mobile"
            anchor_title: "center"
    		md_bg_color: app.theme_cls.primary_color
    		elevation: 10
            pos_hint: {'center_x': 0.95, 'center_y': 0.95}
            left_action_items: [["menu", lambda x: x]]
            right_action_items: [["dots-vertical", lambda x: x]]
    MDTextButton:
        id: btn
        text: "TabbedPanel"
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.3, 'center_y': 0.8}
        font_size: 16
        color: app.theme_cls.primary_color
        underline: True
        on_press: root.manager.current = 'paineltabs'
    MDTextButton:
        id: btn
        text: "Layouts"
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.3, 'center_y': 0.7}
        font_size: 16
        color: app.theme_cls.primary_color
        underline: True
        on_press: root.manager.current = 'layouts'
    BoxLayout:
        orientation: "horizontal"
        MDToolbar:
            title: "Python & KivyMD"
    		md_bg_color: app.theme_cls.primary_dark
            pos_hint: {'center_x': 0.95, 'center_y': 0.05}
            anchor_title: "center"
            size_hint_y: 0.1

<PainelTabs>:
    name: "paineltabs"
    TabPage:
        size_hint: (1, 1)
        do_default_tab: False
        background_color: (1, 0, 0, .5)

        TabbedPanelItem:
            text: 'Buttons'
            background_color: (1, 0, 0, .5)
            Label:
                text: 'Mostraremos as opções de botões disponíveis no KivyMD'
        TabbedPanelItem:
            text: 'Labels'
            background_color: (1, 0, 0, .5)
            Label:
                text: 'Mostraremos as opções de Labels disponíveis no KivyMD'
        TabbedPanelItem:
            text: 'TextField'
            background_color: (1, 0, 0, .5)
    		Label:
                text: 'Mostraremos as opções de Textos disponíveis no KivyMD'

<Layouts>:
    name: "layouts"
    MDIconButton:
        id: voltar
        icon: "arrow-left"
        user_font_size: dp(10)
        pos_hint: {'center_x': 0.1, 'center_y': 0.83}
        md_bg_color: app.theme_cls.primary_dark
        on_press: root.manager.current = "home"
    MDLabel:
        text: "Home Layouts"
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.6, 'center_y': 0.83}
        font_style: "H6"
    MDGridLayout:
        id: grid
        cols: 2
        size_hint: (0.5, 0.5)
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
        md_bg_color: app.theme_cls.primary_light
        padding_top: 30
        spacing: 15
        adaptive_height: True
        MDLabel:
            text: 'BoxLayout'
            color: (0, 0, 1, 1)
        MDRaisedButton:
            id: btn
            text: "Abrir"
            color: app.theme_cls.primary_light
            on_press: root.manager.current = "blayout"
        MDLabel:
            text: 'MDBoxLayout'
            color: (0, 0, 1, 1)
        MDRaisedButton:
            id: btn2
            text: "Abrir"
            color: app.theme_cls.primary_light
            on_press: root.manager.current = "bmdlayout"
        MDLabel:
            text: 'FloatLayout'
            color: (0, 0, 1, 1)
        MDRaisedButton:
            id: btn3
            text: "Abrir"
            color: app.theme_cls.primary_light
            on_press: root.manager.current = "flayout"
        MDLabel:
            text: 'MDFloatLayout'
            color: (0, 0, 1, 1)
        MDRaisedButton:
            id: btn4
            text: "Abrir"
            color: app.theme_cls.primary_light
            on_press: root.manager.current = "fmdlayout"
        MDLabel:
            text: 'GridLayout'
            color: (0, 0, 1, 1)
        MDRaisedButton:
            id: btn5
            text: "Abrir"
            color: app.theme_cls.primary_light
            on_press: root.manager.current = "glayout"
        MDLabel:
            text: 'MDGridLayout'
            color: (0, 0, 1, 1)
        MDRaisedButton:
            id: btn6
            text: "Abrir"
            color: app.theme_cls.primary_light
            on_press: root.manager.current = "gmdlayout"

<BLayout>:
    name: "blayout"
    MDLabel:
        text: "BoxLayout"
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.6, 'center_y': 0.83}
        font_style: "H6"
    BoxLayout:
		orientation: "vertical"
        MDIconButton:
            id: voltar
            icon: "arrow-left"
            user_font_size: dp(10)
            pos_hint: {'center_x': 0.1, 'center_y': 0.75}
            md_bg_color: app.theme_cls.primary_dark
            on_press: root.manager.current = "layouts"
		Button:
			id: btn1
			text: "Botão 1"
			color: app.theme_cls.accent_color
		Button:
			id: btn2
			text: "Botão 2"
			color: app.theme_cls.accent_color

<BMDLayout>:
    name: "bmdlayout"
    MDIconButton:
        id: voltar
        icon: "arrow-left"
        user_font_size: dp(10)
        pos_hint: {'center_x': 0.1, 'center_y': 0.83}
        md_bg_color: app.theme_cls.primary_dark
        on_press: root.manager.current = "layouts"
    MDLabel:
        text: "MDBoxLayout"
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.6, 'center_y': 0.83}
        font_style: "H6"
    MDBoxLayout:
        orientation: "vertical"
        size_hint_x: 0.75
        size_hint_y: 0.3
        spacing: dp(2)
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        Button:
            id: btn1
            text: "Botão 1"
            color: app.theme_cls.accent_color
        Button:
            id: btn2
            text: "Botão 2"
            color: app.theme_cls.accent_color
        Label:
            text: 'Label adicionado como último filho.'
            color: app.theme_cls.accent_color

<FLayout>:
    name: "flayout"
    MDIconButton:
        id: voltar
        icon: "arrow-left"
        user_font_size: dp(10)
        pos_hint: {'center_x': 0.1, 'center_y': 0.83}
        md_bg_color: app.theme_cls.primary_dark
        on_press: root.manager.current = "layouts"
    MDLabel:
        text: "FloatLayout"
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.6, 'center_y': 0.83}
        font_style: "H6"
    FloatLayout:
        size_hint_x: 0.9
        size_hint_y: 0.9
        padding_top: 5
        size_hint: (0.9, 0.9)
        font_size: 10
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        Button:
            id: btn1
            text: "Botão 1"
            color: app.theme_cls.accent_color
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
            size_hint: (0.5, 0.1)
        Button:
            id: btn2
            text: "Botão 3"
            color: app.theme_cls.accent_color
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: (0.5, 0.1)
        Label:
            text: 'Label adicionado como último filho.'
            color: app.theme_cls.accent_color
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
            size_hint: (0.5, 0.1)

<FMDLayout>:
    name: "fmdlayout"
    MDIconButton:
        id: voltar
        icon: "arrow-left"
        user_font_size: dp(10)
        pos_hint: {'center_x': 0.1, 'center_y': 0.83}
        md_bg_color: app.theme_cls.primary_dark
        on_press: root.manager.current = "layouts"
    MDLabel:
        text: "MDFloatLayout"
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.6, 'center_y': 0.83}
        font_style: "H6"
    MDFloatLayout:
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        adaptive_height: True
        MDRaisedButton:
            id: btn1
            text: "Botão 1"
            color: app.theme_cls.accent_color
            pos_hint: {'center_x': 0.5, 'center_y': 0.59}
            size_hint: (0.5, 0.2)
        MDRaisedButton:
            id: btn2
            text: "Botão2"
            color: app.theme_cls.accent_color
            pos_hint: {'center_x': 0.5, 'center_y': 0.39}
            size_hint: (0.5, 0.2)
        MDLabel:
            text: 'Label adicionado como último filho.'
            color: app.theme_cls.accent_color
            pos_hint: {'center_x': 0.5, 'center_y': 0.19}
            size_hint: (0.5, 0.2)

<GLayout>:
    name: "glayout"
    MDIconButton:
        id: voltar
        icon: "arrow-left"
        user_font_size: dp(10)
        pos_hint: {'center_x': 0.1, 'center_y': 0.83}
        md_bg_color: app.theme_cls.primary_dark
        on_press: root.manager.current = "layouts"
    MDLabel:
        text: "GridLayout"
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.6, 'center_y': 0.83}
        font_style: "H6"
    GridLayout:
        id: grid
        cols: 2
        spacing: 10
        padding_top: 15
        pos_hint: {'center_x': 0.5, 'center_y': 0.15}
        size_hint_x: 0.9
        row_force_default: True
        row_default_height: 50
        MDRaisedButton:
            id: btn1
            text: "Botão 1"
            color: app.theme_cls.accent_color
        MDLabel:
            text: 'Label adicionado na segunda coluna da 1a linha.'
            color: app.theme_cls.accent_color
        MDRaisedButton:
            id: btn2
            text: "Botão 2"
            color: app.theme_cls.accent_color
        MDLabel:
            text: 'Label adicionado na segunda coluna da 2a linha.'
            color: app.theme_cls.accent_color

<GMDLayout>:
    name: "gmdlayout"
    MDIconButton:
        id: voltar
        icon: "arrow-left"
        user_font_size: dp(10)
        pos_hint: {'center_x': 0.1, 'center_y': 0.83}
        md_bg_color: app.theme_cls.primary_dark
        on_press: root.manager.current = "layouts"
    MDLabel:
        text: "MDGridLayout"
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.6, 'center_y': 0.83}
        font_style: "H6"
    MDGridLayout:
        id: scroll
        cols: 2
        size_hint: (0.7, None)
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
        md_bg_color: app.theme_cls.primary_light
        padding_top: "15sp"
        spacing: dp(15)
        adaptive_height: True
        MDRaisedButton:
            id: btn1
            text: "Botão 1"
            color: app.theme_cls.accent_color
        MDLabel:
            text: 'Label adicionado na segunda linha.'
            color: app.theme_cls.accent_color
        MDRaisedButton:
            id: btn2
            text: "Botão 2"
            color: app.theme_cls.accent_color
        MDLabel:
            text: 'Label adicionado na quarta linha.'
            color: app.theme_cls.accent_color

'''
