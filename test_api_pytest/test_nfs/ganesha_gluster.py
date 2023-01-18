import json
import requests
import pytest
from conftest import BASEURL, volname
# from conftest import test_ganesha_nfs_list

rdata = {
    "req_host": "127.0.0.1",
    "nfs_mode": "Ganesha"
}
# share_dir = test_ganesha_nfs_list()

@pytest.mark.nfs_service()
def test_gluster_nfs_disable():
    url = BASEURL + '/cluster/nfs/service/disable'
    rdata = rdata = {
        "req_host": "127.0.0.1",
        "nfs_mode": "Kernel"
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
def test_gluster_nfs_update():
    url = BASEURL + '/cluster/nfs/share/update'
    rdata = {
        "req_host": "127.0.0.1",
        "nfs_mode": "GaneshaGluster",
        "vol_name": "pytestvol",
        "share_dir": "/ganeshag",
        "client": "*",
        "readonly": 'false',
        "export_id": 1
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
#     return nfs_path

# @pytest.mark.nfs_service()
# def test_gluster_nfs_list():
#     a = test_ganesha_nfs_list()
#     print(a)
#     assert a != []


# del_data = {
#   "req_host": "127.0.0.1",
#   "nfs_mode": "Ganesha",
#   "vol_name": volname,
#   "share_dir": '/export/{0}/ganeshag'.format(volname),
#   "client": "*"
# }
#
# @pytest.mark.nfs_service()
# def test_gluster_nfs_delete():
#     url = BASEURL + '/cluster/nfs/share/delete'
#     jsonstr = json.dumps(del_data)
#     result = requests.post(url, jsonstr)
#     assert result.status_code == 200
#     print(json.dumps(result.json(), indent=4))
#
# @pytest.mark.nfs_service()
# def test_gluster_nfs_update():
#     url = BASEURL + '/cluster/nfs/share/update'
#     rdata = {
#         "req_host": "127.0.0.1",
#         "nfs_mode": "GaneshaGluster",
#         "vol_name": volname,
#         "share_dir": "/ganeshag",
#         "client": "*",
#         "readonly": 'false',
#         "export_id": 1
#         }
#     jsonstr = json.dumps(rdata)
#     result = requests.post(url, jsonstr)
#     assert result.status_code == 200
#     print(json.dumps(result.json(), indent=4))

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


@pytest.mark.nfs_service()
def test_gluster_nfs_list():
    url = BASEURL + '/cluster/nfs/share/list'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))
