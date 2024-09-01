# Request Body

from fastapi import FastAPI # type: ignore
from pydantic import BaseModel 

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post('/item')
async def creat_item(item: Item):
    return item

@app.post('/items')
async def creat_item_list(item: Item):
    item = item.dict()
    if item['tax']:
        price_with_tax = item['price'] + item['tax']
        item.update({'price_with_tax': price_with_tax})
    return item

@app.put('/item/{item_id}')
async def creat_item_with_put(item_id: int, item: Item, q: str | None=None):
    result = {'item_id': item_id, **item.dict()}
    if q:
        result.update({'q': q})
    return result