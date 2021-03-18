import scrapy
from scrapy import Request

class FootBaseSpider(scrapy.Spider):
    
    name = "Foot"
    start_urls = ['https://m.flashscore.fr/']
    
#    def first_url(self, response):
#        return Request(response.urljoin(response.css('a.fin').attrib['href']))
    
#    def parse(self, response):
#        for a in response.css('a.fin, a.sched'):
#            score = a.css('a.fin::text, a.sched::text').get()
#            next_url = a.css('a.fin').attrib['href']
#            yield Request(response.urljoin(next_url), callback=self.parse)
#            teams = a.css('h3::text').get()
#            yield {
#                "Score": score
#                "Teams": teams
#                }
    
#    def parse2(self, response):
#        for a in response.css('a.fin'):
#            next_url = a.css('a.fin').attrib['href']
#            Request(response.urljoin(next_url), callback=self.parse)
        
# =============================================================================
#     def parse(self, response):
# 
#         next_urls = response.xpath('//a[@class="fin"]/@href').extract()
#         for next_url in next_urls:
#             yield Request(response.urljoin(next_url), callback=self.parse)
#             
#             def parse2(self, response):
#                 teams = response.css('h3::test').get()
#                 score = response.css('b::text').get()
#         
#                 yield{
#                     "Teams": teams,
#                     "Score": score
#                     }
# =============================================================================
        
    def parse(self, response):
        match_page_links = response.css('div.soccer a')
        yield from response.follow_all(match_page_links, self.parse_result)
        
# =============================================================================
#     def parse_result(self, response):
#         def extract_with_css(query):
#             return response.css(query).get(default='').strip()
#         
#         yield {
#             'Teams': extract_with_css('h3::text'),
#             'Score': extract_with_css('b::text'),
#             'Infos_sup': extract_with_css('div.detail::text'),
#             'Cup': extract_with_css('h4')
#             }
# =============================================================================

    def parse_result(self, response):
        yield {
            'Teams': response.css('h3::text').get(default='').strip(),
            'Score': response.css('b::text').get(default='').strip(),
            'Infos_sup': response.css('div.detail::text').getall()[1]
            }