from fastapi import FastAPI
from typing import Dict, Any


app = FastAPI()


Locks = {}
Meta = {}


@app.get("/")
async def root():
    return f"Meta information: {Meta}."


@app.get("/get_meta")
async def get_meta() -> Dict[str, Any]:
    return Meta


@app.post("/set_meta")
async def set_meta(meta_info: Dict[str, Any]) -> Dict[str, Any]:
    Meta.update(meta_info)
    return Meta
