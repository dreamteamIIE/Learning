# encoding=utf-8
import urllib2
from baikeCrawl import html_downloader,html_parser,html_URLmanager


class Crawler(object):
    '主程序'
    def __init__(self):
        self.downloader = html_downloader.Downloader()
        self.parser = html_parser.Parser()
        self.URLmanager = html_URLmanager.URLmanager()


if __name__ == "__main__":
    root_url = 'http://baike.baidu.com/item/Python'
    crawler = Crawler()
    crawler.URLmanager.add_URLS([root_url])
    count = 1
    while True:
        try:
            if count == 10:
                break
            url = crawler.URLmanager.get_newURL()
            result = crawler.downloader.download(url)
            titleName, urls, content = crawler.parser.parse(result)
            crawler.URLmanager.add_URLS(urls)
            print "Title: %s" % titleName
            print 'Summary : \n\t %s' % content
            count+=1
        except Exception, e:
            print e

    print 'collect %d records' % count

