from typing import Optional, List, Union
from pydantic import BaseModel, Field
from bson import ObjectId

# File for the database models

# converts ObjectIds to strings before storing them as `_id`
class PyObjectID(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)
    
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

# User Models
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(Token):
    username: Union[str, None] = None

class User(BaseModel):
    username: str
    email: Union[str, None] = None

class UserInDB(User):
    hashed_password: str

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