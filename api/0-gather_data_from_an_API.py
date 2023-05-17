#!/usr/bin/python3
"""
TEST inin
"""
import urllib.request
import json
import sys

def get_employee_todo_progress(employee_id):
    # Make a GET request to the REST API
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())

    # Calculate the TODO list progress
    total_tasks = len(data)
    done_tasks = [task for task in data if task['completed']]
    done_task_count = len(done_tasks)
    employee_name = data[0]['name']

    # Print the employee's TODO list progress
    print(f"Employee {employee_name} is done with tasks ({done_task_count}/{total_tasks}):")

    # Print the titles of completed tasks
    for task in done_tasks:
        print(f"\t{task['title']}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide an employee ID as an argument.")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)