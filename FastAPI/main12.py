# Response Model

from fastapi import FastAPI, Body, Cookie, Header # type: ignore
from pydantic import BaseModel, Field, EmailStr
from typing import Literal

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None=None
    price: float
    tax: float = 10.5
    tags: set[str]=[]

item_dict = {
    'foo': {'name': 'Foo', 'price': 20},
    'bar': {'name': 'Bar', 'description': 'nice item', 'price': 60.7, 'tax': 20.3},
    'baz': {'name': 'Baz', 'description': None, 'price': 50.7, 'tax': 10.5, 'tags': []}
}

class UserBase(BaseModel):
    user_name: str
    email: EmailStr
    name: str | None=None

class UserIn(UserBase):
    pasword: str

class UserOut(UserBase):
    pass

@app.get('/item_id/{item}', response_model=Item, response_model_exclude_unset=True)
async def read_item(item: Literal['foo', 'bar', 'baz']):
    return item_dict[item]

@app.post('/item', response_model=UserIn)
async def create_user(user: UserIn):
    return user

@app.post('/user', response_model=UserOut)
async def user_read(user: UserIn):
    return user

@app.get(
        '/item_id/{item}/name',
        response_model=Item, 
        response_model_include={'name', 'description'}
)
async def item_name(item: Literal['foo', 'bar', 'baz']):
    return item_dict[item]

@app.get(
        '/item_id/{item}/public',
        response_model=Item,
        response_model_exclude={'tax'}
)
async def public_item(item: Literal['foo', 'bar', 'baz']):
    return item_dict[item]