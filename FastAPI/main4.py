# Query parameter and string validation

from fastapi import FastAPI, Query # type: ignore
from pydantic import BaseModel 

app = FastAPI()

@app.get('/item')
async def read_item(q: str | None = Query(None, min_length=3, max_length=10, regex='^[a-zA-Z_][0-9a-zA-Z_]*')):
    result = {'items': [{'item_id': 11}, {'item_id': 23}]}
    if q:
        result.update({'q': q})
    return result

@app.get('/items')
async def list_item(
    q: list[str] = Query(
        ['foo', 'bar'],
        title='Sample query string',
        description='This is sample query string',
        deprecated=True,
        alias='item-query'
        )
):
    result = {'items': [{'item_id': 11}, {'item_id': 23}]}
    if q:
        result.update({'q': q})
    return result

@app.get('/item_hidden')
async def hidden_quary_route(
    hidden_query: str | None=Query(None, include_in_schema=False)
):
    if hidden_query:
        return({'hidden_query': hidden_query}) # For port=8000, http://127.0.0.1:8000/item_hidden?hidden_query=xyz -- will show {"hidden_query":"xyz"}
    return({'hidden_query': 'hidden query not define'})
