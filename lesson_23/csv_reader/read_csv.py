from typing import List
from user import User


with open("users.csv", "r") as csv_file: 
    for user in User.from_csv(csv_file.read()):
        xml_file_name = (
            f"{user.first_name.lower()}_{user.last_name.lower()}.xml"
        )

        with open(xml_file_name, "w") as xml_file:
            xml_file.write(user.to_xml())
