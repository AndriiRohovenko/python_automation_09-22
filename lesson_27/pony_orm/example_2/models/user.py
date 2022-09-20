from uuid import UUID

from pony.orm import PrimaryKey, Required, Set

from ..core import base


class User(base.Entity):
    _table_ = "users"

    id = PrimaryKey(UUID)
    email = Required(str, 128, unique=True)
    profiles = Set("Profile")

    def __str__(self):
        return f"{self.id} | {self.email}"
