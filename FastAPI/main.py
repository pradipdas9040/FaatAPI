from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get('/')
async def root_base():
    return {'masage': 'hello world'}

@app.post('/')
async def post():
    return {'masage': 'hello from post root'}

@app.put('/')
async def put():
    return {'masage':'hello from put'}