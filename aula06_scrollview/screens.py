appmobile_screen = '''
ScreenManager:
    id: screen_manager
    HomePage:
        id: home
    
    Scroll:
        id: scroll

<HomePage>:
    name: "home"
    MDRaisedButton:
        id: btn
        text: "Doesn't do anything"
        size_hint_x: 0.2
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        font_size: 16
        md_bg_color: app.theme_cls.primary_color

    MDRaisedButton:
        id: btn
        text: "Scroll"
        size_hint_x: 0.2
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        font_size: 16
        md_bg_color: app.theme_cls.primary_color
        on_press: root.manager.current = 'scroll'

<Scroll>
    name: "scroll"
    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "MDTopAppBar"
            right_action_items: [["dots-vertical", lambda x: app.callback_1()], ["clock", lambda x: app.callback_2()]]
        MDLabel:
            text: "Scroll view exemple"
            halign: "center"
    MDIconButton:
        id: voltar
        icon: "arrow-left"
        user_font_size: dp(10)
        pos_hint: {'center_x': 0.1, 'center_y': 0.85}
        on_press: root.manager.current = 'home'
    ScrollView:
        do_scroll_y: True
        do_scroll_x: True
        bar_color: app.theme_cls.primary_color
        bar_color_acrive: app.theme_cls.accent_color
        effect_cls: "DampedScrollEffect"
        scroll_type: ['content']
        pos_hint: {'center_x': 0.5, 'center_y': 0.20}
        size_hint: (1, 0.9)
        MDGridLayout:
            id: grid
            cols: 1
            size_hint: (1, None)
            size_hint_y: None
            pos_hint: {'center_x': 0.5, 'center_y': 0.20}
            md_bg_color: app.theme_cls.primary_light
            podding_top: "15sp"
            spacing: dp(8)
            MDLabel:
                text: "Primeira linha"
            MDSeparator:
                height: dp(2)
            MDLabel:
                text: "Segunda linha"
            MDSeparator:
                height: dp(2)
            MDLabel:
                text: "Terceira linha"
            MDSeparator:
                height: dp(2)
            MDLabel:
                text: "Primeira linha"
            MDSeparator:
                height: dp(2)
            MDLabel:
                text: "Segunda linha"
            MDSeparator:
                height: dp(2)
            MDLabel:
                text: "Terceira linha"
            MDSeparator:
                height: dp(2)
            MDLabel:
                text: "Primeira linha"
            MDSeparator:
                height: dp(2)
            MDLabel:
                text: "Segunda linha"
            MDSeparator:
                height: dp(2)
            MDLabel:
                text: "Terceira linha"
            MDSeparator:
                height: dp(2)
            MDLabel:
                text: "Primeira linha"
            MDSeparator:
                height: dp(2)
            MDLabel:
                text: "Segunda linha"
            MDSeparator:
                height: dp(2)
            MDLabel:
                text: "Terceira linha"
            MDSeparator:
                height: dp(2)
            MDLabel:
                text: "Primeira linha"
            MDSeparator:
                height: dp(2)
            MDLabel:
                text: "Segunda linha"
            MDSeparator:
                height: dp(2)
            MDLabel:
                text: "Terceira linha"
            MDSeparator:
                height: dp(2)

'''