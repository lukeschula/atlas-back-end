#!/usr/bin/python3
"""export data in the JSON format"""


from sys import argv
from requests import get
from json import dump

link = "https://jsonplaceholder.typicode.com/users/"


def convert_JSON(id):
    """retrieves data in JSON format"""
    JSON_file = str(id) + '.json'
    employee = get(link + str(id)).json()
    lists = get(link + str(id) + '/todos/').json()
    data = []
    convert_json = dict()

    for list in lists:
        new_dict = dict()
        new_dict['task'] = list['title']
        new_dict['completed'] = list['completed']
        new_dict['username'] = employee['username']
        data.append(new_dict)

    convert_json[str(id)] = data

    with open (JSON_file, 'w', encoding='utf-8') as f:
        dump(convert_json, f)


if __name__ == '__main__':
    convert_JSON(int(argv[1]))
