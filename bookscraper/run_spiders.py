import schedule
import time
import subprocess


def crawl_site():
    print("Starting the crawl...")
    subprocess.run(["scrapy", "crawl", "bookspider"])
    print("Crawl completed.")


schedule.every(5).minutes.do(crawl_site)

try:
    crawl_site()
    while True:
        print("Waiting for the next crawl...")
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Scheduler stopped!")
