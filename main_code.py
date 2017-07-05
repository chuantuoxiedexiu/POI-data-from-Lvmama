import re
import os

import string
class Spider(object):
    def __init__(self):
        self.citylist={}
        self.citylist["上海"]="http://s.lvmama.com/ticket/P1?keyword=%E4%B8%8A%E6%B5%B7#list"
        self.citylist["山东"]="http://s.lvmama.com/ticket/P1?keyword=%E5%B1%B1%E4%B8%9C#list"
        self.citylist["江苏"]="http://s.lvmama.com/ticket/P1?keyword=%E6%B1%9F%E8%8B%8F#list"
        self.citylist["安徽"]="http://s.lvmama.com/ticket/P1?keyword=%E5%AE%89%E5%BE%BD#list"
        self.citylist["江西"]="http://s.lvmama.com/ticket/P1?keyword=%E6%B1%9F%E8%A5%BF#list"
        self.citylist["浙江"]="http://s.lvmama.com/ticket/P1?keyword=%E6%B5%99%E6%B1%9F#list"
        self.citylist["福建"]="http://s.lvmama.com/ticket/P1?keyword=%E7%A6%8F%E5%BB%BA#list"
        self.citylist["北京"]="http://s.lvmama.com/ticket/?keyword=%E5%8C%97%E4%BA%AC#list"
        self.citylist["天津"]="http://s.lvmama.com/ticket/?keyword=%E5%A4%A9%E6%B4%A5#list"
        self.citylist["重庆"]="http://s.lvmama.com/ticket/?keyword=%E9%87%8D%E5%BA%86#list"
        self.citylist["内蒙古"]="http://s.lvmama.com/ticket/?keyword=%E5%86%85%E8%92%99%E5%8F%A4#list"
        self.citylist["新疆"]="http://s.lvmama.com/ticket/?keyword=%E6%96%B0%E7%96%86#list"
        self.citylist["广西"]="http://s.lvmama.com/ticket/?keyword=%E5%B9%BF%E8%A5%BF#list"
        self.citylist["西藏"]="http://s.lvmama.com/ticket/?keyword=%E8%A5%BF%E8%97%8F#list"
        self.citylist["黑龙江"]="http://s.lvmama.com/ticket/?keyword=%E9%BB%91%E9%BE%99%E6%B1%9F#list"
        self.citylist["吉林"]="http://s.lvmama.com/ticket/?keyword=%E5%90%89%E6%9E%97#list"
        self.citylist["辽宁"]="http://s.lvmama.com/ticket/?keyword=%E8%BE%BD%E5%AE%81#list"
        self.citylist["河北"]="http://s.lvmama.com/ticket/?keyword=%E6%B2%B3%E5%8C%97#list"
        self.citylist["河南"]="http://s.lvmama.com/ticket/?keyword=%E6%B2%B3%E5%8D%97#list"
        self.citylist["山西"]="http://s.lvmama.com/ticket/?keyword=%E5%B1%B1%E8%A5%BF#list"
        self.citylist["湖南"]="http://s.lvmama.com/ticket/?keyword=%E6%B9%96%E5%8D%97#list"
        self.citylist["湖北"]="http://s.lvmama.com/ticket/?keyword=%E6%B9%96%E5%8C%97#list"
        self.citylist["广东"]="http://s.lvmama.com/ticket/?keyword=%E5%B9%BF%E4%B8%9C#list"
        self.citylist["海南"]="http://s.lvmama.com/ticket/?keyword=%E6%B5%B7%E5%8D%97#list"
        self.citylist["贵州"]="http://s.lvmama.com/ticket/?keyword=%E8%B4%B5%E5%B7%9E#list"
        self.citylist["云南"]="http://s.lvmama.com/ticket/?keyword=%E4%BA%91%E5%8D%97#list"
        self.citylist["四川"]="http://s.lvmama.com/ticket/?keyword=%E5%9B%9B%E5%B7%9D#list"
        self.citylist["陕西"]="http://s.lvmama.com/ticket/?keyword=%E9%99%95%E8%A5%BF#list"
        self.citylist["青海"]="http://s.lvmama.com/ticket/?keyword=%E9%9D%92%E6%B5%B7#list"
        self.citylist["甘肃"]="http://s.lvmama.com/ticket/?keyword=%E7%94%98%E8%82%83#list"
        self.citylist["台湾"]="http://s.lvmama.com/ticket/?keyword=%E5%8F%B0%E6%B9%BE#list"
        self.citylist["香港"]="http://s.lvmama.com/ticket/?keyword=%E9%A6%99%E6%B8%AF#list"
        self.citylist["澳门"]="http://s.lvmama.com/ticket/?keyword=%E6%BE%B3%E9%97%A8#list"
        self.citylist["宁夏"]="http://s.lvmama.com/ticket/?keyword=%E5%AE%81%E5%A4%8F#list"
       

    def crowID(self,city):
        url=self.citylist[city]
        response=urllib2.urlopen(url)
        content=response.read()
        result=re.findall('<p class="count_num"><b>1</b>/(\d+)</p>',content)
        total_num=string.atoi(result[0])
        print 'the total pages of ',city,'is : ',total_num
        fileID='D:\\spider\\'+city+'_ID.txt'
        fileTitle='d:\\spider\\'+city+'_Title.txt'
        fID=open(fileID,'w')
        fTitle=open(fileTitle,'w')
        num=total_num+1
        for page in range(1,num):
            per_url=self.citylist[city].split('1?')[0]+str(page)+"?"+self.citylist[city].split('1?')[1]
            print per_url
            text=urllib2.urlopen(per_url).read()
            result=re.findall('<a target=._blank. class="ticket_img"\s+href=.http://ticket.lvmama.com/scenic-(\d+)"\s+title="(.+)".',text)
            for term in result:
                fID.write(term[0]+'\n')
                fTitle.write(term[1]+'\n')
                print term[0]+"\t"+term[1]
            #time.sleep(10)
        fID.close()
        fTitle.close()
        print city,"的ID抓取完毕！"


        
spider=Spider()
while True:  
    city=raw_input("请输入省市（上海，山东，江西，安徽，江苏，浙江，福建）：>")
    spider.crowID(city)

