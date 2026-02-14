from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDList, OneLineIconListItem, IconLeftWidget, IconRightWidget, OneLineAvatarIconListItem

from kivy.uix.accordion import Accordion, AccordionItem
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.metrics import dp, sp
from kivy.utils import platform

# local imports

Builder.load_string('''
#:import parse_color kivy.parser.parse_color

<DeleteModelItems@OneLineAvatarIconListItem>:
    theme_text_color: "Custom"
    text_color: parse_color('#212121')
    md_bg_color: parse_color('#ffffff')
    _no_ripple_effect: False
    
    IconLeftWidget:
        icon: "robot-happy"
        theme_text_color: "Custom"
        text_color: parse_color('#1976d2')
        
    IconRightWidget:
        icon: "delete"
        on_release: app.init_delete_model(root.text)
        theme_text_color: "Custom"
        text_color: parse_color('#f44336')

<SettingsBox>:
    orientation: 'vertical'
    padding: 0, root.top_pad, 0, root.bottom_pad
    canvas.before:
        # Light background
        Color:
            rgba: parse_color('#fafafa')
        Rectangle:
            pos: self.pos
            size: self.size

    # Header
    MDBoxLayout:
        orientation: 'vertical'
        adaptive_height: True
        padding: dp(20), dp(20)
        spacing: dp(10)
        canvas.before:
            Color:
                rgba: parse_color('#1976d2')
            Rectangle:
                pos: self.pos
                size: self.size
        
        MDLabel:
            text: "Settings"
            font_style: "H4"
            halign: "center"
            adaptive_height: True
            theme_text_color: "Custom"
            text_color: parse_color('#ffffff')
            bold: True

    Accordion:
        orientation: 'vertical'
        padding: dp(16)
        spacing: dp(12)

        AccordionItem:
            title: "Manage Downloaded Models"
            title_template: "AccordionItemTitle"
            background_normal: ""
            background_selected: ""
            canvas.before:
                Color:
                    rgba: parse_color('#2196f3')
                RoundedRectangle:
                    size: self.width, self.height if self.collapse else dp(48)
                    pos: self.pos
                    radius: [15,]

            MDScrollView:
                canvas.before:
                    Color:
                        rgba: parse_color('#ffffff')
                    RoundedRectangle:
                        size: self.width, self.height
                        pos: self.pos
                        radius: [10,]
                        
                adaptive_height: True
                MDList:
                    id: delete_model_list
                    padding: dp(8)
                    spacing: dp(8)

    Widget:
        size_hint_y: 1

    # Bottom navigation
    MDBoxLayout:
        size_hint_y: None
        height: dp(80)
        orientation: 'horizontal'
        spacing: dp(12)
        padding: dp(20), dp(12)
        canvas.before:
            Color:
                rgba: parse_color('#f5f5f5')
            Rectangle:
                size: self.width, self.height
                pos: self.pos
                
        MDFillRoundFlatIconButton:
            id: setting_to_chat
            icon: "arrow-left"
            text: "Back to Chat"
            size_hint_x: 1
            height: dp(56)
            font_size: sp(18)
            md_bg_color: parse_color('#1976d2')
            text_color: parse_color('#ffffff')
            icon_color: parse_color('#ffffff')
            on_release: app.go_to_chat_screen()

''')

class DeleteModelItems(OneLineAvatarIconListItem):
    pass

class SettingsBox(MDBoxLayout):
    """ The main settings box which contains the setting, help & other required sections """
    top_pad = NumericProperty(0)
    bottom_pad = NumericProperty(0)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if platform == "android":
            try:
                from android.display_cutout import get_height_of_bar
                self.top_pad = int(get_height_of_bar('status'))
                self.bottom_pad = int(get_height_of_bar('navigation'))
            except Exception as e:
                print(f"Failed android 15 padding: {e}")
                self.top_pad = 32
                self.bottom_pad = 48
