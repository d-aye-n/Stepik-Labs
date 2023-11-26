# TODO решите задачу
import json

IMPORT_FILE = 'input.json'


def task() -> float:
    with open(IMPORT_FILE) as f:
        json_data = json.load(f)

    res = sum([el['score'] * el['weight'] for el in json_data])
    return round(res, 3)


print(task())
