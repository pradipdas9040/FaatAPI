from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get('/')
async def root_base():
    return {'massage': 'hello world'}

@app.post('/')
async def post():
    return {'massage': 'hello from post route'}

@app.put('/')
async def put():
    return {'massage':'hello from put route'}
