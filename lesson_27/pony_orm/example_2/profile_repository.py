from typing import List
from uuid import uuid4

from pony.orm import select, db_session, commit

from .models import Profile, User


class ProfilesRepository:
    @db_session
    def get_all(self) -> List[Profile]:
        return Profile.select()[:]

    @db_session
    def get_all_with_gender(self, gender: str) -> List[Profile]:
        return Profile.select(lambda p: p.gender == gender)[:]

    @db_session
    def get_all_with_first_name(self, first_name: str) -> List[Profile]:
        return Profile.select(lambda p: p.first_name == first_name)[:]

    @db_session
    def create_mocked_profiles(self):
        users = select(user for user in User)[:]

        Profile(
            id=uuid4(),
            first_name="John",
            last_name="Dow",
            gender="MALE",
            country_code="CA",
            user=users[0],
        )
        Profile(
            id=uuid4(),
            first_name="John",
            last_name="Dow",
            gender="MALE",
            country_code="UK",
            user=users[0],
        )
        Profile(
            id=uuid4(),
            first_name="Marta",
            last_name="Stuard",
            gender="FEMALE",
            country_code="US",
            user=users[3],
        )
        Profile(
            id=uuid4(),
            first_name="Jim",
            last_name="Bim",
            gender="MALE",
            country_code="CA",
            user=users[4],
        )
        Profile(
            id=uuid4(),
            first_name="John",
            last_name="Dow",
            gender="MALE",
            country_code="US",
            user=users[0],
        )
        Profile(
            id=uuid4(),
            first_name="Don",
            last_name="Julio",
            gender="MALE",
            country_code="UK",
            user=users[6],
        )
        Profile(
            id=uuid4(),
            first_name="Don",
            last_name="Julio",
            gender="MALE",
            country_code="CA",
            user=users[6],
        )
        commit()

    @db_session
    def delete_all_with_first_name(self, first_name: str):
        Profile.select(lambda p: p.first_name == first_name).delete()

    @db_session
    def update_one_with_id(self, id: str, profile: dict):
        Profile.get(id=id).set(**profile)
