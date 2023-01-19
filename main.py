from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
#from helper import screen_helper

screen_helper = """
ScreenManager:
    LoginScreen:
    MainScreen:

<MainScreen>:
    name: 'mainscreen'
    MDScreen:
        orientation: 'vertical'
        # padding: dp(10)

        MDBottomNavigation:
            panel_color: '#3685FD'
            selected_color_background: 'sandybrown'
            text_color_active: 'sandybrown'
            text_color_normal: 'lightgrey'
            text_size: '20dp'
            padding: dp(8)
            radius: dp(12)
            
            MDBottomNavigationItem:
                name: 'casa'
                text: 'Casa'
                icon: 'home.png'
                MDScreen:
                    orientation: 'vertical'
                    MDLabel:
                        text: 'Home Page'
                        font_style: 'H2'
                        halign: 'center'
                        pos_hint: {'center_x':.5, 'center_y':.7}
                    MDRoundFlatButton:
                        text: 'Back'
                        pos_hint: {'center_x':.5, 'center_y':.5}
                        on_press: root.manager.current='login'
        
            MDBottomNavigationItem:
                name: 'gerador'
                text: 'Gerador'
                icon: 'gerador.png'            
                MDScreen:
                    orientation: 'vertical'
                    MDLabel:
                        text: 'Aluguel do gerador'
                        font_style: 'H2'
                        halign: 'center'
                        pos_hint: {'center_x':.5, 'center_y':.7}
                    MDRoundFlatButton:
                        text: 'Back'
                        pos_hint: {'center_x':.5, 'center_y':.5}
                        on_press: root.manager.current='login'
            
            MDBottomNavigationItem:
                name: 'recarregar'
                text: 'Recarregar'
                icon: 'recarregar-bottombar.png'                
                MDScreen:
                    orientation: 'vertical'
                    MDLabel:
                        text: 'Recarregar o PV'
                        font_style: 'H2'
                        halign: 'center'
                        pos_hint: {'center_x':.5, 'center_y':.7}
                    MDRoundFlatButton:
                        text: 'Back'
                        pos_hint: {'center_x':.5, 'center_y':.5}
                        on_press: root.manager.current='login'
        
            MDBottomNavigationItem:
                name: 'sobre'
                text: 'Sobre'
                icon: 'sobre.png'                
                MDScreen:
                    orientation: 'vertical'
                    MDLabel:
                        text: 'Sobre a SolarGen'
                        font_style: 'H2'
                        halign: 'center'
                        pos_hint: {'center_x':.5, 'center_y':.7}
                    MDRoundFlatButton:
                        text: 'Back'
                        pos_hint: {'center_x':.5, 'center_y':.5}
                        on_press: root.manager.current='login'
        
            MDBottomNavigationItem:
                name: 'profile'
                text: 'Eu'
                icon: 'profile.png'              
                MDScreen:
                    orientation: 'vertical'
                    MDLabel:
                        text: 'Profile'
                        font_style: 'H2'
                        halign: 'center'
                        pos_hint: {'center_x':.5, 'center_y':.7}
                    MDGridLayout:
                        rows: 3
                        cols: 3
                        MDIconButton:
                            icon: 'logout'
                    MDRoundFlatButton:
                        text: 'Back'
                        pos_hint: {'center_x':.5, 'center_y':.5}
                        on_press: root.manager.current='login'


<LoginScreen>:
    name: 'login'
    FloatLayout:
        orientation: 'vertical'

        Image:
            source: 'logo01.png'
            pos_hint: {'center_x':0.48, 'center_y': 0.8}
            size_hint: (0.5, 0.5)


        MDLabel:
            hint_text: "+244"
            pos_hint: {'center_x':0.4, 'center_y':0.6}


        MDTextField:
            hint_text: "Usuário/Telefone"
            helper_text: " "
            helper_text_mode: "on_focus"
            icon_right: "phone"
            icon_right_color: app.theme_cls.primary_color
            pos_hint: {'center_x':0.5, 'center_y':0.6}
            size_hint_x: None
            width: 340

        MDTextField:
            hint_text: "Palavra-passe"
            helper_text: "Esqueceu a password?"
            helper_text_mode: "on_focus"
            password: True
            icon_right: "key"
            icon_right_color: app.theme_cls.primary_color
            pos_hint: {'center_x':0.5, 'center_y':0.5}
            size_hint_x: None
            width: 340

        MDFillRoundFlatButton:
            text: '  Login  '
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
            font_style: 'Button'
            on_press: root.manager.current='mainscreen'

"""


class LoginScreen(Screen):
    pass

class MainScreen(Screen):
    def navigation_draw(self):
        print('Navigation')

#class ProfileScreen(Screen):
    #pass

# class GiftSCreen(Screen):
    # pass

# class TaskSCreen(Screen):
    # pass

sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(MainScreen(name='mainscreen'))


# sm.add_widget(ProfileScreen(name='profile'))

class SolargenApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Blue"
        screen = Builder.load_string(screen_helper)
        return screen


SolargenApp().run()
