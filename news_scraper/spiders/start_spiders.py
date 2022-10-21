import subprocess


def main():
    subprocess.run(["scrapy", "crawl", "hi-tech_crawl", "-o", "../../../data/hi-tech-scraped_data.csv"])
    subprocess.run(["scrapy", "runspider", "habr_news.py", "-o", "../../../data/habr-scraped_data.csv"])


if __name__ == "__main__":
    main()