# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as in_file:
        reader = csv.DictReader(in_file)  # TODO считать содержимое csv файла
        list_of_dict = [row for row in reader]

    with open(OUTPUT_FILENAME, 'w') as out_file:  # TODO Сериализовать в файл с отступами равными 4
        json.dump(list_of_dict, out_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
