# Arquivo Kivy

appdb_screen = '''
ScreenManager:
    id: screen_manager
    HomeDB:
        id: home

<HomeDB>:
    nome: "home"
    MDLabel:
        text: "Nova aplicação para começar usar banco de dados"
        font_size: 18
        color: app.theme_cls.primary_color
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}   

'''