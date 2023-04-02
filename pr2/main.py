from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivymd.uix.card import MDCard
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from firebase import firebase
from kivymd.uix.scrollview import MDScrollView

firebase = firebase.FirebaseApplication('https://fitness-ef4f2-default-rtdb.firebaseio.com/', None)
Window.size = (350, 580)


class MD3Card(MDCard):
    text = StringProperty()


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class ProfileWindow(MDScreen):
    pass


class HomeWindow(MDScreen):
    pass


class MainWindow(MDScreen):
    pass


class LoginWindow(MDScreen):
    pass


class WindowManager(MDScreenManager):
    pass


class SignupWindow(MDScreen):
    pass


class FitnessApp(MDApp):

    def build(self, user=False):

        self.theme_cls.material_style = "M3"
        self.stay_data(user)
        return Builder.load_file("main.kv")

    def on_start(self):
        styles = {
            "elevated": "#f6eeee", "filled": "#f4dedc", "outlined": "#f8f5f4"
        }
        for style in styles.keys():
            self.root.ids.box_1.add_widget(
                MD3Card(
                    line_color=(0.2, 0.2, 0.2, 0.8),
                    style=style,
                    text=style.capitalize(),
                    md_bg_color=styles[style],
                    shadow_softness=2 if style == "elevated" else 12,
                    shadow_offset=(0, 1) if style == "elevated" else (0, 2),
                )
            )

    def send_data(self, username, email, password):
        data = {
            'Username': username,
            'Email': email,
            'Password': password

        }
        firebase.post('fitness-ef4f2-default-rtdb/Users', data)

    def verify_data(self, email1, password1, username1=None, user=None):
        result = firebase.get('fitness-ef4f2-default-rtdb/Users', '')

        if user == False:

            for i in result.keys():
                if result[i]['Email'] == email1:

                    if result[i]['Password'] == password1:
                        user = True
                        self.root.current = "home"
                        result[i]['username'] = username1
                        # self.root.app.ids.label_name.text = username1

                    else:
                        print("Incorrect Password")
                else:
                    print("Incorrect Email")
        else:
            self.root.current = 'home'

    def logout_data(self):
        user = False
        self.root.current = "login"

    def stay_data(self, user):
        if user == True:
            self.root.current = "login"

    def see_profile_data(self):
        self.root.current = "profile"


if __name__ == "__main__":
    LabelBase.register(name="MPoppins", fn_regular="font\Poppins\Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins", fn_regular="font\Poppins\Poppins-SemiBold.ttf")
    FitnessApp().run()
