__debug_build__ = True
__version__ = "0.0.1"
__version_variant__ = "beta"
__version_date_time__ = "2024-10-31 00:00"
__copyright_short__ = "Copyright (c) 2024 Sebastian Obele / obele.eu / MIT License"
__copyright_url__ = "https://obele.eu"
__title__ = "PythonKivyAppExample"
__header__ = "Welcome to PythonKivyAppExample!"
__description__ = "Test app"
__author__ = "Sebastian Obele"
__author_email__ = "info@obele.eu"
__package_domain__ = "eu.obele"
__package_name__ = "pythonkivyappexample"


from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
from kivy.properties import StringProperty
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.label import MDLabel


import os
import sys
import json


from kivy.logger import Logger, LOG_LEVELS

if __debug_build__:
    Logger.setLevel(LOG_LEVELS["debug"])
else:
    Logger.setLevel(LOG_LEVELS["error"])


KV = """
#: import SlideTransition kivy.uix.screenmanager.SlideTransition

MDNavigationLayout:
    md_bg_color: app.theme_cls.bg_darkest

    ScreenManager:
        id: screen_manager
        transition: SlideTransition()

        MDScreen:
            name: "main"

            BoxLayout:
                orientation: "vertical"

                MDBoxLayout:
                    orientation: "vertical"
                    spacing: dp(0)
                    size_hint_y: None
                    height: dp(20)
                    padding: [dp(10), dp(0), dp(10), dp(0)]
                    md_bg_color: app.theme_cls.primary_color

                    MDLabel:
                        id: header
                        text: ""
                        text_size: self.width, None
                        shorten: True
                        shorten_from: "right"
                        theme_text_color: "Custom"
                        text_color: [1, 1, 1, 1]
                        height: dp(20)
                        bold: True
                        halign: "center"

                MDTopAppBar:
                    id: toolbar
                    title: ""
                    anchor_title: "left"
                    elevation: 0
                    left_action_items:
                        [
                        ["power-standby", lambda x: app.close(), ""],
                        ]
                    right_action_items:
                        [
                        ["clipboard-outline", lambda x: app.log_copy(), ""],
                        ["trash-can", lambda x: app.log_delete(), ""],
                        ]

                MDBottomNavigation:
                    id: tabs
                    selected_color_background: 0, 0, 0, 0
                    transition_duration: 0


                    MDBottomNavigationItem:
                        id: execute_tab
                        name: "execute_tab"
                        text: "Execute"
                        icon: "cogs"

                        ScrollView:
                            effect_cls: "ScrollEffect"
                            size_hint: 1.0, 1.0
                            bar_width: dp(10)
                            bar_color: [.7, .7, .7, .9]
                            bar_inactive_color: [.7, .7, .7, .9]
                            scroll_type: ["bars", "content"]
                            scroll_wheel_distance: dp(100)

                            MDBoxLayout:
                                orientation: "vertical"
                                spacing: dp(15)
                                size_hint_y: None
                                height: self.minimum_height
                                padding: [dp(10), dp(10), dp(10), dp(10)]

                                MDCard:
                                    orientation: "vertical"
                                    spacing: dp(20)
                                    size_hint_y: None
                                    height: self.minimum_height
                                    padding: [dp(10), dp(10), dp(10), dp(10)]
                                    radius: [0]

                                    MDLabel:
                                        text: "Example functions"
                                        font_style: "H6"

                                    MDRectangleFlatButton:
                                        text: "execute_1"
                                        size_hint: [1.0, None]
                                        on_release: app.execute_1()


                    MDBottomNavigationItem:
                        id: log_tab
                        name: "log_tab"
                        text: "Log"
                        icon: "text"

                        RecycleView:
                            id: log_view
                            viewclass: "LogViewRow"
                            effect_cls: "ScrollEffect"
                            size_hint: 1.0, 1.0
                            bar_width: dp(10)
                            bar_color: [.7, .7, .7, .9]
                            bar_inactive_color: [.7, .7, .7, .9]
                            scroll_type: ["bars", "content"]
                            scroll_wheel_distance: dp(100)
                            RecycleBoxLayout:
                                spacing: dp(0)
                                default_size: None, None
                                default_size_hint: 1, None
                                orientation: "vertical"
                                size_hint_y: None
                                height: self.minimum_height
                                padding: [dp(10), dp(0), dp(10), dp(0)]


                    MDBottomNavigationItem:
                        id: cfg_tab
                        name: "cfg_tab"
                        text: "Config"
                        icon: "tools"

                        ScrollView:
                            effect_cls: "ScrollEffect"
                            size_hint: 1.0, 1.0
                            bar_width: dp(10)
                            bar_color: [.7, .7, .7, .9]
                            bar_inactive_color: [.7, .7, .7, .9]
                            scroll_type: ["bars", "content"]
                            scroll_wheel_distance: dp(100)

                            MDBoxLayout:
                                orientation: "vertical"
                                spacing: dp(20)
                                size_hint_y: None
                                height: self.minimum_height
                                padding: [dp(10), dp(10), dp(10), dp(10)]

                                MDCard:
                                    orientation: "vertical"
                                    spacing: dp(20)
                                    size_hint_y: None
                                    height: self.minimum_height
                                    padding: [dp(10), dp(10), dp(10), dp(10)]
                                    radius: [0]

                                    MDRectangleFlatButton:
                                        text: "Reset Config"
                                        size_hint: [1.0, None]
                                        on_release: app.cfg_reset()

                                    MDRectangleFlatButton:
                                        text: "Load config"
                                        size_hint: [1.0, None]
                                        on_release: app.cfg_load()

                                    MDRectangleFlatButton:
                                        text: "Save config"
                                        size_hint: [1.0, None]
                                        on_release: app.cfg_save()

                                MDCard:
                                    orientation: "vertical"
                                    spacing: dp(20)
                                    size_hint_y: None
                                    height: self.minimum_height
                                    padding: [dp(10), dp(10), dp(10), dp(10)]
                                    radius: [0]

                                    MDTextField:
                                        id: cfg_server
                                        multiline: False
                                        hint_text: "Server (DNS or IP without Port)"
                                        helper_text: "Default:"
                                        helper_text_mode: "persistent"
                                        text: ""
                                        disabled: False
                                        write_tab: False
                                        text_color_focus: app.theme_cls.text_color
                                        text_color_normal: app.theme_cls.text_color


                    MDBottomNavigationItem:
                        id: infos_tab
                        name: "infos_tab"
                        text: "Infos"
                        icon: "information-variant"
                        on_tab_release: app.infos_action()

                        ScrollView:
                            effect_cls: "ScrollEffect"
                            size_hint: 1.0, 1.0
                            bar_width: dp(10)
                            bar_color: [.7, .7, .7, .9]
                            bar_inactive_color: [.7, .7, .7, .9]
                            scroll_type: ["bars", "content"]
                            scroll_wheel_distance: dp(100)

                            MDBoxLayout:
                                orientation: "vertical"
                                spacing: dp(15)
                                size_hint_y: None
                                height: self.minimum_height
                                padding: [dp(10), dp(10), dp(10), dp(10)]

                                MDCard:
                                    orientation: "vertical"
                                    spacing: dp(20)
                                    size_hint_y: None
                                    height: self.minimum_height
                                    padding: [dp(10), dp(10), dp(10), dp(10)]
                                    radius: [0]

                                    MDLabel:
                                        id: infos_copyright_title
                                        text: ""
                                        font_style: "H6"

                                    MDLabel:
                                        id: infos_copyright_text
                                        markup: True
                                        text: ""
                                        size_hint_y: None
                                        text_size: self.width, None
                                        height: self.texture_size[1]

<LogViewRow>:
    text: root.text
    markup: True
    size_hint_y: None
    text_size: self.width, None
    height: self.texture_size[1]
"""


