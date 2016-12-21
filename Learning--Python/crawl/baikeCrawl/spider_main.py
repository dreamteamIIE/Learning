# encoding=utf-8
import urllib2
from baikeCrawl import html_downloader,html_parser


class Crawler(object):
    '主程序'
    def __init__(self):
        self.downloader = html_downloader.Downloader()
        self.parser = html_parser.Parser()


if __name__ == "__main__":
    root_url = 'http://baike.baidu.com/item/Python'
    crawler = Crawler()
    result = crawler.downloader.download(root_url)
    result, urls, content = crawler.parser.parse(result)
    print result
    for item in urls:
        print item
    print content
