#!/usr/bin/python3
'''The console '''
import cmd
import re
import shlex 
import models 
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __classes = [
        "Amenity",
        "BaseModel",
        "City",
        "Place",
        "Review",
        "State",
        "User"
    ]
    def do_create(self, args):
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            instance = eval(arg[0])()
            instance.save()
            print(instance.id)
    def do_show(self,args):
        string = args.split()
        if len(string) == 0:
            print("** class name missing **")
        elif string[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(string) == 1:
            print("** instance id missing ** ")
        else:
            obj = models.storage.all()
            key_val = string[0] + '.' + string[1]
            if key_val in obj:
                print(obj[key_val])
            else:
                print("** no instance found **")

    def do_quit(self, args):
        """Exit the program. Usage: quit"""
        return True

    def do_EOF(self, args):
        """Exit the program. Usage: Press Ctrl+D (Unix-like) or Ctrl+Z (Windows)"""
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
