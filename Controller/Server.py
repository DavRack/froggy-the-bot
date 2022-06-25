import requests

class Server:
    def __init__(self, url):
        self.url = url

    def sendRequest(self, query):
        response = requests.get(self.url, params=query)
        print(response.status_code)
