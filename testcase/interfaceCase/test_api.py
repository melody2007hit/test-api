#!/usr/bin/python
# - *- encoding: utf- 8 - *-

import pytest
import json
from util.httpUtil import httpUtil
from util.jsonRead import jsonRead

jsonR = jsonRead()
data = jsonR.read("../interfaceCase/data/test_api.json")

# api contain params
@pytest.mark.parametrize("request", data["requests"])
def test_api(request):
    http =httpUtil();
    code, response =http.get(request["url"],request["param"])
    assert code == request["code"]
    assert "TEMPERATURE" in json.loads(response)
    assert "TIME" in json.loads(response)
    assert json.loads(response)["ACTIVE"] == request["response"]["ACTIVE"]



if __name__ == "__main__":
    pytest.main(["-s", "../interfaceCase/test_api.py"])

