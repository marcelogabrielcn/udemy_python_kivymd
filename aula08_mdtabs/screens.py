appmobile_screen = '''
ScreenManager:
    id: screen_manager
    PageMDTabs:
        id: pagemdtabs

<PageMDTabs>:
    name: "pagemdtabs"
    BoxLayout:
        orientation: "horizontal"
        MDTopAppBar: 
            title: "Exemplo de Tabs"
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
    MDTabs:
        id: mdtabs
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
'''