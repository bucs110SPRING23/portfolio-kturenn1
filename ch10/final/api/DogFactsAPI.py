import requests

class DogFactsAPI:
    def __init__(self):
        """ initialize the API url """
        self.api_url = "http://dog-api.kinduff.com/api/facts?raw=true"

    def get_dog_fact(self):
        """ gets a random dog fact
        return: (str) a random dog fact or an error message """
        r = requests.get(self.api_url)
        response = str(r.content)

        if r.status_code == 200:
            return response

        else:
            return "No facts found :("

