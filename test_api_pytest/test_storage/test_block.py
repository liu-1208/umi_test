import json
import requests
import pytest
from conftest import BASEURL, cluster_ip, dev_path, uuid
from logs.loggers import Loggers

rdata = {
  "req_host": "127.0.0.1"
}
# dev_path = "/dev/sdf"
# uuid = "12345678-1234-1234-1234-12345678901g"
log = Loggers(level='debug', filename="test_storage.log")


@pytest.mark.xfail()
@pytest.mark.delete()
@pytest.mark.storage()
def test_gluster_brick_disable():
    for i in cluster_ip:
        url = BASEURL + '/node/storage/block_device/disable'
        rdata = {
            "req_host": i,
            "dev_path": dev_path
        }
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))
        log.log_case_info(url, rdata, __name__, result.status_code, result.json())


@pytest.mark.xfail()
@pytest.mark.delete()
@pytest.mark.storage()
def test_gluster_brick_wipe():
    for i in cluster_ip:
        url = BASEURL + '/node/storage/block_device/wipe'
        rdata = {
            "req_host": i,
            "dev_path": dev_path
        }
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))
        log.log_case_info(url, rdata, __name__, result.status_code, result.json())


@pytest.mark.storage()
def test_gluster_brick_status():
    url = BASEURL + '/node/storage/block_device/status'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))
    log.log_case_info(url, rdata, __name__, result.status_code, result.json())


@pytest.mark.storage()
def test_gluster_brick_init():
    for i in cluster_ip:
        rdata = {
            "req_host": i,
            "dev_path": dev_path,
            "fs_uuid": uuid
        }
        url = BASEURL + '/node/storage/block_device/init'
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))
        log.log_case_info(url, rdata, __name__, result.status_code, result.json())


@pytest.mark.storage()
def test_gluster_brick_enable():
    for i in cluster_ip:
        url = BASEURL + '/node/storage/block_device/enable'
        rdata = {
            "req_host": i,
            "dev_path": dev_path
            }
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))
        log.log_case_info(url, rdata, __name__, result.status_code, result.json())


@pytest.mark.storage()
def test_gluster_mount_status():
    url = BASEURL + '/node/storage/file_system/status'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))
    log.log_case_info(url, rdata, __name__, result.status_code, result.json())


@pytest.mark.storage()
def test_gluster_brick_useage():
    url = BASEURL + '/node/storage/file_system/usage'
    jsonstr = json.dumps(rdata)
    result = requests.post(url, jsonstr)
    assert result.status_code == 200
    print(json.dumps(result.json(), indent=4))
    log.log_case_info(url, rdata, __name__, result.status_code, result.json())

# def test_gluster_brick_wipe():
#     for i in cluster_host_list:
#         url = BASEURL + '/node/storage/block_device/wipe'
#         rdata = {
#         "req_host": i,
#         "dev_path": "/dev/sdb"
#         }
#         jsonstr = json.dumps(rdata)
#         result = requests.post(url, jsonstr)
#         assert result.status_code == 200
#         print(json.dumps(result.json(), indent=4))
#
#
# def test_gluster_brick_disable():
#     for i in cluster_host_list:
#         url = BASEURL + '/node/storage/block_device/disable'
#         rdata = {
#         "req_host": i,
#         "dev_path": "/dev/sdb"
#         }
#         jsonstr = json.dumps(rdata)
#         result = requests.post(url, jsonstr)
#         assert result.status_code == 200
#         print(json.dumps(result.json(), indent=4))
