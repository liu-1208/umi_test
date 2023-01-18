import pytest
from conftest import Basetest, lvmvol
import json

rdata = {
    "req_host": "127.0.0.1",
    "vol_name": lvmvol
}
snap_name = "%s-snapshot-01" % lvmvol


@pytest.mark.snapshot
@pytest.mark.dependency()
def test_snapshot_create():
    uri = "/cluster/volume/snapshot/create"
    rdata = {
      "req_host": "127.0.0.1",
      "snap_name": snap_name,
      "vol_name": lvmvol,
      "snap_description": "pytest-snapshot-01"
    }
    p = Basetest(str(uri), rdata)
    code, result = p.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.snapshot
def test_snapshot_config_init():
    uri = "/cluster/volume/snapshot/config/init"
    p = Basetest(str(uri), rdata)
    code, result = p.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.snapshot
class TestConfig(object):
    def test_snapshot_all_init(self):
        uri = "/cluster/all/snapshots/config/init"
        rdata ={
            "req_host": "127.0.0.1"
        }
        res = Basetest(str(uri), rdata)
        code, result = res.base_test()
        assert code == 200
        print(json.dumps(result.json(), indent=4))
    def test_snapshot_all_update(self):
        uri = "/cluster/all/snapshots/config/update"
        rdata ={
            "req_host": "127.0.0.1",
            "snap_max_hard_limit": 200,
            "snap_max_soft_limit": 80,
            "is_auto_delete": 'true',
            "is_activate_on_create": 'true'
        }
        res = Basetest(str(uri), rdata)
        code, result = res.base_test()
        assert code == 200
        print(json.dumps(result.json(), indent=4))
    def test_snapshot_all_list(self):
        uri = "/cluster/all/snapshots/config/list"
        rdata ={
            "req_host": "127.0.0.1"
        }
        res = Basetest(str(uri), rdata)
        code, result = res.base_test()
        assert code == 200
        print(json.dumps(result.json(), indent=4))

    def test_snapshot_volume_init(self):
        uri = "/cluster/volume/snapshots/config/init"
        rdata = {
            "req_host": "127.0.0.1"
        }
        res = Basetest(str(uri), rdata)
        code, result = res.base_test()
        assert code == 200
        print(json.dumps(result.json(), indent=4))

    def test_snapshot_volume_update(self):
        uri = "/cluster/volume/snapshots/config/update"
        rdata = {
          "req_host": "127.0.0.1",
          "vol_name": lvmvol,
          "is_allow_insecure": 'true',
          "is_uss": 'true',
          "is_show_snapshot_directory": 'true',
          "snap_max_hard_limit": 199
        }
        res = Basetest(str(uri), rdata)
        code, result = res.base_test()
        assert code == 200
        print(json.dumps(result.json(), indent=4))

    def test_snapshot_volume_list(self):
        uri = "/cluster/volume/snapshots/config/list"
        rdata = {
            "req_host": "127.0.0.1"
        }
        res = Basetest(str(uri), rdata)
        code, result = res.base_test()
        assert code == 200
        print(json.dumps(result.json(), indent=4))


@pytest.mark.snapshot
def test_snapshot_restore():
    uri = "/cluster/volume/snapshot/restore"
    rdata = {
      "req_host": "127.0.0.1",
      "snap_name": snap_name
    }
    p = Basetest(str(uri), rdata)
    code, result = p.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.snapshot
def test_snapshot_list():
    uri = "/cluster/volume/snapshot/list"
    p = Basetest(str(uri), rdata)
    code, result = p.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.snapshot
def test_snapshot_info():
    uri = "/cluster/volume/snapshot/info"
    rdata = {
      "req_host": "127.0.0.1",
      "snap_name": snap_name,
      "vol_name": lvmvol
    }
    p = Basetest(str(uri), rdata)
    code, result = p.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.snapshot
def test_snapshot_status():
    uri = "/cluster/volume/snapshot/status"
    rdata = {
      "req_host": "127.0.0.1",
      "snap_name": snap_name
    }
    p = Basetest(str(uri), rdata)
    code, result = p.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.snapshot
def test_snapshot_status():
    uri = "/cluster/volume/snapshot/status"
    rdata = {
      "req_host": "127.0.0.1",
      "clone_name": "{0}-clone-01".format(lvmvol),
      "snap_name": snap_name
    }
    p = Basetest(str(uri), rdata)
    code, result = p.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))
