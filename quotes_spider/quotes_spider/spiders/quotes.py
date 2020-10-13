import scrapy
from ..items import QuotesSpiderItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    

    def parse(self, response):
        item = QuotesSpiderItem()
        #find all cards
        cards = response.css(".quote")
        for card in cards:
            quote = card.css(".text::text").extract_first()
            author = card.css(".author::text").extract_first()
            tags_list = card.css(".tags a::text").extract()
            tags = ",".join(tag for tag in tags_list)
            
            item['quote'] = quote
            item['author'] = author 
            item['tags'] = tags 

            yield item
        
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page,callback = self.parse)
