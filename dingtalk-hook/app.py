#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import json
import requests

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def send():
    if request.method == 'POST':
        post_data = request.get_data()
        post_data = format_message(bytes2json(post_data))
        print(post_data)
        send_alert(post_data)
        return 'success'
    else:
        return 'weclome to use prometheus alertmanager dingtalk webhook server!'


def bytes2json(data_bytes):
    data = data_bytes.decode('utf8').replace("'", '"')
    return json.loads(data)


def format_message(post_data):
    EXCLUDE_LIST = ['prometheus', 'endpoint']
    message_list = []
    message_list.append('### 报警类型：{}'.format(post_data['status']))
    # message_list.append('**alertname:**{}'.format(post_data['alerts'][0]['labels']['alertname']))
    message_list.append('> **startsAt: **{}'.format(post_data['alerts'][0]['startsAt']))
    message_list.append('#### Labels:')
    for label in post_data['alerts'][0]['labels'].keys():
        if label in EXCLUDE_LIST:
            continue
        else:
            message_list.append("> **{}: **{}".format(label, post_data['alerts'][0]['labels'][label]))

    message_list.append('#### Annotations:')
    for annotation in post_data['alerts'][0]['annotations'].keys():
        message_list.append('> **{}: **{}'.format(annotation, post_data['alerts'][0]['annotations'][annotation]))
    message = (" \n\n ".join(message_list))
    title = post_data['alerts'][0]['labels']['alertname']
    data = {"title": title, "message": message}
    return data


def send_alert(data):
    token = os.getenv('ROBOT_TOKEN')
    if not token:
        print('you must set ROBOT_TOKEN env')
        return
    url = 'https://oapi.dingtalk.com/robot/send?access_token=%s' % token
    send_data = {
        "msgtype": "markdown",
        "markdown": {
            "title": data['title'],
            "text": "{}".format(data['message'])
        }
    }
    req = requests.post(url, json=send_data)
    result = req.json()
    print(result)
    if result['errcode'] != 0:
        print('notify dingtalk error: %s' % result['errcode'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
