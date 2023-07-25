import sqlalchemy
from sqlalchemy import Integer,Float,ForeignKey,Text, JSON, String
from .database import metadata

spots = sqlalchemy.Table(
    "spots",
    metadata,
    sqlalchemy.Column("id", Integer, primary_key=True),
    sqlalchemy.Column("sp_latitude", Float),
    sqlalchemy.Column("sp_longitude", Float),
    sqlalchemy.Column("sp_description", Text),
)

forecasts = sqlalchemy.Table(
    "forecasts",
    metadata,
    sqlalchemy.Column("id", Integer, primary_key=True),
    sqlalchemy.Column("spot_id", Integer, ForeignKey("spots.id"), nullable=False),
    sqlalchemy.Column("fc_data", JSON),
    sqlalchemy.Column("fc_source_id", Integer, ForeignKey("forecast_sources.id"), nullable=False),
)

forecast_sources = sqlalchemy.Table(
    "forecast_sources",
    metadata,
    sqlalchemy.Column("id", Integer, primary_key=True),
    sqlalchemy.Column("fs_name", String),
    sqlalchemy.Column("fs_description", Text),
)

sensors = sqlalchemy.Table(
    "sensors",
    metadata,
    sqlalchemy.Column("id", Integer, primary_key=True),
    sqlalchemy.Column("spot_id", Integer,ForeignKey("spots.id"), nullable=False),
    sqlalchemy.Column("s_type_id", Integer,ForeignKey("sensor_types.id"), nullable=False),
    sqlalchemy.Column("s_latitude", Float),
    sqlalchemy.Column("s_longitude", Float),
    sqlalchemy.Column("s_data", JSON),
)

sensor_types = sqlalchemy.Table(
    "sensor_types",
    metadata,
    sqlalchemy.Column("id", Integer, primary_key=True),
    sqlalchemy.Column("st_name", Text),
    sqlalchemy.Column("st_name", Text),
)

rider_sessions = sqlalchemy.Table(
    "rider_sessions",
    metadata,
    sqlalchemy.Column("id", Integer, primary_key=True),
    sqlalchemy.Column("rider_id", Integer, ForeignKey("riders.id"), nullable=False),
    sqlalchemy.Column("spot_id", Integer, ForeignKey("spots.id"), nullable=False),
    sqlalchemy.Column("rs_duration", Integer),
    sqlalchemy.Column("rs_equipment_cfg",  Integer, ForeignKey("equipment_configs.id"), nullable=False),
)


riders = sqlalchemy.Table(
    "riders",
    metadata,
    sqlalchemy.Column("id", Integer, primary_key=True),
    sqlalchemy.Column("r_name", Text),
    sqlalchemy.Column("r_experiance_rank", Integer),
    sqlalchemy.Column("r_specialization", String),
    sqlalchemy.Column("r_body_params", JSON),
    sqlalchemy.Column("r_about_me", Text),
    sqlalchemy.Column("r_contact_info", Text),

)

equipment = sqlalchemy.Table(
    "equipment",
    metadata,
    sqlalchemy.Column("id", Integer, primary_key=True),
    sqlalchemy.Column("e_name", Text),
    sqlalchemy.Column("e_params", JSON),
)


equipment_configs = sqlalchemy.Table(
    "equipment_configs",
    metadata,
    sqlalchemy.Column("id", Integer, primary_key=True),
    sqlalchemy.Column("equipment_id",  Integer, ForeignKey("equipment.id"), nullable=False),

)