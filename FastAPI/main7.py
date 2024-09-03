# Body - Fields
'''
The benefit of Field is in schema
'''

from fastapi import FastAPI, Body # type: ignore
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None=Field(
        None,
        max_length=300
    )
    price: float=Field(
        ...,
        gt=0,
        description='Price must be > 0'
    )
    tax: float | None=None

@app.put('/item_id/{itemid}')
async def items(
    *,
    itemid: int,
    item: Item=Body(..., embed=True)
):
    result = {'item_id': itemid, 'item': item}
    return result