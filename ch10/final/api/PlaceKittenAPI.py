import requests
import random

class PlaceKittenAPI:
    def __init__(self):
        """ initialize the API url """
        cat_choices = (
            cat1 := "/200/287",
            cat2 := "/200/140",
            cat3 := "/200/139",
            cat4 := "/200/286",
            cat5 := "/96/140",
            cat6 := "/96/139",
            cat7 := "/200/138",
            cat8 := "408/287"
        )
        url = "http://placekitten.com"
        self.api_url = (url + random.choice(cat_choices))

    def get_kitten_pic(self):
        """ gets a random cat picture
        return: (response) a random cat picture """
        response = requests.get(self.api_url, stream=True)

        if r.status_code == 200:
            return response