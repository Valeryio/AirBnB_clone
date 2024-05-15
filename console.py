#!/usr/bin/python3

# This is the entry point for the command line interpreter

import cmd

class AirbnbConsole(cmd.Cmd):
    intro = "Welcome to the AirBnB project!"
    prompt = " (hbnb) "

    def do_hello(self, person):
        if person:
            print(f"You're inside the AirBnB app {person}")
        else:
            print("You're inside the AirBnB app!")

    def do_EOF(self):
        print()

if __name__ == "__main__":
    AirbnbConsole().cmdloop()
