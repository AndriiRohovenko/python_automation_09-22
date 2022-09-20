from uuid import UUID

from pony.orm import (
    PrimaryKey,
    Optional,
    Required,
)

from ..core import base


class Profile(base.Entity):
    _table_ = "profiles"

    id = PrimaryKey(UUID)
    first_name = Optional(str, 32)
    last_name = Optional(str, 32)
    gender = Required(str, 6)
    country_code = Required(str, 3)
    user = Optional("User")

    def __str__(self):
        return (
            f"{self.id} | "
            f"{self.first_name} | "
            f"{self.last_name} | "
            f"{self.gender} | "
            f"{self.country_code}"
        )


