# Body - Declare request example data
# Ref-> https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter

from fastapi import FastAPI, Body # type: ignore
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str=Field(..., example="fastapi")
    description: str | None=Field(None, example='A very nice item')
    price: float=Field(..., example=16.4)
    tax: float | None=Field(None, example=2.3)

@app.put('/item_id/{item_id}')
async def items(
    item_id: int,
    item: Item
):
    result = {'item_id': item_id, 'item': item}
    return result

@app.put('/item_id1/{item_id1}')
async def items(
    item_id1: int,
    item: Item=Body(
        ...,
        openapi_examples={
            'normal': {
                'summary': 'A normal example',
                'description': 'A __normal__ item works _correctly_',
                'value': {
                    'name': 'fastapi1',
                    'description': 'A very nice item',
                    'price': 16.25,
                    'tax': 2.4
                }
            },
            'converted': {
                'summary': 'A example with converted data',
                'description': 'FastAPI can convert price `strings` to actual `numbers` automatically',
                'value':{
                    'name': 'fastapi',
                    'price': '16.25'
                }
            },
            'invalid': {
                'summary': 'Invalid data rejected with an error',
                'description': 'Invalid',
                'value': {
                    'name': 'fastapi',
                    'price': 'sixteen point two five'
                }
            }
        }
    )
):
    result = {'item_id': item_id1, 'item': item}
    return result