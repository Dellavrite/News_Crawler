#!/bin/bash
su - controller
cd Project/News_Crawler/news_scraper/spiders
scrapy runspider habr_news.py -o ../../../data/habr-scraped_data.csv