# encoding:utf-8
from bs4 import BeautifulSoup
import re

class Parser(object):
    def parse(self, html):
        soup = BeautifulSoup(html,'lxml')

        # 名称
        # <dd class="lemmaWgt-lemmaTitle-title">
        #     <h1>Python</h1>
        titleName = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1').string

        # 摘要
        # <div class="lemma-summary" label-module="lemmaSummary">
            # <div class="para" label-module="para">
        summary = soup.find('div', class_='lemma-summary')
        content = summary.strings
        strLst = []
        for item in content:
            strLst.append(item)
        str_result = ''.join(strLst)

        # urls
        # <a target="_blank" href="/view/592974.htm">解释器</a>
        urls = []
        urls = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        urls = ['http://baike.baidu.com'+item.attrs['href'] for item in urls]
        return titleName, urls, str_result