from .models import *
from .schemas import *
from .database import database

def get_rider(rider_id: int):
    return riders.query(Rider).filter(Rider.id == rider_id).first()


def get_rider_by_name(name: str):
    return riders.query(Rider).filter(Rider.r_name == name).first()


def get_riders(skip: int = 0, limit: int = 100):
    return riders.query(Rider).offset(skip).limit(limit).all()


async def create_rider(rider: RiderCreate):
    query = riders.insert().values(r_name=rider.r_name,
                                   r_experiance_rank=rider.r_experiance_rank,
                                   r_body_params=rider.r_body_params)
    last_record_id = await database.execute(query)
    return last_record_id
