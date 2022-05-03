#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

folder_name = "your-bash-project"

baseCode = """#! /bin/bash

printf "Hello, World!"
"""


def createAFolder():
    os.mkdir(folder_name)


def main():
    os.mkdir(f"{folder_name}/src")
    main = open(f'{folder_name}/src/main.sh', 'w')
    main.write(baseCode)
    main.close()


def readme():
    readme = open(f'{folder_name}/README.md', 'w')
    readme.write('### My First Bash Script!')
    readme.close()


def license():
    license = open(f'{folder_name}/LICENSE', 'w')
    license.write('License goes here.')
    license.close()


def start():
    createAFolder()
    main()
    license()
    readme()

