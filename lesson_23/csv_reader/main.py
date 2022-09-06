from typing import List
from user import User


with open("users.csv", "r") as csv_file:
    csv_lines = csv_file.readlines()


users_data = {}
users_data["headers"] = csv_lines.pop(0)
users_data["data"] = csv_lines

users: List[User] = User.from_csv(users_data)
