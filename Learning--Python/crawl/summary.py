# encoding:utf-8

from bs4 import BeautifulSoup
import urllib2

response1 = urllib2.urlopen('http://cuiqingcai.com/2599.html')
response2 = urllib2.urlopen('http://cuiqingcai.com/2556.html')
html = response1.read() + '\n' + response2.read()

soup = BeautifulSoup(html,'lxml')
content = soup.body.descendants

f = open('test.txt','w')

for item in content:
    if item.name == 'h2':
        f.write(item.string.encode('utf-8') + '\n')
    elif item.name == 'h3':
        f.write('\t' + item.string.encode('utf-8') + '\n')

f.close()



