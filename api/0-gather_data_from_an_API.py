#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID"""

import requests
import sys


def employee_todo(employeeId):
    """returns all tasks assigned to employee"""
    link = "https://jsonplaceholder.typicode.com/"
    link += "users/{}/todos".format(employeeId)
    display = requests.get(link)
    return display.json()


def employee_name(employeeId):
    """returns name of specific employee"""
    link = "https://jsonplaceholder.typicode.com/"
    link += "users/{}".format(employeeId)
    display = requests.get(link)
    return display.json().get("name")


def tasks_done(tasks):
    """returns number of tasks completed by employee"""
    tasks_completed = []

    for task in tasks:
        if task.get("completed"):
            tasks_completed.append(task)
    return tasks_completed


def print_tasks(employeeName, completedTasks, totalTasks):
    """print all tasks assigned to employee"""
    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, completedTasks, totalTasks))
    for task in completedTasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    employeeId = sys.argv[1]
    tasks = employee_todo(employeeId)
    employeeName = employee_name(employeeId)
    completedTasks = tasks_done(tasks)
    print_tasks(employeeName, completedTasks, tasks)
