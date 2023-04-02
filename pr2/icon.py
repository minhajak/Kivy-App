from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivymd.app import MDApp
from firebase import firebase

KV = '''
<MD3Card>
    padding: 4
    style:"elevated"
    md_bg_color:"#f6eeee"
    size_hint: None, None
    size: "200dp", "100dp"

    MDRelativeLayout:


        MDLabel:
            id: label
            text: root.text
            adaptive_size: True
            color: "black"
            pos: "12dp", "12dp"
            bold: True


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
        icon_color_active: "lightred"
        text_color: "lightgrey"

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Home'
            icon: 'icon/home1.png'

            MDScreen:

                MDBoxLayout:
                    id: box
                    adaptive_size: True
                    spacing: "56dp"
                    pos_hint: {"center_x": .5, "center_y": .5}

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Workout'
            icon: 'icon/workout-report.png'

            MDLabel:
                text: 'Twitter'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Diet'
            icon: 'icon/diet.png'

            MDLabel:
                text: 'LinkedIN'
                halign: 'center'
    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDTopAppBar:
                    title: "Navigation Drawer"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#e7e4c0"
                    specific_text_color: "#4a4939"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

        MDNavigationDrawer:
            icon: "icon/home.png"
            id: nav_drawer
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:
                icon: "icon/home.png"
                MDNavigationDrawerHeader:
                    title: "Header title"
                    text: "Header text"
                    source: "icon/home.png"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

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


'''


class MD3Card(MDCard):
    '''Implements a material design v3 card.'''

    text = StringProperty()


class Example(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)

    def on_start(self):
        nas = {
            "aaaaaaaaaa",
            "cccccccccccc",
        }
        styles = {
            "elevated": "#f6eeee"
        }
        for na in nas:
            for style in styles.keys():
                self.root.ids.box.add_widget(
                    MD3Card(
                        line_color=(0.2, 0.2, 0.2, 0.8),
                        style=style,
                        text=style.capitalize(),
                        md_bg_color=styles[style],
                        shadow_softness=2 if style == "elevated" else 12,
                        shadow_offset=(0, 1) if style == "elevated" else (0, 2),
                    )
                )


Example().run()


