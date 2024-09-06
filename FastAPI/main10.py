# Ref: https://docs.pydantic.dev/1.10/usage/types/

## How to get a UUID?
'''
>>> from uuid import uuid4
>>> uuid4()
UUID('fa397058-b95c-4432-8498-479113f40bb9')
'''

from datetime import datetime, time, timedelta
from uuid import UUID
from fastapi import FastAPI, Body # type: ignore
from pydantic import BaseModel, Field

app = FastAPI()

@app.put('/item/{item_id}')
async def read_item(
    item_id: UUID,
    start_date: datetime | None=Body(None),
    end_date: datetime | None=Body(None),
    repeate_at: time | None=Body(None),
    process: timedelta | None=Body(None)
):
    start_process = start_date + process
    duration = end_date - start_process
    return {
        'item_id': item_id,
        'start_date': start_date,
        'end_date': end_date,
        'process': process,
        'repeate_at': repeate_at,
        'start_process': start_process,
        'duration': duration
    }