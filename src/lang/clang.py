import os

folder_name = "your-c-project"

baseCode = """#include <stdio.h> 
#include <stdlib.h> 

int main() {
    printf("Hello World!\n");
    return 0;
}
"""


def create_a_folder():
    os.mkdir(folder_name)


def main():
    os.mkdir(f"{folder_name}/src")
    main_file = open(f'{folder_name}/src/main.c', 'w')
    main_file.write(baseCode)
    main_file.close()


def readme():
    readme_project = open(f'{folder_name}/README.md', 'w')
    readme_project.write('### My First C App!')
    readme_project.close()


def license_project():
    license_git = open(f'{folder_name}/LICENSE', 'w')
    license_git.write('License goes here.')
    license_git.close()


def start():
    create_a_folder()
    main()
    license_project()
    readme()
