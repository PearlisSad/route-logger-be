from fastapi import Body, status, APIRouter

from ..models.wall_model import WallModel, WallCollection
from ..clients import mongo_client

router = APIRouter(prefix='/api/walls', tags=['walls'], responses={404: {"description": "Not found"}})
collection = mongo_client.client.route_logger.get_collection('walls')

@router.post(
    "/",
    response_description="Add new wall",
    response_model=WallModel,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def create(wall: WallModel = Body(...)):
    new_object = wall.model_dump(by_alias=True, exclude=["id"])
    result = await collection.insert_one(new_object)
    new_object["_id"] = result.inserted_id
    return new_object


@router.get(
    "/",
    response_description="List all walls",
    response_model=WallCollection,
    response_model_by_alias=False,
)
async def list():
    return WallCollection(walls=await collection.find().to_list(1000))

