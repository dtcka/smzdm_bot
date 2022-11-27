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
    sb.load_cookie_str('__ckguid=TNk2n73P7JOfGWu2eJOfLN3; device_id=213070643316695320465371054ae4a5cc5853d6d05e458cab7364c003; homepage_sug=d; r_sort_type=score; sajssdk_2015_cross_new_user=1; _zdmA.uid=ZDMA._VngNPELW.1669532048.2419200; _zdmA.vid=*; footer_floating_layer=0; ad_date=26; bannerCounter=%5B%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%5D; ad_json_feed=%7B%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22184b7dd58f753d-055a9538fde7fe-18525635-1930176-184b7dd58f8155e%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22184b7dd58f753d-055a9538fde7fe-18525635-1930176-184b7dd58f8155e%22%7D; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1669532053; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1669532053; amvid=0abb98d39bf9df8131489088acc0ecb5; _zdmA.time=1669532062629.0.https%3A%2F%2Fwww.smzdm.com%2F; sess=BA-hyN2HzRcOkMxBK2JWdWMsxUb7o9zxTsS12Pzqp3vzrVGmejvEOQC3wRIz8VXfoszuhEnoNRdXVWFYC2CzZHS9%2B8BZE2IERTQtxI5%2BG8Ba2KvaYGpFOb%2F6W8q; user=qq_s6ois%7C1301978685')
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
