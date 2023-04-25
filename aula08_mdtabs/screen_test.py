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
    Scroll:
        id: scroll
    Lista:
        id: lista
    ItensLista:
        id: itenslista
    PageMDTabs:
        id: pagemdtabs

<HomePage>:
    name: "home"
    BoxLayout:
        orientation: "horizontal"
        MDTopAppBar:
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
    MDTextButton:
        id: btn
        text: "Scroll"
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.3, 'center_y': 0.6}
        font_size: 16
        color: app.theme_cls.primary_color
        underline: True
        on_press: root.manager.current = 'scroll'
    MDTextButton:
        id: btn
        text: "Lista"
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.3, 'center_y': 0.5}
        font_size: 16
        color: app.theme_cls.primary_color
        underline: True
        on_press: root.manager.current = 'lista'
    MDTextButton:
        id: btn
        text: "Itens Lista"
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.3, 'center_y': 0.4}
        font_size: 16
        color: app.theme_cls.primary_color
        underline: True
        on_press: root.manager.current = 'itenslista'
    MDTextButton:
        id: btn
        text: "MDTabs"
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.3, 'center_y': 0.3}
        font_size: 16
        color: app.theme_cls.primary_color
        underline: True
        on_press: root.manager.current = 'pagemdtabs'
    BoxLayout:
        orientation: "horizontal"
        MDTopAppBar:
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

<Scroll>:
    name: "scroll"
    BoxLayout:
        orientation: "horizontal"
        MDTopAppBar:
            title: "App Mobile"
            anchor_title: "center"
    		md_bg_color: app.theme_cls.primary_color
    		elevation: 10
            pos_hint: {'center_x': 0.95, 'center_y': 0.95}
            left_action_items: [["menu", lambda x: x]]
            right_action_items: [["dots-vertical", lambda x: x]]
    MDLabel:
        text: "Scroll View"
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.6, 'center_y': 0.83}
        font_style: "H6"
    MDIconButton:
        id: voltar
        icon: "arrow-left"
        user_font_size: dp(10)
        pos_hint: {'center_x': 0.1, 'center_y': 0.83}
        md_bg_color: app.theme_cls.primary_dark
        on_press: root.manager.current = "home"
    ScrollView:
        do_scroll_y: True
        do_scroll_x: True
        bar_color: app.theme_cls.primary_color
        bar_color_active: app.theme_cls.accent_color
        effect_cls: "DampedScrollEffect"
        scroll_type: ['content']
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        size_hint: (0.5, 0.9)
        MDGridLayout:
            id: grid
            cols: 1
            rows: 21
            size_hint: (0.5, None)
            size_hint_y: None
            height: 350
            pos_hint: {'center_x': 0.5, 'center_y': 0.2}
            md_bg_color: app.theme_cls.primary_light
            spacing: dp(15)
            MDSeparator:
                height: dp(2)
            MDLabel:
				text: "Primeira linha"
            MDSeparator:
                height: dp(2)
			MDLabel:
				text: "Secunda linha"
            MDSeparator:
                height: dp(2)
			MDLabel:
				text: "Terceira linha"
            MDSeparator:
                height: dp(2)
            MDLabel:
				text: "Quarta linha"
            MDSeparator:
                height: dp(2)
            MDLabel:
				text: "Quinta linha"
            MDSeparator:
                height: dp(2)
            MDLabel:
				text: "Sexta linha"
            MDSeparator:
                height: dp(2)
            MDLabel:
				text: "Sétima linha"
            MDSeparator:
                height: dp(2)
            MDLabel:
				text: "Oitava linha"
            MDSeparator:
                height: dp(2)
            MDLabel:
				text: "Nona linha"
            MDSeparator:
                height: dp(2)
            MDLabel:
				text: "Décima linha"
            MDSeparator:
                height: dp(2)

