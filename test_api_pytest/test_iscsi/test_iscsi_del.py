import json
import requests
import pytest
from conftest import BASEURL, volname
from test_tgt import lun_name

iqn = 'iqn.2022-07.pytest.target-01'
# lun_path = '/.iscsi/lun-tgt.raw'

@pytest.mark.delete
@pytest.mark.iscsi()
class TestIscsiDel(object):
    for mode in ["TGT", "TCMU"]:
        def test_gluster_tgt_lun_vdelete(self, mode=mode):
            url = BASEURL + '/cluster/iscsi/lun/vfs_delete'
            rdata = {
              "req_host": "127.0.0.1",
              "iscsi_mode": mode,
              "lun_name": lun_name,
              "vol_name": volname,
              "clean_data": 'false'
            }
            # rdata = {
            #   "req_host": "127.0.0.1",
            #   "iscsi_mode": "TGT",
            #   "vol_name": volname,
            #   "path": lun_path,
            #   "clean_data": 'true'
            # }
            jsonstr = json.dumps(rdata)
            result = requests.post(url, jsonstr)
            assert result.status_code == 200
            print(json.dumps(result.json(), indent=4))

        def test_gluster_tgt_target_delete(self, mode=mode):
            url = BASEURL + '/cluster/iscsi/target/delete'
            rdata = {
              "req_host": "127.0.0.1",
              "iscsi_mode": mode,
              "iqn": iqn
            }
            jsonstr = json.dumps(rdata)
            result = requests.post(url, jsonstr)
            assert result.status_code == 200
            print(json.dumps(result.json(), indent=4))

        def test_gluster_tgt_disable(self, mode=mode):
            rdata = {
                "req_host": "127.0.0.1",
                "iscsi_mode": mode
            }
            url = BASEURL + '/cluster/iscsi/service/disable'
            jsonstr = json.dumps(rdata)
            result = requests.post(url, jsonstr)
            assert result.status_code == 200
            print(json.dumps(result.json(), indent=4))
