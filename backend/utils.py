from fastapi import Request, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from urllib.parse import urlencode
from dotenv import load_dotenv

import os

load_dotenv()

API_KEY = os.environ.get("API_KEY")
api_key_header = APIKeyHeader(name="API-Key", auto_error=True)


def build_page_url(request: Request, page_no: int):
    query_params = dict(request.query_params)
    query_params["page_no"] = page_no
    return f"{request.base_url}books/?{urlencode(query_params)}"


async def get_api_key(api_key_header: str = Security(api_key_header)):

    if api_key_header == API_KEY:
        return api_key_header
    raise HTTPException(status_code=403, detail="Could not validate API key")
