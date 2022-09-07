from typing import List


with open("./data.txt", "r") as file:
    lines = file.readlines()


# text = file.read()
# print(text)

# read by one line
# print(file.readline())
# print(file.readline())
# print(file.readline())


# read all lines
# print(file.readlines())


# region task
def make_operation(line: str) -> int:
    cleaned_line = line.strip()
    elements = cleaned_line.split(",")

    left_operand, operator, right_operand = [int(el) for el in elements]

    if operator == 1:
        result = left_operand + right_operand
    elif operator == 2:
        result = left_operand - right_operand
    elif operator == 3:
        result = left_operand * right_operand
    else:
        raise Exception("Incorrect operation...")

    return result


results: List[int] = []


for line in lines:
    results.append(make_operation(line))


with open("./results.txt", "w") as file:
    file.write("\n".join(f"{n}" for n in results))
