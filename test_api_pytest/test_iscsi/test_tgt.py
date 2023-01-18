import json
import requests
import pytest
from conftest import BASEURL, volname

iqn = 'iqn.2022-07.pytest.target-01'
# lun_path = '/.iscsi/lun-tgt.raw'
lun_name = 'lun-tgt'
rdata = {
  "req_host": "127.0.0.1",
  "iscsi_mode": "TGT"
}


@pytest.mark.iscsi()
def test_gluster_tcmu_disable():
    url = BASEURL + '/cluster/iscsi/service/disable'
    rdata = {
        "req_host": "127.0.0.1",
        "iscsi_mode": "TCMU"
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.iscsi()
def test_gluster_tgt_status():
    url = BASEURL + '/cluster/iscsi/service/status'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.iscsi()
def test_gluster_tgt_init():
    url = BASEURL + '/cluster/iscsi/service/init'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.iscsi()
def test_gluster_tgt_enable():
    url = BASEURL + '/cluster/iscsi/service/enable'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.iscsi()
def test_gluster_tgt_target_uptate():
    url = BASEURL + '/cluster/iscsi/target/update'
    rdata = {
      "req_host": "127.0.0.1",
      "iscsi_mode": "TGT",
      "iqn": iqn,
      "port": 3260
    }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.iscsi()
def test_gluster_tgt_target_status():
    url = BASEURL + '/cluster/iscsi/target/status'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.iscsi()
def test_gluster_tgt_target_info():
    url = BASEURL + '/cluster/iscsi/target/info'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.iscsi()
@pytest.mark.xfail
def test_gluster_tgt_lun_gupdate():
    url = BASEURL + '/cluster/iscsi/lun/glfs_update'
    rdata = {
      "req_host": "127.0.0.1",
      "iscsi_mode": "TGT",
      "lun_name": lun_name,
      "vol_name": volname,
      "lun_size": "1 GiB",
      "thin": true,
      "wcache": true
    }
    # rdata = {
    #   "req_host": "127.0.0.1",
    #   "iscsi_mode": "TGT",
    #   "path": lun_path,
    #   "vol_name": volname,
    #   "host": "localhost",
    #   "lun_size": "2 GiB",
    #   "thin": 'true',
    #   "wcache": 'true'
    # }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200, 'Currently there are bugs !'
    print(json.dumps(result.json(), indent=4))

@pytest.mark.iscsi()
@pytest.mark.xfail
def test_gluster_tgt_lun_gdelete():
    url = BASEURL + '/cluster/iscsi/lun/glfs_delete'
    rdata = {
      "req_host": "127.0.0.1",
      "iscsi_mode": "TGT",
      "lun_name": lun_name,
      "vol_name": volname,
      "clean_data": false
    }
    # rdata = {
    #   "req_host": "127.0.0.1",
    #   "iscsi_mode": "TGT",
    #   "path": lun_path,
    #   "vol_name": volname,
    #   "clean_data": 'false'
    # }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200, 'Currently there are bugs !'
    print(json.dumps(result.json(), indent=4))


@pytest.mark.iscsi()
def test_gluster_tgt_lun_vupdate():
    url = BASEURL + '/cluster/iscsi/lun/vfs_update'
    rdata = {
      "req_host": "127.0.0.1",
      "iscsi_mode": "TGT",
      "lun_name": lun_name,
      "vol_name": volname,
      "bstype": "rdwr",
      "lun_size": "1 GiB",
      "thin": 'true',
      "wcache": 'true'
    }
    # rdata = {
    #   "req_host": "127.0.0.1",
    #   "iscsi_mode": "TGT",
    #   "vol_name": volname,
    #   "path": lun_path,
    #   "bstype": "rdwr",
    #   "lun_size": "2 GiB",
    #   "thin": 'true',
    #   "wcache": 'true',
    #   "readonly": 'false'
    # }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.iscsi()
def test_gluster_tgt_lun_info():
    url = BASEURL + '/cluster/iscsi/lun/info'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
#    res = result.json()['data']
#    assert res != ""
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.iscsi()
def test_gluster_tgt_lun_status():
    url = BASEURL + '/cluster/iscsi/lun/status'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.iscsi()
def test_gluster_tgt_lun_mapset():
    url = BASEURL + '/cluster/iscsi/target/lun_map_set'
    rdata = {
      "req_host": "127.0.0.1",
      "iscsi_mode": "TGT",
      "iqn": iqn,
      "lun_name_lst": [
        lun_name
      ]
    }
    # rdata = {
    #   "req_host": "127.0.0.1",
    #   "iscsi_mode": "TGT",
    #   "iqn": iqn,
    #   "lun_sn_lst": [
    #     "/export/%s%s" % (volname, lun_path)
    #   ]
    # }
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.iscsi()
def test_gluster_tgt_lun_mapinfo():
    url = BASEURL + '/cluster/iscsi/target/lun_map_info'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))

