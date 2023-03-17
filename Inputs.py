import keyboard as key
from time import sleep
'''
This file is used to define all the inputs the bot may need to use.
Used to work with an AZERTY keyboard configuration. You may change the inputs depending on the one you use in your game.
'''

def bomb():
    key.press_and_release('a')

def activable():
    key.press_and_release('space')

def shoot_left():
    key.press('left')

def shoot_right():
    key.press('right')

def shoot_up():
    key.press('up')

def shoot_down():
    key.press('down')

def release_shoot():
    key.release('left')
    key.release('right')
    key.release('up')
    key.release('down')

def go_left():
    key.press('q')

def go_right():
    key.press('d')

def go_up():
    key.press('z')

def go_down():
    key.press('s')

def release_dir():
    key.release('z')
    key.release('q')
    key.release('s')
    key.release('d')
    
def switch(n : int):
    key.press('ctrl')
    sleep(n)
    key.release('ctrl')
