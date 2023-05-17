#!/usr/bin/python3
"""
Retrieves information on employee To do list

New stuff ***
Get -> accesses the external source of the API to acquire information
json -> basically used to extract the info into any program
The idea of this is quite simple. It takes a bit to get it but
the premise is getting the variables from the api and doing simple
processes, But still a bit tricky to figure out since this school
doesn't really provide a clearer explanation. They tell you to
figure it out on your own and I always feel Braindead when i'm just
uncomfortable with the topic since its my first try
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    todos_data = response.json()
    completed = 0
    total_task = 0
    tasks = []
    users_get = get('https://jsonplaceholder.typicode.com/users')
    users_data = users_get.json()

    for user in users_data:
        if user.get("id") == int(argv[1]):
            employee_name = user.get("name")

    for ids in todos_data:
        if ids.get("userId") == int(argv[1]):
            total_task += 1

            if ids.get("completed") is True:
                completed += 1
                tasks.append(ids.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          completed, total_task))

    for content in tasks:
        print("\t {}".format(content))
