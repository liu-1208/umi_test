import json
import requests
import pytest
from conftest import BASEURL, volname

# volname = "testvol"
rdata = {
  "req_host": "127.0.0.1"
}


@pytest.mark.nfs_service()
def test_gluster_knfs_disable():
    for i in ["Gluster", "Kernel"]:
        url = BASEURL + '/cluster/nfs/service/disable'
        rdata = {
            "req_host": "127.0.0.1",
            "nfs_mode": i
        }
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))


@pytest.mark.nfs_service
def test_ganesha_enable():
    url = BASEURL + '/cluster/ganesha/service/enable'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

# @pytest.mark.nfs_service
# @pytest.mark.dependency(depends=["test_gluster_ganesha_enable"])
# def test_gluster_ganesha_status():
#     url = BASEURL + '/cluster/ganesha/service/status'
#     jsonstr = json.dumps(rdata)
#     result = requests.post(url, jsonstr)
#     a = result.json()["data"]
#     print(json.dumps(result.json(), indent=4))
#     assert str(a) == "True"


@pytest.mark.nfs_service
def test_ganesha_init():
    url = BASEURL + '/cluster/ganesha/service/init'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.nfs_service
def test_ganesha_share_uptade():
    url = BASEURL + '/cluster/ganesha/share/gluster/update'
    rdata = {
      "req_host": "127.0.0.1",
      "vol_name": volname,
      "volpath": "/ganeshag"
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.nfs_service
def test_ganesha_client_uptade():
    url = BASEURL + '/cluster/ganesha/share/client/update'
    rdata = {
      "req_host": "127.0.0.1",
      "path": "/%s/ganeshag" % volname,
      "clients": "*",
      "access_type": "RW",
      "protocols": "3,4",
      "squash": "No_root_squash",
      "sectype": "sys",
      "transports": "TCP"
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.nfs_service
def test_ganesha_share_list():
    url = BASEURL + '/cluster/ganesha/share/list'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    a = result.json()["data"]
    assert a != []
    # assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.nfs_service
@pytest.mark.xfail(reason="If the client is empty, it is normal !")
def test_ganesha_client_status():
    url = BASEURL + '/cluster/ganesha/client/status'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    data = result.json()['data']['127.0.0.1']
    # for i in data:
    #     # print(i)
    #     print(i['data'])
    #     a = i['data']
    assert data != []
    print(json.dumps(result.json(), indent=4))
