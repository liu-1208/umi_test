import json
import requests
import pytest
from conftest import BASEURL, volname

share_dir = '/cifs_share'
share_name = 'cifs_share'
rdata = {
  "req_host": "127.0.0.1"
}


@pytest.mark.cifs_service()
def test_gluster_cifs_status():
    url = BASEURL + '/cluster/cifs/service/status'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.cifs_service()
def test_gluster_cifs_init():
    url = BASEURL + '/cluster/cifs/service/init'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.cifs_service()
def test_gluster_cifs_enable():
    url = BASEURL + '/cluster/cifs/service/enable'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


# @pytest.mark.cifs_service()
# def test_gluster_cifs_disable():
#     url = BASEURL + '/cluster/cifs/service/disable'
#     jsonstr = json.dumps(rdata)
#     result = requests.post(url, jsonstr)
#     assert result.status_code == 200
#     print(json.dumps(result.json(), indent=4))
#
#
# @pytest.mark.cifs_service()
# def test_gluster_cifs_enable():
#     url = BASEURL + '/cluster/cifs/service/enable'
#     jsonstr = json.dumps(rdata)
#     result = requests.post(url, jsonstr)
#     assert result.status_code == 200
#     print(json.dumps(result.json(), indent=4))


@pytest.mark.cifs_service()
def test_gluster_cifs_user_update():
    for i in range(3):
        url = BASEURL + '/cluster/cifs/user/update'
        rdata = {
            "req_host": "127.0.0.1",
            "user": "pytest-0{0}".format(i),
            "passwd": "111111"
        }
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))


@pytest.mark.cifs_service()
def test_gluster_cifs_user_list():
    url = BASEURL + '/cluster/cifs/user/list'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))
    a = result.json()['data']
    assert a != [], 'Check whether the SMB user is created successfully !'


@pytest.mark.cifs_service()
def test_gluster_cifs_update():
    url = BASEURL + '/cluster/cifs/share/update'
    rdata = {
        "req_host": "127.0.0.1",
        "share_name": share_name,
        "vol_name": volname,
        "share_dir": share_dir,
        "glfs_api": 'true',
        "acls": 'true',
        "allow_hosts": [
            "*"
        ],
        "deny_hosts": [
        ],
        "guest_ok": 'true',
        "admin_users": [
            "pytest-01"
        ],
        "read_list": [
            "pytest-00"
        ],
        "write_list": [
            "pytest-01"
        ],
        "create_mode": "0644",
        "directory_mode": "0755"
        }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.cifs_service()
def test_gluster_cifs_share_list():
    url = BASEURL + '/cluster/cifs/share/list'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))
    redata = result.json()['data']
    assert redata != []


@pytest.mark.cifs_service()
def test_gluster_cifs_client_status():
    url = BASEURL + '/cluster/cifs/client/status'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))
