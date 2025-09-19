from fastapi import Body, status, APIRouter

from ..models.route_model import RouteModel, RouteCollection
from ..clients import mongo_client

router = APIRouter(prefix='/api/routes', tags=['routes'], responses={404: {"description": "Not found"}})
collection = mongo_client.client.route_logger.get_collection('routes')

@router.post(
    "/",
    response_description="Add new route",
    response_model=RouteModel,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def create(student: RouteModel = Body(...)):
    new_object = student.model_dump(by_alias=True, exclude=["id"])
    result = await collection.insert_one(new_object)
    new_object["_id"] = result.inserted_id
    return new_object


@router.get(
    "/",
    response_description="List all routes",
    response_model=RouteCollection,
    response_model_by_alias=False,
)
async def list():
    return RouteCollection(routes=await collection.find().to_list(1000))

