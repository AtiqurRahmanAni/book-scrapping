from pymongo import MongoClient
from fastapi import FastAPI, Query, Request, HTTPException, Depends
from dotenv import load_dotenv
import os
from utils import *

load_dotenv()

client = MongoClient(os.environ.get("MONGO_URI"))
dbname = client[os.environ.get("MONGO_DATABASE")]
collection = dbname["books"]

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "API is working"}


@app.get("/books/")
async def get_books(
    request: Request,
    category: str = Query(None, description="Filter by category"),
    price_min: float = Query(None, description="Minimum price"),
    price_max: float = Query(None, description="Maximum price"),
    sort_by: str = Query("rating", description="Sort by field (e.g., 'rating')"),
    order: str = Query("desc", description="Sort order ('asc' or 'desc')"),
    page_no: int = Query(1, description="Page no"),
    page_size: int = Query(20, description="Number of books in one page"),
    api_key: str = Depends(get_api_key),
):
    query = {}
    if category:
        query["category"] = category
    if price_min is not None and price_max is not None:
        query["price"] = {"$gte": price_min, "$lte": price_max}

    sort_order = -1 if order == "desc" else 1

    books = (
        collection.find(query, {"_id": False})
        .sort(sort_by, sort_order)
        .skip((page_no - 1) * page_size)
        .limit(page_size)
    )
    serialized_books = [book for book in books]

    total_items = collection.count_documents(query)
    total_pages = (total_items + page_size - 1) // page_size

    next_page_url = (
        build_page_url(request, page_no + 1) if page_no < total_pages else None
    )
    prev_page_url = build_page_url(request, page_no - 1) if page_no > 1 else None

    return {
        "books": serialized_books,
        "pagination": {
            "total_items": total_items,
            "total_pages": total_pages,
            "current_page": page_no,
            "next_page": next_page_url,
            "prev_page": prev_page_url,
        },
    }


@app.get("/books/{book_id}")
async def get_book_by_id(
    book_id: str,
    api_key: str = Depends(get_api_key),
):
    book = collection.find_one({"upc": book_id}, {"_id": False})
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return dict(book)
