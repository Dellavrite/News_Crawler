import csv

import scrapy


class HabrNewsSpider(scrapy.Spider):
    name = 'habr_news'
    allowed_domains = ['habr.com']
    start_urls = ['https://habr.com/ru/news/page1/']

    def parse(self, response, **kwargs):
        links = response.xpath('//a[@class="tm-article-snippet__title-link"]/@href').extract()
        titles = response.xpath('//a[@class="tm-article-snippet__title-link"]/span/text()').extract()
        senders_names = list(map(str.strip, response.xpath('//a[@class="tm-user-info__username"]/text()').extract()))
        senders_links = response.xpath('//a[@class="tm-user-info__username"]/@href').extract()
        dates = response.xpath('//span[@class="tm-article-snippet__datetime-published"]/time/@title').extract()
        ids = response.xpath('//article[@class="tm-articles-list__item"]/@id').extract()

        #data = csv.reader(open("scraped_data.csv", "r"), delimiter=",")

        for item in zip(links, titles, senders_names, senders_links, dates, ids):
            scraped_data = {
                "Ссылка": item[0],
                "Заглавие": item[1],
                "Имя отправителя": item[2],
                "Ссылка на отправителя": item[3],
                "Дата": item[4],
                "id": "id=" + item[5]
            }
            next_page = response.xpath('//a[@rel="next"]/@href').extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )
            yield scraped_data
