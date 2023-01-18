import json
import requests
import pytest
from conftest import BASEURL, volname

iqn = 'iqn.2022-07.pytest.target-01'
# lun_path = '/.iscsi/lun-tcmu.raw'
lun_name = 'lun-tcmu'
rdata = {
  "req_host": "127.0.0.1",
  "iscsi_mode": "TCMU"
}


@pytest.mark.iscsi()
def test_gluster_tcmu_disable():
    url = BASEURL + '/cluster/iscsi/service/disable'
    rdata = {
        "req_host": "127.0.0.1",
        "iscsi_mode": "TGT"
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.iscsi()
def test_gluster_tcmu_status():
    url = BASEURL + '/cluster/iscsi/service/status'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.iscsi()
def test_gluster_tcmu_init():
    url = BASEURL + '/cluster/iscsi/service/init'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.iscsi()
def test_gluster_tcmu_enable():
    url = BASEURL + '/cluster/iscsi/service/enable'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.iscsi()
def test_gluster_tcmu_target_uptate():
    url = BASEURL + '/cluster/iscsi/target/update'
    rdata = {
      "req_host": "127.0.0.1",
      "iscsi_mode": "TCMU",
      "iqn": iqn,
      "port": 3260
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.iscsi()
def test_gluster_tcmu_target_status():
    url = BASEURL + '/cluster/iscsi/target/status'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.iscsi()
def test_gluster_tcmu_target_info():
    url = BASEURL + '/cluster/iscsi/target/info'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

# @pytest.mark.iscsi()
# def test_gluster_tcmu_target_delete():
#     url = BASEURL + '/cluster/iscsi/target/delete'
#     rdata = {
#       "req_host": "127.0.0.1",
#       "iscsi_mode": "TCMU",
#       "iqn": iqn
#     }
#     jsonstr = json.dumps(rdata)
#     result = requests.post(url, jsonstr)
#     assert result.status_code == 200
#     print(json.dumps(result.json(), indent=4))
#
# @pytest.mark.iscsi()
# def test_gluster_tcmu_target_uptate():
#     url = BASEURL + '/cluster/iscsi/target/update'
#     rdata = {
#       "req_host": "127.0.0.1",
#       "iscsi_mode": "TCMU",
#       "iqn": iqn,
#       "port": 3260
#       # "acls": [
#       #   "*"
#       # ],
#       # "user": "",
#       # "passwd": ""
#     }
#     jsonstr = json.dumps(rdata)
#     result = requests.post(url, jsonstr)
#     assert result.status_code == 200
#     print(json.dumps(result.json(), indent=4))

@pytest.mark.xfail
@pytest.mark.iscsi()
def test_gluster_tcmu_lun_gupdate():
    url = BASEURL + '/cluster/iscsi/lun/glfs_update'
    rdata = {
      "req_host": "127.0.0.1",
      "iscsi_mode": "TCMU",
      "lun_name": lun_name,
      "vol_name": volname,
      "lun_size": "1 GiB",
      "thin": 'false',
      "wcache": 'true'
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200, 'Currently there are bugs !'
    print(json.dumps(result.json(), indent=4))


@pytest.mark.iscsi()
def test_gluster_tcmu_lun_gdelete():
    url = BASEURL + '/cluster/iscsi/lun/glfs_delete'
    rdata = {
      "req_host": "127.0.0.1",
      "iscsi_mode": "TCMU",
      "lun_name": lun_name,
      "vol_name": volname,
      "clean_data": 'false'
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.iscsi()
def test_gluster_tcmu_lun_vupdate():
    url = BASEURL + '/cluster/iscsi/lun/vfs_update'
    rdata = {
      "req_host": "127.0.0.1",
      "iscsi_mode": "TCMU",
      "lun_name": lun_name,
      "vol_name": volname,
      "bstype": "rdwr",
      "lun_size": "1 GiB",
      "thin": 'false',
      "wcache": 'true'
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

# @pytest.mark.iscsi()
# def test_gluster_tcmu_lun_vdelete():
#     url = BASEURL + '/cluster/iscsi/lun/vfs_delete'
#     rdata = {
#       "req_host": "127.0.0.1",
#       "iscsi_mode": "TCMU",
#       "vol_name": volname,
#       "path": lun_path,
#       "clean_data": 'true'
#     }
#     jsonstr = json.dumps(rdata)
#     result = requests.post(url, jsonstr)
#     assert result.status_code == 200
#     print(json.dumps(result.json(), indent=4))
#
# @pytest.mark.iscsi()
# def test_gluster_tcmu_lun_vupdate():
#     url = BASEURL + '/cluster/iscsi/lun/vfs_update'
#     rdata = {
#       "req_host": "127.0.0.1",
#       "iscsi_mode": "TCMU",
#       "vol_name": volname,
#       "path": lun_path,
#       "bstype": "rdwr",
#       "lun_size": "2 GiB",
#       "thin": 'true',
#       "wcache": 'true',
#       "readonly": 'false'
#     }
#     jsonstr = json.dumps(rdata)
#     result = requests.post(url, jsonstr)
#     assert result.status_code == 200
#     print(json.dumps(result.json(), indent=4))


@pytest.mark.iscsi()
def test_gluster_tcmu_lun_info():
    url = BASEURL + '/cluster/iscsi/lun/info'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    res = result.json()['data']
    assert res != ""
    print(json.dumps(result.json(), indent=4))


@pytest.mark.iscsi()
def test_gluster_tcmu_lun_status():
    url = BASEURL + '/cluster/iscsi/lun/status'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.iscsi()
def test_gluster_tcmu_lun_mapset():
    url = BASEURL + '/cluster/iscsi/target/lun_map_set'
    rdata = {
      "req_host": "127.0.0.1",
      "iscsi_mode": "TCMU",
      "iqn": iqn,
      "lun_name_lst": [
        lun_name
      ]
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.iscsi()
def test_gluster_tcmu_lun_mapinfo():
    url = BASEURL + '/cluster/iscsi/target/lun_map_info'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))
