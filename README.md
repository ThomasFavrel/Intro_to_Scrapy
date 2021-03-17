# Intro_to_Scrapy
Project to learn how to use Scrapy for WebScraping in python.

Install Scrapy : pip install scrapy  
(use conda instead of pip if you are in anaconda terminal)

Start a new project : scrapy startproject WebCrawler

	WebCrawler
	│   scrapy.cgf
	└───WebCrawler
	│   │   __init__
	│   │   items.py
	│   │   middlewares.py
	│   │   pipelines.py
	│   │   settings.py
	│   │
	│   └───__pycache__
	│   │   scrapy.cgf
	│   │
	│   └─── spiders
	│   │   __pycache__
	│   │   __init__ 
	│   │   votre script de webscraping içi


* settings.py : nombre de requêtes par secondes, par IP, extensions,...
* Pipelines.py : pipelines afin d'ajuster le format de sortie
* Items.py : permet de définir les objets Item

## Start scraping
### Extract information in one page

Open the Scrapy Shell : scrapy shell

Send a request to our URL :

url = 'https://myanimelist.net/manga.php?letter=B'
fetch(url)

Return : response

We have identify mangas are in a div : div.js-categories-seasonal

* To extract the first manga's title:

Titles are in balise a : a class="hoverinfo_trigger fw-b" href=

sub = sponse.css('div.js-categories-seasonal tr ~ tr')[0]  
title = ub.xpath('//a[@class="hoverinfo_trigger fw-b"]/strong/text()').extract_first().strip()  
or >>> title = sub.css('a[id] strong::text').extract_first().strip()  
print(title)

* To extract synopsis

xpath  
synopsis = sub.xpath('//div[@class="pt4"]/text()').extract_first()  
css  
synopsis = sub.css("div.pt4::text").extract_first()  

* To extract type, score, volumes

These informations are in td cell in a tr balise

css  
type_= sub.css('td:nth-child(3)::text').extract_first()  
volumes=  sub_block .css('td:nth-child(4)::text').extract_first().strip()  
rating =  sub_block .css('td:nth-child(5)::text').extract_first().strip()  
​  
xpath  
informations = sub.xpath("//tr/td[@class='borderClass ac bgColor0']/text()").extract().strip()  
the 3 first information are type - volumes- score  so :  
type_ = d[:1]  
volumes = d[:2]  
rating = d[:3]  

### Extract from other pages

Url in a span:  
response.xpath('//span[@class="bgColor1"]//a/@href').extract()  
output  
['/manga.php?letter=B&show=50',   
'/manga.php?letter=B&show=100',   
'/manga.php?letter=B&show=950',  
'/manga.php?letter=B&show=50',   
'/manga.php?letter=B&show=100', '/manga.php?letter=B&show=950'  
]  

next_urls = response.xpath('//span[@class="bgColor1"]//a/@href').extract()  
for next_url in next_urls:  
    yield Request(response.urljoin(next_url), callback=self.parse_anime_list_page)  






## Football Score

url = 'https://m.flashscore.fr/'

fetch(url)

resonse.css('div.soccer').get()

scores fini:  
response.css('a.fin').get()  
response.css('a.fin').attrib['href'] --> link  


