#!/usr/bin/python
# - *- encoding: utf- 8 - *-

import pytest
from util.httpUtil import httpUtil
from util.jsonRead import jsonRead


jsonR = jsonRead()
data = jsonR.read("../interfaceCase/data/test_api_abnormal.json")

  # param is empty string/wrong value/different type value
@pytest.mark.parametrize("request", data["requests"])
def test_api(request):
    http =httpUtil();
    code, response =http.get(request["url"],request["param"])
    assert code == request["code"]



if __name__ == "__main__":
    pytest.main(["-s", "../interfaceCase/test_api.py"])

