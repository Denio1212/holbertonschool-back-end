#!/usr/bin/python3
"""
Turns into JSON file now
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
        "https://jsonplaceholder.typicode.com/users/{}".format(id)

    )

    data_todo = todo.text
    data_user = user.text

    current_user = json.loads(data_user)
    current_todo = json.loads(data_todo)

    listed = []
    for data in current_todo:
        if data["userId"] == current_user["id"]:
            json_dict = {}
            json_dict["username"] = data["username"]
            json_dict["task"] = data["title"]
            json_dict["completed"] = data["completed"]
            listed.append(json_dict)
        result = {str(current_user["id"]): listed}
        with open("{}.json".format(emp_ID), "a", newline="") as f:
            json.dump(result, f)
