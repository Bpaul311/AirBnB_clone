#!/usr/bin/python3
<<<<<<< HEAD
"""a model representing a base through a class"""
import uuid
from datetime import datetime
from models import storage

class BaseModel():
     """a representation of the base model class"""


=======
"""

"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *arg, **kwargs):
        time_iso_format = "%Y-%m-%dT%H:%M:%S.%f"
        if (kwargs):
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(
                        value, time_iso_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())

            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

 def __str__(self):
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__)

    def save(self):
        """updates the updated_at variable"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """returns a dictionary representation of the class"""
        obj = self.__dict__.copy()

        obj['__class__'] = self.__class__.__name__

        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()

        return obj

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "First Model"
    my_model.my_number = 66
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
>>>>>>> 60cdf59d4112c566adac1e23acb7fc4744a572ab
