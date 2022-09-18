from context_manager_example import Human


# with Human("John Dow", 32, "Male") as john:
#     john.save()

john = Human("John Dow", 32, "Male")

print(john.name)
