import requests
from  bs4 import BeautifulSoup
class m():
    def __init__(self,url="http://m.360kan.com/m/favnZhH4Rnn8SR.html"):
        self.info={}
        if url.find("360kan")==-1:
            exit()
        html=requests.get(url).text
        doc=BeautifulSoup(html,'lxml')
        try:
            self.info['imgurl']=doc.select(".box .img img")[0].attrs['src']
            self.info['name']=doc.select(".cp-info-main h3")[0].contents[0].strip()
            self.info['year']= doc.select(".cp-info-main h3 i")[0].text
            self.info['area'] = doc.select(".cp-info-main p")[0].contents[2].strip()
            self.info['grade']= doc.select(".cp-info-main p")[1].contents[2].strip()
            self.info['director']= doc.select(".cp-info-main p")[2].contents[2].strip()
            self.info['protagonist']= doc.select(".cp-info-main p")[3].contents[2].strip()
            self.info['type']= doc.select(".cp-info-main p")[4].contents[2].strip()
            self.info['intro'] = doc.select(".cp-describe p")[0].get_text().strip()
            playurl = {}
            self.info['playurl'] = playurl
            itemurl = doc.select(".item")
            if itemurl.__len__() == 0:
                itemurl = doc.select(".p-dianying-play")[0]
                dataurl = itemurl.attrs['href']
                playurl[itemurl.get_text()] = dataurl[:dataurl.find("?")]
            else:
                for oneitem in itemurl:
                    dataurl = oneitem.attrs['data-url'] or oneitem.attrs['href']
                    playurl[oneitem.get_text()] = dataurl[:dataurl.find("?")]
        except:
            pass

class va():
    def __init__(self,url="http://m.360kan.com/va/Y8AtcnNxA2Q6Ez.html"):
        self.info={}
        if url.find("360kan")==-1:
            exit()
        html=requests.get(url).text
        doc=BeautifulSoup(html,'lxml')
        try:
            self.info['imgurl'] = doc.select(".box .img img")[0].attrs['src']
            self.info['name'] = doc.select(".cp-info-main h3")[0].contents[0].strip()
            self.info['updateto'] = doc.select(".js-info-up")[0].contents[0].strip()
            self.info['area'] = doc.select(".cp-info-main p")[1].contents[2].strip()
            self.info['channel'] = doc.select(".cp-info-main p")[2].contents[2].strip()
            self.info['compere'] = doc.select(".cp-info-main p")[3].contents[2].strip()
            self.info['intro'] = doc.select(".cp-describe p")[0].get_text().strip()
            playurl = {}
            self.info['playurl'] = playurl
            item =  doc.select(".single-series")
            for oneitem in item:
                temp=oneitem.text.split("\n")
                tempitem=oneitem.attrs['href']
                playurl[temp[1]+"||"+temp[2]]=tempitem[:tempitem.find("?")]
        except:
            pass

class ct():
    def __init__(self,url="http://m.360kan.com/ct/O0XnacSlMYCwCj.html"):
        self.info={}
        if url.find("360kan")==-1:
            exit()
        html=requests.get(url).text
        doc=BeautifulSoup(html,'lxml')
        try:
            self.info['imgurl'] = doc.select(".box .img img")[0].attrs['src']
            self.info['name'] = doc.select(".cp-info-main h3")[0].contents[0].strip()
            self.info['updateto'] = doc.select(".js-info-up")[0].contents[0].strip()
            self.info['area'] = doc.select(".cp-info-main p")[1].contents[2].strip()
            self.info['year'] = doc.select(".cp-info-main p")[2].contents[2].strip()
            self.info['intro'] = doc.select(".cp-describe p")[0].get_text().strip()
            item=doc.select(".g-clear a")
            playurl = {}
            self.info['playurl'] = playurl
            for oneitem in item:
                temp = oneitem.attrs['href']
                playurl[oneitem.text]=temp[:temp.find("?")]
        except:
            pass

class tv():
    def __init__(self,url="http://m.360kan.com/tv/PbVoc07kRm4uOH.html"):
        self.info={}
        if url.find("360kan")==-1:
            exit()
        html=requests.get(url).text
        doc=BeautifulSoup(html,'lxml')
        try:
            self.info['imgurl'] = doc.select(".box .img img")[0].attrs['src']
            self.info['name'] = doc.select(".cp-info-main h3")[0].contents[0].strip()
            self.info['updateto'] = doc.select(".js-info-up")[0].contents[0].strip()
            self.info['area'] = doc.select(".cp-info-main p")[1].contents[2].strip()
            self.info['year'] = doc.select(".cp-info-main p")[2].contents[2].strip()
            self.info['director'] = doc.select(".cp-info-main p")[3].contents[2].strip()
            self.info['protagonist'] = doc.select(".cp-info-main p")[4].contents[2].strip()
            self.info['intro'] = doc.select(".cp-describe p")[0].get_text().strip()
            item=doc.select(".g-clear a")
            playurl = {}
            self.info['playurl'] = playurl
            for oneitem in item:
                temp=oneitem.attrs['href']
                playurl[oneitem.text]=temp[:temp.find("?")]
        except:
            pass
