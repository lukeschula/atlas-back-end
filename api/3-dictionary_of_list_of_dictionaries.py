#!/usr/bin/python3
"""export data in the JSON format"""


from sys import argv
from requests import get
from json import dump

link = "https://jsonplaceholder.typicode.com/users/"


def print