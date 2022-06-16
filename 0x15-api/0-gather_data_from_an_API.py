#!/usr/bin/python3
"""
For given employee ID, returns information about his/her TODO list progress.
"""
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

    done = [item.get('title') for item in todos if item.get('completed')]

    print('Employee {} is done with tasks({}/{}):'.
          format(user.get('name'), len(done), len(todos)))

    for task in done:
        print("\t {}".format(task))
