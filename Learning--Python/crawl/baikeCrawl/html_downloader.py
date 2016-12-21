import urllib2


class Downloader(object):
    def download(self, url):
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        content = response.read()
        return content