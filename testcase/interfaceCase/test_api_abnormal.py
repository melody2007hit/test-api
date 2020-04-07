#!/usr/bin/python
# - *- encoding: utf- 8 - *-

import pytest
import json
from util.httpUtil import httpUtil
from util.jsonRead import jsonRead
from HTMLTestRunner import HTMLTestRunner

jsonR = jsonRead()
data = jsonR.read("../interfaceCase/data/test_api_abnormal.json")

@pytest.mark.parametrize("request", data["requests"])
def test_api(request):
    http =httpUtil();
    code, response =http.get(request["url"],request["param"])
    assert code == request["code"]



if __name__ == "__main__":
    pytest.main(["-s", "../interfaceCase/test_api.py"])

