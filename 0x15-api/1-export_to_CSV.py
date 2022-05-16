#!/usr/bin/python3
"""getting data from an api and storing as CSV file
"""

import requests
from sys import argv


def main():
    """Main Function"""
    endpoint = "https://jsonplaceholder.typicode.com/"
    userId = argv[1]
    user = requests.get(endpoint + "users/{}".
                        format(userId), verify=False).json()
    todo = requests.get(endpoint + "todos?userId={}".
                        format(userId), verify=False).json()
    with open("{}.csv".format(userId), 'w', newline='') as csvfile:
        my_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            my_writer.writerow([int(userId), user.get('username'),
                                task.get('completed'),
                                task.get('title')])

if __name__ == '__main__':
    main()
