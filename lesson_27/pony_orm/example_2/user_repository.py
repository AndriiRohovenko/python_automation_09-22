from typing import List
from uuid import uuid4

from pony.orm import select, db_session, commit

from .models import User
from ...sqlalchemy_example.models import Profile


class UsersRepository:
    @db_session
    def get_all(self) -> List[User]:
        return select(user for user in User)[:]

    @db_session
    def get_all_canadian_profiles_with_email(self, email: str) -> List[Profile]:
        return (
            User.get(lambda u: u.email == email)
            .profiles.filter(lambda p: p.country_code == "CA")[:]
        )

    @db_session
    def create_mocked_users(self):
        User(id=uuid4(), email="john.dow@gmail.com")
        User(id=uuid4(), email="jane.dow@gmail.com")
        User(id=uuid4(), email="james.dow@gmail.com")
        User(id=uuid4(), email="marta.stuard@gmail.com")
        User(id=uuid4(), email="jim.bim@gmail.com")
        User(id=uuid4(), email="jose.cuervo@gmail.com")
        User(id=uuid4(), email="don.julio@gmail.com")
        commit()

    @db_session
    def delete_with_email(self, email: str):
        User.get(email=email).delete()