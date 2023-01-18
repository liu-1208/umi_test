import pytest
from conftest import Basetest, volname
import json

# volname = "vol-01"
rdata = {
    "req_host": "127.0.0.1",
    "vol_name": volname
}


@pytest.mark.dependency()
def test_volume_heal_enable():
    uri = "/cluster/volume/heal/enable"
    req = Basetest(str(uri), rdata)
    code, result = req.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.dependency(depends=["test_volume_heal_enable"])
def test_volume_heal_update():
    uri = "/cluster/volume/heal/config/update"
    # 修复策略有（none、size、ctime、mtime、majority）
    rdata = {
      "req_host": "127.0.0.1",
      "vol_name": volname,
      "favorite_child_policy": "majority"
    }
    req = Basetest(str(uri), rdata)
    code, result = req.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))


def test_volume_heal_list():
    uri = "/cluster/volume/heal/config/list"
    req = Basetest(str(uri), rdata)
    code, result = req.base_test()
    assert code == 200
    da = result.json()["data"]["cluster.favorite-child-policy"]
    assert da == "majority"
    print(json.dumps(result.json(), indent=4))


def test_volume_heal_status():
    uri = "/cluster/volume/heal/status"
    req = Basetest(str(uri), rdata)
    code, result = req.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))


def test_volume_heal_info():
    uri = "/cluster/volume/heal/info"
    req = Basetest(str(uri), rdata)
    code, result = req.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))


def test_volume_heal_init():
    uri = "/cluster/volume/heal/config/init"
    req = Basetest(str(uri), rdata)
    code, result = req.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))

# def test_volume_heal_disable():
#     uri = "/cluster/volume/heal/disable"
#     req = Basetest(str(uri), rdata)
#     code, result = req.base_test()
#     assert code == 200
#     print(json.dumps(result.json(), indent=4))
#