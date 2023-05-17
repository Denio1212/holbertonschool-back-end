#!/usr/bin/python3
"""
Retrieves information on employee To do list
"""
import requests

if __name__ == "__main__":
    def get_employee_todo_progress(employee_id):
        """
        Make a get request ti Rest API
        """
        response = requests.get(f'https://jsonplaceholder.\
                            typicode.com/todos?userId={employee_id}')

        if response.status_code == 200:
            todos = response.json()
        tasks = len(todos)
        tasks_completed = {todo for todo in todos if todo["completed"]}
        completed = len(tasks_completed)
        employee_name = todos[0]['username']

        print(f"Employee {employee_name} is done with tasks ({completed}/{tasks}):")

        for item in tasks_completed:
            print(f"\t{item['title']}")
        else:
            print(f"Failed to retrieve TODO list. Error: {response.status_code}")
