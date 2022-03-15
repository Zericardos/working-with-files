from os.path import join, dirname
from sys import argv

from controle_log import ControleLog


from pathlib import Path

from utils import timeit_count_all_files


def print_directory_contents():
    log.info("Mostrando algumas propriedades dos arquivos e diretórios usando a biblioteca Pathlib")
    entries = Path.cwd()
    for entry in entries.iterdir():
        if entry.is_file():
            print(f"Nome do arquivo: {entry.name}")
            print(f"Nome do arquivo sem extensão: {entry.stem}")
            print(f"Extensão do arquivo: {entry.suffix}")
            print(f"Nome do diretório do arquivo: {entry.parent}")
            print(f"Nome do diretório pai do diretório do arquivo: {entry.parent.parent}")
            print(f"Metadados do arquivo: {entry.stat()}")
        if entry.is_dir():
            print(f"Nome do diretório: {entry.name}")
            print(f"Nome do diretório pai do diretório: {entry.parent}")
            print(f"Nome do diretório pai do diretório pai do diretório: {entry.parent.parent}")
            print(f"Metadados do diretório: {entry.stat()}")


def make_output_dir():
    dir_path = Path('output/')
    dir_path.mkdir(exist_ok=True)


def count_all_files(path):
    counter = 0
    entries = Path(path)
    for entry in entries.iterdir():
        counter += 1 if entry.is_file() else count_all_files(entry)
    return counter


if __name__ == "__main__":
    log = ControleLog(join(dirname(argv[0]), 'log'), True)
    print_directory_contents()
    log.info("Criando diretório output")
    make_output_dir()
    timeit_count_all_files('Path', count_all_files, log)


