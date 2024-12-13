from fastapi import Request
from urllib.parse import urlencode


def build_page_url(request: Request, page_no: int):
    query_params = dict(request.query_params)
    query_params["page_no"] = page_no
    return f"{request.base_url}books/?{urlencode(query_params)}"
