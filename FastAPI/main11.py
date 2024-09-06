# Cookie and Header Parameters

from fastapi import FastAPI, Body, Cookie, Header # type: ignore
from pydantic import BaseModel, Field

app = FastAPI()

@app.get('/item/{item_id}')
async def read_item(
    cookie_id: str | None=Cookie(None),
    accept_encoding: str | None=Header(None),
    sec_ch_ua: str | None=Header(None),
    user_agent: str | None=Header(None),
    x_list: list[str] | None=Header(None)
):
    return {
        'Cookie id': cookie_id,
        'Accept encoding': accept_encoding,
        'sec_ch_ua': sec_ch_ua,
        'User agent': user_agent,
        'x-list token': x_list
    }