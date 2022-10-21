import subprocess


def main():
    subprocess.Popen(["news_scraper/spiders/scrapy", "crawl", "hi-tech_crawl", "-o", "../../../data/hi-tech-scraped_data.csv"])
    subprocess.Popen(["news_scraper/spiders/scrapy", "runspider", "habr_news.py", "-o", "../../../data/habr-scraped_data.csv"])


if __name__ == "__main__":
    main()