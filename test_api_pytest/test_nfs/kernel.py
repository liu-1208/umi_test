import json
import requests
import pytest
from conftest import BASEURL


rdata = {
    "req_host": "127.0.0.1",
    "nfs_mode": "Kernel"
}

@pytest.mark.nfs_service()
def test_gluster_nfs_disable():
    url = BASEURL + '/cluster/nfs/service/disable'
    rdata = rdata = {
        "req_host": "127.0.0.1",
        "nfs_mode": "Ganesha"
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.nfs_service()
def test_gluster_nfs_disable():
    url = BASEURL + '/cluster/nfs/service/disable'
    rdata = rdata = {
        "req_host": "127.0.0.1",
        "nfs_mode": "Gluster"
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.nfs_service()
def test_gluster_nfs_enable():
    url = BASEURL + '/cluster/nfs/service/enable'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.nfs_service()
def test_gluster_nfs_disable():
    url = BASEURL + '/cluster/nfs/service/disable'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.nfs_service()
def test_gluster_nfs_enable():
    url = BASEURL + '/cluster/nfs/service/enable'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.nfs_service()
def test_gluster_nfs_init():
    url = BASEURL + '/cluster/nfs/service/init'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.nfs_service()
def test_gluster_nfs_status():
    url = BASEURL + '/cluster/nfs/service/status'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.nfs_service()
def test_gluster_nfs_list():
    url = BASEURL + '/cluster/nfs/share/list'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.nfs_service()
def test_gluster_nfs_update():
    url = BASEURL + '/cluster/nfs/share/list'
    rdata = {
    "req_host": "127.0.0.1",
    "nfs_mode": "Kernel",
    "vol_name": "pytestvol",
    "share_dir": "/test_nfs_k",
    "client": "*",
    "readonly": "false"
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.nfs_service()
def test_gluster_nfs_client_status():
    url = BASEURL + '/cluster/nfs/client/status'
    rdata = {
        "req_host": "127.0.0.1"
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.nfs_service()
def test_gluster_nfs_list():
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))
