import json
import Server

movements_file = open('movements.json')

class Froggy:
    def __init__(self, name):
        self.name = name
        self.movements = json.load(movements_file)
        self.legs = {
            "left_front_leg": [0, 0],
            "right_front_leg": [0, 0],
            "left_back_leg": [0, 0],
            "right_back_leg": [0, 0],
        }


    def move(self, direction):
        for leg in self.movements[direction]:
            print(leg)
            Server.sendRequest(this.parseMovementToQueryStructure(self.movements[direction][leg]))

    def parseMovementToQueryStructure(self):
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

froggy = Froggy('Froggy the bot')
froggy.walk('forward')
movements_file.close()
