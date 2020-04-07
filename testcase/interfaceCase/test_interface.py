#!/usr/bin/python
# - *- encoding: utf- 8 - *-

import pytest
import json
from util.httpUtil import httpUtil
from util.jsonRead import jsonRead

jsonR = jsonRead()
data = jsonR.read("../interfaceCase/data/interface.json")


@pytest.mark.parametrize("request", data["requests"])
def test_agent_data(request):
    http = httpUtil()
    statusCode,response = http.get(request["url"])
    assert statusCode == request["code"]
    assert json.loads(response) == request["response"]


if __name__ == "__main__":
    pytest.main(["-s", "../interfaceCase/test_interface.py"])
