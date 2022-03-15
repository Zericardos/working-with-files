import os
import time
from os.path import basename

from controle_log import ControleLog


def timeit_count_all_files(class_method: str, function: callable, log):
    log.info(f"Executada função {function.__name__}")
    attempts = 3
    log.info(f"Measuring time execution to count all files in {basename(os.getcwd())} using {class_method}")
    total_time_interval = 0
    for attempt in range(attempts):
        start_time = time.time()
        total_files = function('.')
        log.info(f"In {basename(os.getcwd())} are {total_files} total files ")
        time_interval = time.time() - start_time
        log.info(f"Took {time_interval} seconds, {attempt + 1} attempt")
        total_time_interval += time_interval
    log.info(f"Mean time {total_time_interval / attempts} seconds, total {attempts} attempts using "
             f"{class_method}")


def function_report(function):
    def report(path, log):
        opening_message = f" Executando função \'{function.__name__}\' "
        highlighted_characters = '*'*count_especial_characters(opening_message)
        log.info(f"{highlighted_characters}{opening_message}{highlighted_characters}")
        function(path, log)
        closing_message = f" Final da execução da função \'{function.__name__}\' "
        highlighted_characters = '*'*count_especial_characters(closing_message)
        log.info(f"{highlighted_characters}{closing_message}{highlighted_characters}")
    return report


def count_especial_characters(message: str) -> int:
    length_message = int((81 - len(message))/2)
    return length_message if length_message > 0 else 0


def timeit_count_words(function: callable, path: str, log: ControleLog):
    attempts = 3
    log.info(f"Measuring time execution to count most common word in {basename(os.getcwd())} using {function.__name__}")
    total_time_interval = 0
    for attempt in range(attempts):
        start_time = time.time()
        function(path, log)
        time_interval = time.time() - start_time
        log.info(f"Took {time_interval} seconds, {attempt + 1} attempt")
        total_time_interval += time_interval
    log.info(f"Mean time {total_time_interval / attempts} seconds, total {attempts} attempts using "
             f"{function.__name__}")
