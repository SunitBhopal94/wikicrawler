import scrapy
import re

class wikicrawler(scrapy.Spider):
    name = "wikiscrap"

    def start_requests(self):
        urls =['https://en.wikipedia.org/wiki/Edge_computing']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def remove_img_tags(self, data):
      p  = re.compile(r'<img.*?/>')
      return p.sub('', data)
      
    def parse(self, response):
         filename = "test.html"
 
         with open(filename, 'wb') as f:
            f.write(response.body)     