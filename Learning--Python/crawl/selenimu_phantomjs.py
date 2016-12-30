# encoding=utf-8
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# try:
# 	driver = webdriver.Chrome()
# 	driver.get('http://www.baidu.com')
# 	# assert "Python" in driver.title
# 	elem = driver.find_element_by_name("wd")
# 	elem.send_keys("test")
# 	elem.send_keys(Keys.RETURN)
# 	print driver.page_source
# except Exception,e:
# 	print e


class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_search_in_python_org(self):
		driver = self.driver
		driver.get('http://www.baidu.com')
		# self.assertIn("Python", driver.title)
		elem = driver.find_element_by_name('wd')
		elem.send_keys('pycon')
		elem.send_keys(Keys.RETURN)
		# assert "No results found." not in driver.page_source
		print driver.page_source

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()