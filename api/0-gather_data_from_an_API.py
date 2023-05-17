#!/usr/bin/python3
"""
Retrieves information on employee To do list

New stuff ***
Get -> accesses the external source of the API to acquire information
json -> basically used to extract the info into any program
text-> accesses the data in string format

The idea of this is quite simple. It takes a bit to get it but
the premise is getting the variables from the api and doing simple
processes, But still a bit tricky to figure out since this school
doesn't really provide a clearer explanation. They tell you to
figure it out on your own and I always feel Braindead when i'm just
uncomfortable with the topic since its my first try
"""
import json
from requests import get
from sys import argv


if __name__ == "__main__":
    """
    Api script
    """
    emp_ID = argv[1]
    todos = get(
        "https://jsonplaceholder.typicode.com/todos"
    )
    user = get(
        "https://jsonplaceholder.typicode.com/users/{}".format(emp_ID)
    )
    data_todo = todos.text
    data_user = user.text

    current_todo = json.loads(todos.text)
    current_user = json.loads(user.text)

    task_count = 0
    completed_todo = []

    for data in current_todo:
        if data["userID"] == current_user["id"]:
            task_count += 1
            if data["completed"]:
                completed_todo.append(data)

    print("Employee {} is done with tasks({}/{}):".format(
        current_user['name'], len(completed_todo), task_count))

    for done in completed_todo:
        print(f"\t {done['title']}")
