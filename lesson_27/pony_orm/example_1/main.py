from pony.orm import Database, Required, PrimaryKey, Set, commit, db_session, select

db = Database()


class User(db.Entity):
    id = PrimaryKey(str)
    email = Required(str)
    age = Required(int)
    gender = Required(str)

    def __str__(self):
        return f"{self.id} | {self.email} | {self.age} | {self.gender}"


db.bind(provider='postgres', user='postgres', password='postgres', host='localhost', database='test')
db.generate_mapping(create_tables=False)


@db_session
def insers_users():
    User(id="aaaaa", email="john.dow@gmail.com", age=12, gender="male")
    User(id="bbbbb", email="jane.dow@gmail.com", age=21, gender="female")
    User(id="vvvvv", email="marta.stuard@gmail.com", age=34, gender="female")

    commit()


# insers_users()


@db_session
def get_all() -> User:
    # return select(user for user in User).show()

    for user in select(user for user in User):
        print(user)


get_all()
