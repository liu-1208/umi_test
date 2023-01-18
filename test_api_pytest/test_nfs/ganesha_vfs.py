import json
import requests
import pytest
from conftest import BASEURL, volname
from conftest import test_ganesha_nfs_list

rdata = {
    "req_host": "127.0.0.1",
    "nfs_mode": "Ganesha"
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
def test_gluster_nfs_update():
    url = BASEURL + '/cluster/nfs/share/update'
    rdata = {
        "req_host": "127.0.0.1",
        "nfs_mode": "GaneshaVfs",
        "vol_name": volname,
        "share_dir": "/ganeshav",
        "client": "*",
        "readonly": "false",
        "export_id":  2
        }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.nfs_service()
def test_gluster_nfs_list():
    url = BASEURL + '/cluster/nfs/share/list'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    a = result.json()["data"]
    nfs_path = a[0]['path']
    print(json.dumps(result.json(), indent=4))
    print(nfs_path)
    assert nfs_path != []

# @pytest.mark.nfs_service()
# def test_gluster_nfs_list():
#     a = test_ganesha_nfs_list()
#     print(a)
#     assert a != []
#
# share_dir = test_ganesha_nfs_list()

del_data = {
  "req_host": "127.0.0.1",
  "nfs_mode": "Ganesha",
  "vol_name": volname,
  "share_dir": "/pytestvol/ganeshav",
  "client": "*"
}

@pytest.mark.nfs_service()
def test_gluster_nfs_delete():
    url = BASEURL + '/cluster/nfs/share/delete'
    # rdata = {
    #   "req_host": "127.0.0.1",
    #   "nfs_mode": "Ganesha",
    #   "vol_name": volname,
    #   "share_dir": "/pytestvol/ganeshav",
    #   "client": "*"
    # }
    jsonstr = json.dumps(del_data)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.nfs_service()
def test_gluster_nfs_update():
    url = BASEURL + '/cluster/nfs/share/update'
    rdata = {
    "req_host": "127.0.0.1",
    "nfs_mode": "GaneshaVfs",
    "vol_name": volname,
    "share_dir": "/ganeshav",
    "client": "*",
    "readonly": "false",
    "export_id":  2
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
    data = result.json()["data"]
    assert data['ganesha_clients'] != ""
    print(json.dumps(result.json(), indent=4))


# @pytest.mark.nfs_service()
# def test_gluster_nfs_list():
#     url = BASEURL + '/cluster/nfs/share/list'
#     jsonstr = json.dumps(rdata)
#     result = requests.post(url, jsonstr)
#     a = result.dict(export_id)
#     print(json.dumps(result.json(), indent=4))
#     assert result.status_code == 200 or 222


# @pytest.mark.nfs_service()
# def test_gluster_nfs_delete():
#     url = BASEURL + '/cluster/nfs/share/delete'
#     jsonstr = json.dumps(del_data)
#     result = requests.post(url, jsonstr)
#     assert result.status_code == 200
#     print(json.dumps(result.json(), indent=4))

