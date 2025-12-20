#!/usr/bin/python3
<<<<<<< HEAD
"""Add all arguments to a Python list and save them to a JSON file."""
=======
"""Add all arguments to a Python list and save them to a file."""
>>>>>>> 7158139 (added new repo)
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

<<<<<<< HEAD

if __name__ == "__main__":
    filename = "add_item.json"

    try:
        items = load_from_json_file(filename)
    except Exception:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)
=======
filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
>>>>>>> 7158139 (added new repo)
