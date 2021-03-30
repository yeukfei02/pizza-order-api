from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
import uuid

router = APIRouter()

pizza_list = []


@router.post("/pizza")
async def create_pizza(request: Request):
    request_body = await request.json()

    response = None

    if request_body:
        name = request_body['name']
        type = request_body['type']
        price = request_body['price']

        obj = {
            'id': str(uuid.uuid4()),
            'name': name,
            'type': type,
            'price': price
        }
        pizza_list.append(obj)

        data = {
            "message": "createPizza",
        }
        response = JSONResponse(
            status_code=status.HTTP_201_CREATED, content=data)

    return response


@router.get("/pizza")
async def get_pizzas():
    data = {
        "message": "getPizzas",
        "pizzas": pizza_list
    }
    return JSONResponse(status_code=status.HTTP_200_OK, content=data)


@router.get("/pizza/{id}")
async def get_pizza_by_id(id):
    print("id = {0}".format(id))

    response = None

    if id:
        if pizza_list:
            pizza_obj = {}
            for pizza in pizza_list:
                if pizza['id'] == id:
                    pizza_obj = pizza

            data = {
                "message": "getPizzaById",
                "pizza": pizza_obj
            }
            response = JSONResponse(
                status_code=status.HTTP_200_OK, content=data)
    else:
        data = {
            "message": "getPizzaById error, there is no id",
        }
        response = JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content=data)

    return response
