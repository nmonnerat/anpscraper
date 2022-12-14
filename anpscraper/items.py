# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
#####
# Set file name as item and the original file name to be used
#
# Nelson Monnerat
# 13/12/2022
#####

import scrapy


class AnpscraperItem(scrapy.Item):
    # define the fields for your item here like:
    file_urls = scrapy.Field()
    # add the file name to be saved instead of the hash code
    original_file_name = scrapy.Field()
    # the file to be saved
    files = scrapy.Field
