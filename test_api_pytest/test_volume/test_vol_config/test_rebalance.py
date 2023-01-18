import pytest
from conftest import Basetest, volname
import json

# volname = "vol-01"
rdata = {
    "req_host": "127.0.0.1",
    "vol_name": volname
}


@pytest.mark.dependency(name="rebalance")
def test_volume_rebalance_enable():
    uri = "/cluster/volume/rebalance/enable"
    req = Basetest(str(uri), rdata)
    code, result = req.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.dependency(depends=["rebalance"])
def test_volume_rebalance_update():
    uri = "/cluster/volume/rebalance/config/update"
    # 修复策略有（lazy|normal|aggressive）
    rdata = {
      "req_host": "127.0.0.1",
      "vol_name": volname,
      "favorite_child_policy": "lazy"
    }
    req = Basetest(str(uri), rdata)
    code, result = req.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))


def test_volume_rebalance_list():
    uri = "/cluster/volume/rebalance/config/list"
    req = Basetest(str(uri), rdata)
    code, result = req.base_test()
    assert code == 200
    da = result.json()["data"]["cluster.rebal-throttle"]
    assert da == "lazy"
    print(json.dumps(result.json(), indent=4))


def test_volume_rebalance_status():
    uri = "/cluster/volume/rebalance/status"
    req = Basetest(str(uri), rdata)
    code, result = req.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))


def test_volume_rebalance_init():
    uri = "/cluster/volume/rebalance/config/init"
    req = Basetest(str(uri), rdata)
    code, result = req.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))

# def test_volume_rebalance_disable():
#     uri = "/cluster/volume/rebalance/disable"
#     req = Basetest(str(uri), rdata)
#     code, result = req.base_test()
#     assert code == 200
#     print(json.dumps(result.json(), indent=4))