# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

import json
import requests
from common.mymako import render_mako_context

url="http://192.168.1.185/zabbix/api_jsonrpc.php"
header = {"Content-Type": "application/json"}

def home(request):
    """
    首页
    """
    host_data = gethost()
    host_num = host_data[0]
    enable_host = host_data[1]
    disable_host = host_data[2]

    return render_mako_context(request, '/index.html',{'total_host':host_num,
                                                       'enable_host':enable_host,
                                                       'disable_host':disable_host})

def auth_login():
    """
    zabbix auth
    :return: auth result
    """
    data = json.dumps(
    {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
        "user": "zengcunkai",
        "password": "Zck199162718@"
    },
    "id": 0
    })

    auth = requests.post(url,headers=header,data=data)
    auth_code = json.loads(auth.text)["result"]
    return auth_code

def gethost():
    return_data = []
    auth = auth_login()
    data = json.dumps(
        {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": [
                    "hostid",
                    "host",
                    "status",
                ],
                "selectInterfaces": [
                    "interfaceid",
                    "ip"
                ]
            },
            "auth": auth,
            "id": 2
        })

    result = requests.get(url, headers=header, data=data)
    host = json.loads(result.text)['result']
    num = 0
    for i in host:
        if i["status"] == "0":
            num += 1
    enable_host = num
    disable_host = len(host) - num

    return_data.extend([len(host), enable_host, disable_host])

    return return_data

