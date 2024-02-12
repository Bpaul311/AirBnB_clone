#!/usr/bin/python3
"""Class for reviews."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent reviews"""

    place_id = ""
    user_id = ""
    text = ""
