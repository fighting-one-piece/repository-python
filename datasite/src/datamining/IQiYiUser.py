# -*- coding:utf-8 -*-

'''
@author: wulin
'''

import json
import requests
from bs4 import BeautifulSoup

profileUrl = 'http://www.iqiyi.com/u/1239622920'
followProfileUrl = profileUrl + '/follow'
fansProfileUrl = profileUrl + '/fans'
fProfileUrl = profileUrl + '/f'
vProfileUrl = profileUrl + '/v'

def handleProfileURL():
    response = requests.get(profileUrl).text
    bs = BeautifulSoup(response, "html.parser")
    print bs.select('div.num_item a i')[0].text
    print bs.select('div.num_item a i')[1].text
    #print bs.find('span', {"class" : "f14 ml10"}).text
    print '====================================='
    for div in bs.select('div.pc-item-box') :
        spans = div.findAll('span', {"class" : "f14 ml10"})
        for span in spans :
            print span.text
    print '=='
    spans = bs.findAll('span', {"class" : "f14 ml10"})
    for span in spans :
        print span.text

def handleFollowProfileURL(followProfileUrl):
    response = requests.get(followProfileUrl).text
    bs = BeautifulSoup(response, "html.parser")
    divs = bs.select('div.item-detail')
    for div in  divs :
        a = div.find("a", {"data-v2":"1"})
        if a is not None :
            print a.text + '-' + a['data-userinfopopup-id'] + '-' + a['href']
        desc_as = div.select('div.detail_desc a')
        for desc_a in desc_as :
            print desc_a.text
            print str(desc_a.text).split(' ')[1]
            
def handleFollowURL():
    url = 'http://www.iqiyi.com/u/api/space/relation/get_list?target_uid=2303207288&section=2&page=0&type=follow'
    response = requests.get(url).text
    bs = BeautifulSoup(json.loads(response)['data'], "html.parser")
    divs = bs.select('div.item-detail')
    for div in  divs :
        a = div.find("a", {"data-v2":"1"})
        if a is not None :
            print a.text + '-' + a['data-userinfopopup-id'] + '-' + a['href']
        desc_as = div.select('div.detail_desc a')
        for desc_a in desc_as :
            print desc_a.text
            print str(desc_a.text).split(' ')[1]
            
def handleFansProfileURL(fansProfileUrl):
    response = requests.get(fansProfileUrl).text
    bs = BeautifulSoup(response, "html.parser")
    divs = bs.select('div.item-detail')
    for div in  divs :
        a = div.find("a", {"data-v2":"1"})
        if a is not None :
            print a.text + '-' + a['data-userinfopopup-id'] + '-' + a['href']
        desc_as = div.select('div.detail_desc a')
        for desc_a in desc_as :
            print desc_a.text
            print str(desc_a.text).split(' ')[1]
            
def handleFansURL():
    url = 'http://www.iqiyi.com/u/api/space/relation/get_list?target_uid=1239622920&section=2&page=1&type=fans'
    response = requests.get(url).text
    bs = BeautifulSoup(json.loads(response)['data'], "html.parser")
    divs = bs.select('div.item-detail')
    for div in  divs :
        a = div.find("a", {"data-v2":"1"})
        if a is not None :
            print a.text + '-' + a['data-userinfopopup-id'] + '-' + a['href']
        desc_as = div.select('div.detail_desc a')
        for desc_a in desc_as :
            print desc_a.text
            print str(desc_a.text).split(' ')[1]
    
def handleFProfileURL(fProfileUrl):
    responseText = requests.get(fProfileUrl).text
    handleFURLText(responseText)
        
def handleFURLText(text):
    bs = BeautifulSoup(text, "html.parser")
    divs = bs.findAll('div', {"class" : "user-feed-wrapBox clearfix"})
    for div in divs :
        pdivs = div.select('div.user-feed-wrap')
        for pdiv in pdivs :
            titleDivs = pdiv.findAll('div', attrs = {"class" : "title clearfix"})
            for titleDiv in titleDivs :
                print titleDiv.select_one('div.title_info span').text
                print titleDiv.select_one('div.title_desc p').text
            videoNameTag = pdiv.select_one('div.mod-piclist_info p.mod-piclist_info_title a')
            print videoNameTag.text
            print videoNameTag['data-videoid']
            print videoNameTag['href']
            videoPlayTag = pdiv.select_one('div.mod-piclist_info p.mod-piclist_info_times span.playTimes a')
            if videoPlayTag is not None :
                videoPlayNum = videoPlayTag.text
                print videoPlayNum
            videoCommentTag = pdiv.select_one('div.mod-piclist_info p.mod-piclist_info_times span.commentTimes a')
            if videoCommentTag is not None :
                videoCommentNum = videoCommentTag.text
                print videoCommentNum
            emTag = pdiv.find('em', attrs = {"class" : "con fs14"})
            if emTag is not None :
                print emTag.text
    tipsDiv = bs.select_one('div.tips-loading')
    if tipsDiv is not None :
        fURL = tipsDiv['data-loading-src']
        handleFURLPageText(fURL)
        
def handleFURLPageText(url):
    response = requests.get(url).text
    data = json.loads(response)['data']
    handleFURLText(data)
    
def handleVProfileURL(vProfileUrl):
    print ''
    
if __name__ == '__main__' :
#     handleFollowProfileURL(followProfileUrl)
#     handleFansProfileURL(fansProfileUrl)
#     handleFProfileURL(fProfileUrl)
    handleFProfileURL(fProfileUrl)
    