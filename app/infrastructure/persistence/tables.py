from sqlalchemy import (
    Table,
    Column,
    UUID,
    String,
    Numeric,
    Integer,
    MetaData,
    Boolean,
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import ARRAY

metadata = MetaData()


carpet_table = Table(
    "carpets",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("title", String),
    Column("description", String, nullable=True),
    Column("width", Integer),
    Column("height", Integer),
    Column("base_price", Numeric(10, 2)),
    Column("retail_price", Numeric(10, 2)),
    Column("stock_amount", Integer),
    Column("main_image_path", String),
    Column("image_paths", ARRAY(String)),
    Column("pattern_id", ForeignKey("patterns.id")),
)


user_table = Table(
    "users",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("hashed_password", String, nullable=True),
    Column("tg_id", String, nullable=True),
    Column("tg_username", String, nullable=True),
    Column("role", String),
    Column("phone_number", String, nullable=True),
    Column("is_active", Boolean),
)


pattern_table = Table(
    "patterns",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("title", String),
    Column("description", String),
    Column("color", String),
    Column("pile_structure", String),
    Column("region", String),
)
