import urllib2


class Downloader(object):

    def download(self, url):
        if url is None:
            return

        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        if response.getcode() != 200:
            return None

        content = response.read()
        return content