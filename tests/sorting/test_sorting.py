from src.pre_built.sorting import sort_by
import pytest


@pytest.fixture
def min():
    return [
        {"min_salary": 0, "max_salary": "", "date_posted": ""},
        {"min_salary": 1000, "max_salary": 2500, "date_posted": "2022-11-15"},
        {"min_salary": 1500, "max_salary": 3000, "date_posted": "2021-01-01"},
        {"min_salary": 5000, "max_salary": 10000, "date_posted": "2023-01-13"},
    ]


@pytest.fixture
def max():
    return [
        {"min_salary": 5000, "max_salary": 10000, "date_posted": "2023-01-13"},
        {"min_salary": 1500, "max_salary": 3000, "date_posted": "2021-01-01"},
        {"min_salary": 1000, "max_salary": 2500, "date_posted": "2022-11-15"},
        {"min_salary": 0, "max_salary": "", "date_posted": ""},
    ]


@pytest.fixture
def date():
    return [
        {"min_salary": 5000, "max_salary": 10000, "date_posted": "2023-01-13"},
        {"min_salary": 1000, "max_salary": 2500, "date_posted": "2022-11-15"},
        {"min_salary": 1500, "max_salary": 3000, "date_posted": "2021-01-01"},
        {"min_salary": 0, "max_salary": "", "date_posted": ""},
    ]


def test_sort_by_criteria(min, max, date):
    data = [
        {"min_salary": 1500, "max_salary": 3000, "date_posted": "2021-01-01"},
        {"min_salary": 5000, "max_salary": 10000, "date_posted": "2023-01-13"},
        {"min_salary": 0, "max_salary": "", "date_posted": ""},
        {"min_salary": 1000, "max_salary": 2500, "date_posted": "2022-11-15"},
    ]
    critery = ["min_salary", "max_salary", "date_posted"]
    list_itens = [min, max, date]
    for index, criteria in enumerate(critery):
        sort_by(data, criteria)
        assert data == list_itens[index]

    with pytest.raises(ValueError, match="invalid sorting criteria: error"):
        sort_by(data, "error")
