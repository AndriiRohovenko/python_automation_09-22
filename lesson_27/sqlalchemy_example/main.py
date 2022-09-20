from lesson_27.sqlalchemy_example.models import User

# User(id="aaaaa", email="john.dow@gmail.com").insert()
# User(id="bbbbb", email="jane.dow@gmail.com").insert()
# User(id="ccccc", email="james.dow@gmail.com").insert()
# User(id="ddddd", email="marta.stuard@gmail.com").insert()

# user = User.by_email("john.dow@gmail.com")
# print(user)


# Profile(id="acaca", first_name="John", last_name="Dow", country_code="CA", user_id="aaaaa").insert()
# Profile(id="ababa", first_name="John", last_name="Dow", country_code="UK", user_id="aaaaa").insert()
# Profile(id="adada", first_name="John", last_name="Dow", country_code="US", user_id="aaaaa").insert()
# Profile(id="hjhjh", first_name="Jane", last_name="Dow", country_code="CA", user_id="bbbbb").insert()
# Profile(id="jkjkj", first_name="James", last_name="Dow", country_code="CA", user_id="ccccc").insert()
# Profile(id="oioio", first_name="Marta", last_name="Stuard", country_code="CA", user_id="ddddd").insert()


user = User.by_email("john.dow@gmail.com")
print(user)
for profile in user.profiles:
    print(profile)
