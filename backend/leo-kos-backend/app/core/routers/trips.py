from fastapi import APIRouter, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List

from app.core.routers.database_client import db
from app.core.models.database import TripModel


router = APIRouter()

@router.get('/',response_description='List all trips', response_model= 
    List[TripModel])
async def read_trips():
    trips = await db['trips'].find().to_list(1000)
    return trips

@router.post('/', response_description='Add new trip', response_model=TripModel)
async def create_trip(trip: TripModel = Body(...)):
    trip = jsonable_encoder(trip)
    new_trip = await db['trips_trip'].insert_one(trip)
    created_trip = await db['trips_trip'].find_one({"_id": new_trip.inserted_id})
    return JSONResponse(status_code = status.HTTP_201_CREATED, content=created_trip)