<Lista>:
    name: "lista"
    BoxLayout:
        orientation: "horizontal"
        MDTopAppBar:
            title: "App Mobile"
            anchor_title: "center"
    		md_bg_color: app.theme_cls.primary_color
    		elevation: 10
            pos_hint: {'center_x': 0.95, 'center_y': 0.95}
            left_action_items: [["menu", lambda x: x]]
            right_action_items: [["dots-vertical", lambda x: x]]
    MDIconButton:
        id: voltar
        icon: "arrow-left"
        user_font_size: dp(10)
        pos_hint: {'center_x': 0.1, 'center_y': 0.83}
        md_bg_color: app.theme_cls.primary_dark
        on_press: root.manager.current = "home"
    MDLabel:
        text: "Lista"
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.6, 'center_y': 0.83}
        font_style: "H6"
    ScrollView:
        do_scroll_y: True
        do_scroll_x: True
        bar_color: app.theme_cls.primary_color
        bar_color_active: app.theme_cls.accent_color
        effect_cls: "DampedScrollEffect"
        scroll_type: ['content']
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        size_hint: (1, 0.9)
        MDList:
            id: mdlista
            size_hint_y: 0
            size_hint_x: 1
            OneLineListItem:
                text: "Item 1"
                center_x: 0.8
                halign: "center"
                valign: "center"
            OneLineListItem:
                text: "Item 2"
                center_x: 0.8
                halign: "center"
                valign: "center"
            OneLineListItem:
                text: "Item 3"
                center_x: 0.8
            OneLineListItem:
                text: "Item 4"
                halign: "center"
                valign: "center"
                center_x: 0.8
            OneLineListItem:
                text: "Item 5"
                halign: "center"
                valign: "center"
                center_x: 0.8

