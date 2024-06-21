import scrapy


class HouseItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    pictures = scrapy.Field()
    rent_price = scrapy.Field()
    description = scrapy.Field()
    email = scrapy.Field()
    phone_number = scrapy.Field()

    country = scrapy.Field()
    domain = scrapy.Field()
