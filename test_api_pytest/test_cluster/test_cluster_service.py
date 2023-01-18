import json
import requests
import pytest
from conftest import BASEURL, Basetest, cluster_ip
from logs.loggers import Loggers

log = Loggers(level='debug', filename="test_cluster_base.log")
rdata = {
  "req_host": "127.0.0.1"
}


# @pytest.mark.cluster()
# def test_gluster_cluster_serveice_status():
#     for i in cluster_ip:
#         url = 'http://%s:8001/gluster/service/status' % i
#         rdata = {}
#         jsonstr = json.dumps(rdata)
#         result = requests.post(url, jsonstr)
#         assert result.status_code == 200
#         print(json.dumps(result.json(), indent=4))
#         log.log_case_info(url, rdata, __name__, result.status_code, result.json())


@pytest.mark.cluster()
def test_gluster_cluster_server_enable():
    for i in cluster_ip:
        url = 'http://%s:8001/gluster/service/enable' % i
        rdata = {}
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))
        log.log_case_info(url, rdata, __name__, result.status_code, result.json())

@pytest.mark.cluster
# @pytest.mark.xfail()
def test_gluster_cluster_enable():
    for i in cluster_ip:
        url = BASEURL + '/cluster/service/enable'
        rdata = {
            "req_host": i
        }
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200, 'There is a bug gluster.info !'
        print(json.dumps(result.json(), indent=4))
        log.log_case_info(url, rdata, __name__, result.status_code, result.json())


@pytest.mark.cluster()
def test_gluster_cluster_append():
    for i in cluster_ip:
        url = BASEURL + '/cluster/node/append'
        rdata = {
          "req_host": "127.0.0.1",
          "node_addr": i
        }
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))


@pytest.mark.cluster()
def test_gluster_cluster_list():
    uri = "/cluster/node/list"
    p = Basetest(str(uri), rdata)
    code, result = p.base_test()
    s = result.json()['data']
    assert s != []
    assert code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.cluster
def test_gluster_time_set():
    URI = '/cluster/time/set'
    rdata = {
      "req_host": "127.0.0.1",
      "timezone": "Asia/Shanghai",
      "ntp_server": [
        "cn.pool.ntp.org"
      ]
    }
    p = Basetest(str(URI), rdata)
    code, result = p.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.cluster
def test_gluster_time_get():
    URI = '/cluster/time/get'
    p = Basetest(str(URI), rdata)
    code, result = p.base_test()
    assert code == 200, f"如果状态码为222集群内时间不一致，set接口未生效；其余状态码为该接口存在问题\n 状态码：{code}"
    print(json.dumps(result.json(), indent=4))



@pytest.mark.cluster()
def test_gluster_cluster_status():
    for i in cluster_ip:
        rdata = {
            "req_host": i
        }
        url = BASEURL + '/cluster/node/status'
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))


@pytest.mark.cluster
@pytest.mark.xfail()
def test_gluster_cluster_info():
    url = BASEURL + '/cluster/op_version/info'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200, 'Current bugs exist !'
    print(json.dumps(result.json(), indent=4))


@pytest.mark.cluster()
def test_gluster_cluster_service_status():
    url = BASEURL + '/cluster/service/status'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.cluster()
def test_gluster_cluster_version():
    url = BASEURL + '/cluster/version/info'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


