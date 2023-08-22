import os
os.environ['KIVY_GL_BACKEND'] = 'sdl2'
from kivy.config import Config
Config.set('kivy','keyboard_mode', 'dock')
from ast import Str
import asyncio
import imp
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.app import async_runTouchApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
import time
import random
import threading
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime
from kivymd.app import MDApp
from kivy.clock import Clock
from functools import partial
from multiprocessing import Process, Manager
import keyboard
from kivy.uix.vkeyboard import *
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.utils import get_color_from_hex

class HomeWindow(Screen):
    def __init__(self, wifiApp, **kw):
        self.wifiApp = wifiApp
        super().__init__(**kw)

    def on_pre_enter(self, *args):
        return super().on_pre_enter(*args)

    def on_enter(self, *args):
        wifi_connected = False
        if wifi_connected:
            threading.Thread(target=self.open_visi_help_window,daemon=True).start()
        else:
            threading.Thread(target=self.open_wifi_selector_window,daemon=True).start()
        return super().on_enter(*args)
    
    def open_visi_help_window(self):
        pass

    def open_wifi_selector_window(self):
        time.sleep(10)
        self.wifiApp.openWifiSelectorWindow()
    
    def on_pre_leave(self, *args):
        return super().on_pre_leave(*args)
    
    def on_leave(self, *args):
        return super().on_leave(*args)
    
class WifiSelectorWindow(Screen):
    def __init__(self, wifiApp, **kw):
        self.wifiApp = wifiApp
        self.startNumber = -1
        super().__init__(**kw)

    def on_pre_enter(self, *args):
        self.wifiApp.wifi_selector_window.startNumber = -1
        if len(self.wifiApp.active_wifi_names) > 0:
            self.wifiApp.wifi_selector_window.ids.wifi_name_label_1.text = ""
            self.wifiApp.wifi_selector_window.ids.wifi_name_label_2.text = self.wifiApp.active_wifi_names[0]
            if len(self.wifiApp.active_wifi_names) > 1:
                self.wifiApp.wifi_selector_window.ids.wifi_name_label_3.text = self.wifiApp.active_wifi_names[1]
        else:
            print("Wifi bulunamadı!")

        return super().on_pre_enter(*args)

    def on_enter(self, *args):
        return super().on_enter(*args)
    
    def on_pre_leave(self, *args):
        return super().on_pre_leave(*args)
    
    def on_leave(self, *args):
        return super().on_leave(*args)
    

    

            # MDCard:
            #     size_hint: 0.05,0.1
            #     radius:6,6,6,6
            #     pos_hint: {'x': 0,'y': .9}   
            #     #md_bg_color:(0,0,0,0)
            #     md_bg_color:get_color_from_hex("#7b9cb5")
            #     ripple_behavior: True
            #     elevation:0

            #     MDLabel:
            #         size_hint:0.5,0.5
            #         text: "'"
            #         theme_text_color:"Custom"
            #         font_size:self.height
            #         font_name: "font/SF-Pro-Rounded-Medium.otf"
            #         text_color:get_color_from_hex("#f2eded")
            #         pos_hint: {'center_x': 0.5,'center_y': 0.5}
            #         #md_bg_color:get_color_from_hex("#fefefe")
            #         halign:"center"

            #     MDLabel:
            #         size_hint:0.3,0.3
            #         text: "~"
            #         theme_text_color:"Custom"
            #         font_size:self.height
            #         font_name: "font/SF-Pro-Rounded-Medium.otf"
            #         text_color:get_color_from_hex("#f2eded")
            #         pos_hint: {'center_x': 0,'center_y': 0.8}
            #         #md_bg_color:get_color_from_hex("#fefefe")
            #         halign:"center"

            # MDCard:
            #     size_hint: 0.05,0.1
            #     radius:6,6,6,6
            #     pos_hint: {'x': 0.06,'y': .9}   
            #     #md_bg_color:(0,0,0,0)
            #     md_bg_color:get_color_from_hex("#7b9cb5")
            #     ripple_behavior: True
            #     elevation:0

            #     MDLabel:
            #         size_hint:0.5,0.5
            #         text: "1"
            #         theme_text_color:"Custom"
            #         font_size:self.height
            #         font_name: "font/SF-Pro-Rounded-Medium.otf"
            #         text_color:get_color_from_hex("#f2eded")
            #         pos_hint: {'center_x': 0.5,'center_y': 0.5}
            #         #md_bg_color:get_color_from_hex("#fefefe")
            #         halign:"center"

            #     MDLabel:
            #         size_hint:0.3,0.3
            #         text: "!"
            #         theme_text_color:"Custom"
            #         font_size:self.height
            #         font_name: "font/SF-Pro-Rounded-Medium.otf"
            #         text_color:get_color_from_hex("#f2eded")
            #         pos_hint: {'center_x': 0,'center_y': 0.8}
            #         #md_bg_color:get_color_from_hex("#fefefe")
            #         halign:"center"

            # MDCard:
            #     size_hint: 0.05,0.1
            #     radius:6,6,6,6
            #     pos_hint: {'x': 0.12,'y': .9}   
            #     #md_bg_color:(0,0,0,0)
            #     md_bg_color:get_color_from_hex("#7b9cb5")
            #     ripple_behavior: True
            #     elevation:0

            #     MDLabel:
            #         size_hint:0.5,0.5
            #         text: "2"
            #         theme_text_color:"Custom"
            #         font_size:self.height
            #         font_name: "font/SF-Pro-Rounded-Medium.otf"
            #         text_color:get_color_from_hex("#f2eded")
            #         pos_hint: {'center_x': 0.5,'center_y': 0.5}
            #         #md_bg_color:get_color_from_hex("#fefefe")
            #         halign:"center"

            #     MDLabel:
            #         size_hint:0.3,0.3
            #         text: "@"
            #         theme_text_color:"Custom"
            #         font_size:self.height
            #         font_name: "font/SF-Pro-Rounded-Medium.otf"
            #         text_color:get_color_from_hex("#f2eded")
            #         pos_hint: {'center_x': 0,'center_y': 0.8}
            #         #md_bg_color:get_color_from_hex("#fefefe")
            #         halign:"center"
            

    
