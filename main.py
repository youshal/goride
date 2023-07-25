
from fastapi import FastAPI
from db.database import database
from db import crud
from db.schemas import Rider, RiderCreate

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/riders/" , response_model=Rider)
async def get_riders() :
    riders=crud.get_riders()
    return riders


@app.post("/create_rider/", response_model=RiderCreate)
async def create_rider(rider: RiderCreate):
    rider_id=crud.create_rider(rider)
    return {**rider.model_dump(), "id": rider_id}


@app.post("/push_forecast/")
async def forecasted_weather():
    return {"message": "forecast saved"}