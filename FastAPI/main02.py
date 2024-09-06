# Query Parameter

from typing import Optional
from fastapi import FastAPI # type: ignore

app = FastAPI()

fake_item_db = [{'item_name': 'Foo'}, {'item_name': 'Bsr'}, {'item_name': 'Baz'}]

@app.get('/items')
async def list_item(skip: int=0, limit: int=10):
    return fake_item_db[skip : skip+limit]

@app.get('/items/{item_id}')
async def get_items(item_id: int, q: str|None=None):
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}

# for port=5000: return value - http://127.0.0.1:5000/user_id/33?q=44&short=1
@app.get('/user_id/{user_id}')
async def get_user(user_id: int, q: str|None=None, short: bool=False):
    user = {'user_id': user_id}
    if q:
        user.update({'q': q})
    if not short:
        user.update({'description': 'I am user'})
    return user

# for port=5000: return value - http://127.0.0.1:5000/user_id/33/item/hello?q=44&short=on
@app.get('/user_id/{user_id}/item/{item_id}')
async def get_user_item(user_id: int, item_id:str, q: Optional[str]=None, short: bool=True):
    user = {'user_id': user_id, 'item_id': item_id}
    if q:
        user.update({'q': q})
    if short:
        user.update({'description': 'I am user'})
    return user
