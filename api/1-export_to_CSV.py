#!/usr/bin/python3
"""export data in the CSV format"""

from sys import argv
from requests import get

link = "https://jsonplaceholder.typicode.com/"


def export_data_CSV():
    employee = get(link + argv[1]).json()
    tasks = get(link + argv[1] + '/todos').json()
    convert = argv[1] + '.csv'

    for task in tasks:
        display = '"' + str(employee['id']) + '",' + '"' + employee['username'] + '",' +\
        '"' + str(task['completed']) + '",' + '"' + task['title'] +\
        '"\n'

        with open(convert, 'a', encoding='uft-8') as f:
            f.write(display)


if __name__ == '__main__':
    export_data_CSV()
