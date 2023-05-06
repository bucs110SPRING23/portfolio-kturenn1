import requests

class PlaceDogAPI:
    def __init__(self):
        """ initialize the API url """
        self.api_url = "https://place.dog/500/500"

    def get_dog_pic(self):
        """ gets a random dog picture
        return: (response) a random dog picture """
        response = requests.get(self.api_url, stream=True)

        if r.status_code == 200:
            return response
