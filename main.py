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
    sb.load_cookie_str('__ckguid=B1c177YgXJeeQ5yFib8fQ5; __jsluid_s=9459b8bf6677327ebbef4e07050de53a; device_id=351440579516617885737893887bd19d9df50747020c9f9a8b7b6078e5; homepage_sug=d; r_sort_type=score; _zdmA.uid=ZDMA.RTBv6P1Iv.1663580679.2419200; _zdmA.vid=*; footer_floating_layer=0; ad_date=19; bannerCounter=%5B%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%5D; ad_json_feed=%7B%7D; amvid=d1793fdef2242cf7ed54266bbe1d77a4; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1661788573,1663580683; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1663580683; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22182ea51447ee8e-0d9e21e9dfa6dc-1b525635-1930176-182ea51447f19e0%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22182ea51447ee8e-0d9e21e9dfa6dc-1b525635-1930176-182ea51447f19e0%22%7D; _zdmA.time=1663580685872.0.https%3A%2F%2Fwww.smzdm.com%2F; sess=BA-hyN2HzRcOkMwO6tnZXvt%2BYQnQ%2Fk78yLVJkhEXgGDqCmeddTR9Lg8GwdnelOWqQtpCoomQSAr8CTRBUG3HimgO%2FgXtBfGshU%2BKfxtkHIe3sMXn06yf07gs8ux; user=qq_s6ois%7C1301978685')
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
