#!/usr/bin/python3
"A class for places"

from models.base_models import Basemodel

class place(Basemodel):
    "Represents places"

city_id = ""
user_id = ""
nam = ""
description = ""
number_rooms = 0
number_bathrooms = 0
max_guest = 0
price_by_night = 0
latitude = 0.0
longitude = 0.0
amenity_ids = []
