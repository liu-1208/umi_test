import json
import requests
import pytest
from conftest import volname, BASEURL, Basetest

rdata = {
    "req_host": "127.0.0.1",
    "nfs_mode": "Gluster"
}
share_dir = "/test_gnfs"


@pytest.mark.delete
class TestGNfsDel(object):
    @pytest.mark.nfs_service()
    def test_gluster_nfs_delete(self):
        url = BASEURL + '/cluster/nfs/share/delete'
        rdata = {
          "req_host": "127.0.0.1",
          "nfs_mode": "Gluster",
          "vol_name": volname,
          "share_dir": share_dir,
          "client": "*"
        }
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200, "Here are the bug !"
        print(json.dumps(result.json(), indent=4))


    @pytest.mark.nfs_service()
    def test_gluster_nfs_disable(self):
        url = BASEURL + '/cluster/nfs/service/disable'
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))

    @pytest.mark.nfs_service()
    def test_gluster_nfs_status(self):
        uri = '/cluster/nfs/service/status'
        p = Basetest(str(uri), rdata)
        code, result = p.base_test()
        c = result.json()['data']
        assert code == 200
        assert str(c) == 'False'
        print(json.dumps(result.json(), indent=4))

