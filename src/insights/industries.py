from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    arq = read(path)
    list_item = []
    for job in arq:
        list_item.append(job['industry'])

    unique_numbers = set(list_item)
    unique = list(filter(None, unique_numbers))
    return unique


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    list_item = []
    for job in jobs:
        if (job['industry'] == industry):
            list_item.append(job)
    if (len(list_item) != 0):
        return list_item
    else:
        return []
