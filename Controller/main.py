import requests
import time
from pynput.keyboard import *
import Froggy

server_URL = "http://192.168.4.1/"
query = {'S0': 0, 'S1': 0, 'S2': 0, 'S3': 0, 'S4': 0, 'S5': 0, 'S6': 0, 'S7': 0}
# query = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0}

froggy = Froggy('Froggy the fucking bot')

def press_on(key):
    if key == Key.up:
        froggy.move('forward')
    elif key == Key.down:
        froggy.move('backward')
    elif key == Key.right:
        froggy.move('right')
    elif key == Key.left:
        froggy.move('left')
    elif key == Key.t:
        froggy.move('twerk')
    elif key == Key.c:
        froggy.move('crouch')

def press_off(key):
    if key == Key.esc:
        return False

def main():
    global Listener

    with Listener(on_press = press_on, on_release = press_off) as Listener:
        Listener.join()

main()
