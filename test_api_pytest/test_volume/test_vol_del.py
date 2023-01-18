import json
import pytest
from conftest import volname, Basetest
from logs.loggers import Loggers

log = Loggers(level='debug', filename="test_vol_base.log")

rdata = {
    "req_host": "127.0.0.1",
    "vol_name": volname
}


@pytest.mark.volbase
@pytest.mark.delete
class TestVolDel(object):
    def test_vol_stop(self):
        uri = '/cluster/volume/stop'
        p = Basetest(str(uri), rdata)
        code, result = p.base_test()
        assert code == 200
        print(json.dumps(result.json(), indent=4))
        log.log_case_info(uri, rdata, __name__, result.status_code, result.json())

    def test_vol_status(self):
        uri = '/cluster/volume/info'
        p = Basetest(str(uri), rdata)
        code, result = p.base_test()
        assert code == 200
        res = result.json()['data']['{0}'.format(volname)]["statusStr"]
        assert str(res) == "Stopped"
        print(json.dumps(result.json(), indent=4))
        log.log_case_info(uri, rdata, __name__, result.status_code, result.json())

    def test_vol_delete(self):
        uri = '/cluster/volume/delete'
        p = Basetest(str(uri), rdata)
        code, result = p.base_test()
        assert code == 200
        print(json.dumps(result.json(), indent=4))
        log.log_case_info(uri, rdata, __name__, result.status_code, result.json())
