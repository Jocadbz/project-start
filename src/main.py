import sys
import lang.python as python
import lang.clang as clang
import lang.vala as vala
import lang.cpp as cpp
import lang.julia as julia
import lang.cs as cs

help = """
    Currently supported languages:
    - Python
    - C/C++/C#
    - Vala
    - Julia
       """

version = "Version 1.2.0"

abbreviationsDict = {"python": python.start, "c": clang.start,
                     "vala": vala.start, "cpp": cpp.start,
                     "julia": julia.start, "cs": cs.start}


def DO_WORK():
    """ Function to handle command line usage"""
    args = sys.argv
    args = args[1:]  # First element of args is the file name

    if len(args) == 0:
        print('Wrong usage.')
        sys.exit(1)
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
                    # Get your function based on key in abbreviationsDict
                    languageRequired = abbreviationsDict[arguments]
                    languageRequired()  # Execute this function.
                    print(f"Your {arguments.title()} Project was created!")
                except KeyError:
                    print(f'Unrecognized Language: {arguments}.')


if __name__ == '__main__':
    DO_WORK()
