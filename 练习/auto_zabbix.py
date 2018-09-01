#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from urllib import request
import requests
import json


# zabbix
class ZabbixAPI:
    def __init__(self, username, password, url):
        headers = {'Content-Type': 'application/json-rpc'}
        self.username = username
        self.password = password
        self.headers = headers
        self.url = url
        data = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": username,
                "password": password
            },
            "id": 1
        }
        r = requests.post(self.url, headers=headers, data=json.dumps(data)).text  # 取得令牌
        token = json.loads(r)['result']
        self.token = token
        # print(self.token)

    def list_hosts(self,fil_name='default'):
        fil_name = fil_name.strip()
        if fil_name =='default':
            data = {
                "jsonrpc": "2.0",
                "method": "host.get",
                "params": {
                    "output": "extend",
                },
                "auth": self.token,
                "id": 1
            }
        else:
            data = {
                "jsonrpc": "2.0",
                "method": "host.get",
                "params": {
                    "output": "extend",
                    "filter": {
                        "host": [fil_name
                        ]
                    }
                },
                "auth": self.token,
                "id": 1
            }
        r = requests.post(self.url, headers=self.headers, data=json.dumps(data)).text
        get_hosts = json.loads(r)
        for index in range(len(get_hosts['result'])):
            for key,val in get_hosts['result'][index].items():
                if key in 'hostid,host,status,name,templateid':
                    print('%s:%s'%(key,val))
            print()

    def list_hostgroups(self,fil_name='default'):
        fil_name = fil_name.strip()
        if fil_name == 'default':
            data = {
                "jsonrpc": "2.0",
                "method": "hostgroup.get",
                "params": {
                    "output": "extend",
                },
                "auth": self.token,
                "id": 1
            }
        else:
            data ={
                "jsonrpc": "2.0",
                "method": "hostgroup.get",
                "params": {
                    "output": "extend",
                    "filter": {
                        "name": [fil_name]
                    }
                    },
                    "auth": self.token,
                    "id": 1
                }
        r = requests.post(self.url ,headers=self.headers,data=json.dumps(data)).text
        get_host_gou = json.loads(r)
        # print(get_host_gou)
        for index in range(len(get_host_gou['result'])):
            for key ,val in get_host_gou['result'][index].items():
                if key in 'groupid,name':
                    print('%s:%s'%(key,val))
            print()

    def list_templates(self,fil_name='default'):
        fil_name = fil_name.strip()
        if fil_name == 'default':
            data = {
                "jsonrpc": "2.0",
                "method": "template.get",
                "params": {
                    "output": "extend",
                },
                "auth": self.token,
                "id": 1
            }
        else:
            data = {
                "jsonrpc": "2.0",
                "method": "template.get",
                "params": {
                    "output": "extend",
                    "filter": {
                        "host": [fil_name]
                    }
                },
                "auth": self.token,
                "id": 1
            }
        r = requests.post(self.url,headers=self.headers,data=json.dumps(data)).text
        get_template = json.loads(r)
        for index in range(len(get_template['result'])):
            for key ,val in get_template['result'][index].items():
                if  key in 'templateid,host':
                    print('%s:%s'%(key , val))
            print()


    def create_host(self, hostname, group_id, template_id,agent_ip):
        data = {
            "jsonrpc": "2.0",
            "method": "host.create",
            "params": {
                "host": hostname,
                "interfaces": [
                    {
                        "type": 1,
                        "main": 1,
                        "useip": 1,
                        "ip": agent_ip,
                        "dns": "",
                        "port": "10050"
                    }
                ],
                "groups": [
                    {
                        "groupid": group_id
                    }
                ],
                "templates": [
                    {
                        "templateid": template_id
                    }
                ],
                "inventory_mode": 0,
            },
            "auth": self.token,
            "id": 1
        }
        requests.post(self.url,headers=self.headers,data=json.dumps(data))



if __name__ == '__main__':
    zabbix_ip = '127.0.0.1'
    z_api_url = 'http://' + zabbix_ip + '/zabbix/api_jsonrpc.php'
    zabbix = ZabbixAPI('admin', 'zabbix' ,z_api_url)
    zabbix.list_hosts('test')
    # zabbix.list_hostgroups()
    # zabbix.list_templates()
    # zabbix.create_host('mylinux', '2', '10001','192.168.122.248')
