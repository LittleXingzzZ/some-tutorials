import requests
import time

url = "https://api.xiaoheihe.cn/task/sign_v3/get_sign_state"

headers = {
    "User-Agent": "xiaoheihe/1.3.240 (iPhone; iOS 16.3.1; Scale/3.00)",
    "Referer": "http://api.maxjia.com/",
    "Cookie": "pkey=MTY4MTA0MjI3NC42NV8zODkwOTk5dWt0bXZsdXNkY2h1d3ZjYw____;hkey=c71160c0b254725a389bce0fa5170caf;x_xhh_tokenid=BTJynmFUFIOsV/VCbNb7mgfqVK9a/jmv3oloVmYr00UTYqfxkOG1gXdsVG/iAF8htqixuUCHb4X28uJ/fiybY/A==",
}

params = {
    "lang": "zh-cn",
    "os_type": "iOS",
    "os_version": "16.3.1",
    "_time": str(int(time.time())),
    "version": "1.3.240",
    "device_id": "1EC67981-9B5F-4CF4-B9A2-EDE8AC02D11A",
    "heybox_id": "3890999",
    "nonce": "4ftIXtOhw99JcQjlw6NYX2dicggGKF01",
    "dw": "428",
    "x_app": "heybox",
    "x_client_type": "mobile",
    "x_os_type": "iOS",
    "hkey": "FJ5K694",
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
