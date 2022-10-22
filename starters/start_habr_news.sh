#!/bin/bash
cd ../news_scraper/spiders
scrapy runspider habr_news.py -o ~/Project/data/hi-tech-scraped_data.csv