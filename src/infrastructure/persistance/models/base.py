from sqlalchemy import MetaData
from sqlalchemy.orm import registry

meta = MetaData()
mapper_registry = registry(metadata=meta)