<ItensLista>:
    name: "itenslista"
    MDIconButton:
        id: voltar
        icon: "arrow-left"
        user_font_size: dp(10)
        pos_hint: {'center_x': 0.1, 'center_y': 0.94}
        md_bg_color: app.theme_cls.primary_dark
        on_press: root.manager.current = "home"
    TabPageItensLista:
        id: pageitens
        size_hint: (1, 0.9)
        do_default_tab: False
        background_color: (1, 0, 0, .5)
        tab_width: self.size[0]/len(self.tab_list)

        TabbedPanelItem:
            text: 'ListItem'
            background_color: app.theme_cls.primary_dark
            color: app.theme_cls.accent_dark
            ScrollView:
                do_scroll_y: True
                do_scroll_x: True
                bar_color: app.theme_cls.primary_color
                bar_color_active: app.theme_cls.accent_color
                effect_cls: "DampedScrollEffect"
                scroll_type: ['content']
                pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                size_hint: (0.7, 0.7)
                MDList:
                    id: itemlist
                    size_hint_y: 0
                    size_hint_x: 0.7
                    OneLineListItem:
                        text: "Texto 1"
                    TwoLineListItem:
                        text: "Texto 2"
                        secondary_text: "Texto da segunda linha"
                    ThreeLineListItem:
                        text: "Texto 3"
                        secondary_text: "Texto da segunda linha"
        				tertiary_text: "Texto da Terceira lnha"

        TabbedPanelItem:
            text: 'AvatarListItem'
            background_color: app.theme_cls.primary_dark
            color: app.theme_cls.accent_dark
            ScrollView:
                do_scroll_y: True
                do_scroll_x: True
                bar_color: app.theme_cls.primary_color
                bar_color_active: app.theme_cls.accent_color
                effect_cls: "DampedScrollEffect"
                scroll_type: ['content']
                pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                size_hint: (1, 0.9)
                MDList:
                    id: avataritemlist
                    size_hint_y: 0
                    size_hint_x: 1
        			OneLineAvatarListItem:
        				text: "Texto do Item de uma linha de texto"

        				ImageLeftWidget:
        					source: "imagens\kivymd.png"

        			TwoLineAvatarListItem:
        				text: "Texto do Item de duas linhas de texto"
        				secondary_text: "Texto da segunda linha"

        				ImageLeftWidget:
        					source: "imagens\python.png"

        			ThreeLineAvatarListItem:
        				text: "Texto do Item de três linhas de texto"
                        secondary_text: "Texto da segunda linha"
        				tertiary_text: "Texto da Terceira lnha"

        				ImageLeftWidget:
        					source: "imagens\md_icone.png"

        TabbedPanelItem:
            text: 'AvatarIconListItem'
            background_color: app.theme_cls.primary_dark
            color: app.theme_cls.accent_dark
    		ScrollView:
                do_scroll_y: True
                do_scroll_x: True
                bar_color: app.theme_cls.primary_color
                bar_color_active: app.theme_cls.accent_color
                effect_cls: "DampedScrollEffect"
                scroll_type: ['content']
                pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                size_hint: (1, 0.9)
        		MDList:
        			id: avatariconitemlist
        			size_hint_y: 0
        			size_hint_x: 1
        			OneLineAvatarIconListItem:
        				text: "Texto do Item de uma linha com imagem à esquerda e ícone à direita"

        				ImageLeftWidget:
        					source: "imagens\kivymd.png"

        				IconRightWidget:
        					icon: "baby-face"

        			TwoLineAvatarIconListItem:
        				text: "Texto do Item de duas linhas com ícone à direita"
        				secondary_text: "Texto da segunda linha"

    					IconRightWidget:
    						icon: "cat"

        			ThreeLineAvatarIconListItem:
        				text: "Texto do Item de três linhas com ícone à esquerda"
        				secondary_text: "Texto da segunda linha"
        				tertiary_text: "Texto da Terceira lnha"

    					IconLeftWidget:
    						icon: "panda"

        TabbedPanelItem:
            text: 'IconListItem'
            background_color: app.theme_cls.primary_dark
            color: app.theme_cls.accent_dark
    		ScrollView:
                do_scroll_y: True
                do_scroll_x: True
                bar_color: app.theme_cls.primary_color
                bar_color_active: app.theme_cls.accent_color
                effect_cls: "DampedScrollEffect"
                scroll_type: ['content']
                pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                size_hint: (1, 0.9)
                MDList:
                    id: itemiconlist
                    size_hint_y: 0
                    size_hint_x: 1
        			OneLineIconListItem:
        				text: "Texto do Item de uma linha com dois ícones à esquerda"

        				IconLeftWidget:
        					icon: "language-python"

        				IconLeftWidget:
        					icon: "plus"

        			TwoLineIconListItem:
        				text: "Texto do Item de duas linhas com um ícone à esquerda"
        				secondary_text: "Texto da segunda linha"

        				IconLeftWidget:
        					icon: "robot-dead"

        			ThreeLineIconListItem:
        				text: "Texto do Item de três linhas com um ícone à direita"
        				secondary_text: "Texto da segunda linha"
        				tertiary_text: "Texto da Terceira lnha"

                        IconLeftWidget:
    						icon: "language-python"

        TabbedPanelItem:
            id: bodytouch
            text: 'BodyTouch'
            background_color: app.theme_cls.primary_dark
            color: app.theme_cls.accent_dark
    		Label:
        		id: lblcat
        		text: "Clicando no ícone do gato, este texto será alterado!"
        		pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        	ScrollView:
                do_scroll_y: True
                do_scroll_x: True
                bar_color: app.theme_cls.primary_color
                bar_color_active: app.theme_cls.accent_color
                effect_cls: "DampedScrollEffect"
                scroll_type: ['content']
                pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                size_hint: (1, 0.8)
                MDList:
                    id: tbody
                    size_hint_y: 0
                    size_hint_x: 1
        			OneLineIconListItem:
        				text: "Texto para OneLineIconListItem sem ação sobre o botão"

        				IconLeftWidgetWithoutTouch:
                            icon: "language-python"

        			OneLineIconListItem:
        				text: "Texto para OneLineIconListItem com ação sobre o botão à esquerda"

                        IconLeftSampleWidget:
                            icon: "cat"

        			OneLineAvatarIconListItem:
        				text: "Texto para OneLineIconListItem com ação sobre o botão à direita"

        				IconRightSampleWidget:
                            icon: "robot-dead"

<PageMDTabs>:
    name: "pagemdtabs"
    BoxLayout:
        orientation: "horizontal"
        MDTopAppBar:
            title: "Exemplos de Tabs"
            pos_hint: {'center_x': 0.95, 'center_y': 0.95}
            md_bg_color: app.theme_cls.primary_color
    MDTabs:
        id: mdtabs
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        Tab:
            text: "Tab 1"
            MDLabel:
                text: "Texto da Tab 1"
                size_hint_x: 0.5
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        Tab:
            text: "Tab 2"
            MDIconButton:
                icon: "robot-dead"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

'''
