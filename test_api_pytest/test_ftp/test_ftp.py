import json
import requests
import pytest
from conftest import BASEURL, volname

share_dir = '/ftp_share'
share_name = 'ftp_share'

rdata = {
  "req_host": "127.0.0.1"
}

@pytest.mark.ftp_service()
def test_gluster_ftp_status():  # 获取ftp 服务状态
    url = BASEURL + '/cluster/ftp/service/status'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.ftp_service()
def test_gluster_ftp_enable(): #开启 ftp 服务
    url = BASEURL + '/cluster/ftp/service/enable'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.ftp_service()
def test_gluster_ftp_share_update():  #创建 ftp_share
    url = BASEURL + '/cluster/ftp/share/update'
    rdata = {
      "req_host": "127.0.0.1",
      "share_name": share_name,
      "vol_name": volname,
      "share_dir": share_dir,
      "browseable": 'true',
      "rw": 'pytest-01',
      "ro": 'pytest-02',
      "disable_ls": "",
      "disable_modify": "",
      "disable_download": ""
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.ftp_service()
def test_gluster_ftp_share_list(): #获取share_list
    url = BASEURL + '/cluster/ftp/share/list'
    rdata = {
        "req_host": "127.0.0.1",
        "name": share_name
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


