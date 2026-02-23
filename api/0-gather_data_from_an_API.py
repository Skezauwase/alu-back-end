#!/usr/bin/python3
"""
Script that returns information about an employee's TODO list progress
using a REST API.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch employee data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch TODO list
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Count completed tasks
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Print progress line
    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, number_of_done_tasks, total_tasks
        )
    )

    # Print each completed task with correct formatting
    for task in done_tasks:
        print("\t {}".format(task.get("title")))

