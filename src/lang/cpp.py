import os

folder_name = "your-cpp-project"

baseCode = """
#include <iostream> 

int main() {
    std::cout << "Goodbye World!"; 
    return 0;
}
"""


def createAFolder():
    os.mkdir(folder_name)


def main():
    os.mkdir(f"{folder_name}/src")
    main = open(f'{folder_name}/src/main.cpp', 'w')
    main.write(baseCode)
    main.close()


def readme():
    readme = open(f'{folder_name}/README.md', 'w')
    readme.write('### My First C++ App!')
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
