from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
import sqlite3
from appDataBase import appdb_screen


Window.size = (800,600)

class HomeDB(Screen):
    def menu_esquerda(self, button, color):
        itens_menu = [
            {
                'viewclass':'OneLineListItem',
                'color': [0.1, 0, 0, 1],
                'text': 'Cadastrar Usuário',
                'height': dp(40),
                'on_release': lambda x="Cadastrar Usuário": Usuarios.cadastrar_usuario(self, button)
            },
        ]
        self.menu = MDDropdownMenu(
                caller=button,
                items=itens_menu,
                width_mult=3,
                background_color=color,
        )
        self.menu.open()

        def fechar_menu(self, button):
            self.menu.caller = button
            self.menu.dismiss()

class Usuarios(Screen):
	def cadastrar_usuario(self, button):
		pass


sm = ScreenManager()
sm.add_widget(HomeDB(name='home'))
sm.add_widget(Usuarios(name='usuarios'))

class AppDataBase(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Orange"

        conn = sqlite3.connect('datas.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE if not exists Usuarios(
            	nome text,
            	email text,
            	senha text,
            	grupo text,
            	dt_nascimento date
        )
        """)

        conn.commit()
        conn.close()

        return Builder.load_string(appdb_screen)
    
AppDataBase().run()
