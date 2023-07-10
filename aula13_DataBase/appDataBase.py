appdb_screen = '''
ScreenManager:
    id: screen_manager
    HomeDB:
        id: home
    Usuarios:
        id: usuarios

<HomeDB>:
    nome: "home"
    BoxLayout:
    	orientation: "horizontal"
    	MDTopAppBar:
    		title: "App Mobile Database"
    		valign: "center"
    		md_bg_color: app.theme_cls.primary_color
    		elevation: 10
    		pos_hint: {'center_x': 0.95, 'center_y': 0.95}
    		left_action_items: [["menu", lambda x: root.menu_esquerda(x, app.theme_cls.accent_color)]]
    MDLabel:
        text: "Nova aplicação para começar usar banco de dados"
        font_size: 18
        color: app.theme_cls.primary_color
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}   

<Usuarios>:
    name: "usuarios"
    BoxLayout:
    	orientation: "horizontal"
    	MDTopAppBar:
    		title: "App Mobile Database"
    		valign: "center"
    		md_bg_color: app.theme_cls.primary_color
    		elevation: 10
    		pos_hint: {'center_x': 0.95, 'center_y': 0.95}
    MDLabel:
        text: "Cadastrar Usuário"
        font_size: 20
        color: app.theme_cls.primary_color
        size_hint_x: 0.4
        pos_hint: {'center_x': 0.5, 'center_y': 0.85}
    MDIconButton:
        icon: "arrow-left-circle"
        icon_size: dp(40)
        theme_icon_color: "Custom"
        pos_hint: {'center_x':0.1, 'center_y': 0.83}
        on_press: root.manager.current = "home"
    MDGridLayout:
        cols: 1
        size_hint_x: 0.5 
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
        spacing: 10
        adaptive_height: True
        MDTextField:
            id: nome
            hint_text: 'Informe seu nome'
            text: ''
            size_hint_x: 0.5
            focus: True
        MDTextField:
            id: email
            hint_text: 'Informe seu e-mail'
            text: ''
            size_hint_x: 0.5
        MDTextField:
            id: senha
            hint_text: 'Informe sua senha'
            text: ''
            size_hint_x: 0.5
            password: True
        MDTextField:
            id: repsenha
            hint_text: 'Repita sua senha'
            text: ''
            size_hint_x: 0.5
            password: True
        MDTextField:
            id: grupo
            hint_text: 'Informe seu grupo'
            text: 'CLIENT'
            size_hint_x: 0.5
            color: app.theme_cls.primary_light
        MDLabel:
            text: "Data de nascimento"
            size_hint_x: 0.5
            color: app.theme_cls.primary_light
            MDIconButton:
                id: btn_calendario
                icon: "calendar-month"
                color: app.theme_cls.accent_color
                icon_size: dp(6)
    MDRaisedButton:
        text: "Salvar"
        siz: (0.3, 0.2)
        font_size: 18
        md_bg_color: (0, 0, 1, 1)
        color: (0, 0, 0, 0)
        pos_hint: {'center_x':0.5, 'center_y': 0.05}
    MDIconButton:
        id: btn_calendario
        icon: "calendar-month"
        theme_icon_color: "Custom"
        icon_size: dp(35)
        pos_hint: {'center_x':0.45, 'center_y': 0.15}

'''