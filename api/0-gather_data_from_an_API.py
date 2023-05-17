#!/usr/bin/python3
"""
Retrieves information on employee To do list
"""
import urllib.request
import json
import sys


def get_employee_todo_progress(employee_id):
    """
    Gets the employee to do requests
    """
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = urllib.request.urlopen(url)
    data = json.lo
    total_tasks = len(data)
    done_tasks = [task for task in data if task['completed']]
    done_task_count = len(done_tasks)
    employee_name = data[0]['name']

    print(f"Employee {employee_name} is done with tasks ({done_task_count}/{total_tasks}):")

    for task in done_tasks:
        print(f"\t{task['title']}")


if __name__ == '__main__':
    """
    doctor is the one
    """
    if len(sys.argv) < 2:
        print("Please provide an employee ID as an argument.")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)ads(response.read().decode())

