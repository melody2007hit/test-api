#!/usr/bin/python
# - *- encoding: utf- 8 - *-

import json

class jsonRead(object):
    """
    读取json文件的值
    """

    @staticmethod
    def read(file):
        with open(file, "r") as f:
            json_dict = json.load(f,'utf-8')
        return json_dict