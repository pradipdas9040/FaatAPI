# Body - Nested Models

from fastapi import FastAPI, Body # type: ignore
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl # for RE: https://ihateregex.io/expr/url/
    name: str

class Item(BaseModel):
    name: str
    description: str | None=None
    price: float
    tax: float | None=None
    tags: set[str]=[]
    inage: Image | None=None

class Offer(BaseModel):
    name: str
    description: str | None=None
    items: list[Item]

@app.put('/item_id/{item_id}')
async def items(
    *,
    item_id: int,
    item: Item
):
    result = {'item_id': item_id, 'item': item}
    return result

@app.post('/offer')
async def create_offer(
    offer: Offer=Body(..., embed=True) # embed=True return a dict with key 'offer'
):
    return offer

@app.post('/images')
async def multiple_images(image: list[Image]):
    return image

@app.post('/blah')
async def create_some_blahs(blah: dict[int, float]):
    return blah
