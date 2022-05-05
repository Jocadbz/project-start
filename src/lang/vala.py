import os

folder_name = "your-vala-project"

baseCode = """public class MyApp : Gtk.Application {
    public MyApp () {
        Object (
            application_id: "com.github.yourusername.yourrepositoryname",
            flags: ApplicationFlags.FLAGS_NONE
        );
    }

    protected override void activate () {
        var main_window = new Gtk.ApplicationWindow (this) {
            default_height = 300,
            default_width = 300,
            title = "Hello World"
        };
        main_window.show_all ();
    }

    public static int main (string[] args) {
        return new MyApp ().run (args);
    }
}
"""


def create_a_folder():
    os.mkdir(folder_name)


def main():
    os.mkdir(f"{folder_name}/src")
    main_file = open(f'{folder_name}/src/main.vala', 'w')
    main_file.write(baseCode)
    main_file.close()


def readme():
    readme_git = open(f'{folder_name}/README.md', 'w')
    readme_git.write('### My First Vala App!')
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
