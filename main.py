from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
import json


app = FastAPI()
class Item(BaseModel):
    url: str
app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    url = item.url
    subprocess.run(['python3', 'detect.py','--source', item.url])
    with open('final_result.json') as f:
        data = json.load(f)

    return data

