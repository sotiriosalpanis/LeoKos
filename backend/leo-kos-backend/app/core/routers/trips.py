from fastapi import APIRouter, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List

from core.routers.database_client import db
from core.models.database import TripModel


router = APIRouter()

@router.get('',response_description='List all trips', response_model= 
    List[TripModel])
async def read_trips():
    trips = await db['trips'].find().to_list(1000)
    return trips

@router.get('/{id}', response_description='Get a single trip', response_model=TripModel)
async def show_trip(id: str):
    if (trip := await db['trips'].find_one({"_id": id})) is not None:
        return trip
    
    raise HTTPException(status_code=404, detail=f'Trip {id} not found')

@router.post('/', response_description='Add new trip', response_model=TripModel)
async def create_trip(trip: TripModel = Body(...)):
    trip = jsonable_encoder(trip)
    new_trip = await db['trips'].insert_one(trip)
    created_trip = await db['trips'].find_one({"_id": new_trip.inserted_id})
    return JSONResponse(status_code = status.HTTP_201_CREATED, content=created_trip)