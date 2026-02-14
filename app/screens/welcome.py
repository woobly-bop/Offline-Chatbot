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

<WelcomeScreen>:
    #on_enter: app.update_chatbot_welcome(self)

    MDBoxLayout: # main box
        orientation: 'vertical'
        # padding: 8, root.top_pad, 8, root.bottom_pad
        padding: "20dp"
        spacing: dp(16)
        adaptive_height: True
        pos_hint: {"center_x": .5, "center_y": .5}

        MDLabel:
            font_style: "H4"
            halign: 'center'
            adaptive_height: True
            markup: True
            text: "OFFLINE AI CHATBOT"

        MDLabel:
            font_style: "H6"
            halign: 'center'
            adaptive_height: True
            markup: True
            text: "PBL project made by DEEP KIRAN KAUR"

        MDLabel:
            font_style: "Body1"
            halign: 'center'
            adaptive_height: True
            text: "This application enables you to run powerful AI models directly on your device without internet. It supports private offline chat and document analysis (RAG) for your PDF and DOCX files."

        MDLabel:
            font_style: "Body1"
            halign: 'center'
            adaptive_height: True
            markup: True
            text: "You can select your local [i][b]PDF[/b][/i] or [i][b]DOCX[/b][/i] file to ask questions on the document."

        MDLabel:
            id: download_stat
            font_style: "Subtitle1"
            halign: 'center'
            adaptive_height: True
            text: "Click Start to go to the chatbot screen"

        MDFillRoundFlatButton:
            id: btn_start_chat
            pos_hint: {'center_x': 0.5}
            size_hint_x: 0.4
            text: "Start"
            font_size: sp(18)
            on_release: app.start_from_welcome()

''')

class WelcomeScreen(MDScreen):
    fav_path = StringProperty()
    top_pad = NumericProperty(0)
    bottom_pad = NumericProperty(0)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'welcome_screen'
        self.fav_path = favicon

