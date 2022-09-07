# numbers = [1, 2, 3, 4, 5]

# write bytes into the file
# with open("./data_new.txt", "wb") as file:
#     file.write(
#         bytes(numbers)
#     )


# read bytes from file and convert back to structure
with open("./data_new.txt", "rb") as file:
    bytes = file.read()
    print(list(bytes))
