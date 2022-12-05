import urllib.request
from PIL import Image
import apikey

def streetviewImage(place):
    urllib.request.urlretrieve(
    apikey.places[place],
    str(place) + ".png")
    # img = Image.open(str(place) + ".png")
    # img.show()
