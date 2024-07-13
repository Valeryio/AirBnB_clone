#!/usr/bin/env python3

"""This is the module about the console of HBNB"""

import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """This is the HBNB Class for the Airbnb project

    Attributes:
        @prompt:(str), the prompt for the beginning of the line
    """
    prompt = "(hbnb) "
    all_classes = ["BaseModel", "FileStorage", ""]

    def do_create(self, line):
        """This methods creates a new instance of BaseModel and
        save it to a json file"""
        if line == "":
            print("** class name missing **")
        elif line not in self.all_classes:
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            new_model.save()

    def do_show(self, line):
        """This method prints the string representation of an instance based
        on the class name and the id"""

        line_parameters = line.split(' ')
        if line == "":
            print("** class name missing **")

        if len(line_parameters) >= 2:
            print(line)
            if line_parameters[0] not in self.all_classes:
                print("** class doesn't exist **")
            elif line_parameters[1] == "":
                print("** instance id missing **")
            else:
                all_objects = storage.all()
                if all_objects[line_parameters[1]] is None:
                    print("** no instance found **")
                else:
                    print(all_objects[line_parameters[1]])

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
