__author__ = 'root'

import cmd


class Helloworld(cmd.Cmd):
    prompt = "pichuang > "

    def do_greet(self, line):
        print("greet")

    def do_EOF(self, line):
        return True

    def do_print(self, line):
        print(line)

if __name__ == "__main__":
    Helloworld().cmdloop()