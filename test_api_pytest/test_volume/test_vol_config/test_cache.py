from conftest import Basetest, volname
import json

rdata = {
    "req_host": "127.0.0.1",
    "vol_name": volname
}


def test_volume_cache_init():
    uri = "/cluster/volume/cache/config/init"
    req = Basetest(str(uri), rdata)
    code, result = req.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))


def test_volume_cache_update():
    uri = "/cluster/volume/cache/config/update"
    rdata = {
      "req_host": "127.0.0.1",
      "vol_name": volname,
      "cache_size": "1024MB"
    }
    req = Basetest(str(uri), rdata)
    code, result = req.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))


def test_volume_cache_list():
    uri = "/cluster/volume/cache/config/list"
    req = Basetest(str(uri), rdata)
    code, result = req.base_test()
    assert code == 200
    value = result.json()["data"]["performance.cache-size"]
    assert  value == "1024MB"
    print(json.dumps(result.json(), indent=4))
