#!/usr/bin/python3
"""
Simple command-line interface for the HBNB clone project using the cmd module.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class: a cmd module subclass for the HBNB clone project."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the program. Usage: quit"""
        return True

    def do_EOF(self, arg):
        """Exit the program. Usage: Press Ctrl+D (Unix-like) or Ctrl+Z (Windows)"""
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

