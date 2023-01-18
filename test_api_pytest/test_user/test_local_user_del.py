import json
import requests
import pytest
from conftest import BASEURL
from logs.loggers import Loggers

log = Loggers(level='debug', filename="test_local_user.log")
@pytest.mark.delete()
@pytest.mark.user()
def test_gluster_user_delete():
    for i in range(5):
        rdata = {
          "req_host": "127.0.0.1",
          "user": "pytest-0%s" % i
        }
        url = BASEURL + '/cluster/user/local/user/delete'
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))
        log.log_case_info(url, rdata, __name__, result.status_code, result.json())


@pytest.mark.delete()
@pytest.mark.user()
def test_gluster_group_delete():
    for i in range(5):
        rdata = {
          "req_host": "127.0.0.1",
          "group": "group-0%s".format(i)
        }
        url = BASEURL + '/cluster/user/local/group/delete'
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))
        log.log_case_info(url, rdata, __name__, result.status_code, result.json())

@pytest.mark.user()
def test_gluster_user_list():
    url = BASEURL + '/cluster/user/local/user/list'
    rdata = {
        "req_host": "127.0.0.1"
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    log.log_case_info(url, rdata, __name__, result.status_code, result.json())
    print(json.dumps(result.json(), indent=4))
    res = len(result.json()['data'])
    assert res == 0

