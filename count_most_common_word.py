import glob
import os
import re
from collections import Counter, defaultdict
from os.path import join, dirname
from sys import argv
from controle_log import ControleLog
from utils import function_report, timeit_count_words


@function_report
def count_words_using_scandir(directory_path: str, log: ControleLog):
    most_common_word_list = []
    for file in os.scandir(directory_path):
        words_list = []
        if file.is_file():
            with open(file) as text_file:
                for line in text_file:
                    line = line.rstrip().lower()
                    words_list.extend(list(filter(None, re.sub(r'[\.,]', ' ', line).split(' '))))
                most_common_word_list.extend(words_list)
                counter = Counter(words_list)
                most_common_word = max(counter, key=counter.get)
                times_appeared = max(counter.values())
                log.info(f"A palavra mais comum no arquivo {file.name} é \'{most_common_word}\' e apareceu "
                         f"{times_appeared} vezes.")
    counter = Counter(most_common_word_list)
    most_common_word_at_all = max(counter, key=counter.get)
    times_appeared = max(counter.values())
    log.info(f"A palavra mais comum em todos os arquivos é \'{most_common_word_at_all}\' e apareceu {times_appeared}"
             f" vezes.")


@function_report
def count_words_using_glob(pattern_path: str, log: ControleLog):
    dict_files_words = Counter(defaultdict(int))
    for text_file in glob.glob(pattern_path):
        with open(text_file) as file:
            dict_file_words = defaultdict(int)
            for line in file:
                line = list(filter(None, re.sub(r'[\.,]', ' ', line.lower().rstrip()).split(' ')))
                for word in line:
                    dict_file_words[word] += 1
            file_most_common_word = max(Counter(dict_file_words), key=Counter(dict_file_words).get)
            log.info(f"A palavra mais comum no arquivo {file.name} é \'{file_most_common_word}\' e apareceu "
                     f"{dict_file_words[file_most_common_word]} vezes.")
        dict_files_words += Counter(dict_file_words)
    files_most_common_word = max(Counter(dict_files_words), key=Counter(dict_files_words).get)
    log.info(f"A palavra mais comum em todos os arquivos é \'{files_most_common_word}\' e apareceu "
             f"{dict_files_words[files_most_common_word]} vezes.")


@function_report
def official_count_words(pattern_path: str, log: ControleLog):
    txt_files = glob.glob(pattern_path)
    tracker = dict()
    log.info(f"Number of Txt Files: {len(txt_files)}")

    for txt in txt_files:
        with open(txt) as f:
            line = f.readline()
            while line != '':
                words = line.split()
                for word in words:
                    word = word.replace(',', '').replace('.', '').lower()
                    if word not in tracker:
                        tracker[word] = 1
                    else:
                        tracker[word] = tracker[word] + 1
                line = f.readline()

    maxKey = max(tracker, key=tracker.get)
    maxValue = max(tracker.values())

    log.info(f"Most common word: {maxKey}")
    log.info(f"How many times: {maxValue}")
    # log.info(f"Dictionary: {tracker}")


if __name__ == "__main__":
    controlelog = ControleLog(join(dirname(argv[0]), 'log'), True)
    timeit_count_words(count_words_using_scandir, 'articles', controlelog)
    timeit_count_words(count_words_using_glob, 'articles/*.txt', controlelog)
    timeit_count_words(official_count_words, 'articles/*.txt', controlelog)
