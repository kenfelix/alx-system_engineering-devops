#!/usr/bin/python3
"""
For given employee ID, returns information about his/her TODO list progress.
Export data in the CSV format.
"""
import csv
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

    name = user.get('username')
    file = "{}.csv".format(arg)

    with open(file, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for item in todos:
            writer.writerow([arg, name,
                            item.get('completed'),
                            item.get('title')])
