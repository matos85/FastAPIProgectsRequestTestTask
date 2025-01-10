from fastapi import APIRouter, HTTPException
from typing import Any
from services import fetch_tariffs

router = APIRouter()

@router.get("/tariffs", response_model=Any)
async def get_tariffs(currency: str = "RUB"):
    try:
        tariffs = await fetch_tariffs(currency)
        return tariffs
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
