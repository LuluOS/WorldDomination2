# /home/bot/tutorial/tutorial/spiders/reddit_spider.py
# to run: scrapy crawl reddit
import scrapy
import os
 
class RedditSpider(scrapy.Spider):
    name = "reddit"
    allowed_domains = ["reddit.com"]
    start_urls = [
        "http://www.reddit.com/r/technology/"
    ]
 
    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
       
        # os.getcwd() gets the path
        path = os.getcwd()
        # os.mkdir("newFolder") creates a new folder
        os.mkdir("Resources")
        # os.chdir("newFolder") change to the new folder
        os.chdir("Resources")
       
        with open(filename, 'wb') as f:
            f.write(response.body)
