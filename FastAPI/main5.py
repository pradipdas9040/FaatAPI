# Path parameter and numeric validation

from fastapi import FastAPI, Query, Path # type: ignore
from pydantic import BaseModel 

app = FastAPI()

@app.get('/item_validation/{item_id}')
async def read_item_val(
    item_id: int=Path(..., title='The id of the item to get', ge=9, le=100),
    q: str | None=Query(None, alias='item-query'),
    size: float=Query(..., gt=2, lt=7.75)
):
    result = {'item_id': item_id, 'size': size}
    if q:
        result.update({'query': q})
    return result

@app.get('/item/{item_id}')
async def read_item(
    *,
    item_id: str=Path(...,  regex='^@[a-zA-Z_][0-9a-zA-Z_]*'),
    q: str,
    size: float=Query(..., gt=2, lt=7.75)
):
    result = {'item_id': item_id, 'size': size}
    if q:
        result.update({'query': q})
    return result