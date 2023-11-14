import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:

    with open(INPUT_FILENAME, "r") as f_in:
        csv_data = []

        for row in csv.DictReader(f_in):
            csv_data.append(row)


    with open(OUTPUT_FILENAME, 'w') as f_out:
        json.dump(csv_data, f_out, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
