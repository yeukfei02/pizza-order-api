from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/")
async def main():
    data = {
        "message": "pizza-order-api"
    }
    return JSONResponse(status_code=status.HTTP_200_OK, content=data)
