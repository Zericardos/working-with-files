from os import mkdir
from sys import argv
from time import strftime
from os.path import join, isdir
from logging import Logger, Formatter, FileHandler, StreamHandler, CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET


class ControleLog(Logger):

    def __init__(self, diretorio: str, console: bool = False, nome: str = 'log', nivel: int = NOTSET):
        if not isdir(diretorio):
            mkdir(diretorio)
        Logger.__init__(self, nome, nivel)
        formato = Formatter('%(asctime)s - %(process)d - %(levelname)s - %(message)s', '%Y/%m/%d - %H:%M:%S')
        arquivo = FileHandler(join(diretorio, strftime('%Y-%m-%d') + '.log'))
        arquivo.setFormatter(formato)
        self.addHandler(arquivo)
        if console:
            console = StreamHandler()
            console.setFormatter(formato)
            self.addHandler(console)

    def cabecalho(self):
        self.info('------------------------------- PROCESSO INICIADO -------------------------------')
        argumentos = ''
        for arg in argv:
            argumentos += f' "{arg}"'
        self.info(f'Executando:{argumentos}')
        self.info('---------------------------------------------------------------------------------')

    def rodape(self):
        self.info('---------------------------------------------------------------------------------')
        self.info('------------------------------ PROCESSO FINALIZADO ------------------------------\n')

    CRT = CRITICAL
    ERR = ERROR
    WRN = WARNING
    INF = INFO
    DBG = DEBUG
    NTS = NOTSET
