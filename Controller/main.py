import requests
import time

api_url = "http://192.168.4.1/"
query = {'S0': 0, 'S1': 0, 'S2': 0, 'S3': 0, 'S4': 0, 'S5': 0, 'S6': 0, 'S7': 0}
# query = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0}
# response = requests.get(api_url, params=query)
# print(response.json())
# print(response.status_code)
# print(response)

legs = {
    "left_front_leg": [0, 0],
    "right_front_leg": [0, 0],
    "left_back_leg": [0, 0],
    "right_back_leg": [0, 0],
}

def moveFroggy(query):
    response = requests.get(api_url, params=query)
    print(response.status_code)

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
        print("Caminando adelante")

        # 1st leg
        legs["left_front_leg"] = ["000", "045"]
        moveFroggy(parseMovementToQueryStructure(legs))
        legs["left_front_leg"] = ["045", "000"]
        moveFroggy(parseMovementToQueryStructure(legs))

        # # 2nd leg
        # legs["right_front_leg"] = ["000", "045"]
        # legs["right_front_leg"] = ["045", "000"]

        # #
        
    elif (direction == 'backward'):
        print("caminando atras")

def main():
    walk('forward')

main()


# for i in range(20):
#     response = requests.get(api_url)
#     print(response.status_code)
