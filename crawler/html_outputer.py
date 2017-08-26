'''
Created on 2017年6月28日

@author: wyq
'''
# -*- coding: utf-8 -*-
import csv
import codecs
from filecmp import cmp

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
        
    def collect_data(self,data):
        if data is None:
            return 
        for element in data:
            self.datas.append(element)

    def output_musicurl_list(self):
        urls = []
        url_pre = 'http://music.163.com'
        for data in self.datas:
            urls.append(url_pre + data[1])
        return urls

    
    
    
    



