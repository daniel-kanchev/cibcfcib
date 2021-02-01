import scrapy
from datetime import datetime
from itemloaders.processors import TakeFirst
from cibcfcib.items import Article
from scrapy.loader import ItemLoader


class CibcSpider(scrapy.Spider):
    name = 'cibc'
    allowed_domains = ['cibcfcib.com']
    start_urls = ['https://www.cibcfcib.com/news-releases']

    def parse(self, response):
        articles = response.xpath('//section[@class="content"]//li')
        for article in articles:
            item = ItemLoader(Article())
            item.default_output_processor = TakeFirst()

            date = article.xpath('.//p[@class="title"]/text()').get()
            title = article.xpath('.//a/text()').get()
            link = article.xpath('.//a/@href').get()

            date = datetime.strptime(date, '%d %B, %Y')
            date = date.strftime('%Y/%m/%d')

            item.add_value('title', title)
            item.add_value('date', date)
            item.add_value('link', response.urljoin(link))

            yield item.load_item()
