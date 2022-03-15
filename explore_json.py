import json
from os.path import join, dirname
from sys import argv

from controle_log import ControleLog


def display_json():
    log.info("Lendo o arquivo monster.json")
    with open('json_files/monster.json') as json_file:
        content_json = json.load(json_file)
        log.info("Imprimindo o seu conteúdo")
        print(content_json)


def display_monster_name():
    log.info("Lendo o arquivo monster.json")
    with open('json_files/monster.json') as json_file:
        content_json = json.load(json_file)
        log.info("Dar bom dia ao monstro")
        print(f"Welcome {content_json['monsterName']}")


if __name__ == "__main__":
    log = ControleLog(join(dirname(argv[0]), 'log'), True)
    display_json()
    display_monster_name()