class WifiPasswordWindow(Screen):
    def __init__(self, wifiApp, **kw):
        self.wifiApp = wifiApp
        super().__init__(**kw)

    def on_pre_enter(self, *args):
        self.eng_keyboard_add()
        return super().on_pre_enter(*args)

    def on_enter(self, *args):
        return super().on_enter(*args)
    
    def on_pre_leave(self, *args):
        return super().on_pre_leave(*args)
    
    def on_leave(self, *args):
        return super().on_leave(*args)


    def add_mdcard(self,pos_hint):
        widget_card = MDCard()
        widget_card.size_hint = 0.05,0.1
        widget_card.radius = 6,6,6,6
        widget_card.pos_hint = pos_hint 
        widget_card.md_bg_color = get_color_from_hex("#7b9cb5")
        widget_card.ripple_behavior: True
        widget_card.elevation = True
        return widget_card
    

            #     MDLabel:
            #         size_hint:0.5,0.5
            #         text: "'"
            #         theme_text_color:"Custom"
            #         font_size:self.height
            #         font_name: "font/SF-Pro-Rounded-Medium.otf"
            #         text_color:get_color_from_hex("#f2eded")
            #         pos_hint: {'center_x': 0.5,'center_y': 0.5}
            #         #md_bg_color:get_color_from_hex("#fefefe")
            #         halign:"center"

            #     MDLabel:
            #         size_hint:0.3,0.3
            #         text: "~"
            #         theme_text_color:"Custom"
            #         font_size:self.height
            #         font_name: "font/SF-Pro-Rounded-Medium.otf"
            #         text_color:get_color_from_hex("#f2eded")
            #         pos_hint: {'center_x': 0,'center_y': 0.8}
            #         #md_bg_color:get_color_from_hex("#fefefe")
            #         halign:"center"
    
    def add_top_label(self,text):
        widget_label = MDLabel()
        widget_label.size_hint = 0.5,0.5
        widget_label.text = text
        widget_label.theme_text_color = "Custom"
        widget_label.font_size = "25sp"
        widget_label.font_name = "font/SF-Pro-Rounded-Medium.otf"
        widget_label.text_color = get_color_from_hex("#f2eded")
        widget_label.pos_hint = {'center_x': 0.5,'center_y': 0.5}
        widget_label.halign = "center"
        return widget_label

    def add_main_label(self,text):
        widget_label = MDLabel()
        widget_label.size_hint = 0.3,0.3
        widget_label.text = text
        widget_label.theme_text_color = "Custom"
        widget_label.font_size = "20sp"
        widget_label.font_name = "font/SF-Pro-Rounded-Medium.otf"
        widget_label.text_color = get_color_from_hex("#f2eded")
        widget_label.pos_hint = {'center_x': 0,'center_y': 0.8}
        widget_label.halign = "center"
        return widget_label
    
    def add_keyboard_key(self,pos_hint,text_top,text_main):
        pos_hint = pos_hint
        mdcard = self.add_mdcard(pos_hint)
        top_label = self.add_top_label(text_top)
        main_label = self.add_main_label(text_main)
        mdcard.add_widget(top_label)
        mdcard.add_widget(main_label)
        self.ids.keyboard.add_widget(mdcard)

    
    def eng_keyboard_add(self):
        #     '     ~
        self.add_keyboard_key({'x': 0,'y': .9},"'","~")
        #       1       !
        self.add_keyboard_key({'x': 0.06,'y': .9},"1","!")
        #       2       @
        self.add_keyboard_key({'x': 0.12,'y': .9},"2","@")
        #       3       #
        self.add_keyboard_key({'x': 0.18,'y': .9},"3","#")
        #       4       $
        self.add_keyboard_key({'x': 0.24,'y': .9},"4","$")
        #       5       %
        self.add_keyboard_key({'x': 0.3,'y': .9},"5","%")
        #       6       ^
        self.add_keyboard_key({'x': 0.36,'y': .9},"6","^")
        #       7       &
        self.add_keyboard_key({'x': 0.42,'y': .9},"7","&")
        #       8       *
        self.add_keyboard_key({'x': 0.48,'y': .9},"8","*")
        #       9       (
        self.add_keyboard_key({'x': 0.54,'y': .9},"9","(")
        #       0       )
        self.add_keyboard_key({'x': 0.6,'y': .9},"0",")")
        #       -       _
        self.add_keyboard_key({'x': 0.66,'y': .9},"-","_")
    