class LogViewRow(MDLabel):
    text = StringProperty()


class MainApp(MDApp):
    #################################################
    # Init/Build                                    #
    #################################################


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.log_init()

        self.cfg_init()


    def on_start(self):
        self.cfg_load()
        self.root.ids.toolbar.title = __title__
        self.root.ids.header.text = __header__


    def build(self):
        return Builder.load_string(KV)


    def close(self):
        self.stop()


    #################################################
    # Execute                                       #
    #################################################


    def execute_1(self):
        try:
            result = "OK"
            self.log(result, "execute_1")
            return result
        except Exception as e:
            self.log_exception(e, "execute_1")
            return ""


    #################################################
    # Log                                           #
    #################################################


    def log_init(self):
        self.log_data = []


    def log(self, text="", title=""):
        if title != "":
            print("----"+title+"----")
            self.root.ids.header.text = title
            title = "\n\n[b]"+title+"[/b]\n"
        print(text)
        self.root.ids.log_view.data.append({"text": title+text})


    def log_copy(self):
        self.root.ids.header.text = "OK: Log copied"
        text = "\n".join(item["text"] for item in self.root.ids.log_view.data)
        Clipboard.copy(text)


    def log_delete(self):
        self.root.ids.header.text = "OK: Log deleted"
        self.root.ids.log_view.data = []


    def log_exception(self, e, title=""):
        import traceback
        text = "An "+str(type(e))+" occurred: "+str(e)
        self.log(text=text, title="ERROR: "+title)
        self.log(text="".join(traceback.TracebackException.from_exception(e).format()))


    #################################################
    # Cfg                                           #
    #################################################


    def cfg_init(self):
        self.cfg = None

        def get_platform():
            if "ANDROID_ARGUMENT" in os.environ:
                return "android"
            elif "ANDROID_ROOT" in os.environ:
                return "android"
            else:
                return sys.platform

        if get_platform() == "android":
            from plyer import storagepath
            self.cfg_dir = storagepath.get_application_dir()+"/"+__package_domain__+"."+__package_name__+"/files"
        elif get_platform() == "darwin":
            from plyer import storagepath
            self.cfg_dir = storagepath.get_home_dir().replace("file://", "")+"/.config/"+__package_name__
        elif get_platform() == "linux":
            from plyer import storagepath
            self.cfg_dir = storagepath.get_home_dir().replace("file://", "")+"/.config/"+__package_name__
        elif str(get_platform()).startswith("win"):
            from plyer import storagepath
            self.cfg_dir = storagepath.get_home_dir().replace("file://", "")+"/.config/"+__package_name__
        else:
            from plyer import storagepath
            self.cfg_dir = storagepath.get_home_dir().replace("file://", "")+"/.config/"+__package_name__

        if not os.path.isdir(self.cfg_dir):
            os.makedirs(self.cfg_dir)

        self.cfg_file = self.cfg_dir+"/config.json"


    def cfg_load(self):
        try:
            if os.path.exists(self.cfg_file):
                with open(self.cfg_file, "r") as fh:
                    self.cfg = json.load(fh)
        except:
            pass

        if not self.cfg or len(self.cfg) == 0:
            self.cfg_reset()

        self.root.ids.cfg_server.text = self.cfg["cfg_server"].strip()

        self.root.ids.header.text = "OK: Config loaded"


    def cfg_reset(self):
        self.cfg = {
            "cfg_server": ""
        }

        try:
            with open(self.cfg_file, "w") as fh:
                json.dump(self.cfg, fh)
        except:
            pass

        self.cfg_load()

        self.root.ids.header.text = "OK: Config reset"


    def cfg_save(self):
        self.cfg = {
            "cfg_server": self.root.ids.cfg_server.text.strip()
        }

        try:
            with open(self.cfg_file, "w") as fh:
                json.dump(self.cfg, fh)
        except:
            pass

        self.root.ids.header.text = "OK: Config saved"


    #################################################
    # Infos                                         #
    #################################################


    def infos_action(self):
        self.root.ids.infos_copyright_title.text = __title__+" v"+__version__+" "+__version_variant__
        self.root.ids.infos_copyright_text.text = __copyright_short__


#################################################
# Run                                           #
#################################################


from kivy.base import ExceptionManager, ExceptionHandler
class AppExceptionHandler(ExceptionHandler):
    def handle_exception(self, e):
        if isinstance(e, SystemExit):
            return ExceptionManager.RAISE

        import traceback
        print("An unhandled "+str(type(e))+" exception occurred: "+str(e))
        print("".join(traceback.TracebackException.from_exception(e).format()))

        return ExceptionManager.PASS


if __name__ == "__main__":
    MainApp().run()
