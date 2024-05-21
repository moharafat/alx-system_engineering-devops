#!/usr/bin/python3
"""script to export data in the CSV format."""
import csv
import requests
import sys


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    EMPLOYEE_DATA = requests.get(URL + "users/{}".format(sys.argv[1])).json()
    EMPLOYEE_ID = EMPLOYEE_DATA.get("id")
    EMPLOYEE_USERNAME = EMPLOYEE_DATA.get("username")

    todos_response = requests.get(
        URL + "todos/", params={"userId": sys.argv[1]})
    todos_response.raise_for_status()
    todos_data = todos_response.json()
    file_name = f"{EMPLOYEE_ID}.csv"

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                EMPLOYEE_ID, EMPLOYEE_USERNAME, task.get(
                    "completed"), task.get("title")])
