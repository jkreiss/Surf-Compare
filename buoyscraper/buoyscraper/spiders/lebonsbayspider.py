import re
from datetime import datetime
import scrapy

class LebonsbaySpider(scrapy.Spider):
    name = 'lebonsbay'
    start_urls = ['https://www.ecan.govt.nz/data/current-wave-data']


    def parse(self, response):
        resp = response.css('div.summary-table-wrapper table#riverflow-by-region tbody tr')
        time = resp.css('td:nth-child(1)::text').get()
        style_card = resp.css('td:nth-child(2) i::attr(style)').get()
        degree_match = re.search(r'rotate\((\d+)', style_card)
        degree = int(degree_match.group((1)))

        nums = resp.css('td:nth-child(n+3):nth-child(-n+5)::text').getall()

        nums = [float(x.strip()) for x in nums if x.strip()]
        yield {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'buoytime': time,
            'direction': degree,
            'wave_height': nums[0],
            'max_wave_height': nums[1],
            'wave_period': int(nums[2])
        }
        return nums