class WifiApp(MDApp):
    def __init__(self,loop,**kwargs):
        super().__init__(**kwargs)
        self.screenmanager = None
        self.home_window = None
        self.wifi_selector_window = None

        self.active_wifi_names = ["Atlastek1", "Atlastek2", "Atlastek3", "Atlastek4", "Atlastek5", "Atlastek6", "Atlastek7","Atlastek8"]

        threading.Thread(target=self.main,daemon=True).start()

    def openHomeWindow(self):
        Clock.schedule_once(self.call_home_window, 0)

    def openWifiSelectorWindow(self):
        Clock.schedule_once(self.call_wifi_selector_window, 0)

    def openWifiPasswordWindow(self):
        Clock.schedule_once(self.call_wifi_password_window, 0)

    def call_home_window(self,event):
        self.screenmanager.current_screen.manager.current = "HomeWindow"
        self.screenmanager.current_screen.manager.transition.direction = "left"

    def call_wifi_selector_window(self,event):
        self.screenmanager.current_screen.manager.current = "WifiSelectorWindow"
        self.screenmanager.current_screen.manager.transition.direction = "left"

    def call_wifi_password_window(self,event):
        self.screenmanager.current_screen.manager.current = "WifiPasswordWindow"
        self.screenmanager.current_screen.manager.transition.direction = "left"

    def main(self):
        time.sleep(5)
        self.openHomeWindow()
        # start playing the video at creation
        # video = VideoPlayer(source='boot1080.mp4', play=True)

        # # create the video, and start later
        # video = VideoPlayer(source='boot1080.mp4')
        # # and later
        # video.play = True
        while True:
            print("hey")
            time.sleep(1)

    def build(self):
        # Window classes definition
        self.screenmanager = ScreenManager()

        self.home_window = HomeWindow(self,name="HomeWindow")
        self.wifi_selector_window = WifiSelectorWindow(self,name="WifiSelectorWindow")
        self.wifi_password_window = WifiPasswordWindow(self,name="WifiPasswordWindow")
        

        self.screenmanager.add_widget(self.home_window)
        self.screenmanager.add_widget(self.wifi_selector_window)
        self.screenmanager.add_widget(self.wifi_password_window)


        return self.screenmanager
    
