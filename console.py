#!/usr/bin/python3
"""Defines a simple command interpreter for the console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter"""
    prompt = "(hbnb)"
    intro = "Welcome to the AirBnB project type 'help' for a list of commands."

    def do_quit(self, arg):
        """Quit the command interpreter."""
        print("Exiting HBNB console")
        exit()

    def emptyline(self):
        pass

    def do_help(self, arg):
        """Available commands"""
        print("Available commands:")
        super().do_help(arg)

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
