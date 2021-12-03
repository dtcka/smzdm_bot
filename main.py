"""
什么值得买自动签到脚本
使用github actions 定时执行
@author : stark
"""
import requests,os
from sys import argv

import config
from utils.serverchan_push import push_to_wechat

class SMZDM_Bot(object):
    def __init__(self):
        self.session = requests.Session()
        # 添加 headers
        self.session.headers = config.DEFAULT_HEADERS

    def __json_check(self, msg):
        """
        对请求 盖乐世社区 返回的数据进行进行检查
        1.判断是否 json 形式
        """
        try:
            result = msg.json()
            print(result)
            return True
        except Exception as e:
            print(f'Error : {e}')            
            return False

    def load_cookie_str(self, cookies):
        """
        起一个什么值得买的，带cookie的session
        cookie 为浏览器复制来的字符串
        :param cookie: 登录过的社区网站 cookie
        """
        self.session.headers['Cookie'] = cookies    

    def checkin(self):
        """
        签到函数1
        """
        url = 'https://zhiyou.smzdm.com/user/checkin/jsonp_checkin'
        msg = self.session.get(url)
        if self.__json_check(msg):
            return msg.json()
        return msg.content




if __name__ == '__main__':
    sb = SMZDM_Bot()
    sb.load_cookie_str('__ckguid=TGI4pSQIjLHEcVlilWftCY2; __jsluid_s=71364b4795307492ec52ba56cf1e8599; device_id=10182188081634371457765640e35e961140b915105ddbed3ef8a94b50; _ga=GA1.2.136267252.1634371461; _ga_09SRZM2FDD=GS1.1.1634371458.1.1.1634372195.0; homepage_sug=c; r_sort_type=score; __gads=ID=abfc6f7d52fd473b:T=1634371460:S=ALNI_MYDDbBKCVFZpkmq9Q0aDA5_qXTW7Q; sess=AT-n8gje%2FmQXPS8668PtTfoeU7%2F4WDw%2BzsucL4XHGlFrgURChoIRS4jDRwNGHLhzL9i0bgID5vqGQUVdD75pXedU3b8tzk2%2FhZvb5GY4TEz6HBhno7jcDPrVvuG; user=qq_s6ois%7C1301978685; shequ_pc_sug=b; smzdm_id=1301978685; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1638547801; footer_floating_layer=0; ad_date=4; ad_json_feed=%7B%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217c882153932e6-06d35cd11a20f6-123b6650-1296000-17c882153941699%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.smzdm.com%2F%22%7D%2C%22%24device_id%22%3A%2217c882153932e6-06d35cd11a20f6-123b6650-1296000-17c882153941699%22%7D; _zdmA.uid=ZDMA.eRtiwtf6y.1638548993.2419200; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1638548993; bannerCounter=%5B%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%5D; amvid=3decde4c6b26e761b842e43d45a0551d; _zdmA.time=1638550935078.0.https%3A%2F%2Fwww.smzdm.com%2F')
    res = sb.checkin()
    print(res)
    SERVERCHAN_SECRETKEY = os.environ["SERVERCHAN_SECRETKEY"]
    print('sc_key: ', SERVERCHAN_SECRETKEY)
    if isinstance(SERVERCHAN_SECRETKEY,str) and len(SERVERCHAN_SECRETKEY)>0:
        print('检测到 SCKEY， 准备推送')
        push_to_wechat(text = '什么值得买每日签到',
                        desp = str(res),
                        secretKey = SERVERCHAN_SECRETKEY)
    print('代码完毕')
