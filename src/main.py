#!/usr/bin/env python3
import sys
import lang.python as python
import lang.clang as clang
import lang.vala as vala
import lang.cpp as cpp
import lang.julia as julia
import lang.cs as cs
import lang.bash as bash

app_help = """
    Currently supported languages:
    - Python
    - C/C++/C#
    - Vala
    - Julia
    - Bash
       """

version = "Version 1.2.0"

abbreviationsDict = {"python": python.start, "c": clang.start,
                     "vala": vala.start, "cpp": cpp.start,
                     "julia": julia.start, "cs": cs.start, "bash": bash.start}


def do_work():
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
                print(app_help)
                sys.exit(0)
            elif arguments == '--version':
                print(version)
                sys.exit(0)
            else:
                try:
                    # Get your function based on key in abbreviationsDict
                    language_required = abbreviationsDict[arguments]
                    language_required()  # Execute this function.
                    print(f"Your {arguments.title()} Project was created!")
                except KeyError:
                    print(f'Unrecognized Language: {arguments}.')


if __name__ == '__main__':
    do_work()
