import csv
import time

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HiTechCrawlSpider(CrawlSpider):
    name = 'hi-tech_crawl'
    allowed_domains = ['hi-news.ru']
    start_urls = ['http://hi-news.ru']
    start_page_crawl = False
    le_next = LinkExtractor(restrict_css="li > a.next")
    rule_next = Rule(le_next, callback="parse_item", follow=True)
    post_ids_text = []
    with open("~/Project/my_django_project/static/post_ids.csv", "r") as post_ids_file:
        post_ids_text.extend(list(csv.reader(post_ids_file, delimiter="~")))
    rules = (
        rule_next,
    )

    def parse_item(self, response):
        if not self.start_page_crawl:
            yield scrapy.Request(
                    response.urljoin("http://hi-news.ru/page/1"),
                    callback=self.parse_item
                )
            self.start_page_crawl = True
        titles = response.css('h2.post__title.post__title_preview > a::text').extract()
        links = response.xpath('//article/h2/a/@href').extract()
        senders_names = response.xpath('//div[@class="author"]/text()').extract()
        senders_links = "NONE"
        dates = response.xpath('//time[@class="post__date"]/@datetime').extract()
        ids = response.xpath('//div[@id="content"]//article/@id').extract()
        for item in zip(links, titles, senders_names, senders_links, dates, ids):
            if item[5] in self.post_ids_text:
                break
            scraped_data = {
                "Ссылка": item[0],
                "Заглавие": item[1],
                "Имя отправителя": item[2],
                "Ссылка на отправителя": "#",
                "Дата": item[4].split("T")[0],
                "id": item[5]
            }
            yield scraped_data
