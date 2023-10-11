#!/usr/bin/python3
"""
This is the base or parent class for the Air B&B project, all the other classes
will inharit from this class, it is the main blueprint of the application

We use the UUID an the DATETIME packages, for creating a unique ID 
and date and time respectively

This model will be used to manipulate the console
"""

import cmd, sys

class console(cmd.Cmd):
    """
    the commandline interface that will execute the Air B&B project
    """
    
    intro = "Welcome to Air B&B CML Interface, Type help or ? to list commands.\n"
    prompt = '(AirB&B)'
    file = None
    
    
if __name__ == '__main__':
    console().cmdloop()