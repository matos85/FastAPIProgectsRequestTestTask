import httpx
from config import Config

async def fetch_tariffs(currency: str = "RUB"):
    headers = {
        "X-Whatsapp-Token": Config.API_TOKEN
    }
    params = {
        "currency": currency,
        "crm": "lk"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(Config.API_URL, headers=headers, params=params)
        response.raise_for_status()  
        return response.json()
