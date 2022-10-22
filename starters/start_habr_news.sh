#!/bin/bash
cd ../news_scraper/spiders
scrapy runspider habr_news.py -o ~/Project/data/habr_news-scraped_data.csv