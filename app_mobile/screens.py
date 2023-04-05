appmobile_screen = '''
ScreenManager:
    id: screen_manager
    HomePage:
        id: home

<HomePage>:
    name: "Home"
    MDLabel:
        id: label
        text: "Hello world"
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.6, 'center_y': 0.5}
        font_size: 16
        color: app.theme_cls.primary_color
        
'''