import os
import sys

folder_name = "your-py-project"


def createAFolder():
    os.mkdir(folder_name)


def main():
    print()
    os.mkdir(f"{folder_name}/src")
    main = open(f'{folder_name}/src/main.py', 'w')
    main.write('# !/usr/bin/env python3')
    main.close()


def readme():
    readme = open(f'{folder_name}/README.md', 'w')
    readme.write('### My First Python App!')
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
