# 1. Create a script that should find the lines by provided pattern in the
# provided path directory with recursion* and threads


import glob
import time
from concurrent.futures import ThreadPoolExecutor
import psutil

core_num = psutil.cpu_count()


def find_by_pattern(filename, pattern):
    container = []
    with open(filename) as file:
        for line in file:
            if pattern in line:
                container.append(line)
    return container


def find_all_files(directory_path, pattern):
    files = glob.glob(f'{directory_path}/**/*.py', recursive=True)
    container = []
    with ThreadPoolExecutor(core_num - 1) as executor:
        result = list(executor.map(find_by_pattern, files, pattern))
        container.append(result)
    return container


if __name__ == '__main__':
    start = time.time()
    first = find_all_files('.', pattern=['ThreadPoolExecutor'])
    second = find_all_files('.', pattern=['ProcessPoolExecutor'])
    third = find_all_files('.', pattern=['get_session'])
    fourth = find_all_files('.', pattern=['result.text'])
    fifth = find_all_files('../threads_processes_practice', pattern=['ThreadPoolExecutor'])
    sixth = find_all_files('../threads_processes_practice', pattern=['ProcessPoolExecutor'])
    seventh = find_all_files('../threads_processes_practice', pattern=['get_session'])
    eighth = find_all_files('../threads_processes_practice', pattern=['result.text'])
    print(f'Total time for search: {time.time() - start}')
    all_search = [first, second, third, fourth, fifth, sixth, seventh, eighth]

    for search in all_search:
        for element in search:
            print(element)
