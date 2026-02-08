import os, sys

from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton, MDFillRoundFlatButton

from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.metrics import dp, sp
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.utils import platform

# get path details
if getattr(sys, 'frozen', False):
    # Running as a PyInstaller bundle
    base_path = sys._MEIPASS
    favicon = os.path.join(base_path, "data/images/favicon.png")
else:
    # Running in a normal Python environment
    base_path = os.path.dirname(os.path.abspath(__file__))
    favicon = os.path.abspath(os.path.join(base_path, "..", "data/images/favicon.png"))

Builder.load_string('''
#:import parse_color kivy.parser.parse_color

<WelcomeScreen>:
    canvas.before:
        # Modern gradient background
        Color:
            rgba: parse_color('#0f0c29')
        Rectangle:
            pos: self.pos
            size: self.size
        Color:
            rgba: parse_color('#302b63')
        Rectangle:
            pos: self.x, self.y + self.height * 0.3
            size: self.width, self.height * 0.4
        Color:
            rgba: parse_color('#24243e')
        Rectangle:
            pos: self.x, self.y + self.height * 0.6
            size: self.width, self.height * 0.4

    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(40), dp(60), dp(40), dp(60)
        spacing: dp(30)
        pos_hint: {"center_x": .5, "center_y": .5}

        # Icon/Logo area with glow effect
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            spacing: dp(10)
            
            MDIcon:
                icon: "robot-happy"
                halign: 'center'
                font_size: dp(80)
                theme_text_color: "Custom"
                text_color: parse_color('#bb86fc')
                adaptive_height: True

        # Main title with gradient text effect
        MDLabel:
            font_style: "H3"
            halign: 'center'
            adaptive_height: True
            markup: True
            bold: True
            text: "[b]OFFLINE AI CHATBOT[/b]"
            theme_text_color: "Custom"
            text_color: parse_color('#e1bee7')

        # Subtitle
        MDLabel:
            font_style: "H6"
            halign: 'center'
            adaptive_height: True
            markup: True
            text: "[i]PBL project by DEEP KIRAN KAUR[/i]"
            theme_text_color: "Custom"
            text_color: parse_color('#a29bfe')

        # Features cards
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            spacing: dp(15)
            padding: dp(20), dp(10)
            
            # Feature 1
            MDBoxLayout:
                orientation: 'horizontal'
                adaptive_height: True
                spacing: dp(15)
                padding: dp(15)
                canvas.before:
                    Color:
                        rgba: parse_color('#6c5ce7')
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [15,]
                        
                MDIcon:
                    icon: "brain"
                    font_size: dp(30)
                    theme_text_color: "Custom"
                    text_color: parse_color('#ffffff')
                    size_hint_x: None
                    width: dp(40)
                    
                MDLabel:
                    font_style: "Body1"
                    text: "Run powerful AI models on your device"
                    theme_text_color: "Custom"
                    text_color: parse_color('#ffffff')
                    adaptive_height: True
            
            # Feature 2
            MDBoxLayout:
                orientation: 'horizontal'
                adaptive_height: True
                spacing: dp(15)
                padding: dp(15)
                canvas.before:
                    Color:
                        rgba: parse_color('#a29bfe')
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [15,]
                        
                MDIcon:
                    icon: "shield-lock"
                    font_size: dp(30)
                    theme_text_color: "Custom"
                    text_color: parse_color('#ffffff')
                    size_hint_x: None
                    width: dp(40)
                    
                MDLabel:
                    font_style: "Body1"
                    text: "100% Private & Offline - No internet needed"
                    theme_text_color: "Custom"
                    text_color: parse_color('#ffffff')
                    adaptive_height: True
            
            # Feature 3
            MDBoxLayout:
                orientation: 'horizontal'
                adaptive_height: True
                spacing: dp(15)
                padding: dp(15)
                canvas.before:
                    Color:
                        rgba: parse_color('#fd79a8')
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [15,]
                        
                MDIcon:
                    icon: "file-document-multiple"
                    font_size: dp(30)
                    theme_text_color: "Custom"
                    text_color: parse_color('#ffffff')
                    size_hint_x: None
                    width: dp(40)
                    
                MDLabel:
                    font_style: "Body1"
                    markup: True
                    text: "Ask questions from your [b]PDF & DOCX[/b] files"
                    theme_text_color: "Custom"
                    text_color: parse_color('#ffffff')
                    adaptive_height: True

        Widget:
            size_hint_y: None
            height: dp(20)

        # Start button with modern styling
        MDFillRoundFlatButton:
            id: btn_start_chat
            pos_hint: {'center_x': 0.5}
            size_hint: 0.6, None
            height: dp(56)
            text: "Start Chatting"
            font_size: sp(20)
            md_bg_color: parse_color('#bb86fc')
            text_color: parse_color('#0f0c29')
            on_release: app.start_from_welcome()

        MDLabel:
            id: download_stat
            font_style: "Caption"
            halign: 'center'
            adaptive_height: True
            text: "Powered by ONNX Runtime"
            theme_text_color: "Custom"
            text_color: parse_color('#74b9ff')

''')

class WelcomeScreen(MDScreen):
    fav_path = StringProperty()
    top_pad = NumericProperty(0)
    bottom_pad = NumericProperty(0)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'welcome_screen'
        self.fav_path = favicon

