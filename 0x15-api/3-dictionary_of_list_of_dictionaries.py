#!/usr/bin/python3
"""This script exports all employees data to json file"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users_url = url + "users"
    todos_url = url + "todos"

    users = requests.get(users_url).json()

    with open("todo_all_employees.json", mode="w") as json_file:
        json.dump({
            user.get("id"): [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            } for todo in requests.get(todos_url,
                                       params={"userId": user.get("id")}
                                       ).json()]
            for user in users}, json_file)
