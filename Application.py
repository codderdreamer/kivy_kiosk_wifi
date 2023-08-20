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
from collections import defaultdict

class Login(Screen):
    def on_enter(self, *args):
        print("here2")
        return super().on_enter(*args)

class HomeWindow(Screen):
    def __init__(self, wifiApp, **kw):
        super().__init__(**kw)

    def on_pre_enter(self, *args):
        return super().on_pre_enter(*args)

    def on_enter(self, *args):
        return super().on_enter(*args)
    
    def on_pre_leave(self, *args):
        return super().on_pre_leave(*args)
    
    def on_leave(self, *args):
        return super().on_leave(*args)
    

class WifiApp(MDApp):
    def __init__(self,loop,**kwargs):
        super().__init__(**kwargs)
        self.screenmanager = None

        threading.Thread(target=self.main,daemon=True).start()

    def openHomeWindow(self):
        Clock.schedule_once(self.call_home_window, 0)

    def call_home_window(self,event):
        self.screenmanager.current_screen.manager.current = "HomeWindow"
        self.screenmanager.current_screen.manager.transition.direction = "left"

    def main(self):
        time.sleep(5)
        self.openHomeWindow()
        while True:
            print("hey")
            time.sleep(1)

    def build(self):
        # Window classes definition
        self.screenmanager = ScreenManager()

        home_window = HomeWindow(self,name="HomeWindow")
        loadingWindow = Login(name="Login")

        self.screenmanager.add_widget(loadingWindow)
        self.screenmanager.add_widget(home_window)
        print("here")
        
        return self.screenmanager
    
class Application:
    def __init__(self,loop) -> None:
        self.wifiApp = None
        self.loop = loop


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


    # Window.size = (setting.sizeX, setting.sizeY)
    Window.size = (300, 530)

    loop = asyncio.get_event_loop()
    app = Application(loop)


    loop.run_until_complete(app.root_func())
    loop.close()
