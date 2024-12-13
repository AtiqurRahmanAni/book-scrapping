# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# yield {
#             "url": response.url,
#             "book_name": response.css(".product_main h1::text").get(),
#             "book_image": book_image,
#             "category": category,
#             "rating": rating,
#             "book_description": book_description,
#             "upc": table_rows[0].css("td::text").get(),
#             "price": table_rows[2].css("td::text").get(),
#             "price_with_tax": table_rows[3].css("td::text").get(),
#             "tax": table_rows[4].css("td::text").get(),
#             "availability": table_rows[5].css("td::text").get(),
#             "num_reviews": table_rows[6].css("td::text").get(),
#         }


class BookItem(scrapy.Item):
    url = scrapy.Field()
    book_name = scrapy.Field()
    book_image = scrapy.Field()
    category = scrapy.Field()
    rating = scrapy.Field()
    book_description = scrapy.Field()
    upc = scrapy.Field()
    price = scrapy.Field()
    price_with_tax = scrapy.Field()
    tax = scrapy.Field()
    availability = scrapy.Field()
    available_quantity = scrapy.Field()
    num_reviews = scrapy.Field()
