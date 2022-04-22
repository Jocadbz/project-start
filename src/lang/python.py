import os
import sys

def main():
    os.mkdir("src")
    main = open('src/main.py', 'w')
    main.write('#!/usr/bin/env python3')
    main.close()


def readme():
    readme = open('README.md', 'w')
    readme.write('### My first App!')
    readme.close()


def license():
    license = open('LICENSE', 'w')
    license.write('License goes here.')
    license.close()


def start():
    main()
    license()
    readme()
