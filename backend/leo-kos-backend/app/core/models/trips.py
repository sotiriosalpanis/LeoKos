from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional, List

from core.models.database import PyObjectID

# Trip Models
class Stop(BaseModel):
    stop_name: str

class TripModel(BaseModel):
    id: PyObjectID = Field(default_factory=PyObjectID, alias="_id")
    trip_name: str = Field(...)
    description: str = Field(...)
    stops: List[Stop] = []

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example" : {
                "trip_name" : "Wolves",
                "description" : "Bostin' aye it!?",
                "stops": [
                    {"stop_name":"Perton"}
                ]
            }
        }

class UpdateTripModel(BaseModel):
    trip_name: Optional[str]
    description: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example" : {
                "trip_name" : "Telford",
                "description" : "Shite, ar it!?",
            }
        }