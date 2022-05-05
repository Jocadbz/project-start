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


def create_a_folder():
    os.mkdir(folder_name)


def main():
    os.mkdir(f"{folder_name}/src")
    main_file = open(f'{folder_name}/src/main.cs', 'w')
    main_file.write(baseCode)
    main_file.close()


def readme():
    readme_git = open(f'{folder_name}/README.md', 'w')
    readme_git.write('### My First C# App!')
    readme_git.close()


def license_git():
    license_git_project = open(f'{folder_name}/LICENSE', 'w')
    license_git_project.write('License goes here.')
    license_git_project.close()


def start():
    create_a_folder()
    main()
    license_git()
    readme()
