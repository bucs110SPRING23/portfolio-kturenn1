from api import DogFactsAPI
from api import MeowFactsAPI
from api import PlaceDogAPI
from api import PlaceKittenAPI
from PIL import Image

def main():

    #CHOICE - dog
    dog_facts_api = DogFactsAPI.DogFactsAPI()
    df_results = dog_facts_api.get_dog_fact()

    place_dog_api = PlaceDogAPI.PlaceDogAPI()
    pd_results = place_dog_api.get_dog_pic()
    dog = Image.open(pd_results.raw)

    #CHOICE - cat
    meow_facts_api = MeowFactsAPI.MeowFactsAPI()
    mf_results = meow_facts_api.get_cat_fact()

    place_kitten_api = PlaceKittenAPI.PlaceKittenAPI()
    pk_results = place_kitten_api.get_kitten_pic()
    cat = Image.open(pk_results.raw)

    print("Hello! Do you prefer dogs or cats?")
    user_input = input("Type 'dog' or 'cat': ")

    run = True
    while run:
        if user_input.lower() == "dog":
            print("Here's a dog fact: " + df_results)
            print("Here's a dog picture:")
            dog.show()
            run = False

        elif user_input.lower() == "cat":
            print("Here's a cat fact: " + mf_results)
            print("Here's a cat picture:")
            cat.show()
            run = False

        else:
            print("Sorry, I didn't understand that.")
            user_input = input("Please type 'dog' or 'cat': ")

main()