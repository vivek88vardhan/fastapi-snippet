from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status

router = APIRouter()

@router.get("/")
async def getHelloWorld(name: str=None) -> str:
    return {"name": name +" hello world"}