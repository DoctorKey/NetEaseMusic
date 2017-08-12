'''
Created on 2017.8.12

@author: flourish

'''
# -*- coding: utf-8 -*-

import html_downloader, listhtml_parser, listhtml_outputer

class PrepareData(object):
    
    def __init__(self, urls):
        self.urls = urls
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = listhtml_parser.HtmlParser()
        self.outputer = listhtml_outputer.HtmlOutputer()

    def gendata(self):
        print('total numbers:' + str(len(self.urls)))
        count = 0
        for url in self.urls:
            count += 1
            print(str(count) + ':' + url)
            html_cont = self.downloader.download(url)
            new_data = self.parser.parse(url, html_cont)
            self.outputer.collect_data(new_data)

        self.outputer.output_data()
