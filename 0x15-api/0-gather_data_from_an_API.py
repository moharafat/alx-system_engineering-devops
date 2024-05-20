#!/usr/bin/python3
"""Returns INFO. of employee after it's ID is passed as argumeent"""
import sys
import requests


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    EMPLOYEE_DATA = requests.get(URL + "users/{}".format(sys.argv[1])).json()
    EMPLOYEE_NAME = EMPLOYEE_DATA.get("name")

    EMPLOYEE_TASKS_FOR_SPECIFIC_EMPLOYEE =requests.get(URL + "todos/", params={"userId": sys.argv[1]}).json()
    COMPLETED_TASKS = []
    counter = 0
    for task in EMPLOYEE_TASKS_FOR_SPECIFIC_EMPLOYEE:
        if task.get("completed") == True:
            COMPLETED_TASKS.append(task.get("title"))
    len_T_C = (len(COMPLETED_TASKS))
    len_e_t_c = (len(EMPLOYEE_TASKS_FOR_SPECIFIC_EMPLOYEE))
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,len_T_C, len_e_t_c))
    for task in COMPLETED_TASKS:
        print("\t {}".format(task))