class Application:
    def __init__(self,loop) -> None:
        self.wifiApp = None
        self.loop = loop

        self.key_down_press = 0
        self.counter = 0

        threading.Thread(target=self.key_control, daemon=True).start()

    def key_counter(self):
        if self.key_down_press==0:
            self.counter += 1
            if self.counter == 1:
                return True
        else:
            self.counter = 0
        return False


    def key1(self):
        if self.key_counter():
            print('************************* ctrl+shift+1 ')

    def key2(self):
        if self.key_counter():
            print('************************* ctrl+shift+2')

    def key3(self):
        if self.key_counter():
            print('************************* ctrl+shift+3')

    def key4(self):
        if self.key_counter():
            print('************************* ctrl+shift+4')

    def key5(self):
        if self.key_counter():
            print('************************* ctrl+shift+5')

    def key6(self):
        if self.key_counter():
            print('************************* ctrl+shift+6')

    def key7(self):
        if self.key_counter():
            print('************************* ctrl+shift+7')

    def key_up(self):
        if self.key_counter():
            print('************************* up')
            if self.wifiApp.screenmanager.current_screen.manager.current == "WifiSelectorWindow":
                print("WifiSelectorWindow","up")
                self.wifiApp.wifi_selector_window.startNumber = self.wifiApp.wifi_selector_window.startNumber - 1

                if len(self.wifiApp.active_wifi_names) - 2 == self.wifiApp.wifi_selector_window.startNumber:
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_1.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber]
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_2.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+1]
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_3.text = self.wifiApp.active_wifi_names[0]
                    self.wifiApp.wifi_selector_window.startNumber = -2
                elif self.wifiApp.wifi_selector_window.startNumber == -1:
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_1.text = self.wifiApp.active_wifi_names[len(self.wifiApp.active_wifi_names)-1]
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_2.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+1]
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_3.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+2]
                elif self.wifiApp.wifi_selector_window.startNumber == 0:
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_1.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber]
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_2.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+1]
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_3.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+2]
                else:
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_1.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber]
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_2.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+1]
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_3.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+2]

    def key_down(self):
        if self.key_counter():
            print('************************* down')
            if self.wifiApp.screenmanager.current_screen.manager.current == "WifiSelectorWindow":
                print("WifiSelectorWindow","down")
                self.wifiApp.wifi_selector_window.startNumber = self.wifiApp.wifi_selector_window.startNumber + 1

                if len(self.wifiApp.active_wifi_names) - 2 == self.wifiApp.wifi_selector_window.startNumber:
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_1.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber]
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_2.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+1]
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_3.text = self.wifiApp.active_wifi_names[0]
                    self.wifiApp.wifi_selector_window.startNumber = -2
                elif self.wifiApp.wifi_selector_window.startNumber == -1:
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_1.text = self.wifiApp.active_wifi_names[len(self.wifiApp.active_wifi_names)-1]
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_2.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+1]
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_3.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+2]
                elif self.wifiApp.wifi_selector_window.startNumber == 0:
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_1.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber]
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_2.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+1]
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_3.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+2]
                else:
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_1.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber]
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_2.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+1]
                    self.wifiApp.wifi_selector_window.ids.wifi_name_label_3.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+2]


    def key_left(self):
        if self.key_counter():
            print('************************* left')

    def key_right(self):
        if self.key_counter():
            print('************************* right')

    def key_enter(self):
        if self.key_counter():
            print('************************* enter')
            if self.wifiApp.screenmanager.current_screen.manager.current == "WifiSelectorWindow":
                print("WifiSelectorWindow","enter")
                self.wifiApp.openWifiPasswordWindow()


    def key_control(self):
        keyboard.add_hotkey('ctrl+shift+1', self.key1)
        keyboard.add_hotkey('ctrl+shift+2', self.key2)
        keyboard.add_hotkey('ctrl+shift+3', self.key3)
        keyboard.add_hotkey('ctrl+shift+4', self.key4)
        keyboard.add_hotkey('ctrl+shift+5', self.key5)
        keyboard.add_hotkey('ctrl+shift+6', self.key6)
        keyboard.add_hotkey('ctrl+shift+7', self.key7)
        keyboard.add_hotkey('up',self.key_up)
        keyboard.add_hotkey('down',self.key_down)
        keyboard.add_hotkey('right',self.key_right)
        keyboard.add_hotkey('left',self.key_left)
        keyboard.add_hotkey('enter',self.key_enter)

        while True:  # Loop to capture keys continuously
            try:
                event = keyboard.read_event()
                if event.event_type == keyboard.KEY_DOWN:
                    self.key_down_press += 1
                if event.event_type == keyboard.KEY_UP:
                    self.key_down_press = 0
                    self.counter = 0

            except Exception as e:
                print(e)


    async def run_app(self):
        '''This method, which runs Kivy, is run by the asyncio loop as one of the
        coroutines.
        '''
        # we don't actually need to set asyncio as the lib because it is the
        # default, but it doesn't hurt to be explicit
        await self.wifiApp.async_run(async_lib='asyncio')
        print(datetime.now(),'App done')

    def root_func(self):
        '''This will run both methods asynchronously and then block until they
        are finished
        '''
        self.wifiApp = WifiApp(self.loop)

        return asyncio.gather(self.run_app())
    
if __name__ == '__main__':
    Window.size = (800, 500)

    loop = asyncio.get_event_loop()
    app = Application(loop)


    loop.run_until_complete(app.root_func())
    loop.close()
