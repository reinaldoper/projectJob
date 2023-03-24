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
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
