import json
import requests
import pytest
from conftest import BASEURL, volname, Basetest

rdata = {
  "req_host": "127.0.0.1"
}
share_dir = "/ganeshav"
g_dir = "/ganeshag"


@pytest.mark.delete
@pytest.mark.nfs_service
class TestGaGNfsDel(object):
    def test_vfs_client_delete(self):
        uri = '/cluster/ganesha/share/client/delete'
        rdata = {
          "req_host": "127.0.0.1",
          "path": "/export/{0}{1}".format(volname, share_dir),
          "clients": "*"
        }
        p = Basetest(str(uri), rdata)
        code, result = p.base_test()
        assert code == 200
        print(json.dumps(result.json(), indent=4))

    def test_client_gluster_delete(self):
        uri = '/cluster/ganesha/share/client/delete'
        rdata = {
          "req_host": "127.0.0.1",
          "path": "/{0}{1}".format(volname, g_dir),
          "clients": "*"
        }
        p = Basetest(str(uri), rdata)
        code, result = p.base_test()
        assert code == 200
        print(json.dumps(result.json(), indent=4))

    def test_vfs_share_delete(self):
        uri = '/cluster/ganesha/share/delete'
        rdata = {
          "req_host": "127.0.0.1",
          "path": "/export/{0}{1}".format(volname, share_dir),
          "force": 'false'
        }
        p = Basetest(str(uri), rdata)
        code, result = p.base_test()
        assert code == 200
        print(json.dumps(result.json(), indent=4))

    def test_share_gluster_delete(self):
        uri = '/cluster/ganesha/share/delete'
        rdata = {
          "req_host": "127.0.0.1",
          "path": "/{0}{1}".format(volname, g_dir),
          "force": 'false'
        }
        p = Basetest(str(uri), rdata)
        code, result = p.base_test()
        assert code == 200
        print(json.dumps(result.json(), indent=4))

    @pytest.mark.dependency()
    def test_ganesha_disable(self):
        url = BASEURL + '/cluster/ganesha/service/disable'
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))

    @pytest.mark.dependency(depends=["TestGaGNfsDel::test_ganesha_disable"])
    def test_gluster_ganesha_status(self):
        url = BASEURL + '/cluster/ganesha/service/status'
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        a = result.json()["data"]
        print(json.dumps(result.json(), indent=4))
        assert str(a) == "False"
