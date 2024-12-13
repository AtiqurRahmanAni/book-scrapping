import schedule
import time
from scrapy.crawler import CrawlerProcess
from bookscraper.spiders.bookspider import BookspiderSpider


def run_spider():
    print("Start Scrapping")
    process = CrawlerProcess(
        {"USER_AGENT": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"}
    )
    process.crawl(BookspiderSpider)
    process.start()


schedule.every(2).minutes.do(run_spider)

try:
    while True:
        print("Here")
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Scheduler stopped!")
