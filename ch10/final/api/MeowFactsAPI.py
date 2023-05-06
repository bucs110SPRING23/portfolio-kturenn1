import requests

class MeowFactsAPI:
    def __init__(self):
        """ initialize the API url """
        self.api_url = "https://meowfacts.herokuapp.com/"
   
    def get_cat_fact(self):
        """ gets a random cat fact
        return: (str) a random cat fact or an error message """
        r = requests.get(self.api_url)
        response = str(r.content)

        if r.status_code == 200:
            return response

        else:
            return "No facts found :("