#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Command line intepreter"""
    prompt = '(hbnb) '

    def emptyline(self):
        """Execute nothing if empty line is entered"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
