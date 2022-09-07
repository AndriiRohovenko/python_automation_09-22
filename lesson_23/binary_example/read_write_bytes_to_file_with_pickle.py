import pickle


numbers = [1, 2, 3, 4, 5, 6]


# write binary data into the file
with open("./binary_example/data.txt", "wb") as file:
    # file.write(numbers) # error will occured

    # solution using pickle module
    file.write(pickle.dumps(numbers))

    # from scratch solution

# with open("./data.txt", "rb") as file:
#     _bytes = file.read()
#     read_numbers = pickle.loads(_bytes)

#     print(read_numbers)
#     print(type(read_numbers))


# with open("./data.txt", "wb") as file:
#     pickle.dump(numbers, file)


# with open("./data.txt", "rb") as file:
#     read_numbers = pickle.load(file)
#     print(read_numbers)
