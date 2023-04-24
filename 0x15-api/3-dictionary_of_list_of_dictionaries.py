#!/usr/bin/python3
""" a Python script that, using a REST API, for a given employee ID,
    returns information about his/her TODO list progress."""
import json
import requests
import sys


if __name__ == '__main__':
    data = {}
    url2 = 'https://jsonplaceholder.typicode.com/todos'
    r2 = requests.get(url2)
    for item in r2.json():
        if str(item.get('userId')) not in data:
            data[str(item.get('userId'))] = []
        url = 'https://jsonplaceholder.typicode.com/users?id='\
              + str(item.get('userId'))
        r = requests.get(url)
        r = r.json()
        username = r[0]['username']
        d = {}
        d['task'] = item.get('title')
        d['completed'] = item.get('completed')
        d['username'] = username
        data[str(item.get('userId'))].append(d)

    filename = 'todo_all_employees.json'
    with open(filename, 'w') as f:
        json.dump(data, f)
