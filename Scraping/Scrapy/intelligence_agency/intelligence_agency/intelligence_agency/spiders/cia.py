import scrapy

## links: //a[starts-with(@href,"collection") and (parent::h3 | parent::h2)]/@href
## title: //h1[@class="documentFirstHeading"]/text()  
## body: //div[@class="field-item even"]//p[not(@class)]/text()'

class SpyderCIA(scrapy.Spider):
    name = 'cia'
    start_urls = [
        'https://www.cia.gov/readingroom/historical-collections'
    ]

    custom_settings = {
        'FEED_URI': 'cia.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        links_desclassified = response.xpath('//a[starts-with(@href,"collection") and (parent::h3|parent::h2)]/@href').getall()#extract()
        for link in links_desclassified:
            ## execution in zyte (scrapingHub)
            #yield response.follow(link, callback=self.parse_link_zyte, meta={'url':response.urljoin(link)})
            ## Para ejecución en local
            yield response.follow(link, callback=self.parse_link, cb_kwargs={'url': response.urljoin(link)})

    # For local execution
    def parse_link(self, response, **kwargs):
        link = kwargs['url']
        title = response.xpath('//h1[@class="documentFirstHeading"]/text()').get()
        paragraph = response.xpath('//div[@class="field-item even"]//p[not(@class)]/text()').get()

        yield {
            'url': link,
            'title': title,
            'body': paragraph
        }

    ## execution in zyte (scrapingHub)
    def parse_link_zyte(self, response):
        link = response.meta['url']
        title = response.xpath('//h1[@class="documentFirstHeading"]/text()').extract()
        paragraph = response.xpath('//div[@class="field-item even"]//p[not(@class)]/text()').extract()

        yield {
            'url': link,    
            'title': title,
            'body': paragraph
        }