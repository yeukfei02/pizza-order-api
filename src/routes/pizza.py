from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
from datetime import datetime
from src.db.db import session
from src.model.Pizza import Pizza

router = APIRouter()


@router.post("/pizza")
async def create_pizza(request: Request):
    request_body = await request.json()

    response = None

    if request_body:
        name = request_body['name']
        type = request_body['type']
        price = request_body['price']
        quantity = request_body['quantity']
        created_by = datetime.now()
        updated_by = datetime.now()

        pizza = Pizza(name=name, type=type, price=price,
                      quantity=quantity, created_by=created_by, updated_by=updated_by)
        session.add(pizza)
        session.commit()

        data = {
            "message": "createPizza",
        }
        response = JSONResponse(
            status_code=status.HTTP_201_CREATED, content=data)

    return response


@router.get("/pizza")
async def get_pizzas():
    pizza_list = session.query(Pizza).all()

    data = {}
    formatted_pizza_list = []

    if pizza_list:
        for pizza in pizza_list:
            pizza_obj = {
                'pizza_id': pizza.pizza_id,
                'name': pizza.name,
                'type': pizza.type,
                'price': pizza.price,
                'quantity': pizza.quantity,
                'created_by': str(pizza.created_by),
                'updated_by': str(pizza.updated_by),
            }
            formatted_pizza_list.append(pizza_obj)

    data = {
        "message": "getPizzas",
        "pizzas": formatted_pizza_list
    }

    return JSONResponse(status_code=status.HTTP_200_OK, content=data)


@router.get("/pizza/{id}")
async def get_pizza_by_id(id):
    print("id = {0}".format(id))

    response = None

    if id:
        pizza = session.query(Pizza).get(id)

        pizza_obj = {}

        if pizza:
            pizza_obj = {
                'pizza_id': pizza.pizza_id,
                'name': pizza.name,
                'type': pizza.type,
                'price': pizza.price,
                'quantity': pizza.quantity,
                'created_by': str(pizza.created_by),
                'updated_by': str(pizza.updated_by),
            }

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


@router.put("/pizza/{id}")
async def update_pizza_by_id(request: Request, id):
    print("id = {0}".format(id))

    response = None

    if id:
        pizza = session.query(Pizza).get(id)
        if pizza:
            request_body = await request.json()
            if request_body:
                pizza.name = request_body['name']
                pizza.type = request_body['type']
                pizza.price = request_body['price']
                pizza.quantity = request_body['quantity']
                pizza.updated_by = datetime.now()
                session.commit()

                data = {
                    "message": "updatePizzaById",
                }
                response = JSONResponse(
                    status_code=status.HTTP_200_OK, content=data)
        else:
            data = {
                "message": "updatePizzaById, no this id",
            }
            response = JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST, content=data)
    else:
        data = {
            "message": "updatePizzaById error, there is no id",
        }
        response = JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content=data)

    return response


@router.delete("/pizza/{id}")
async def delete_pizza_by_id(id):
    print("id = {0}".format(id))

    response = None

    if id:
        pizza = session.query(Pizza).get(id)
        if pizza:
            session.delete(pizza)
            session.commit()

            data = {
                "message": "deletePizzaById",
            }
            response = JSONResponse(
                status_code=status.HTTP_200_OK, content=data)
        else:
            data = {
                "message": "deletePizzaById, no this id",
            }
            response = JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST, content=data)
    else:
        data = {
            "message": "deletePizzaById error, there is no id",
        }
        response = JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content=data)

    return response
