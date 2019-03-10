import os,random
from multiprocessing.pool import ThreadPool
from base.rule import *
def writecache(name,data):
        with open('./cache/'+name,'wb') as f:
            f.write(data.encode('UTF-8'))
        return True
def readcache(name):
    with open('./cache/' + name, 'rb') as f:
        return f.read()

def existfile(name):
    return os.path.exists('./cache/'+name)

def ran(count=20):#20%概率返回True
    if random.randint(0,100)>count:
        return True
    else:
        return False

def run(name):
    pool = ThreadPool(20)
    # 定义线程数量
    def play(url):
        if url.find("/m/") > 0:
            temp = m(url).info
            data.append(temp)
        elif url.find("/ct/") > 0:
            temp = ct(url).info
            data.append(temp)
        elif url.find("/tv/") > 0:
            temp = tv(url).info
            data.append(temp)
        elif url.find("/va/") > 0:
            temp = va(url).info
            data.append(temp)
        else:
            data.append({})
    html = requests.get("http://m.360kan.com/search/index?kw={0}".format(name)).text
    doc = BeautifulSoup(html, 'lxml')
    try:
        img = doc.select(".longlist")[0].select(".img")
    except:
        return {}
    data = []
    for one in img:
        url = "http://m.360kan.com"+one.attrs['href']
        pool.apply_async(play,args=(url,))
    pool.close()
    pool.join()
    return data