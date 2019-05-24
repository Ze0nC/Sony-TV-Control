import argparse, requests, pickle
from tv_config import *

try:
    import wakeonlan
except ImportError:
    print("Module wakeonlan not found. Please try to install it with pip.")
    exit()


buttons = [
    "1",
    "2",
    "3",
]


button_data_template = '<?xml version="1.0" encoding="utf-8"?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:X_SendIRCC xmlns:u="urn:schemas-sony-com:service:IRCC:1"><IRCCCode>%s</IRCCCode></u:X_SendIRCC></s:Body></s:Envelope>'


parser = argparse.ArgumentParser(description="Use Python to control Sony TV. Not fully tested.")
main_action_group = parser.add_mutually_exclusive_group()
main_action_group.add_argument("-i", "--init", help="Init registration on TV.", action="store_true")
main_action_group.add_argument("-w", "--wakeup", help="Turn on TV with Wake On Lan.", action="store_true")
main_action_group.add_argument("-b", "--button", type=str, choices=buttons, help="Press Button")

args = parser.parse_args()

print(args)

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
    data = '{"method":"actRegister","params":[{"clientid":"%s","nickname":"%s"},[{"function":"WOL","value":"no"}]],"id":%s,"version":"1.0"}' % (client_id, nickname, cid)
    print(url, data)
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Registration seems to be completed.")

if args.wakeup:
    wakeonlan.send_magic_packet(mac)

if args.button:
    url = "http://%s/sony/IRCC" % ip
    #url = "http://httpbin.org/get"
    data = button_data_template % "AAAAAQAAAAEAAAAvAw=="
    response = requests.put(url, data=data)
    print(response)


