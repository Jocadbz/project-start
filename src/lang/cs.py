#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

folder_name = "your-c#-project"

baseCode = """
using System;
  
namespace HelloWorldApp {
      
    class Geeks {
          
        static void Main(string[] args) {
              
            Console.WriteLine("Hello World!");
              
            Console.ReadKey();
        }
    }
}

"""


def createAFolder():
    os.mkdir(folder_name)


def main():
    os.mkdir(f"{folder_name}/src")
    main = open(f'{folder_name}/src/main.cs', 'w')
    main.write(baseCode)
    main.close()


def readme():
    readme = open(f'{folder_name}/README.md', 'w')
    readme.write('### My First C# App!')
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

