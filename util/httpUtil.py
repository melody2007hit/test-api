#!/usr/bin/python
# - *- encoding: utf- 8 - *-

import requests
import json


class httpUtil(object):
    def __init__(self):
        pass

    def get(self,url,param=None):
        response = requests.get(url,param)
        print response, response.url
        return response.status_code,response.content

