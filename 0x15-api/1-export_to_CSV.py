#!/usr/bin/python3
"""
This script send request to get employees done data
This script writes the request response to csv file
"""
import csv
import requests
import sys


def get_employee_progress(employee_id):
    """this method sends http request to get response data"""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)

        user_data = user_response.json()
        todo_data = todo_response.json()

        if (user_response.status_code == 200 and
                todo_response.status_code == 200):
            employee_name = user_data["name"]

            employee_id = user_data["id"]
            employee_name = user_data["username"]

            csv_filename = f"{employee_id}.csv"

            with open(csv_filename, mode="w", newline="") as csv_file:
                csv_writer = csv.writer(csv_file,
                                        delimiter=",",
                                        quotechar='"',
                                        quoting=csv.QUOTE_ALL
                                        )

                for task in todo_data:
                    task_completed = task["completed"]
                    task_title = task["title"]
                    csv_writer.writerow(
                        [employee_id,
                         employee_name,
                         task_completed,
                         task_title]
                        )
            print(f"Data exported to {csv_filename}")
        else:
            print("Request failed")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
    else:
        employee_id = int(sys.argv[1])
        get_employee_progress(employee_id)
