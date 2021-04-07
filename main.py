import re
import os
import sys
import requests
from bs4 import BeautifulSoup

sys.setdefaultencoding("utf-8")

findImgsrc = re.compile('r<img.*src="(.*?)">')

url = 'https://www.zhihu.com/question/297160118/answer/503842679'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}


def askhtml(url):
    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    return soup


def getdata(soup):
    img_list = soup.find_all('img')
    title_list = soup.find_all('h1')
    tag = str(title_list)
    tags = tag[34:-6]
    tags = tags.encode('gbk')
    if not os.path.exists('./' + 'tags' + '/'):
        os.mkdir('./' + 'tags' + '/')

    i = 0
    z = 0
    t = 0
    for img in img_list:
        img_url = img['src']
        i = i + 1
        img_title = i
        print(img_url, img_title)
        t = t + 1
        if (t == 50):
            break
        try:
            with open('./' + 'tags' + '/' + '%d' % img_title + '.png', 'wb') as f:
                image = requests.get(img_url, headers=headers).content
                f.write(image)
                print ('Successful!', img_title)
        except Exception as e:
            print(repr(e))


if __name__ == '__main__':
    soup = askhtml(url)
    getdata(soup)
