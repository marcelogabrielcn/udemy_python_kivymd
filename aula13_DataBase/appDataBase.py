# Arquivo Kivy

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


'''