import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ..items import HouseItem


class AllHouses(CrawlSpider):
    name = 'kelm_immobilien'
    start_urls = ['https://kelm-immobilien.de/immobilien/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="property-details col-sm-12 vertical"]/h3/a'),
             callback='parse_items', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="paginator row"]'))
    )

    def parse_items(self, response):
        house_item = HouseItem()
        house_item['url'] = response.urljoin(response.css('a::attr(href)').get())
        house_item['title'] = response.css('h1.property-title::text').get()
        house_item['pictures'] = response.css('img::attr(src)').getall()
        house_item['rent_price'] = response.css('li.list-group-item.data-kaufpreis>div>div.dd.col-sm-7::text').get().split()[0]
        house_item['description'] = response.css('p::text').get()
        house_item['email'] = response.css('div.dd.col-sm-7.u-email.value > a::text').get()
        house_item['phone_number'] = response.css('div.dd.col-sm-7.p-tel.value>a::text').get()

        house_item['country'] = response.css('h2.property-subtitle::text').get().split()[1]
        house_item['domain'] = response.url.split('//')[-1].split('/')[0]
        yield house_item

