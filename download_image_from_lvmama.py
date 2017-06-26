import os
import re
import time
import urllib
import urllib2
def crow_url(city):
        citypath="d:\\spider\\"+city+"图片\\"
        print citypath
        if(os.path.exists(citypath)):
                pass
        else:
                os.mkdir(citypath)
        f=open("d:\\spider\\"+city+"_ID.txt",'r')
        url="http://ticket.lvmama.com/scenic-"
        for each  in f.readlines() :
                each=each.strip()
                filename=citypath+each+".txt"
                print filename
                furl=open(filename,'w')
                print each
                full_url=url+each
                print full_url
                try:
                        res=urllib2.urlopen(full_url)
                except:
                        print 'url not found'
                        continue
               
                text1=res.read()
                result1=re.findall('<img src="(.+\jpg)" data-big-img="(.+\.jpg)".+>',text1)
                for term in result1:
                        try:
                                print "ONE:  ",term[0]
                                furl.write(term[0]+'\n')
                        except:
                                print 'erro '
                                continue
                        else:
                                continue
                furl.close()
               
               
                furl=open(filename,'a')

                result2=re.findall('<div class="imgbox">\s+<img src="(.+jpg)" width="720" alt=".+" />',text1)

                for term2 in result2:
                        try:
                                print "TWO:  ",term2
                                furl.write(term2+'\n')
                        except:
                                continue
                        else:
                                continue
                #try:  
                 #       url_file=urllib2.urlopen(term[0])
                 #       name=term[0].split('/')[-1]
                 #       trueimage=filedirs+"\\"+name
                 #       print trueimage
                 #       fimage=open(trueimage,'wb')  
                 #       while True:  
                 #           r=url_file.read(1024)  
                 #          if not r:  
                 #               break  
                 #          fimage.write(r)  
                 #      fimage.close()
                 # time.sleep(1)
              #  except:  
              #          print "噢，保存图片出现问题。。。"  
             #           
              #  else:  
              #          print "保存图片成功。。。"  
                furl.close()

        f.close()
        print "浙江的图片抓取完毕！！"


for i in ('上海','浙江'):
        print '开始抓取的城市是：',i
        crow_url(i)
        print '城市：',i,"抓取完毕"
        

