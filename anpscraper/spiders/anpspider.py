#####
# Spider for download file from a define url
# this is looking for .csv and .pdf files
#
# Nelson Monnerat
# 13/12/2022
#####

import scrapy
from anpscraper.items import AnpscraperItem

class AnpspiderSpider(scrapy.Spider):
    #the name of the spider
    name = 'anpspider'
    
    allowed_domains = ['www.gov.br']
    
    #the url of the first page that we will start scraping
    start_urls = ['https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/anuario-estatistico-2022']

    def parse(self, response):
        #here we are looping through the products and extracting the name, price & url
        title = response.css('title::text').extract_first()
        yield {'title': title }
        
        links = response.css('a::attr(href)').extract()
        for link in links:
            if ('.csv' in link) or ('.pdf' in link):
                item = AnpscraperItem()
                item['file_urls'] = [link]
                item['original_file_name'] = link.split('/')[-1]
                #yield {'links': link }
                yield item