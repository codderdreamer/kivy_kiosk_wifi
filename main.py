import keyboard
import os
import threading
from multiprocessing import Process, Manager

class Application:
    def __init__(self):
        self.evet_keyboard = False
        self.key_down_press = 0

    def key_control(self):
        try:
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
        except Exception as e:
            print("Keyboard exception",e)

        while True:  # Loop to capture keys continuously
            print("event keyboard")
            try:
                event = keyboard.read_event()
                print(event)
                self.evet_keyboard = True
                if event.event_type == keyboard.KEY_DOWN:
                    self.key_down_press += 1
                if event.event_type == keyboard.KEY_UP:
                    self.key_down_press = 0
                    self.counter = 0
            except Exception as e:
                print("Keyboard exception",e)

    def key1(self):
        if self.evet_keyboard == True:
            print('*************************key: ctrl+shift+1')
            print('Wifi Login screen')
            os.system('sudo python Application.py')
            
        self.evet_keyboard = False

    def key2(self):
        if self.evet_keyboard == True:
            print('*************************key: ctrl+shift+2')
            os.system("sudo su -l pi -c startx")

        self.evet_keyboard = False

    def key3(self):
        if self.evet_keyboard == True:
            print('*************************key: ctrl+shift+3')
        self.evet_keyboard = False

    def key4(self):
        if self.evet_keyboard == True:
            print('*************************key: ctrl+shift+4')
        self.evet_keyboard = False

    def key5(self):
        if self.evet_keyboard == True:
            print('*************************key: ctrl+shift+5')
        self.evet_keyboard = False

    def key6(self):
        if self.evet_keyboard == True:
            print('*************************key: ctrl+shift+6')
        self.evet_keyboard = False

    def key7(self):
        if self.evet_keyboard == True:
            print('*************************key: ctrl+shift+7')
        self.evet_keyboard = False

    def key_up(self):
        if self.evet_keyboard == True:
            print('*************************key: up')
        self.evet_keyboard = False

    def key_down(self):
        if self.evet_keyboard == True:
            print('*************************key: down')
        self.evet_keyboard=False

    def key_left(self):
        if self.evet_keyboard == True:
            print('*************************key: left')
        self.evet_keyboard = False

    def key_right(self):
        if self.evet_keyboard == True:
            print('*************************key: right')
        self.evet_keyboard = False


    def key_enter(self):
        if self.evet_keyboard == True:
            print('*************************key: enter')        
        self.evet_keyboard = False

app = Application()
app.key_control()
