import json


FILE_NAME = "input.json"


def task() -> float:
    with open(FILE_NAME, "r") as f:
        json_data = json.load(f)

    result = sum([i["score"] * i["weight"] for i in json_data])
    return round(result, 3)


if __name__ == '__main__':
    print(task())