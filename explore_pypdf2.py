import time
from os.path import join, dirname
from sys import argv

import PyPDF2

from controle_log import ControleLog

SPC = '-' * 39


def read_pdf(log: ControleLog):
    log.info(f"Executada função {read_pdf.__name__}")
    arquivo_pdf = 'pdf_files/recipe-book.pdf'
    log.info(f"Lendo arquivo {arquivo_pdf}")
    with open(arquivo_pdf, 'rb') as pdf_file:
        log.info(f"Construindo o objeto pdf")
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        log.info(f"Imprimindo o número de páginas: {pdf_reader.numPages}")
        info = pdf_reader.getDocumentInfo()
        data_criacao = time.strftime('%d/%m/%Y', time.strptime(info['/CreationDate'][2:8], '%y%d%m'))
        log.info(f"Informações do documento, Autor: {info['/Author']}, Data de criação: {data_criacao}")
        # page_two = pdf_reader.getPage(2)
        # log.info(f"Imprimindo a segunda página \n{SPC} {page_two.extractText()}")


def read_all_pages(log: ControleLog):
    log.info(f"Executada função {read_all_pages.__name__}")
    arquivo_pdf = 'pdf_files/recipe-book.pdf'
    log.info(f"Lendo arquivo {arquivo_pdf}")
    with open(arquivo_pdf, 'rb') as pdf_file:
        log.info(f"Construindo o objeto pdf")
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        numero_paginas = pdf_reader.numPages
        log.info(f"Imprimindo todas as {numero_paginas} páginas")
        info = pdf_reader.getDocumentInfo()
        data_criacao = time.strftime('%d/%m/%Y', time.strptime(info['/CreationDate'][2:8], '%y%d%m'))
        log.info(f"Informações do documento, Autor: {info['/Author']}, Data de criação: {data_criacao}")
        for page_number in range(numero_paginas):
            n_page = pdf_reader.getPage(page_number)
            log.info(f"Imprimindo a {page_number+1}ª página \n{SPC} {n_page.extractText()}")


if __name__ == "__main__":
    controlelog = ControleLog(join(dirname(argv[0]), 'log'), True)
    read_pdf(controlelog)
    read_all_pages(controlelog)
