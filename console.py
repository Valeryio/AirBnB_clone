#!/usr/bin/env python3

"""This is the module about the console of HBNB"""

import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ This is the HBNB Class for the Airbnb project

    Attributes:
        @prompt:(str), the prompt for the beginning of the line
    """
    prompt = "(hbnb) "
    known_classes = ["BaseModel", "FileStorage", ""]

    def do_create(self, line):
        """ This methods creates a new instance of BaseModel and
        save it to a json file"""
        if line == "":
            print("** class name missing **")
        elif line not in self.known_classes:
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            storage.new(new_model)
            print(storage.objects)

    def do_show(self, line):
        """This method prints the string representation of an instance based
        on the class name and the id

        Arguments:
            @line
        """

        # Verifications of the line input
        right_command = self.checker(line)

        # Execution if the params are right
        if right_command:
            line_parameters = line.split(' ')
            class_name = line_parameters[0]
            object_id = line_parameters[1]

            object_to_show = ''
            all_objects = storage.all()
            object_key = class_name + '.' + object_id

            for key, value in all_objects.items():
                if object_key == key:
                    object_to_show = value

            if object_to_show != '':
                print(object_to_show)
            else:
                print("** no instance found **")

    def do_destroy(self, id):
        pass

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

    def checker(self, line):
        """This method checks a line with its parameters to
            execute the right command of the terminal

            Arguments:
                @line: (str), the line to check

            Returns:
                0 on FAILURE
                1 on SUCCESS
        """
        # Verifications of the line input
        line_parameters = line.split(' ')
        if line == "":
            print("** class name missing **")
            return 0
        elif len(line_parameters) != 0:
            try:
                class_name = line_parameters[0]
                object_id = line_parameters[1]
            except IndexError:
                object_id = None
                pass

            if class_name and class_name not in self.known_classes\
                    or type(class_name) is not str:
                print("** class doesn't exist **")
                return 0

            elif object_id is None:
                print("** instance id missing **")
                return 0

            else:
                return 1


if __name__ == "__main__":
    HBNBCommand().cmdloop()
