#!/bin/bash
su - controller
cd Project/News_Crawler/news_scraper/spiders
scrapy crawl hi-tech_crawl -o ../../../data/hi-tech-scraped_data.csv