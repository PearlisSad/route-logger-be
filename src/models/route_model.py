from typing import Optional, List
from typing_extensions import Annotated
from pydantic import ConfigDict, BaseModel, Field
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated
from datetime import datetime
from bson import ObjectId

# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]

class RouteModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    colour: str = Field(...)
    grade: str = Field(...)
    date_set: Optional[datetime] = Field(...)
    date_strip: Optional[datetime] = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "colour": "Green",
                "grade": "f7a",
                "date_set": "1970-01-30 00:00:00",
                "date_strip": "1970-01-30 00:00:00",
            }
        },
    )

class UpdateRouteModel(BaseModel):
    colour: Optional[str] = None
    grade: Optional[str] = None
    date_set: Optional[datetime] = datetime.now()
    date_strip: Optional[datetime] = None
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra={
            "example": {
                "colour": "Green",
                "grade": "f7a",
                "date_set": "2025-08-26 01:41:35.596570",
                "date_strip": "1970-01-30 00:00:00",
            }
        },
    )

class RouteCollection(BaseModel):
    routes: List[RouteModel]