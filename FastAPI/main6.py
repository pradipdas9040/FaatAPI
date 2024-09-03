# Body - Multiple Parameter

from fastapi import FastAPI, Body, Path # type: ignore
from pydantic import BaseModel 

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    user_name: str
    user_id: int

@app.put('/item/{item_id}')
async def update_item(
    *,
    item_id: int=Path(..., ge=0, le=150),
    q:str | None=None,
    item: Item | None=None,
    user: User,
    importance: int=Body(...)
):
    result = {'item_id': item_id}
    if q:
        result.update({'q': q})
    if item:
        result.update({'item': item})
    if user:
        result.update({'user': user})
    if importance:
        result.update({'importance': importance})
    return result

@app.put('/item_id/{itemid}')
async def items(
    *,
    itemid: int=Path(..., ge=0, le=150),
    q:str | None=None,
    item: Item=Body(None, embed=True)
):
    result1 = {'item_id': itemid}
    if q:
        result1.update({'q': q})
    if item:
        result1.update({'item': item})
    return result1