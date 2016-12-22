# encoding=utf-8
import urllib2
from baikeCrawl import html_downloader,html_parser,html_URLmanager


class Crawler(object):
    '主程序'
    def __init__(self):
        self.downloader = html_downloader.Downloader()
        self.parser = html_parser.Parser()
        self.URLmanager = html_URLmanager.URLmanager()


    def crawl(self, root_url):
        self.URLmanager.add_URLS([root_url])
        count = 1
        while self.URLmanager.has_new_url():
            try:
                if count == 10:
                    break
                url = self.URLmanager.get_newURL()
                html_cont = self.downloader.download(url)
                urls, data_parsed = self.parser.parse(html_cont)
                self.URLmanager.add_URLS(urls)
                print "Title: %s" % data_parsed['title']
                print 'Summary : \n\t %s' % data_parsed['summary']
                count+=1
            except Exception, e:
                print e

        print 'collect %d records' % count


if __name__ == "__main__":
    root_url = 'http://baike.baidu.com/item/Python'
    obj_crawler = Crawler()
    obj_crawler.crawl(root_url)



