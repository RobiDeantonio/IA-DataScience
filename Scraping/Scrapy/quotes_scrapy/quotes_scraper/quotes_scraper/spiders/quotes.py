import scrapy

#/////////////////////////////////////
### Create a new project $ scrapy startproject tutorial
### Open shell with a web page:  $scrapy shell 'http://quotes.toscrape.com/'
### xpath example in shell: $response.xpath('//div[contains(@class,"tags-box")]//a[@class="tag"]/text()').getall()
### execute code in terminal:  $scrapy crawl quotes
#/////////////////////////////////////

#Titulo = //h1/a/text()
#Citas = //span[@class="text" and @itemprop="text"]/text()
#Top tags = //div[contains(@class,"tags-box")]//a[@class="tag"]/text()
#Next page Buttom = //ul[@class="pager"]//li[@class="next"]/a/@href

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [ 
        'http://quotes.toscrape.com/'
    ]
    custom_settings = {
        'FEED_URI': 'quotes.json',
        'FEDD_FORMAT': 'json',
        'CONCURRENT-REQUEST' : 24,
        'MEMUSAGE_LIMIT_MB': 2048,
        'MEMUSAGE_NOTIFY_MAIL':['rysanchezd@unal.edu.co'],
        'ROBOTSTXT_OBEY': True,
        'USAGE_AGENT': 'Pepito',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse_only_quotes(self, response, **kwargs):
        if kwargs:
            quotes = kwargs['cites']['quotes']
            author = kwargs['cites']['author']
        quotes.extend(response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall())
        author.extend(response.xpath('//small[@class="author" and @itemprop="author"]/text()').getall())

        next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs={'cites':{'quotes': quotes,'author': author}})
        else:
            yield {
                'cites':{'quotes':quotes, 'author':author}
                }

    def parse(self, response):
        
        title = response.xpath('//h1/a/text()').get()
        top_tags = response.xpath('//div[contains(@class,"tags-box")]//a[@class="tag"]/text()').getall()
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        author = response.xpath('//small[@class="author" and @itemprop="author"]/text()').getall()

        # 'Use in Terminal'  $ scrapy crawl quotes -a top=3
        top = getattr(self, 'top', None)
        if top:
            top = int(top)
            top_tags = top_tags[:top]

        yield {
            'title': title,
            'top_ten_tags':top_tags
        }

        next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs={'cites':{'quotes': quotes,'author': author}})