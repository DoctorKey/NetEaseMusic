from crawler import spider_main, prepare_data
from pymining import itemmining

if __name__ == "__main__":
    root_url = "http://music.163.com/discover/playlist"
    obj_spider = spider_main.SpiderMain()
    print("crawler begins")
    musiclist_urls = obj_spider.craw(root_url, 5)
    print("crawler Work Done!")
    '''
    print("length:" + str(len(urls)))
    for url in urls:
        print(url)
    '''
    preparedata = prepare_data.PrepareData(musiclist_urls)
    data = preparedata.gendata()
    '''
    for lists in data:
        print(lists)
        '''

    transactions = data
    relim_input = itemmining.get_relim_input(transactions)
    report = itemmining.relim(relim_input, min_support = 5)
    print(report)
