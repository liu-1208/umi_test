import json
import requests
import pytest
from conftest import cluster_ip, BASEURL, Basetest

rdata = {
    "req_host": "127.0.0.1",
    "vol_name": "test"
}


# @pytest.mark.cluster()
@pytest.mark.delte()
class TestClusterDel(object):
    def test_gluster_cluster_remove(self):
        for i in cluster_ip:
            url = BASEURL + '/cluster/node/remove'
            rdata = {
                "req_host": "127.0.0.1",
                "node_addr": i
            }
            jsonstr = json.dumps(rdata)
            result = requests.post(url, jsonstr)
            assert result.status_code == 200
            print(json.dumps(result.json(), indent=4))

# 清空/var/lib/gluster目录下所有文件
    def test_gluster_cluster_init(self):
        for i in cluster_ip:
            url = BASEURL + '/cluster/service/init'
            rdata = {
                "req_host": i
            }
            jsonstr = json.dumps(rdata)
            result = requests.post(url, jsonstr)
            assert result.status_code == 200
            print(json.dumps(result.json(), indent=4))

# 会执行smb，knfs，gnfs，ganesha，smbftpd初始化init
    def test_gluster_node_init(self):
        for i in cluster_ip:
            url = BASEURL + '/cluster/node/init'
            rdata = {
                "req_host": i
            }
            jsonstr = json.dumps(rdata)
            result = requests.post(url, jsonstr)
            assert result.status_code == 200
            print(json.dumps(result.json(), indent=4))

    def test_gluster_cluster_disable(self):
        url = BASEURL + '/cluster/service/disable'
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))

