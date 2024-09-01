# path paraneter

from enum import Enum

from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get('/', description='This our first route', deprecated=True)
async def root_base():
    return {'massage': 'hello world'}

@app.get('/items')
async def list_items():
    return {'massage': 'list items route'}

@app.get('/items/{item_id}')
async def get_id(item_id: str):
    return {'item_id': item_id}

@app.get('/item/{item_id}')
async def get_int_id(item_id: int):
    return {'item_id': item_id}

@app.get('/user/me')
async def get_current_user():
    return {'massage': 'this is current user'}

class FoodEnum(str, Enum):
    fruits = 'fruits'
    vegetables = 'vegetables'
    dairy = 'dairy'

@app.get('/food/{food_name}')
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {'food_name': food_name, 'massage': 'you are healthy'}
    if food_name.value == 'fruits':
        return {'food_name': food_name, 'massage': 'you are still healthy'}
    return {'food_name': food_name, 'massage': 'i like chocolate milk'}