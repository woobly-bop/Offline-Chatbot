# screens/chatbot_screen.py
import sys, os

from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.label import MDLabel
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.button import MDIconButton, MDFillRoundFlatButton, MDFillRoundFlatIconButton, MDFloatingActionButton

from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.metrics import dp, sp
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.utils import platform

# local imports
from .myrst import MyRstDocument

# get path details
if getattr(sys, 'frozen', False):
    # Running as a PyInstaller bundle
    base_path = sys._MEIPASS
    noto_font = os.path.join(base_path, "data/fonts/NotoSans-Merged.ttf")
else:
    # Running in a normal Python environment
    base_path = os.path.dirname(os.path.abspath(__file__))
    noto_font = os.path.abspath(os.path.join(base_path, "..", "data/fonts/NotoSans-Merged.ttf"))

Builder.load_string('''
#:import parse_color kivy.parser.parse_color
#:import Window kivy.core.window.Window

<TempSpinWait>:
    id: temp_spin
    orientation: 'horizontal'
    adaptive_height: True
    padding: dp(12)
    canvas.before:
        Color:
            rgba: parse_color('#e3f2fd')
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [15,]

    MDLabel:
        text: root.text
        font_style: "Subtitle1"
        adaptive_width: True
        theme_text_color: "Custom"
        text_color: parse_color('#1976d2')

    MDSpinner:
        size_hint: None, None
        size: dp(20), dp(20)
        active: True
        color: parse_color('#1976d2')

<UsrResp>:
    orientation: 'vertical'
    size_hint: None, None
    width: dp(300)
    height: content.texture_size[1] + dp(24)
    pos_hint: {"right": 1}
    padding: dp(16), dp(12)
    spacing: dp(4)
    canvas.before:
        # Message shadow
        Color:
            rgba: 0, 0, 0, 0.1
        RoundedRectangle:
            size: self.width + dp(2), self.height + dp(2)
            pos: self.x - dp(1), self.y - dp(2)
            radius: [20, 20, 4, 20]
        # Main message bubble
        Color:
            rgba: parse_color('#2196f3')
        RoundedRectangle:
            size: self.width, self.height
            pos: self.pos
            radius: [20, 20, 4, 20]

    MDLabel:
        id: content
        font_style: "Body1"
        text: root.text
        markup: True
        size_hint_y: None
        height: self.texture_size[1]
        text_size: root.width - dp(32), None
        halign: 'right'
        allow_selection: True
        allow_copy: True
        theme_text_color: "Custom"
        text_color: parse_color('#ffffff')
        padding: 0

<BotResp>:
    orientation: 'vertical'
    size_hint: None, None
    width: dp(400)
    height: self.minimum_height + dp(12)
    pos_hint: {"x": 0}
    padding: dp(16), dp(12)
    spacing: dp(8)
    canvas.before:
        # Message shadow
        Color:
            rgba: 0, 0, 0, 0.08
        RoundedRectangle:
            size: self.width + dp(2), self.height + dp(2)
            pos: self.x - dp(1), self.y - dp(2)
            radius: [4, 20, 20, 20]
        # Main message bubble
        Color:
            rgba: parse_color('#f5f5f5')
        RoundedRectangle:
            size: self.width, self.height
            pos: self.pos
            radius: [4, 20, 20, 20]

    MyRstDocument:
        id: rst_content
        base_font_size: 36
        padding: 4
        text: root.text
        background_color: parse_color('#f5f5f5')

    MDBoxLayout:
        orientation: 'horizontal'
        padding: dp(4)
        size_hint_y: None
        height: self.minimum_height
        Widget:
            size_hint_x: 1
        MDFloatingActionButton:
            icon: 'content-copy'
            type: 'small'
            theme_icon_color: "Custom"
            md_bg_color: parse_color('#2196f3')
            icon_color: parse_color('#ffffff')
            on_release: app.copy_final_msg(self)

<BotTmpResp>:
    orientation: 'vertical'
    size_hint: None, None
    width: dp(400)
    height: content.texture_size[1] + dp(48)
    pos_hint: {"x": 0}
    padding: dp(16), dp(12)
    spacing: dp(8)
    canvas.before:
        # Message shadow
        Color:
            rgba: 0, 0, 0, 0.08
        RoundedRectangle:
            size: self.width + dp(2), self.height + dp(2)
            pos: self.x - dp(1), self.y - dp(2)
            radius: [4, 20, 20, 20]
        # Main message bubble
        Color:
            rgba: parse_color('#f5f5f5')
        RoundedRectangle:
            size: self.width, self.height
            pos: self.pos
            radius: [4, 20, 20, 20]

    MDLabel:
        id: content
        font_style: "Body1"
        text: root.text
        valign: 'top'
        halign: 'left'
        padding: 4
        theme_text_color: "Custom"
        text_color: parse_color('#424242')
        size_hint_y: None
        height: self.texture_size[1]
        text_size: root.width - dp(32), None

    MDBoxLayout:
        orientation: 'horizontal'
        spacing: dp(8)
        size_hint_y: None
        height: self.minimum_height
        Widget:
            size_hint_x: 1
        MDFloatingActionButton:
            icon: 'content-copy'
            type: 'small'
            theme_icon_color: "Custom"
            md_bg_color: parse_color('#2196f3')
            icon_color: parse_color('#ffffff')
            on_release: app.copy_tmp_msg(self)
        MDFloatingActionButton:
            icon: 'stop'
            type: 'small'
            theme_icon_color: "Custom"
            md_bg_color: parse_color('#ff5722')
            icon_color: parse_color('#ffffff')
            on_release: app.stop_chat()

<ChatbotScreen>:
    canvas.before:
        # Light background
        Color:
            rgba: parse_color('#ffffff')
        Rectangle:
            pos: self.pos
            size: self.size

    MDBoxLayout:
        orientation: 'vertical'
        padding: 0, root.top_pad, 0, root.bottom_pad

        # Top bar with blue theme
        MDBoxLayout:
            orientation: 'horizontal'
            adaptive_height: True
            spacing: dp(12)
            padding: dp(12), dp(10)
            canvas.before:
                Color:
                    rgba: parse_color('#1976d2')
                Rectangle:
                    size: self.width, self.height
                    pos: self.pos

            MDFillRoundFlatIconButton:
                icon: "chat-plus"
                text: "New"
                md_bg_color: parse_color('#0d47a1')
                text_color: parse_color('#ffffff')
                icon_color: parse_color('#ffffff')
                font_size: sp(12)
                size_hint_x: None
                width: dp(100)
                pos_hint: {'center_y': 0.5}
                on_release: app.new_chat()

            MDDropDownItem:
                on_release: app.llm_menu.open()
                text: "Model"
                id: llm_menu
                font_size: sp(16)
                bold: True
                pos_hint: {'center_y': 0.5}
                md_bg_color: parse_color('#0d47a1')
                theme_text_color: "Custom"
                text_color: parse_color('#ffffff')

            MDDropDownItem:
                on_release: app.token_menu.open()
                text: "Length"
                id: token_menu
                font_size: sp(16)
                bold: True
                pos_hint: {'center_y': 0.5}
                md_bg_color: parse_color('#0d47a1')
                theme_text_color: "Custom"
                text_color: parse_color('#ffffff')

            Widget:
                size_hint_x: 1

            MDIconButton:
                icon: "menu"
                theme_icon_color: "Custom"
                icon_color: parse_color('#ffffff')
                on_release: app.menu_bar_callback(self)

        # Chat history section
        MDScrollView:
            size_hint_y: 0.7
            adaptive_height: True
            canvas.before:
                Color:
                    rgba: parse_color('#fafafa')
                Rectangle:
                    size: self.width, self.height
                    pos: self.pos

            MDBoxLayout:
                id: chat_history_id
                padding: dp(12)
                orientation: 'vertical'
                spacing: dp(16)
                size_hint_y: None
                height: self.minimum_height

        # Input section with light styling
        MDBoxLayout:
            size_hint_y: 0.2
            orientation: 'horizontal'
            spacing: dp(12)
            padding: dp(16), dp(12)
            adaptive_height: True
            canvas.before:
                Color:
                    rgba: parse_color('#f5f5f5')
                Rectangle:
                    size: self.width, self.height
                    pos: self.pos

            MDIconButton:
                id: rag_doc
                icon: "file-document-plus"
                icon_size: sp(24)
                pos_hint: {'center_y': 0.5}
                theme_icon_color: "Custom"
                icon_color: parse_color('#1976d2')
                on_release: app.rag_file_manager()

            MDTextField:
                id: chat_input
                font_name: root.noto_path
                hint_text: "Ask anything..."
                mode: "rectangle"
                multiline: True
                max_height: dp(200)
                size_hint_x: 0.75
                input_type: 'text'
                keyboard_suggestions: True
                font_size: sp(16)
                theme_text_color: "Custom"
                text_color: parse_color('#212121')
                hint_text_color: parse_color('#757575')
                line_color_focus: parse_color('#2196f3')

            MDFloatingActionButton:
                icon: "send"
                type: "standard"
                pos_hint: {'center_y': 0.5}
                md_bg_color: parse_color('#2196f3')
                icon_color: parse_color('#ffffff')
                on_release: app.send_message(self, chat_input)

''')

class TempSpinWait(MDBoxLayout):
    text = StringProperty("")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class UsrResp(MDBoxLayout):
    text = StringProperty("")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class BotTmpResp(MDBoxLayout):
    text = StringProperty("")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class BotResp(MDBoxLayout):
    text = StringProperty("")
    given_id = NumericProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class ChatbotScreen(MDScreen):
    noto_path = StringProperty()
    top_pad = NumericProperty(0)
    bottom_pad = NumericProperty(0)
    def __init__(self, noto=noto_font, **kwargs):
        super().__init__(**kwargs)
        self.name = 'chatbot_screen'
        self.noto_path = noto
        if platform == "android":
            try:
                from android.display_cutout import get_height_of_bar
                self.top_pad = int(get_height_of_bar('status'))
                self.bottom_pad = int(get_height_of_bar('navigation'))
            except Exception as e:
                print(f"Failed android 15 padding: {e}")
                self.top_pad = 32
                self.bottom_pad = 48
