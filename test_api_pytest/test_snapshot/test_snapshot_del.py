import pytest
from conftest import Basetest, lvmvol
import json

rdata = {
    "req_host": "127.0.0.1",
    "vol_name": lvmvol
}
snap_name = "%s-snapshot-01" % lvmvol

@pytest.mark.snapshot
def test_snapshot_deactivate():
    uri = "/cluster/volume/snapshot/deactivate"
    rdata = {
      "req_host": "127.0.0.1",
      "snap_name": snap_name
    }
    p = Basetest(str(uri), rdata)
    code, result = p.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))


@pytest.mark.snapshot
def test_snapshot_delete():
    uri = "/cluster/volume/snapshot/delete"
    rdata = {
      "req_host": "127.0.0.1",
      "snap_name": snap_name,
      "is_all": 'false',
      "vol_name": lvmvol
    }
    p = Basetest(str(uri), rdata)
    code, result = p.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))

@pytest.mark.snapshot
def test_snapvol_delete():
    uri = "/cluster/volume/snapvol/delete"
    p = Basetest(str(uri), rdata)
    code, result = p.base_test()
    assert code == 200
    print(json.dumps(result.json(), indent=4))