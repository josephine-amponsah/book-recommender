import scrapy
import json
import time
import requests
from scrapy.spiders import CrawlSpider, Rule

class PyBooks(CrawlSpider):
    name = 'pybooks'
    start_urls = ['https://www.amazon.com/s?i=stripbooks&rh=n%3A285856&fs=true&qid=1652778600&ref=sr_pg_1']
    
    def parse(self, response, **kwargs):
        url = response.url
        booktitle = response.css('h2.a-size-mini').get()
        print(booktitle)