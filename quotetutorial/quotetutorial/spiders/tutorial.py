import scrapy
import re
from ..items import QuotetutorialItem
from scrapy.http import FormRequest

class TutorialSpider(scrapy.Spider):
    name = 'tutorial'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        token= response.xpath("//input[@name='csrf_token']/@value").get()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'asdf',
            'password': 'sdffg'
        }, callback= self.scraping)

    def scraping(self, response):
        pat= r"(\u201c|\u201d)"
        items= QuotetutorialItem()

        for post in response.css('div.quote'):
            quote=  re.sub(pat , "" , post.css('span.text::text').get())
            author= post.css('.author::text').get()
            tags= post.css('a.tag::text').getall()
            items['quote']= quote
            items['author']= author
            items['tags']= tags
            yield items


        
        next_page= response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.scraping)
        