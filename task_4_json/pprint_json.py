import json
import sys


def load_data(filepath):
    with open(filepath, "r") as shops:
        return json.load(shops)


def pretty_print_json(shops):
    print(json.dumps(shops, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    pretty_print_json(load_data(sys.argv[1]))
