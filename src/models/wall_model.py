from typing import Optional, List
from typing_extensions import Annotated
from pydantic import ConfigDict, BaseModel, Field
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]

class WallModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(...)
    open: bool = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "name": "Cave",
                "open": False,
            }
        },
    )
    
class WallModel(BaseModel):
    id: PyObjectId = Field(..., alias='_id')
    name: Optional[str] = None
    open: bool = False
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "name": "Cave",
                "open": False,
            }
        },
    )


class WallCollection(BaseModel):
    walls: List[WallModel]