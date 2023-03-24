import csv
from functools import lru_cache
from typing import List, Dict


@lru_cache
def read(path: str) -> List[Dict]:
    arquivo = path
    with open(arquivo, encoding="utf-8") as file:
        graduacao_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        array = []
        for reader in graduacao_reader:
            array.append(reader)
    return array


def get_unique_job_types(path: str) -> List[str]:
    arq = read(path)
    list_item = []
    for job in arq:
        list_item.append(job['job_type'])

    unique_numbers = set(list_item)
    return list(unique_numbers)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    list_item = []
    for job in jobs:
        if (job['job_type'] == job_type):
            list_item.append(job)
    if (len(list_item) != 0):
        return list_item
    else:
        return []
