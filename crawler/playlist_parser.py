'''
Created on 2017年6月28日

@author: wyq

Changed on 2017.8.13

@author: flourish

'''
from bs4 import BeautifulSoup
import urllib.parse


class HtmlParser(object):
    
    def get_songslist(self, page_url, soup):
        res_data = []
        
        list_playcount = soup.select('div.u-title div.more strong#play-count')
        list_author = soup.select('div.m-info div.cnt div.cntc div.user span.name a.s-fc7')
        list_playlistcount = soup.select('span.sub span#playlist-track-count')
        list_allcount = soup.select('div#content-operation a')
        list_music = soup.select('div#song-list-pre-cache li a')

#         print(list_playcount[0].text)
#         print(list_author)
#         print(list_playlistcount)
#         print(list_collectcount[2]['data-count'])
#         print(list_collectcount[3]['data-count'])
#         print(list_music)

        #无创建人、歌曲数、播放量的歌单不进行计算
        if len(list_author) != 0 and int(list_playlistcount[0].text) > 1: 
#                 print('歌单播放量:'+list_playcount[0].text)
            list_playcounts = int(list_playcount[0].text)
            if list_playcounts >= 100:
                if list_allcount[2]['data-res-action'] == 'fav':
                    list_collectcount = int(list_allcount[2]['data-count'])
#                     print('收藏数:'+list_collectcount[2]['data-count'])
                if list_allcount[3]['data-res-action'] == 'share':
                    list_sharecount = int(list_allcount[3]['data-count'])
#                     print('分享数:'+list_collectcount[3]['data-count'])
                if list_allcount[5]['data-res-action'] == 'comment':
                    if list_allcount[5].next()[0].text != '评论':
                        list_commentcount = int(list_allcount[5].next()[0].text)
                    else:
                        list_commentcount = 0
#                         print('评论数:'+list_collectcount[5].next()[0].text)
                #获取歌单中歌曲
                music = []
                for element in list_music:
                    music.append(element.text)
                
                #播放量、收藏数、分享数、评论数、歌曲列表
                res_data.append([list_playcounts, 
                                list_collectcount, list_sharecount, list_commentcount, music])     
        return res_data
    
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont, "lxml")
        new_data = self.get_songslist(page_url, soup)
        return new_data
    
    



