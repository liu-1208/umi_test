import json
import requests
import pytest
from conftest import BASEURL, volname

rdata = {
  "req_host": "127.0.0.1"
}


@pytest.mark.nfs_service
def test_ganesha_vfs_share_uptade():
    url = BASEURL + '/cluster/ganesha/share/vfs/update'
    rdata = {
      "req_host": "127.0.0.1",
      "vol_name": volname,
      "volpath": "ganeshav"
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
      "path": "/export/%s/ganeshav" % volname,
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
    a = result.json()["data"]
    assert a != ""


@pytest.mark.nfs_service
def test_ganesha_client_status():
    url = BASEURL + '/cluster/ganesha/client/status'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    # data = result.json()['detail']
    # for i in data:
    #     # print(i)
    #     print(i['data'])
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))





