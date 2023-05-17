#!/usr/bin/python3
"""
Exports data to the csv format
Basically the new stuff here is the csv module
csv.writer -> writes a file in a csv format
quotechar -> the character to be quoted
quoting -> where quoting should take place
has a bunch of options to customise it
"""
import csv
import json
from requests import get
from sys import argv

if __name__ == "__main__":
    """
    api script
    """
    emp_ID = argv[1]

    todo = get(
        "https://jsonplaceholder.typicode.com/todos"
    )

    user = get(
        "https://jsonplaceholder.typicode.com/todos".format(id)

    )

    data_todo = todo.text
    data_user = user.text

    current_user = json.loads(data_user)
    current_todo = json.loads(data_todo)

    with open("{}.csv".format(emp_ID), 'a', newline='') as f:
        for data in current_todo:
            if data["userId"] == current_user["id"]:
                listed = (id, current_user["username"], str(data["completed"]),
                          str(data["title"]))
                file = csv.writer(f, delimiter=',',
                                  quotechar='"', quoting=csv.QUOTE_ALL)
                file.writerow(listed)
