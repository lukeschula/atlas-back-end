#!/usr/bin/python3
"""export data in the JSON format"""


from sys import argv
from requests import get
from json import dump

link = "https://jsonplaceholder.typicode.com/users/"


def data_to_JSON():
    """export data in the JSON format"""
    employees = get(link).json()
    get_json = dict()

    for employee in employees:
        emp_id = employee['id']
        stats = []
        tasks = get(link + str(emp_id) + '/todos/').json()

        for todo in tasks:
            new_dict = {
                'task': todo['title'],
                'completed': todo['completed'],
                'username': employee['username']
            }
            stats.append(new_dict)
        get_json[emp_id] = stats

    with open('todo_all_employees.json', 'w', encoding='utf-8') as f:
        dump(get_json, f)


if __name__ == '__main__':
    data_to_JSON()
