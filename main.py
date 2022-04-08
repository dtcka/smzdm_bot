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
    sb.load_cookie_str('__ckguid=7j35we6kQ8Ee97jKr5q18I2; device_id=21307064331649407055071915f9d66956fc4941f015b2eb3c60f9b99c; homepage_sug=c; r_sort_type=score; __jsluid_s=1f0ff97f58f2e8e4fe5aacb410022b2c; sajssdk_2015_cross_new_user=1; _zdmA.uid=ZDMA.8bQVTWxg3.1649407056.2419200; _zdmA.vid=*; footer_floating_layer=0; ad_date=8; bannerCounter=%5B%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%5D; ad_json_feed=%7B%7D; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1649407058; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1649407058; amvid=302687fd1e03e293aba5c6ce0fa373f0; _zdmA.time=1649407058367.0.https%3A%2F%2Fwww.smzdm.com%2F; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22180085258ca2df-01417cac6cb5f8-1c3a645d-2007040-180085258cbbe5%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22180085258ca2df-01417cac6cb5f8-1c3a645d-2007040-180085258cbbe5%22%7D; sess=AT-n8gje%2FmQXPS9KzAki1Z0ADXnES5g4x8n3qLwZXu5v3QEsLQDgcXNZg7da%2BtkXOakn9A0VfB1uEgFelTVnB6SqQZrWMfuR%2B3YF4RzSNWRyk9gbciZfJaP1WO9; user=qq_s6ois%7C1301978685')
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
