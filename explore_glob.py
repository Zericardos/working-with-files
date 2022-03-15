import glob
from explore_os import display_current_working_directory


def display_pngs() -> None:
    print(glob.glob('images/*.png'))


def find_monster_one_in_subdirs():
    for file in glob.iglob('**/*monster01*', recursive=True):
        print(file)


if __name__ == "__main__":
    display_current_working_directory()
    display_pngs()
    find_monster_one_in_subdirs()
