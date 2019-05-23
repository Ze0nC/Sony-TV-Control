from tv_config import *

import argparse
import requests, pickle

parser = argparse.ArgumentParser(description="Use Python to control Sony TV. Not fully tested.")

#parser.add_argument("config", help="Config ")
parser.add_argument("-i", "--init", help="Init registration on TV.", action="store_true")

args = parser.parse_args()

if args.init:
    url = "http://%s/sony/accessControl" % ip
    #url = "http://httpbin.org/get"
    data = {
        "method": "actRegister", 
        "params": [
            {"clientid":client_id,"nickname":nickname},
            [{"function":"WOL","value":"no"}]
        ],
        "id":cid,
        "version":"1.0"
    }
    #data = '{"method":"actRegister","params":[{"clientid":"%s","nickname":"%s"},[{"function":"WOL","value":"no"}]],"id":%s,"version":"1.0"}' % (client_id, nickname, cid)
    
    print(url, data)
    response = requests.post(url, data=data)
    print(response)
    #curl -d '{"method":"actRegister","params":[{"clientid":"raspberrypi2","nickname":"raspberrypi2"},[{"function":"WOL","value":"no"}]],"id":1234562,"version":"1.0"}' -c cookie.txt http://192.168.10.4/sony/accessControl