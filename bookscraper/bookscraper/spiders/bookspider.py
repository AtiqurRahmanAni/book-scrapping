import scrapy
from html import unescape
from bookscraper.items import BookItem

base_url = "https://books.toscrape.com"


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = [base_url]

    def parse(self, response):
        book_categories = response.xpath(
            '//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a'
        )
        for category in book_categories:
            href = category.xpath("@href").get()
            category_name = category.xpath("text()").get().strip()
            url = f"{base_url}/{href}"

            yield response.follow(
                url, callback=self.parse_category, meta={"category": category_name}
            )

    def parse_category(self, response):
        category = response.meta["category"]

        yield from self.parse_books(response, category)

        next_page_url = response.css("li.next a::attr(href)").get()
        if next_page_url is not None:
            next_page_url = response.urljoin(next_page_url)
            yield response.follow(
                next_page_url, callback=self.parse_category, meta={"category": category}
            )

    def parse_books(self, response, category):
        books = response.css("article.product_pod")
        for book in books:
            book_details_url = book.css("h3 a::attr(href)").get()
            book_details_url = response.urljoin(book_details_url)
            yield response.follow(
                book_details_url,
                callback=self.parse_book_details,
                meta={"category": category},
            )

    def parse_book_details(self, response):
        category = response.meta["category"]

        book_image = response.xpath(
            '//*[@id="product_gallery"]/div/div/div/img/@src'
        ).get()

        book_image = response.urljoin(book_image)

        book_description = response.xpath(
            '//*[@id="content_inner"]/article/p/text()'
        ).get()
        book_description = unescape(book_description)

        rating_class = response.css("p.star-rating::attr(class)").get()
        rating = rating_class.split()[-1]

        table_rows = response.css("table tr")
        book_item = BookItem()

        book_item["url"] = response.url
        book_item["book_name"] = response.css(".product_main h1::text").get()
        book_item["book_image"] = book_image
        book_item["category"] = category
        book_item["rating"] = rating
        book_item["book_description"] = book_description
        book_item["upc"] = table_rows[0].css("td::text").get()
        book_item["price"] = table_rows[2].css("td::text").get()
        book_item["price_with_tax"] = table_rows[3].css("td::text").get()
        book_item["tax"] = table_rows[4].css("td::text").get()
        book_item["availability"] = table_rows[5].css("td::text").get()
        book_item["num_reviews"] = table_rows[6].css("td::text").get()

        yield book_item
