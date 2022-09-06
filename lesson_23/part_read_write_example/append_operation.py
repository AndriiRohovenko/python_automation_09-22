
names = ["John Dow", "Marta Stuard", "Jane Dow", "John Johns"]

for name in names:
    with open("some_text.txt", "a") as file:
        file.write(name)
