import csv


def get_unique_and_broken_lines(path: str):
    broken_lines = list()
    uniq_lines = list()

    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='|')
        data = [*reader]

    data.sort(key=lambda x: x["id"])

    i = 0
    while i < len(data) - 1:
        # Delete duplicate lines. Duplicate lines will not be included to broken_lines
        if data[i] == data[i + 1]:
            del data[i]
            continue
        # Check on unique or broken line
        unique_ctx = (False if data[i]["id"] in (data[i - 1]["id"], data[i + 1]["id"]) else True)
        uniq_lines.append(data[i]) if unique_ctx else broken_lines.append(data[i])
        i += 1

    # Treatment last element
    unique_ctx = (False if data[-1]["id"] == data[-2]["id"] else True)
    uniq_lines.append(data[-1]) if unique_ctx else broken_lines.append(data[-1])

    return [uniq_lines, broken_lines]
