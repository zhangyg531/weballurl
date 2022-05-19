import traceback

import requests
from fake_useragent import UserAgent
import re
from delay_wrapper import delayed


class geturl:
    def __init__(self):
        self.header = {
            'user-agent': str(UserAgent().random)
        }
        self.url_list = []
        self.err_url = []

    # @delayed(0)
    def request(self, url, domain):
        try:
            res = requests.get(url, headers=self.header, timeout=3)
            res.encoding = res.apparent_encoding
            html = res.text
            self.all_url(html, domain)
        except:
            self.err_url.append(url)

    def all_url(self, resp, domain):
        all_url = re.findall('href="(.+?)"', resp)
        for link in all_url:
            if (link.startswith('http')) and (link not in self.url_list) and (domain in link):
                self.url_list.append(link)
                print(self.url_list)
                self.request(link, domain)

    def startres(self, url, domain):
        self.request(url, domain)
        return self.url_list


if __name__ == '__main__':
    allurl = geturl()
    url_list = allurl.startres('https://blog.csdn.net', 'csdn.net')