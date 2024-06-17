#!/usr/bin/env python3

"""This is the module about the console of HBNB"""

import cmd


class HBNBCommand(cmd.Cmd):
    """This is the HBNB Class for the Airbnb project

    Attributes:
        @prompt:(str), the prompt for the beginning of the line
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """This method quits the interpreter"""
        print("Quit command to exit the program")
        return True

    def do_EOF(self, line):
        """This is the end of file program that quits the cmd"""
        return True

    def emptyline(self):
        """This method do nothing when the line is empty"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
