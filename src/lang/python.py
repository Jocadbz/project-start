import os
import sys

folder_name = "your-py-project"

baseCode = """# !/usr/bin/env python3

print("Hello World!")
"""


def createAFolder():
    os.mkdir(folder_name)


def main():
    os.mkdir(f"{folder_name}/src")
    main = open(f'{folder_name}/src/main.py', 'w')
    main.write(baseCode)
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
