import platform

import os
from datetime import datetime, timezone, timedelta
from os.path import join, dirname
from sys import argv
import time

from controle_log import ControleLog
from utils import timeit_count_all_files


def display_current_working_directory() -> None:
    current_working_directory = os.getcwd()
    print(f"Current Working Directory: {current_working_directory}")


def up_one_directory_level() -> None:
    os.chdir("../")


def format_datetime(timestamp: float) -> str:
    utc_timestamp = datetime.utcfromtimestamp(timestamp)
    sp_timezone = timezone(timedelta(hours=-3))
    return utc_timestamp.astimezone(sp_timezone).strftime("%d %b %Y, %H:%M:%S")


def display_creation_time(info: 'os.stat_result') -> None:
    if 'linux' == check_operating_system():
        print(f"Last Modification Time: {format_datetime(info.st_ctime)}")
    else:
        attribute = 'st_ctime' if 'windows' == check_operating_system() else 'st_birthtime'
        print(f"Creation Time: {format_datetime(getattr(info, attribute))}")


def display_entries_in_directory(directory: str) -> None:
    with os.scandir(directory) as entries:
        for entry in entries:
            print("Name: ", entry.name)
            print("Relative path: ", entry.path)
            info = entry.stat()
            display_creation_time(info)
            print("Last Access Time: ", format_datetime(info.st_atime))
            print("Size: ", info.st_size, "bytes")


def display_directories(directory: str) -> None:
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_dir():
                print("Direcotry Name: ", entry.name)


def display_files(directory: str) -> None:
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                print("File Name: ", entry.name)


def check_operating_system() -> str:
    current_operating_system = platform.platform().lower()
    list_operating_system = ['linux', 'windows', 'mac']
    for operating_system in list_operating_system:
        if operating_system in current_operating_system:
            return operating_system
    raise ValueError("Not recognized operating system")


def top_down_walk():
    for dirpath, dirnames, files in os.walk('.'):
        print("Directory: ", dirpath)
        print("Includes these directories")
        for dirname in dirnames:
            print(dirname)
        for filename in files:
            print(filename)
        print()


def down_top_walk() -> None:
    for dirpath, dirnames, files in os.walk('.', topdown=False):
        print("Directory: ", dirpath)
        print("Includes these directories")
        for dirname in dirnames:
            print(dirname)
        for filename in files:
            print(filename)
        print()


def make_logs_dir() -> None:
    try:
        os.mkdir('logs/')
    except FileExistsError as exception:
        log.warning(f"Error: {exception}. Logs directory already exists")


def down_one_level() -> None:
    os.chdir("working_with_files/")


def count_all_files_with_os_walk(path):
    counter = 0
    for dirpath, dirnames, files in os.walk(path):
        counter += len(files)
    return counter


def count_all_files_with_os_scandir(path):
    counter = 0
    with os.scandir(path) as entries:
        for entry in entries:
            counter += 1 if entry.is_file() else count_all_files_with_os_scandir(entry)
        return counter


if __name__ == "__main__":
    log = ControleLog(join(dirname(argv[0]), 'log'), True)
    # display_current_working_directory()
    # log.info("Subir um nível")
    # up_one_directory_level()
    # display_current_working_directory()
    # log.info("Mostrar todas os objetos no diretório working_with_files/images/")
    # display_entries_in_directory("working_with_files/images/")
    # log.info("Mostrar todas os diretórios no diretório working_with_files/")
    # display_directories("working_with_files/")
    # log.info("Mostrar todas os arquivos no diretório working_with_files/")
    # display_files("working_with_files/")
    # log.info(f"Mostrar todas os arquivos e subdiretórios no diretório {os.getcwd()} de cima para baixo na árvore")
    # top_down_walk()
    # log.info(f"Mostrar todas os arquivos e subdiretórios no diretório {os.getcwd()} de baixo para cima na árvore")
    # down_top_walk()
    # log.info("Descer novamente para o diretório do projeto working_with_files")
    # down_one_level()
    # display_current_working_directory()
    # log.info("Tentar criar o diretório logs")
    # make_logs_dir()
    # timeit_count_all_files('os.walk', count_all_files_with_os_walk, log)
    # timeit_count_all_files('os.scandir', count_all_files_with_os_scandir, log)
