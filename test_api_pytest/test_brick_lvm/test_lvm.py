import pytest
from conftest import Basetest, lvm_brick_names, cluster_ip
import json


@pytest.mark.lvm
def test_brick_lvm_enable():
    for i in cluster_ip:
        uri = "/node/gsnap/thin_lvm/enable"
        rdata = {
          "req_host": i,
          "dev_names": lvm_brick_names
        }
        p1 = Basetest(str(uri), rdata)
        code, result = p1.base_test()
        assert code == 200
        print(json.dumps(result.json(), indent=4))


@pytest.mark.lvm
def test_brick_lvm_disable():
    for i in cluster_host_list:
        uri = "/node/gsnap/thin_lvm/disable"
        rdata = {
          "req_host": i,
          "dev_names": lvm_brick_names
        }
        p = Basetest(str(uri), rdata)
        code, result = p.base_test()
        assert code == 200
        print(json.dumps(result.json(), indent=4))

# # @pytest.mark.lvm
# def test_brick_lvm():
#     uri = "/node/gsnap/thin_lvm/enable"
#     rdata = {
#       "req_host": "127.0.0.1",
#       "dev_names": [
#         "/dev/sde"
#       ]
#     }
#     url = BASEURL + '/node/gsnap/thin_lvm/enable'
#     jsonstr = json.dumps(rdata)
#     result = requests.post(url, jsonstr)
#     print(json.dumps(result.json(), indent=4))
#     assert result.status_code == 200
