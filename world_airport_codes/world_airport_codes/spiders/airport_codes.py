# -*- coding: utf-8 -*-
import scrapy


class AirportCodesSpider(scrapy.Spider):
    name = 'airport_codes'
    allowed_domains = ['www.world-airport-codes.com/alphabetical/airport-name/a.html']
    start_urls = ['www.world-airport-codes.com/alphabetical/airport-name/a.html']

    def parse(self, response):
        data = []

        table = response.css('.stack2')

        row_selector = ".//tr[@class='light-row']|.//tr[@class='dark-row']"

        for row in table.xpath(row_selector):
            print(row)

        return data
