#!/usr/bin/env python3

"""This is the module about the console of HBNB"""

import cmd
from models.engine.file_storage import FileStorage
from models.user import User
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ This is the HBNB Class for the Airbnb project

    @param:
        prompt:(str), the prompt for the beginning of the line
    """
    prompt = "(hbnb) "
    known_classes = {"BaseModel": BaseModel, "FileStorage": FileStorage,
                     "User": User}

    def do_create(self, line):
        """ This method creates a new instance of BaseModel and
        save it to a json file"""
        if line == "":
            print("** class name missing **")
        elif line not in self.known_classes:
            print("** class doesn't exist **")
        else:
            for key, class_value in self.known_classes.items():
                if key == line:
                    new_model = class_value()

            storage.new(new_model)
            storage.save()
            print(new_model.id)

    def do_show(self, line):
        """This method prints the string representation of an instance based
        on the class name and the id

        @param:
            line: the line of the prompt with the class instance to show
        """

        # Verifications of the line input
        right_command = self.checker(line)

        # Execution if the params are right
        if right_command:
            line_parameters = line.split(' ')
            class_name = line_parameters[0]
            object_id = line_parameters[1]

            object_to_show = ""
            all_objects = storage.all()
            object_key = class_name + "." + object_id

            for key, value in all_objects.items():
                if object_key == key:
                    object_to_show = value

            if object_to_show != "":
                print(object_to_show)

    def do_destroy(self, line):

        right_command = self.checker(line)

        if right_command:
            line_arguments = line.split(" ")
            id_to_delete = line_arguments[1]
            key_to_delete = ""
            all_objects = storage.objects

            for key, value in all_objects.items():
                if value.__dict__['id'] == id_to_delete:
                    key_to_delete = key

            storage.objects.pop(key_to_delete)
            storage.save()

    def do_all(self, line):
        """This method prints all the objects in the local storage"""

        if line not in self.known_classes:
            print("** class doesn't exist **")
        else:
            all_objects = storage.objects
            print(all_objects)

    def do_update(self, line):
        """This method updates an object in the storage instance
            @param:
                line: the command line to execute
        """

        right_command = self.update_checker(line)

        if right_command:

            line_arguments = line.split(" ")

            object_class_name = line_arguments[0]
            object_id = line_arguments[1]
            object_attr = line_arguments[2].replace("\"", "")
            object_attr_value = line_arguments[3].replace("\"", "")
            object_key = object_class_name + "." + object_id

            setattr(storage.objects[object_key], object_attr, object_attr_value)
            storage.save()

    def do_quit(self, line):
        """This method quits the interpreter
            @return:
            True to quit the cmd
        """
        print("Quit command to exit the program")
        return True

    def emptyline(self):
        """This method makes that nothing executes when an empty
            is sent as parameter"""
        pass

    def do_EOF(self, line):
        """This is the end of file program that quits the cmd
        @param
            line: 
        @return:
            True for the execution of the program
        """
        return True

    def checker(self, line):
        """This method checks a line with its parameters to
            execute the right command of the terminal

            @param:
                @line: (str), the line to check

            @return:
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

            if class_name and class_name not in self.known_classes.keys()\
                    or type(class_name) is not str:
                print("** class doesn't exist **")
                return 0

            elif object_id is None:
                print("** instance id missing **")
                return 0

            elif object_id:
                all_objects = storage.all()
                object_is_present = 0
                object_key = class_name + "." + object_id

                for key, value in all_objects.items():
                    if object_key == key:
                        object_is_present = 1

                if object_is_present == 0:
                    print("** no instance found **")
                    return 0
                else:
                    return 1

            else:
                return 1

    def update_checker(self, line):
        """
            This method checks the line parameters of the command for an update
            of characteristics

            @param line:
            @return:
        """
        simple_check = self.checker(line)

        if simple_check == 1:
            line_arguments = line.split(' ')

            if len(line_arguments) >= 2:
                try:
                    attribute_name = line_arguments[2]
                except IndexError:
                    attribute_name = "No name"

                try:
                    attribute_value = line_arguments[3]
                except IndexError:
                    attribute_value = "No value"

                if attribute_name == "No name":
                    print("** attribute name missing **")
                    return 0
                elif attribute_value == "No value":
                    print("** value missing **")
                    return 0
                else:
                    return 1


if __name__ == "__main__":
    HBNBCommand().cmdloop()
