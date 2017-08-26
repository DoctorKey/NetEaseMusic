'''
Created on 2017年6月28日

@author: wyq

Changed on 2017.8.12

@author: flourish

'''
from crawler import url_manager, html_downloader, html_outputer
from crawler import html_parser

class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url, times):
        count = 1
        x = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try :
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont, x)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                x = x+1

                if count == times:
                    break
                count = count + 1
            except Exception as e:
                print('craw failed',e)

        urls = self.outputer.output_musicurl_list()
        return urls

