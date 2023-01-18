import json
import requests
import pytest

BASEURL = 'http://172.26.172.12:8000'
rdata = {
    "req_host": "127.0.0.1",
    "nfs_mode": "Gluster"
}

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
    "nfs_mode": "Gluster",
    "vol_name": "pytestvol",
    "share_dir": "/test_nfs_g",
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
