import json
import requests
import pytest
from conftest import BASEURL
from logs.loggers import Loggers

rdata = {
    "req_host": "127.0.0.1"
}

log = Loggers(level='debug', filename="test_local_user.log")

@pytest.mark.user()
def test_gluster_group_update():
    for i in range(5):
        rdata = {
          "req_host": "127.0.0.1",
          "group": "group-0%s" % i,
          "gid": '1111%s' % i
        }
        url = BASEURL + '/cluster/user/local/group/update'
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))
        log.log_case_info(url, rdata, __name__, result.status_code, result.json())

@pytest.mark.user()
def test_gluster_user_update():
    for i in range(5):
        rdata = {
          "req_host": "127.0.0.1",
          "user": "pytest-0%s" % i,
          "passwd": "111111",
          "groups": [
            "group-0%s" % i
          ],
          "uid": "1111%s" % i
        }
        url = BASEURL + '/cluster/user/local/user/update'
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))
        log.log_case_info(url, rdata, __name__, result.status_code, result.json())

@pytest.mark.user()
def test_gluster_group_list():
    url = BASEURL + '/cluster/user/local/group/list'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))
    res = len(result.json()['data'])
    assert res > 2
    log.log_case_info(url, rdata, __name__, result.status_code, result.json())

@pytest.mark.user()
def test_gluster_user_list():
    url = BASEURL + '/cluster/user/local/user/list'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))
    res = len(result.json()['data'])
    assert res > 1
    log.log_case_info(url, rdata, __name__, result.status_code, result.json())


