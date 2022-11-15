
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.scrollview import MDScrollView


KV = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True


MDScreen:
    
    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "orange"
        text_color_active: "lightgrey"
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Каталог'
            icon: 'image-search-outline'
            

            MDLabel:
                text: 'Каталог'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Заявки'
            icon: 'list-box-outline'
            
            
            MDLabel:

                MDTabs:
                    id: tabs


                        
                            
                    
            Widget:
                MDList:
                    MDBoxLayout:
                        adaptive_height: True

                        MDFlatButton:
                            text: "ADD TAB"
                            on_release: app.add_tab()

                        MDFlatButton:
                            text: "REMOVE LAST TAB"
                            on_release: app.remove_tab()

                        MDFlatButton:
                            text: "GET TAB LIST"
                            on_release: app.get_tab_list()
        

                
     


        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Карта'
            icon: 'map-marker'

            MDLabel:
                text: 'Карта'
                halign: 'center'


    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDTopAppBar:
                    title: "MOI PROGA"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#e7e4c0"
                    specific_text_color: "#4a4939"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:

                DrawerClickableItem:
                    icon_radius:(50, 50, 50, 50)
                    icon: "image.jpg"

                    text_color: "#4a4939"
                    text: "profile"
                

                MDNavigationDrawerLabel:
                    text: "Mail"

                DrawerClickableItem:
                    icon: "gmail"
                    right_text: "+99"
                    text_right_color: "#4a4939"
                    text: "Inbox"

                DrawerClickableItem:
                    icon: "send"
                    text: "Outbox"

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "Labels"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Label"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Label"
<Tab>
    MDList:
        size_hint: .9, .95   

'''
class Tab(MDScrollView, MDTabsBase):
    '''Class implementing content for a tab.'''


class Programs(MDApp):
    index = 0
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Orange"
        
        return Builder.load_string(KV)

    def on_start(self):
        self.add_tab()
        Tab(width="200dp")
    def get_tab_list(self):
        '''Prints a list of tab objects.'''

        print(self.root.ids.tabs.get_tab_list())

    def add_tab(self):
        self.index += 1
        self.root.ids.tabs.add_widget(Tab(title=f"{self.index} заявка"))

    def remove_tab(self):
        if self.index > 1:
            self.index -= 1
            self.root.ids.tabs.remove_widget(
            self.root.ids.tabs.get_tab_list()[-1]
        )
           

    

Programs().run()