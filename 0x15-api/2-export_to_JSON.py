#!/usr/bin/python3
"""
For given employee ID, returns information about his/her TODO list progress.
Export data in the JSON format.
"""
import json
import requests
import sys

if __name__ == '__main__':

    arg = sys.argv[1]

    base = 'https://jsonplaceholder.typicode.com/'

    user_url = base + 'users/{}'.format(arg)
    user = requests.get(user_url).json()
    query_params = {"userId": arg}
    todo_url = base + 'todos'
    todos = requests.get(url=todo_url, params=query_params).json()

    file = "{}.json".format(arg)

    dict_list = []
    for item in todos:
        todo_dict['task'] = item.get('title')
        todo_dict['completed'] = item.get('completed')
        todo_dict['username'] = user.get('username')
        dict_list.append(todo_dict)

    with open(file, 'w') as f:
        json.dump({arg: dict_list})
