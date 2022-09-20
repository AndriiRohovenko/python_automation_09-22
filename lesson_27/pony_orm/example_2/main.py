from typing import List

from pony.orm import db_session, select

from lesson_27.pony_orm.example_2.core import base

# here we have get both models and after this step we can generate mapping
from lesson_27.pony_orm.example_2.models import *
from lesson_27.pony_orm.example_2.profile_repository import ProfilesRepository
from lesson_27.pony_orm.example_2.user_repository import UsersRepository

# This step should be placed after declaring all models for mapping
base.generate_mapping(create_tables=False)


users_repository = UsersRepository()
profiles_repository = ProfilesRepository()

# repository.create_mocked_users()
# users = users_repository.get_all()
# profiles_repository.create_mocked_profiles()

# users = users_repository.get_all()

# profiles = profiles_repository.get_all()
# profiles = profiles_repository.get_all_with_first_name("John")
# profiles = users_repository.get_all_canadian_profiles_with_email("john.dow@gmail.com")
# profiles = profiles_repository.get_all_with_gender("FEMALE")


# for profile in profiles:
#     print(profile)

# will be error since with have related rows in profiles and we have not setup cascad delete
# users_repository.delete_with_email("jim.bim@gmail.com")
# profiles_repository.delete_all_with_first_name("Jim")
profiles_repository.update_one_with_id("4b66f2f6-2535-4ad5-b1c4-dd7005bd228f", {"gender": "FEMALE"})
