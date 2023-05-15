#!/usr/bin/python3
"""Defines the HBnB console module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class for the HBnB command line intepreter"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Execute nothing if empty line is entered"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
