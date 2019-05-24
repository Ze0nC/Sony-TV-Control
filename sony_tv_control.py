import argparse, requests, pickle
from tv_config import *

try:
    import wakeonlan
except ImportError:
    print("Module wakeonlan not found. Please try to install it with pip.")
    exit()


buttons = {
    "power_off" : "AAAAAQAAAAEAAAAvAw==",
    "volume_down" : "AAAAAQAAAAEAAAATAw==",
    "volume_up" : "AAAAAQAAAAEAAAASAw==",
    "mute_toggle" : "AAAAAQAAAAEAAAAUAw==",
    "channel_down" : "AAAAAQAAAAEAAAARAw==",
    "channel_up" : "AAAAAQAAAAEAAAAQAw==",
    "cursor_down" : "AAAAAQAAAAEAAAB1Aw==",
    "cursor_up" : "AAAAAQAAAAEAAAB0Aw==",
    "cursor_right" : "AAAAAQAAAAEAAAAzAw==",
    "cursor_left" : "AAAAAQAAAAEAAAA0Aw==",
    "cursor_enter" : "AAAAAQAAAAEAAABlAw==",
    "menu_home" : "AAAAAQAAAAEAAABgAw==",
    "exit" : "AAAAAQAAAAEAAABjAw==",
    "return" : "AAAAAgAAAJcAAAAjAw==",
    "display" : "AAAAAQAAAAEAAAA6Aw==",
    "guide" : "AAAAAgAAAKQAAABbAw==",
    "0" : "AAAAAQAAAAEAAAAJAw==",
    "1" : "AAAAAQAAAAEAAAAAAw==",
    "2" : "AAAAAQAAAAEAAAABAw==",
    "3" : "AAAAAQAAAAEAAAACAw==",
    "4" : "AAAAAQAAAAEAAAADAw==",
    "5" : "AAAAAQAAAAEAAAAEAw==",
    "6" : "AAAAAQAAAAEAAAAFAw==",
    "7" : "AAAAAQAAAAEAAAAGAw==",
    "8" : "AAAAAQAAAAEAAAAHAw==",
    "9" : "AAAAAQAAAAEAAAAIAw==",
    "10" : "AAAAAgAAAJcAAAAMAw==",
    "digit_separator" : "AAAAAgAAAJcAAAAdAw==",
    "enter" : "AAAAAQAAAAEAAABlAw/Aw==",
    "menu_popup" : "AAAAAgAAABoAAABhAw+Aw==",
    "function_red" : "AAAAAgAAAJcAAAAlAw==",
    "function_yellow" : "AAAAAgAAAJcAAAAnAw==",
    "function_green" : "AAAAAgAAAJcAAAAmAw==",
    "function_blue" : "AAAAAgAAAJcAAAAkAw==",
    "3d" : "AAAAAgAAAHcAAABNAw==",
    "subtitle" : "AAAAAgAAAJcAAAAoAw==",
    "previous_channel" : "AAAAAQAAAAEAAAA7Aw==",
    "help" : "AAAAAgAAABoAAAB7Aw==",
    "sync_menu" : "AAAAAgAAABoAAABYAw==",
    "options" : "AAAAAgAAAJcAAAA2Aw==",
    "input_toggle" : "AAAAAQAAAAEAAAAlAw==",
    "wide" : "AAAAAgAAAKQAAAA9Aw==",
    "sony_entertainment_network" : "AAAAAgAAABoAAAB9Aw==",
    "pause" : "AAAAAgAAAJcAAAAZAw==",
    "play" : "AAAAAgAAAJcAAAAaAw==",
    "stop" : "AAAAAgAAAJcAAAAYAw==",
    "forward" : "AAAAAgAAAJcAAAAcAw==",
    "reverse" : "AAAAAgAAAJcAAAAbAw==",
    "previous" : "AAAAAgAAAJcAAAA8Aw==",
    "next" : "AAAAAgAAAJcAAAA9Aw=="
}


button_data_template = '<?xml version="1.0" encoding="utf-8"?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:X_SendIRCC xmlns:u="urn:schemas-sony-com:service:IRCC:1"><IRCCCode>%s</IRCCCode></u:X_SendIRCC></s:Body></s:Envelope>'


parser = argparse.ArgumentParser(description="Use Python to control Sony TV. Not fully tested.")
main_action_group = parser.add_mutually_exclusive_group()
main_action_group.add_argument("-i", "--init", help="Init registration on TV.", action="store_true")
main_action_group.add_argument("-w", "--wakeup", help="Turn on TV with Wake On Lan.", action="store_true")
main_action_group.add_argument("-b", "--button", type=str, choices=list(buttons.keys()), help="Press Button")

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
    print(response.cookies)
    with open(cookie_file, "w") as f:
        pickle.dump(response.cookies,f)   

    if response.status_code == 200:
        print("Registration seems to be completed.")


if args.wakeup:
    wakeonlan.send_magic_packet(mac)

if args.button:
    with open(cookie_file, "w") as f:
        cookies = pickle.load(f) 

    url = "http://%s/sony/IRCC" % ip
    #url = "http://httpbin.org/get"
    data = button_data_template % buttons[args.button]
    response = requests.post(url, data=data, cookies=cookies)
    print(response)


