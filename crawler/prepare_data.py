'''
Created on 2017.8.12

@author: flourish

'''
# -*- coding: utf-8 -*-

from crawler import html_downloader, playlist_parser, playlist_outputer

class PrepareData(object):
    
    def __init__(self, urls):
        self.urls = urls
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = playlist_parser.HtmlParser()
        self.outputer = playlist_outputer.HtmlOutputer()

    def gendata(self):
        print('total numbers:' + str(len(self.urls)))
        count = 0
        for url in self.urls:
            count += 1
            print(str(count) + ':' + url)
            html_cont = self.downloader.download(url)
            new_data = self.parser.parse(url, html_cont)
            self.outputer.collect_data(new_data)

        data = self.outputer.output_data()
        return data
