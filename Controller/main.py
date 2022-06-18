import requests
import time
from pynput.keyboard import *

server_URL = "http://192.168.4.1/"
query = {'S0': 0, 'S1': 0, 'S2': 0, 'S3': 0, 'S4': 0, 'S5': 0, 'S6': 0, 'S7': 0}
# query = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0}

legs = {
    "left_front_leg": [0, 0],
    "right_front_leg": [0, 0],
    "left_back_leg": [0, 0],
    "right_back_leg": [0, 0],
}

def moveFroggy(query):
    #response = requests.get(server_URL, params=query)
    #print(response.status_code)
    #print(query)
    pass    

def parseMovementToQueryStructure(legs):
    query = { 
        'S0': legs["left_front_leg"][0], 
        'S1': legs["left_front_leg"][1], 
        'S2': legs["right_front_leg"][0], 
        'S3': legs["right_front_leg"][1], 
        'S4': legs["left_back_leg"][0], 
        'S5': legs["left_back_leg"][1], 
        'S6': legs["right_back_leg"][0], 
        'S7': legs["right_back_leg"][1] 
    }
    return query

def walk(direction):
    if (direction == 'forward'):
        print("⬆️")

        # left front leg
        legs["left_front_leg"] = ["000", "045"]
        moveFroggy(parseMovementToQueryStructure(legs))
        legs["left_front_leg"] = ["045", "000"]
        moveFroggy(parseMovementToQueryStructure(legs))
        legs["left_front_leg"] = ["000", "000"]
        moveFroggy(parseMovementToQueryStructure(legs))
        
        # right front leg
        legs["right_front_leg"] = ["000", "045"]
        moveFroggy(parseMovementToQueryStructure(legs))
        legs["right_front_leg"] = ["045", "000"]
        moveFroggy(parseMovementToQueryStructure(legs))
        legs["right_front_leg"] = ["000", "000"]
        moveFroggy(parseMovementToQueryStructure(legs))
        
        # left back leg
        legs["left_back_leg"] = ["000", "045"]
        moveFroggy(parseMovementToQueryStructure(legs))
        legs["left_back_leg"] = ["045", "000"]
        moveFroggy(parseMovementToQueryStructure(legs))
        legs["left_back_leg"] = ["000", "000"]
        moveFroggy(parseMovementToQueryStructure(legs))
        
        # right back leg
        legs["right_back_leg"] = ["000", "045"]
        moveFroggy(parseMovementToQueryStructure(legs))
        legs["right_back_leg"] = ["045", "000"]
        moveFroggy(parseMovementToQueryStructure(legs))
        legs["right_back_leg"] = ["000", "000"]
        moveFroggy(parseMovementToQueryStructure(legs))
    
    elif (direction == 'backward'):
        print("⬇️")

    elif (direction == 'right'):
        print("➡️")
    
    elif (direction == 'left'):
        print("⬅️:")

def press_on(key):
    if key == Key.up:
        walk('forward')
    elif key == Key.down:
        walk('backward')
    elif key == Key.right:
        walk('right')
    elif key == Key.left:
        walk('left')

def press_off(key):
    if key == Key.esc:
        return False

def main():
    global Listener

    with Listener(on_press = press_on, on_release = press_off) as Listener:
        Listener.join()

main()
