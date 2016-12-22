# encoding:utf-8
from bs4 import BeautifulSoup
import re


class Parser(object):

    # def _getTitleName(self,soup):
    #     # 名称
    #     # <dd class="lemmaWgt-lemmaTitle-title">
    #     #     <h1>Python</h1>
    #     return soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1').string
	#
    #
    # def _getSummary(self,soup):
    #     # 摘要
    #     # <div class="lemma-summary" label-module="lemmaSummary">
    #         # <div class="para" label-module="para">
    #     summary = soup.find('div', class_='lemma-summary')
    #     content = summary.strings
    #     strLst = []
    #     for item in content:
    #         strLst.append(item)
    #     str_result = ''.join(strLst)
    #     return str_result



    def _getURLs(self,soup):
         # urls
        # <a target="_blank" href="/view/592974.htm">解释器</a>

        urls = []
        urls = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        urls = ['http://baike.baidu.com'+item['href'] for item in urls]
        return urls

    def _get_data(self,soup):

        res_data = {}

        # 摘要
        # <div class="lemma-summary" label-module="lemmaSummary">
            # <div class="para" label-module="para">
        summary = soup.find('div', class_='lemma-summary')
        content = summary.strings
        strLst = []
        for item in content:
            strLst.append(item)
        str_result = ''.join(strLst)
        res_data['summary'] = str_result


        # 名称
        # <dd class="lemmaWgt-lemmaTitle-title">
        #     <h1>Python</h1>
        res_data['title'] = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1').string

        return res_data



    def parse(self, html):
        soup = BeautifulSoup(html,'lxml',from_encoding='utf-8')

        # titleName = self._getTitleName(soup)
        # summary = self._getSummary(soup)

        data_parsed = self._get_data(soup)
        urls = self._getURLs(soup)

        return urls, data_parsed