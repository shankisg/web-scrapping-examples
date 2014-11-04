import scrapy
from mycrawler.items import MycrawlerItem
from mechanize import Browser

class MySpider(scrapy.Spider):
    """
    Spider with fixed start url
    """

    name = 'flipkart'
    allowed_domains = ['flipkart.com']
    start_urls = [
        'http://www.flipkart.com/search?q=htc&as=off&as-show=on&otracker=start'
    ]

    def parse(self, response):
        '''
        scraping the url present in start_urls list.
        '''
        
        #Get the parent div
        xdata = response.xpath(
            '//div[@class=" product-unit unit-4  browse-product  "]'
        )

        #setting the crawled data
        for d in xdata:
            item = MycrawlerItem()
            item['product_name'] = d.xpath(
                'div/div/a[@class="fk-display-block"]/@title'
            ).extract()
            item['product_url'] = d.xpath(
                'div/a[@class="pu-image fk-product-thumb "]/@href'
            ).extract()
            item['price'] = d.xpath(
                'div/div/div/div[@class = "pu-final"]/span/text()'
            ).extract()

            item['image_url'] = d.xpath(
                'div[@class="pu-visual-section"]/a[@class="pu-image fk-product-thumb "]/img/@data-src'
            ).extract()

            if item['product_url']:
                item['product_url'] = 'http://www.flipkart.com' + item['product_url'][0]
            else:
                item['product_url'] = "NULL"

            yield item


class MySpider2(scrapy.Spider):
    """
    Spider with dynamic start url
    """

    name = 'flipkart_2'
    allowed_domains = ['flipkart.com']
    start_urls = []

    def __init__(self):
        '''
        Setting start urls dynamically using mechanize
        '''

        product_list = ['micromax', 'apple']
        br = Browser()
        br.set_handle_robots( False )
        br.addheaders = [('User-agent', 'Firefox')]

        for pl in product_list:
            br.open("http://www.flipkart.com/")
            br.select_form(nr=1)
            br.form['q'] = pl
            self.resp = br.submit()
            self.start_urls.append(self.resp.geturl())

    def parse(self, response):
        '''
        scraping the url present in start_urls list.
        '''
       
        #Getting the parent div
        xdata = response.xpath(
            '//div[@class=" product-unit unit-4  browse-product  "]'
        )

        for d in xdata:
            item = MycrawlerItem()
            item['product_name'] = d.xpath(
                'div/div/a[@class="fk-display-block"]/@title'
            ).extract()
            item['product_url'] = d.xpath(
                'div/a[@class="pu-image fk-product-thumb "]/@href'
            ).extract()
            item['price'] = d.xpath(
                'div/div/div/div[@class = "pu-final"]/span/text()'
            ).extract()

            item['image_url'] = d.xpath(
                'div[@class="pu-visual-section"]/a[@class="pu-image fk-product-thumb "]/img/@data-src'
            ).extract()

            if item['product_url']:
                item['product_url'] = 'http://www.flipkart.com' + item['product_url'][0]
            else:
                item['product_url'] = "NULL"

            yield item