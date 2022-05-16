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
    with open("{}.json".format(userId), "w") as json_file:
        json.dump({userId: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")} for task in todo]}, json_file)
        
if __name__ == '__main__':
    main()
