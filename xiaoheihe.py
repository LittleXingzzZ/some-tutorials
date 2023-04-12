import requests
import time
import os

url = "https://api.xiaoheihe.cn/task/sign_v3/get_sign_state"

headers = {
    "User-Agent": "xiaoheihe/1.3.240 (iPhone; iOS 16.3.1; Scale/3.00)",
    "Referer": "http://api.maxjia.com/",
    "Cookie": os.environ.get("Box_Cookie"),
}

params = {
    "lang": "zh-cn",
    "os_type": "iOS",
    "os_version": "16.3.1",
    "_time": str(int(time.time())),
    "version": "1.3.240",
    "device_id": os.environ.get("Box_device_id"),
    "heybox_id": os.environ.get("Box_heybox_id"),
    "nonce": os.environ.get("Box_nonce"),
    "dw": "428",
    "x_app": "heybox",
    "x_client_type": "mobile",
    "x_os_type": "iOS",
    "hkey": os.environ.get("Box_hkey"),
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    json_data = response.json()
    if json_data["status"] == "ok":
        print(json_data["msg"])
    else:
        print("签到失败")
else:
    print("请求失败")
