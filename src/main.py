import subprocess
import sys
import lang.python as python
import lang.clang as clang
import lang.vala as vala

help = """
    Currently supported languages:
    - Python
    - C
    - Vala
       """

abbreviationsDict = {"python": python.start, "c": clang.start, "vala": vala.start}


def DO_WORK():
    """ Function to handle command line usage"""
    args = sys.argv
    args = args[1:]  # First element of args is the file name

    if len(args) == 0:
        print('Wrong usage.')
    else:
        for arguments in args:
            if arguments == '--help':
                print(help)
                break
            else:
                try:
                    if (arguments in abbreviationsDict.keys()):
                        # get your function based on key in abbreviationsDict
                        requiredFunction = abbreviationsDict[arguments]
                        requiredFunction()  # Execute this function.
                        break
# Since the user input a command that can't be used as the name of a function..
                    else:
                        # install = INSTALL + () = INSTALL() and eval it.
                        eval(f"{arguments.upper()}()")
                        break
# (NameError) will be throw in case you use a command which is not present.
                except NameError:
                    print('Unrecognized Language.')
                    break
    print("Project was created!")


if __name__ == '__main__':
    DO_WORK()
