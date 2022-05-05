import os

folder_name = "your-py-project"

baseCode = """# !/usr/bin/env python3

print("Hello World!")
"""


def create_a_folder():
    os.mkdir(folder_name)


def main():
    os.mkdir(f"{folder_name}/src")
    main_file = open(f'{folder_name}/src/main.py', 'w')
    main_file.write(baseCode)
    main_file.close()


def readme():
    readme_git = open(f'{folder_name}/README.md', 'w')
    readme_git.write('### My First Python App!')
    readme_git.close()


def license_project():
    license_git = open(f'{folder_name}/LICENSE', 'w')
    license_git.write('License goes here.')
    license_git.close()


def start():
    create_a_folder()
    main()
    license_project()
    readme()
