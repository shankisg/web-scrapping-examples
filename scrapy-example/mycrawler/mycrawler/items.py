from scrapy.item import Item, Field


class MycrawlerItem(Item):
    product_name = Field()
    product_url  = Field()
    price = Field()
    image_url = Field()
