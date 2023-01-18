import pytest
from conftest import Basetest, volname
import json

# volname = "vol-01"
rdata = {
    "req_host": "127.0.0.1",
    "vol_name": volname
}


@pytest.mark.dependency()
def test_volume_trash_enable():
    uri = "/cluster/volume/trash/enable"
    req = Basetest(str(uri), rdata)
    code, result = req.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.dependency(depends=["test_volume_trash_enable"])
def test_volume_trash_update():
    uri = "/cluster/volume/trash/config/update"
    rdata = {
      "req_host": "127.0.0.1",
      "vol_name": volname,
      "trash_dir": ".trashcan",
      "max_filesize": "100MB"
    }
    req = Basetest(str(uri), rdata)
    code, result = req.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))


def test_volume_trash_list():
    uri = "/cluster/volume/trash/config/list"
    req = Basetest(str(uri), rdata)
    code, result = req.base_test()
    assert code == 200
    da = result.json()["data"]["features.trash-max-filesize"]
    assert da == "100MB"
    print(json.dumps(result.json(), indent=4))

def test_volume_trash_init():
    uri = "/cluster/volume/trash/config/init"
    req = Basetest(str(uri), rdata)
    code, result = req.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))

# def test_volume_trash_disable():
#     uri = "/cluster/volume/trash/disable"
#     req = Basetest(str(uri), rdata)
#     code, result = req.base_test()
#     assert code == 200
#     print(json.dumps(result.json(), indent=4))