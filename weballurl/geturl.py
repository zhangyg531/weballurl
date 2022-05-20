import time
import traceback

import requests
from fake_useragent import UserAgent
import re
import sys
from .delay_wrapper import delayed

sys.setrecursionlimit(100000)


class geturl:
    def __init__(self):
        self.header = {
            'user-agent': str(UserAgent().random)
        }
        self.url_list = []
        self.err_url = []
        self.start_time = int(time.time())

    @delayed(0)
    def request(self, url, domain, timeout, count, is_external=0):
        try:
            res = requests.get(url, headers=self.header, timeout=3)
            res.encoding = res.apparent_encoding
            html = res.text
            self.all_url(html, domain, timeout, count, is_external)
        except:
            self.err_url.append(url)

    def all_url(self, resp, domain, timeout, count, is_external=0):
        all_url = re.findall('href="(.+?)"', resp) + re.findall('src="(.+?)"', resp)\
                  + re.findall('target="(.+?)"', resp)
        for link in all_url:
            if is_external == 0:
                if (link.startswith('http')) and (link not in self.url_list) and (domain in link) and \
                        (len(url_list) < int(count)) and ((int(time.time()) - self.start_time) < int(timeout)):
                    self.url_list.append(link)
                    f = open('url.txt', 'a+', encoding='utf-8')
                    f.write(str(link) + '\n')
                    f.close()
                    print(link)
                    self.request(link, domain,  timeout, count, is_external)
            else:
                if (link.startswith('http')) and (link not in self.url_list)  and \
                        (len(url_list) < int(count)) and ((int(time.time()) - self.start_time) < int(timeout)):
                    self.url_list.append(link)
                    f = open('url.txt', 'a+', encoding='utf-8')
                    f.write(str(link) + '\n')
                    f.close()
                    print(link)
                    self.request(link, domain,  timeout, count, is_external)


    def startres(self, url, domain, timeout, count, is_external=0):
        self.request(url, domain, timeout, count, is_external)
        return self.url_list


if __name__ == '__main__':
    allurl = geturl()
    url_list = allurl.startres('https://blog.csdn.net', 'csdn.net', 300, 300, is_external=0)