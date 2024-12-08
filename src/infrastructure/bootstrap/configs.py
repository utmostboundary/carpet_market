import os
from dataclasses import dataclass

from dotenv import load_dotenv

from src.infrastructure.persistence.config import DBConfig


@dataclass
class AllConfigs:
    db: DBConfig


def load_all_configs() -> AllConfigs:
    load_dotenv()

    db_config = DBConfig(
        host=os.getenv("POSTGRES_HOST"),
        db_name=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
    )

    return AllConfigs(db=db_config)