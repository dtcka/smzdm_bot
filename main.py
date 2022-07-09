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
    sb.load_cookie_str('__ckguid=Hwt7csX961ckOa2VWog8rt7; device_id=21307064331657333546783542d1895735bbde22be896a153417aeb33f; homepage_sug=d; r_sort_type=score; __jsluid_s=45ba4de5baec86fe1b9b2a4c1f15b477; footer_floating_layer=0; ad_date=9; bannerCounter=%5B%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%5D; ad_json_feed=%7B%7D; _zdmA.vid=*; sajssdk_2015_cross_new_user=1; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1657333549; _zdmA.time=1657333570453.21116.https%3A%2F%2Fwww.smzdm.com%2F; _zdmA.uid=ZDMA.McxgNiKVD.1657333571.2419200; amvid=06be51a959c09950071e48a7ae4a171e; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1657333572; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22181e0c706865a6-0ac67ce6d62773-1c525635-1930176-181e0c706871c38%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22181e0c706865a6-0ac67ce6d62773-1c525635-1930176-181e0c706871c38%22%7D; sess=AT-n8gje%2FmQXPS%2BvcnqVXUInfS3%2FMKoR1ii0AL5%2FFqkl4wxOaChfaYqfnkXt4eG5lGsUxJqIg17nHjeUHHJBLX3%2BRh0U0JutfALV7JDvCYkpG6TAfEHGn%2FAx7Mt; user=qq_s6ois%7C1301978685')
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
