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

version = "Version 1.1.0"

abbreviationsDict = {"python": python.start, "c": clang.start,
                     "vala": vala.start}


def DO_WORK():
    """ Function to handle command line usage"""
    args = sys.argv
    args = args[1:]  # First element of args is the file name

    if len(args) == 0:
        print('Wrong usage.')
    else:
        for arguments in args:
            arguments = arguments.lower()
            if arguments == '--help':
                print(help)
                sys.exit(0)
            elif arguments == '--version':
                print(version)
                sys.exit(0)
            else:
                try:
                    # get your function based on key in abbreviationsDict
                    languageRequired = abbreviationsDict[arguments]
                    languageRequired()  # Execute this function.
                    print(f"Your {arguments.title()} Project was created!")
                # (KeyError) will be throw in case you request a Language which is not present (yet).
                except KeyError:
                    print('Unrecognized Language.')


if __name__ == '__main__':
    DO_WORK()
