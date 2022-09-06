with open("text.txt") as file:
    text = file.read()


print(text)
print()


with open("text.txt") as file:
    text = file.read(30)
    another_text = file.read(30)


print(text)
print(another_text)
