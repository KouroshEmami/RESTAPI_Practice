from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def index() -> dict[str : str]:
    return {'hello': 'world'}

@app.get('/about')
async def about() -> str:
    return 'An exceptional Company'