import json
import requests
import pytest
from conftest import BASEURL, volname, cluster_host_list, uuid
from logs.loggers import Loggers

log = Loggers(level='debug', filename="test_vol_base.log")
# volname = "testvol"
rdata = {
    "req_host": "127.0.0.1",
    "vol_name": volname
}


@pytest.mark.volbase()
def test_gluster_vol_create():
    url = BASEURL + '/cluster/volume/create'
    rdata = {
        "req_host": "127.0.0.1",
        "vol_name": volname,
        "remote_mnts": [
            "%s:/data/%s" % (cluster_host_list[0], uuid),
            "%s:/data/%s" % (cluster_host_list[1], uuid)
        ],
        "vol_type": "Repalica",
        "vol_pattern": "2",
        "rdma": "false"
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))
    log.log_case_info(url, rdata, __name__, result.status_code, result.json())


@pytest.mark.volbase()
def test_gluster_vol_start():
    url = BASEURL + '/cluster/volume/start'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))
    log.log_case_info(url, rdata, __name__, result.status_code, result.json())


@pytest.mark.volbase()
def test_gluster_vol_info():
    url = BASEURL + '/cluster/volume/info'
    rdata = {
        "req_host": "127.0.0.1",
        "vol_name": "all"
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))
    log.log_case_info(url, rdata, __name__, result.status_code, result.json())


@pytest.mark.volbase()
def test_gluster_vol_status():
    url = BASEURL + '/cluster/volume/status'
    rdata = {
        "req_host": "127.0.0.1",
        "vol_name": "all"
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))
    log.log_case_info(url, rdata, __name__, result.status_code, result.json())


if __name__ == "__main__":
    # 常规运行
    pytest.main(["-s", "test_vol_config/test_*.py", "--alluredir", "./report"])
    # 并行运行
    pytest.main(["-s", "-v", "test_vol_config", "-n=5"])
    # 并发运行
    pytest.main(["-s", "-v", "test_vol_config", "--workers=1", "--tests-per-worker=5"])