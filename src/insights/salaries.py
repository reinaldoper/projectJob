from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    arq = read(path)
    max = 0
    list_item = []
    for job in arq:
        list_item.append(job['max_salary'])
    unique_numbers = set(list_item)
    unique = list(filter(lambda i: i if i.isdigit() else None, unique_numbers))
    nums = list(map(int, unique))
    for num in nums:
        if num > max:
            max = num
        else:
            num = num
    return max


def get_min_salary(path: str) -> int:
    arq = read(path)
    min = 9999999
    list_item = []
    for job in arq:
        list_item.append(job['min_salary'])
    unique_numbers = set(list_item)
    unique = list(filter(lambda i: i if i.isdigit() else None, unique_numbers))
    nums = list(map(int, unique))
    for num in nums:
        if num < min:
            min = num
        else:
            num = num
    return min


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    min_salary = job.get("min_salary", None)
    max_salary = job.get("max_salary", None)
    exists_salary(min_salary, max_salary)
    salary_is_number(min_salary, max_salary)
    salary_not_confusing(min_salary, max_salary)
    salary_than_0(min_salary, max_salary)
    salary_contaem_numbers(salary)

    if int(min_salary) <= int(salary) <= int(max_salary):
        print(True)
        return True
    print(False)
    return False


def exists_salary(min_salary, max_salary):
    if min_salary == "" or max_salary == "":
        raise ValueError("min e max salary necessarie")
    else:
        return True


def salary_is_number(min_salary, max_salary):
    if not str(min_salary).isdigit() or not str(max_salary).isdigit():
        raise ValueError("salary needs to be number")
    else:
        return True


def salary_than_0(min_salary, max_salary):
    if int(min_salary) < 0 or int(max_salary) <= 0:
        raise ValueError("salary cannot be 0")
    else:
        return True


def salary_not_confusing(min_salary, max_salary):
    if int(min_salary) > int(max_salary):
        raise ValueError("max salary needs to be greater than min salary")
    else:
        return True


def salary_contaem_numbers(salary):
    if salary == "":
        raise ValueError("salary necessarie")
    if str(salary).isdigit() or (
        str(salary)[0] == "-" and str(salary)[1:].isdigit()
    ):
        return True
    else:
        raise ValueError("entry salary needs to be numbers")


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    list_item_jobs = []
    Error = "Error: "
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_item_jobs.append(job)
        except ValueError as erro:
            print(Error + f"{erro}")
    return list_item_jobs
