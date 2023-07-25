from pydantic import BaseModel


class SpotsCreate(BaseModel):
    sp_description: str
    sp_latitude: float
    sp_longitude: float


class SpotsUpdate(BaseModel):
    sp_description: str


class Spots(BaseModel):
    id: int
    sp_description: str
    sp_latitude: float
    sp_longitude: float


class RiderCreate(BaseModel):
    r_name: str
    r_experiance_rank: int
    r_body_params: dict
    r_about_me: str
    r_contact_info: str


class RiderUpdateName(BaseModel):
    r_name: str


class Rider(BaseModel):
    id: int
    r_name: str
    r_experiance_rank: int
    r_body_params: dict
    r_about_me: str
    r_contact_info: str