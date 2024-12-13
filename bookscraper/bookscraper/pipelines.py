from itemadapter import ItemAdapter
from pymongo import MongoClient
import re

rating_dict = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


class BookscraperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name in ["book_description", "book_name"]:
                value = adapter.get(field_name)
                adapter[field_name] = value.strip()
            elif field_name in ["price", "price_with_tax", "tax"]:
                value = adapter.get(field_name)
                adapter[field_name] = float(value[1:])
            elif field_name == "rating":
                value = adapter.get(field_name)
                adapter[field_name] = rating_dict[value]
            elif field_name == "num_reviews":
                value = adapter.get(field_name)
                adapter[field_name] = int(value)
            elif field_name == "category":
                value = adapter.get(field_name)
                adapter[field_name] = value.lower().replace(" ", "_")
            elif field_name == "availability":
                value = adapter.get(field_name)
                match = re.search(r"\((\d+) available\)", value)
                available_quantity = int(match.group(1)) if match else 0
                adapter["available_quantity"] = available_quantity

        return item


class SaveToMongoPipeline:

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DATABASE", "book_collection"),
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.collection = self.db["books"]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):

        data = {
            "upc": item.get("upc"),
            "url": item.get("url"),
            "book_name": item.get("book_name"),
            "book_image": item.get("book_image"),
            "category": item.get("category"),
            "rating": item.get("rating"),
            "book_description": item.get("book_description"),
            "price": item.get("price"),
            "price_with_tax": item.get("price_with_tax"),
            "tax": item.get("tax"),
            "availability": item.get("availability"),
            "available_quantity": item.get("available_quantity"),
            "num_reviews": item.get("num_reviews"),
        }

        upc = data["upc"]

        existing_book = self.collection.find_one({"upc": upc})
        if existing_book:
            updates = {}
            for field, value in data.items():
                if field in existing_book and existing_book[field] != value:
                    updates[field] = value

            if updates:
                self.collection.update_one({"upc": upc}, {"$set": updates})
                spider.logger.info(f"Updated book: {item['book_name']} ({upc})")
            else:
                spider.logger.info(
                    f"No changes detected for book: {item['book_name']} ({upc})"
                )

        else:
            self.collection.insert_one(data)
            spider.logger.info(f"Inserted new book: {item['book_name']} ({upc})")

        return item
