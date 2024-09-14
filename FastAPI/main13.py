# Extra Model

from fastapi import FastAPI, Body, Cookie, Header # type: ignore
from pydantic import BaseModel, Field, EmailStr
from typing import Union, Literal

app = FastAPI()

class UserBase(BaseModel):
    user_name: str
    email: EmailStr
    name: str | None=None

class UserIn(UserBase):
    pasword: str

class UserOut(UserBase):
    pass

class UserInDB(UserBase):
    hashed_pasword: str

def fake_pasword_hasher(raw_pasword: str):
    return f'supersecret{raw_pasword}'

def fake_save_user(user_in: UserIn):
    hashed_pasword = fake_pasword_hasher(user_in.pasword)
    user_indb = UserInDB(**user_in.dict(), hashed_pasword=hashed_pasword)
    print("user 'saved'.")
    return user_indb

@app.post('/user', response_model=UserOut)
async def create_user(user_in: UserIn):
    user_save = fake_save_user(user_in)
    return user_save

class BaseItem(BaseModel):
    description: str
    type: str

class CarItem(BaseItem):
    type: str='car'

class PlaneItem(BaseItem):
    type: str='plane'
    size: int

item = {
    'item1': {
        'description': 'A nice car',
        'type': 'car'
    },
    'item2': {
        'description': 'A big plane',
        'type': 'plane',
        'size': 5
    }
}

@app.get('/item/{item_id}', response_model=Union[PlaneItem, CarItem])
async def return_item(item_id: Literal['item1', 'item2']):
    return item[item_id]

@app.get('/arbitrary', response_model=dict[str, float])
async def arbitrary_item():
    return {'a': 1, 'b': '2'}