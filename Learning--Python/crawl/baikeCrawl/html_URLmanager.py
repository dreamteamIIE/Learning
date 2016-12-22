# encoding=utf-8

class URLmanager(object):
	def __init__(self):
		self.newURLs = set()
		self.oldURLs = set()

	def get_newURL(self):
		aURL = (self.newURLs.pop())
		self.oldURLs.add(aURL)
		return aURL

	def add_URLS(self,urls):
		if len(urls)==0:
			return
		for item in urls:
			if item not in self.oldURLs:
				self.newURLs.add(item)

	def has_new_url(self):
		return len(self.newURLs)!=0