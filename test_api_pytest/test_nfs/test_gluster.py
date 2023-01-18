import json
import requests
import pytest
from conftest import BASEURL, volname
# import time

rdata = {
    "req_host": "127.0.0.1",
    "nfs_mode": "Gluster"
}
share_dir = "/test_gnfs"


@pytest.mark.nfs_service
def test_gluster_nfs_disable():
    url = BASEURL + '/cluster/nfs/service/disable'
    rdata = {
        "req_host": "127.0.0.1",
        "nfs_mode": "Kernel"
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.nfs_service
def test_ganesha_disable():
    url = BASEURL + '/cluster/ganesha/service/disable'
    rdata = {
        "req_host": "127.0.0.1"
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.nfs_service
def test_gluster_nfs_init():
    url = BASEURL + '/cluster/nfs/service/init'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200, 'Bugs are not adjusted !'
    print(json.dumps(result.json(), indent=4))


@pytest.mark.nfs_service
def test_gluster_nfs_enable():
    url = BASEURL + '/cluster/nfs/service/enable'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.nfs_service
def test_gluster_nfs_status():
    url = BASEURL + '/cluster/nfs/service/status'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200 or 222, 'Bugs are not adjusted !'
    print(json.dumps(result.json(), indent=4))
    res = result.json()['data']
    assert str(res) == 'True'


@pytest.mark.nfs_service
def test_gluster_nfs_update():
    url = BASEURL + '/cluster/nfs/share/update'
    rdata = {
        "req_host": "127.0.0.1",
        "nfs_mode": "Gluster",
        "vol_name": volname,
        "share_dir": share_dir,
        "client": "*",
        "readonly": 'false'
        }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.nfs_service
def test_gluster_nfs_list():
    url = BASEURL + '/cluster/nfs/share/list'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    a = result.json()['data']
    assert result.status_code == 200
    assert a != []
    print(json.dumps(result.json(), indent=4))


# @pytest.mark.nfs_service()
# def test_gluster_nfs_client_status():
#     url = BASEURL + '/cluster/nfs/client/status'
#     rdata = {
#         "req_host": "127.0.0.1"
#     }
#     jsonstr = json.dumps(rdata)
#     result = requests.post(url, jsonstr)
#     assert result.status_code == 200
#     print(json.dumps(result.json(), indent=4))
