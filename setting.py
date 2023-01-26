from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    admin_id: int


@dataclass
class Settings:
    bots: Bots


def get_settings(path: str):
    evn = Env()
    evn.read_env(path)

    return Settings(
        bots=Bots(bot_token=evn.str("TOKEN"),
                  admin_id=evn.int("ADMIN_ID"))
    )


settings = get_settings("input")
print(settings)
