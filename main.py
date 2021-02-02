from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
#from kivy.animation import Animation
#from kivymd.uix.picker import MDThemePicker



class MainScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass


class LoginScreen(Screen):
    pass

class DashboardScreen(Screen):
    pass

class Tikerwit(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Gray"
        #self.theme_cls.primary_hue = "500"
        #self.theme_cls.theme_style = "Dark"

        self.load_kv('tikerwit.kv')

        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        return sm


Tikerwit().run()
