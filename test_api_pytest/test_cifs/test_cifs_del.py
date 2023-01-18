import json
import requests
import pytest
from conftest import BASEURL

share_dir = '/cifs_share'
share_name = 'cifs_share'
rdata = {
  "req_host": "127.0.0.1"
}


@pytest.mark.delete
class TestCifsDel(object):
    @pytest.mark.cifs_service()
    def test_gluster_cifs_userdel(self):
        for i in range(2):
            smbuser = {
                "req_host": "127.0.0.1",
                "user": "pytest-0" + str(i)
            }
            url = BASEURL + '/cluster/cifs/user/delete'
            jsonstr = json.dumps(smbuser)
            result = requests.post(url, jsonstr)
            assert result.status_code == 200
            print(json.dumps(result.json(), indent=4))

    @pytest.mark.cifs_service()
    def test_gluster_cifs_delete(self):
        url = BASEURL + '/cluster/cifs/share/delete'
        rdata = {
          "req_host": "127.0.0.1",
          "name": share_name
        }
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))

    @pytest.mark.cifs_service()
    def test_gluster_cifs_disable(self):
        url = BASEURL + '/cluster/cifs/service/disable'
        jsonstr = json.dumps(rdata)
        result = requests.post(url, jsonstr)
        assert result.status_code == 200
        print(json.dumps(result.json(), indent=4))
