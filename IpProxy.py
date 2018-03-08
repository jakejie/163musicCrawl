#! python2
# coding: utf-8

import requests


# from requests import exceptions
# import random
# from bs4 import BeautifulSoup as Bs
# import time
# import threading
# import os


class IpProxy:
    api_url = 'http://api.xdaili.cn/xdaili-api/privateProxy/applyStaticProxy' \
              '?spiderId=b7b51607bf9b4bff8fc512cee5f14a07&returnType=2&count=1'

    test_url = 'http://wenshu.court.gov.cn/CreateContentJS/CreateContentJS.aspx?DocID=6184edd5-cfe1-43d1-9908-a80700a09c24'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/62.0.3202.94 Safari/537.36',
    }
    current_proxy = None
    proxy_list = list()
    lock = False

    def validate_proxy(self, proxy, timeout=10):
        try:
            print('[i] 正在测试 %s' % proxy)
            response_wenshu = requests.get(self.test_url, headers=self.headers, proxies=proxy, timeout=timeout)
            if 'createcontentjs' in response_wenshu.url.lower() and 'var jsonhtmldata' in response_wenshu.text.lower():
                return True
            else:
                print('%s\n代理测试结果为失效。' % response_wenshu.text.decode(response_wenshu.encoding))
                return False
        except Exception as e:
            print('[x] 失败: %s' % e)
            return False

    def change(self, proxy_type='http', level='fast', selfcall=False):
        '''if not self.lock:
            self.lock = True
        elif not selfcall:
            time.sleep(10)
            return self.current_proxy
        if self.current_proxy and self.validate_proxy(self.current_proxy):
            print('当前代理依然可用: %s' % self.current_proxy
            self.lock = False
            return self.current_proxy
        while self.proxy_list:
            proxy = self.proxy_list.pop()
            if self.validate_proxy(proxy):
                self.current_proxy = proxy
                self.lock = False
                return proxy
        while True:
            try:
                response = requests.get(self.api_url)
                dic_proxies = response.json()
                if 0 != int(dic_proxies['ERRORCODE']):
                    print('代理池返回错误码 %s. 休眠10秒后重试。' % dic_proxies['ERRORCODE']
                    time.sleep(10)
                    continue
                for dic in dic_proxies['RESULT']:
                    proxy_ip = dic['ip']
                    proxy_port = dic['port']
                    proxy = {proxy_type: proxy_type + '://' + proxy_ip + ':' + str(proxy_port)}
                    self.proxy_list.append(proxy)
                return self.change(proxy_type, selfcall=True)
                #proxy = {'http': u'http://101.37.79.125:3128'}
                #test_proxy(proxy)
            except Exception as e:
                print('[x] 尝试访问api失败: %s; api_url: %s' % (e, api_url)
        '''
        # 代理服务器
        proxyHost = "http-dyn.abuyun.com"
        proxyPort = "9020"

        # 代理隧道验证信息
        proxyUser = "HA8S948CPYMECB6D"  # "H69157Q3M809705D"  # "H01234567890123D"
        proxyPass = "1E5B62FDD6067BB3"  # "41D9DF45C57759A6"  # "0123456789012345"

        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }

        proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }
        return proxies


DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    # "Cookie": "_ntes_nnid=825b4dc594d9317b392b5eb07d3340c5,1512955897763; _ntes_nuid=825b4dc594d9317b392b5eb07d3340c5; _iuqxldmzr_=32; vjuids=-3b1da70ef.1605e5e08c4.0.807cbde916537; __e_=1514512434019; usertrack=ezq0pVppmc9QPg7nBDMgAg==; _ga=GA1.2.1180874737.1516870099; mail_psc_fingerprint=968fe8952daea2f8e6ef7990514c74d4; __gads=ID=63e18c04aae884a8:T=1517208778:S=ALNI_MZro7wT4DGlaDmAKLhNRZ0_9JBpPw; UM_distinctid=16140b0bad52f7-0e65b8ef44c77f-4323461-1fa400-16140b0bad6e7a; __f_=1517561993329; Province=0349; City=0351; P_INFO=jakejie@163.com|1519709982|0|other|00&99|shx&1519692896&other#shx&140100#10#0#0|&0|imooc|jakejie@163.com; __utmz=94650624.1519714396.2.2.utmcsr=blog.csdn.net|utmccn=(referral)|utmcmd=referral|utmcct=/sunhuaqiang1/article/details/72821694; vjlast=1513411709.1519883768.11; vinfo_n_f_l_n3=f7ace340dffdbaba.1.3.1513411709138.1519629164475.1519883964657; JSESSIONID-WYYY=6Uk0GtEqOGGI5whotQ2ZDQobgGnQ8gO05vnNRMUaMqJtaI%2BIWjvR9meoH1HoUsdXhKORCJkqAlR5SvNf7xpaT3aZ5D733m6SkVCfDUvZPJeImnaav088RVNFvZ0U%2FTggkiMVvD%2B5%2BoFs%2B7fSoAXZeYSkKbJQKM6YdDbZjSH%5C9b3Z%5CO%5Cr%3A1520391285024; __utma=94650624.1976315094.1512955900.1519714396.1520389485.3; __utmc=94650624; __utmb=94650624.19.10.1520389485",
    "Host": "music.163.com",
    "Pragma": "no-cache",
    "Referer": "http://music.163.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}


def crawl(proxy):
    url = "http://music.163.com/#/song?id=4876404"
    try:
        response = requests.get(url, proxies=proxy, headers=DEFAULT_REQUEST_HEADERS, timeout=10)
        print(response.text)
        return True
    except:
        return False


if __name__ == '__main__':
    while True:
        proxy = requests.get("http://localhost:8000/").json()
        proxyMeta = (list(proxy)[0])
        proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }
        print(proxies)
        if crawl(proxies):
            break
