#!/usr/bin/python3
"""script to export data in the CSV format."""
import requests
import sys


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"


    EMPLOYEE_DATA = requests.get(URL + "users/{}".format(sys.argv[1])).json()
    EMPLOYEE_ID = EMPLOYEE_DATA.get("id")
    EMPLOYEE_USERNAME = EMPLOYEE_DATA.get("username")

    Tasks_4_emply = requests.get(
        URL + "todos/", params={"userId": sys.argv[1]}).json()
    COMPLETED_TASKS = []
    for task in Tasks_4_emply:
        if task.get("completed"):
            COMPLETED_TASKS.append(task.get("title"))
    len_T_C = (len(COMPLETED_TASKS))
    len_e_t_c = (len(Tasks_4_emply))
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, len_T_C, len_e_t_c))
    for task in COMPLETED_TASKS:
        print("\t {}".format(task))
