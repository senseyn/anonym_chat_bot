import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class BotConfig:
    token: str
    admins: list[int]


@dataclass
class SchedulerConfig:
    timezone: str = "Europe/Moscow"


@dataclass
class RedisConfig:
    redis_url: str


@dataclass
class DBConfig:
    pg_link: str


@dataclass
class Config:
    bot: BotConfig
    scheduler: SchedulerConfig
    redis: RedisConfig
    db: DBConfig


def load_config() -> Config:
    return Config(
        bot=BotConfig(
            token=os.getenv("TOKEN", ""),
            admins=[int(admin_id) for admin_id in os.getenv("ADMINS", "").split(",") if admin_id]
        ),
        scheduler=SchedulerConfig(
            timezone=os.getenv("TIMEZONE", "Europe/Moscow")
        ),
        redis=RedisConfig(
            redis_url=os.getenv("REDIS_URL", "")
        ),
        db=DBConfig(
            pg_link=os.getenv("PG_LINK", "")
        )
    )
