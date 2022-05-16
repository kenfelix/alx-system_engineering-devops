"""Getting Data from an API"""

import requests
from sys import argv


def main():
    """Main function"""
    user_Id = argv[1]
    todo = requests.get("https://jsonplaceholder.typicode.com/todos/{}".format(user_Id), verify=false).json()
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(user_Id), verify=false).json()
    
    completed_tasks = []
    for task in todo:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(completed_tasks), len(todo)))
    print("\n".join("\t {}".format(task) for task in completed_tasks))

if __name__ == '__main__':
    main()
