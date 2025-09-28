from fastapi import status, APIRouter, responses

router = APIRouter(
    prefix="/api/health", tags=["health"], responses={404: {"description": "Not found"}}
)


@router.get(
    "/",
    response_description="Health check",
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def get_health():
    return responses.Response(status_code=status.HTTP_200_OK)
