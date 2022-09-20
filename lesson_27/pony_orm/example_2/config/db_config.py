from dataclasses import dataclass


@dataclass
class DBConfig:
    database = "test"
    port = 5432
    host = "localhost"
    password = "postgres"
    user = "postgres"
