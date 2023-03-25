from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():

    jobs = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    list_item = []
    for job in jobs:
        list_item.append(set(job.keys()))
    for keys in list_item:
        for key in list(keys):
            assert key in ["title", "salary", "type"]
